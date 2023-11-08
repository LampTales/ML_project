# Machine learning final project 2023

In this project, please choose **ONE** of the following eight jobs (choosing more than one job will **NOT** give you more score):

 + [1. Object detection and tracking](#1-object-detection-and-tracking)
 + [2. GAN for self-driving data augmentation](#2-gan-for-self-driving-data-augmentation)
 + [3. CARLA Simulator](#3-carla-simulator)
 + [4. Traffic-Sign Detection and Recognition](#4-traffic-sign-detection-and-recognition)
 + [5. Lane Detection](#5-lane-detection)
 + [6. Vehicle road cooperative](#6-vehicle-road-cooperative)
 + [7. RL-based Motion Planning for Robot](#7-rl-based-motion-planning-for-robot)
 + [8. Semantic Segmentation](#8-semantic-segmentation)


## 4. Traffic-Sign Detection and Recognition


### Project Background

Traffic-sign detection and recognition refer to the technology and processes used to identify and interpret various road signs and signals in the context of intelligent transportation systems (ITS) and autonomous vehicles. This vital field plays a crucial role in enhancing road safety, improving traffic management, and enabling the successful deployment of autonomous vehicles.


### Project Description


This project aims to delve into the intricacies of Traffic-Sign Detection and Recognition, ultimately developing and deploying a custom deep neural network to address real-world scenarios.


### Project Objectives

+ Based on their research, students will meticulously evaluate the various models and select the most suitable one to implement for this project. The chosen model should exhibit the potential for real-world applicability and robust performance
+ (Optional) Building upon the selected model, students will actively seek opportunities to enhance its performance. This may involve fine-tuning parameters, implementing innovative algorithms, or exploring novel techniques to optimize Traffic-Sign Detection and Recognition.



## Project Tasks

#### Task 1

Identify existing models, datasets, and benchmarking methodologies.
Evaluate the strengths and weaknesses of different approaches.
Choose a suitable deep neural network architecture for Traffic-Sign Detection.
Justify the selection based on research findings and project requirements.

#### Task 2

Evaluate the trained model's performance using appropriate metrics such as accuracy, precision, recall, and F1 score.
Test the model on real-world traffic sign images or video streams to assess its robustness and reliability.

**Note: Please pay attention to safety when shooting videos!!**

#### Task 3 (Optional)

Fine-tune the model to improve its performance on the chosen dataset such as hyperparameter tuning, loss functions, and regularization techniques.


### Materials

#### Paper reading:

<table>
  <colgroup>
    <col style="border: 1px solid" span="5" />
  </colgroup>
  <tr>
    <th>Paper</th>
    <th>Recommended Codebase</th>
  </tr>

  <tr>
    <td>Zhang, J., Huang, M., Jin, X., & Li, X. (2017). A real-time chinese traffic sign detection algorithm based on modified YOLOv2. Algorithms, 10(4), 127.</td>
  </tr>

  <tr>
    <td>Tabernik, D., & Skočaj, D. (2019). Deep learning for large- scale traffic-sign detection and recognition. IEEE transactions on intelligent transportation systems, 21(4), 1427-1440.</td>
    <td><a href="https://github.com/skokec/detectron-traffic-signs">https://github.com/skokec/detectron-traffic-signs</a></td>
  </tr>

  <tr>
    <td>Arcos-Garcia, A., Alvarez-Garcia, J. A., & Soria-Morillo, L. M. (2018). Evaluation of deep neural networks for traffic sign detection systems. Neurocomputing, 316, 332-344.</td>
    <td><a href="https://github.com/aarcosg/traffic-sign-detection">https://github.com/aarcosg/traffic-sign-detection</a></td>
  </tr>

  <tr>
    <td>Liu, Z., Li, D., Ge, S. S., & Tian, F. (2020). Small traffic sign detection from large image. Applied Intelligence, 50(1), 1-13.</td>
    <td></td>
  </tr>

  <tr>
    <td>Zhu, Z., Liang, D., Zhang, S., Huang, X., Li, B., & Hu, S. (2016). Traffic-sign detection and classification in the wild. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 2110-2118).</td>
    <td><a href="https://cg.cs.tsinghua.edu.cn/traffic-sign">https://cg.cs.tsinghua.edu.cn/traffic-sign</a></td>
  </tr>

  <tr>
    <td>Arcos-García, Á., Alvarez-Garcia, J. A., & Soria-Morillo, L. M. (2018). Deep neural network for traffic sign recognition systems: An analysis of spatial transformers and stochastic optimisation methods. Neural Networks, 99, 158-165.</td>
    <td><a href="https://github.com/aarcosg/tsr-torch">https://github.com/aarcosg/tsr-torch</a></td>
  </tr>

  <tr>
    <td>Sanyal, B., Mohapatra, R. K., & Dash, R. (2020, January). Traffic sign recognition: A survey. In 2020 International Conference on Artificial Intelligence and Signal Processing (AISP) (pp. 1-6). IEEE.</td>
    <td></td>
  </tr>

  <tr>
    <td>Bochkovskiy, A., Wang, C. Y., & Liao, H. Y. M. (2020). Yolov4: Optimal speed and accuracy of object detection. arXiv preprint arXiv:2004.10934.</td>
    <td><a href="https://github.com/Tianxiaomo/pytorch-YOLOv4">https://github.com/Tianxiaomo/pytorch-YOLOv4</a></td>
  </tr>

</table>


#### Datasets:

+ [Tsinghua-Tencent 100K Annotations 2021](https://cg.cs.tsinghua.edu.cn/traffic-sign/)

+ [Chinese Traffic Sign Database](http://www.nlpr.ia.ac.cn/pal/trafficdata/recognition.html)

+ [German Traffic Sign Recognition/Detection Benchmark](https://benchmark.ini.rub.de/index.html)



#### Others:

MMDetection. [https://github.com/open-mmlab/mmdetection](https://github.com/open-mmlab/mmdetection)

Awesome object detection. [https://github.com/amusi/awesome-object-detection](https://github.com/amusi/awesome-object-detection)



