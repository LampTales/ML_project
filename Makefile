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

vis:
	python ${DETECTRON_PATH}/../tools/visualize_results.py \
		--dataset TT100K_val \
		--detections ${DETECTRON_PATH}/../output/test/TT100K_val/generalized_rcnn/detections.pkl \
		--output-dir ./prediction 


