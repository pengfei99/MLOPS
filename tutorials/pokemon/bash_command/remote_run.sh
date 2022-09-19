#! /bin/bash
export MLFLOW_S3_ENDPOINT_URL='https://minio.lab.sspcloud.fr'
export MLFLOW_TRACKING_URI='https://user-pengfei-837304.kub.sspcloud.fr/'
export MLFLOW_EXPERIMENT_NAME="pokemon"

run_name="default"
data_url="https://minio.lab.sspcloud.fr/pengfei/sspcloud-demo/pokemon-cleaned.csv"

# set the hyper parameters
n_estimator="50"
max_depth="30"
min_samples_split="2"

mlflow run https://github.com/pengfei99/MLOPS.git -P remote_server_uri=${MLFLOW_TRACKING_URI} \
-P experiment_name=${MLFLOW_EXPERIMENT_NAME} \
-P data_url=${data_url} \
-P n_estimator=${n_estimator} -P max_depth=${max_depth} -P min_samples_split=${min_samples_split}