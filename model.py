import time
import numpy as np
from PIL import Image, ImageFile
import tflite_runtime.interpreter as tflite  # 使用 tflite_runtime 以減少資源需求


class TrashClassify:
   def __init__(self, model_file, label_file):
      # 初始化 tflite 解析器
      self.interpreter = tflite.Interpreter(model_path=model_file)
      self.interpreter.allocate_tensors()
      self.labels = self.load_labels(label_file)
      self.input_mean = 127.5
      self.input_std = 127.5
      print(self.labels)

   def load_labels(self, filename):
      with open(filename, 'r') as f:
         return [line.strip() for line in f.readlines()]

   def predict(self, image:ImageFile):
      input_details = self.interpreter.get_input_details()
      output_details = self.interpreter.get_output_details()

      # 獲取輸入張量的尺寸
      height = input_details[0]['shape'][1]
      width = input_details[0]['shape'][2]

      square_image = self.crop_img(image)
      img = square_image.resize((width, height))
      input_data = np.expand_dims(img, axis=0)
      # 檢查是否為浮點模型
      floating_model = input_details[0]['dtype'] == np.float32

      if floating_model:
         input_data = (np.float32(input_data) - self.input_mean) / self.input_std

      # 將圖像數據傳入模型
      self.interpreter.set_tensor(input_details[0]['index'], input_data)

      # 執行推論
      start_time = time.time()
      self.interpreter.invoke()
      stop_time = time.time()

      # 獲取輸出結果
      output_data = self.interpreter.get_tensor(output_details[0]['index'])
      results = np.squeeze(output_data)
      # 排序並顯示前 5 名結果
      top_k = results.argsort()[-5:][::-1]
      
      #for i in top_k:
          #print(f"{(results[i]/255.0)}: {self.labels[i]}")
          
      return self.labels[top_k[0]]

   def crop_img(self, image:ImageFile):
      original_width, original_height = image.size
      short_side = min(original_width, original_height)
      left = (original_width - short_side) / 2
      top = (original_height - short_side) / 2
      right = (original_width + short_side) / 2
      bottom = (original_height + short_side) / 2
      square_image = image.crop((left, top, right, bottom))
      return square_image


