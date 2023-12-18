DETECTRON2_PATH = ./models/detectron2

download_dataset:
	if [ ! -d "data/TT100K" ]; then \
		echo "Downloading TT100K dataset..."; \
		mkdir -p data/TT100K && cd data/TT100K; \
		wget http://cg.cs.tsinghua.edu.cn/traffic-sign/data_model_code/data.zip; \
		unzip data.zip; \
	else \
		echo "TT100K dataset already exists."; \
	fi
	

preprocess_dataset_detectron:
	python process/detectron/convertTT100K2coco.py

preprocess_dataset: preprocess_dataset_detectron

train_detectron:
	python ${DETECTRON_PATH}/../tools/train_net.py \
    --multi-gpu-testing \
    --cfg ${DETECTRON_PATH}/../configs/TT100K.yaml \
    OUTPUT_DIR ${DETECTRON_PATH}/../output

infer_detectron:
	python ${DETECTRON_PATH}/../tools/infer_simple.py \
		--cfg ${DETECTRON_PATH}/../configs/TT100K.yaml \
		--output-dir ./prediction \
		--image-ext jpg \
		--wts ${DETECTRON_PATH}/../output/train/TT100K_train/generalized_rcnn/model_final.pkl \
		${DETECTRON_PATH}/datasets/data/TT100K/train

detect_yolov5:
	python ./models/yolov5/detect.py --weights ./models/yolov5/runs/train/exp13/weights/best.pt --source data/sustc

train_detectron2:
	python ./models/detectron2/tools/train_net.py --num-gpus 2 --resume \
	--config-file ./models/detectron2/configs/TT100K_FPN.yaml 

vis_output_detectron2:
	python ./models/detectron2/tools/visualize_json_results.py \
		--input  ./output/detectron2/FPN/inference/coco_instances_results.json \
		--output ./output/detectron2/FPN/inference/inference_results_vis \
		--dataset TT100K_val \
		--conf-threshold 0.5

vis_data_detectron2:
	python ./models/detectron2/tools/visualize_data.py --source annotation --config-file ./models/detectron2/configs/TT100K_FPN.yaml --output-dir ./output/detectron2/data_visualization 
	
	

infer_detectron2_video:
	python ./models/detectron2/demo/demo.py --config-file ./models/detectron2/configs/TT100K_FPN.yaml \
	--video-input ./data/sustc/v4.mp4 \
	--output output/detectron2/FPN/inference/v4.mp4 \
	--opts MODEL.WEIGHTS ./output/detectron2/FPN/model_final.pth 

infer_detectron2_demo:
	python ./models/detectron2/demo/demo.py --config-file ./models/detectron2/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml \
	--video-input ./data/test/car.mp4 \
	--output car.mp4 \
	--opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl 

infer_detectron2_image:
	python ./models/detectron2/demo/demo.py --config-file ./models/detectron2/configs/TT100K_FPN.yaml \
	--input ./data/sustc/*.jpg \
	--output output/detectron2/FPN/inference \
	--opts MODEL.WEIGHTS ./output/detectron2/FPN/model_final.pth 