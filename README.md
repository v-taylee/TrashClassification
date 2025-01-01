# Trash Classifier　垃圾分類器
112453019 李雅芸
## Overview
垃圾分類常因不便或疏忽，導致分類不確實，若能有自動垃圾分類工具，應能提高分類意願與準確性。
裝置若安裝在社區內，除了便利住戶進行正確分類，還能減少回收業者整理垃圾的時間，進而與業者洽談回收費用的優惠。
節省的費用則可回饋至社區管理費中，減輕住戶的經濟負擔外同時促進永續發展。

## Required
### Software
* Tensorflow lite  
使用Teachable Machine進行訓練
* Gpiozero
* opencv
* IP攝像頭(app)  
使用方式參考:[如何把手機當作ipCam](
https://medium.com/nine9devtw/%E5%A6%82%E4%BD%95%E6%8A%8A%E6%89%8B%E6%A9%9F%E7%95%B6%E4%BD%9Cipcam-234586a220d4  
)
#### how to install
* Tensorflow lite  
詳細官方說明可參考:[LiteRT](https://ai.google.dev/edge/litert/microcontrollers/python?hl=zh-tw)
```
python3 -m pip install tflite-runtime
```
* opencv
```
cd ~/
sudo apt install git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev libatlas-base-dev python3-scipy
git clone --depth 1 --branch 4.5.2-openvino https://github.com/opencv/opencv.git
cd opencv && mkdir build && cd build
cmake –DCMAKE_BUILD_TYPE=Release –DCMAKE_INSTALL_PREFIX=/usr/local ..
make -j4
```
#### Teachable Machine 
* 進入Image Project
![step1](https://github.com/v-taylee/TrashClassification/blob/main/img/teachable_step1.jpg)
* 分別給定類別名稱與圖片後，按下 Train Model
![step2](https://github.com/v-taylee/TrashClassification/blob/main/img/teachable_step2.png)
**訓練期間不能切換分頁!**
* 訓練完成後按下 Export Model
* 輸出tensorfloe lite 的權重
![step3](https://github.com/v-taylee/TrashClassification/blob/main/img/teachable_step3.jpg)
### Hardware
* MG996R 180度 *2  
* 電池盒 + 4顆1.5V電池  
為MG996R供電，因樹梅派本身僅提供5V的供電，使用上馬達較為沒力，故額外接電池盒
* 按鈕
* LED
* 手機相機

## Shape of Trash Classifier
* Appearance
![Appearance](https://github.com/v-taylee/TrashClassification/blob/main/img/appearance.jpg)
* Detail
![detail_overlook](https://github.com/v-taylee/TrashClassification/blob/main/img/detail_overlook.jpg)
![detail_side](https://github.com/v-taylee/TrashClassification/blob/main/img/detail_side.jpg)
* Servo for direction determination after classification
![servo](https://github.com/v-taylee/TrashClassification/blob/main/img/servo.jpg)
* Button and LED
![btn and led](https://github.com/v-taylee/TrashClassification/blob/main/img/button.jpg)
## Circuit Diagram
![Circuit Diagram](https://github.com/v-taylee/TrashClassification/blob/main/img/raspberry.png)
## Usage
* step 1  
  LED燈長亮時，可放入物品
* step 2  
  按下按鈕後，LED燈轉為閃爍，表示裝置運行中
* step 3
  待辨識與分類完畢，LED燈長亮，可回到step 1 進行下一次使用

## Working Demo
[demo影片連結](https://youtube.com/shorts/2tcxWRNsKkk)
## Reference
* TensorFlow Lite Python image classification demo  
https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/examples/python/
* LiteRT 的 Linux 裝置快速入門導覽課程  
https://ai.google.dev/edge/litert/microcontrollers/python?hl=zh-tw
* GPIOZERO  
https://gpiozero.readthedocs.io/en/stable/api_output.html
* 口罩辨識訓練機  
https://hackmd.io/@LHB-0222/maker-1
* 如何把手機當作ipCam  
https://medium.com/nine9devtw/%E5%A6%82%E4%BD%95%E6%8A%8A%E6%89%8B%E6%A9%9F%E7%95%B6%E4%BD%9Cipcam-234586a220d4
* Data Source:Garbage Classification  
https://www.kaggle.com/datasets/mostafaabla/garbage-classification
* Teachable Machine  
https://teachablemachine.withgoogle.com/
