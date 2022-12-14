#! /bin/bash
export MLFLOW_S3_ENDPOINT_URL='https://minio.lab.sspcloud.fr'
export MLFLOW_TRACKING_URI='https://user-pengfei-287428.user.lab.sspcloud.fr/'
export MLFLOW_EXPERIMENT_NAME="pokemon"

run_name="default"

# don't forget to change me
data_url="https://minio.lab.sspcloud.fr/pengfei/sspcloud-demo/pokemon-cleaned.csv"

# set the hyper parameters
n_estimator="50"
max_depth="30"
min_samples_split="2"

root_path="/home/onyxia/work/MLOPS"

python ${root_path}/tutorials/pokemon/train_model.py ${MLFLOW_EXPERIMENT_NAME} ${run_name} ${data_url} ${n_estimator} ${max_depth} ${min_samples_split}