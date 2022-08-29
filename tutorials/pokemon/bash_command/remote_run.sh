#! /bin/bash
export MLFLOW_S3_ENDPOINT_URL='https://minio.lab.sspcloud.fr'
export MLFLOW_TRACKING_URI='https://user-pengfei-866801.kub.sspcloud.fr/'
export MLFLOW_EXPERIMENT_NAME="pokemon"

run_name="default"
data_url="https://minio.lab.sspcloud.fr/pengfei/sspcloud-demo/pokemon-cleaned.csv"

# set the hyper parameters
n_estimator="50"
max_depth="30"
min_samples_split="2"

mlflow run https://github.com/pengfei99/mlflow-pokemon-example.git -P remote_server_uri=$MLFLOW_TRACKING_URI -P experiment_name=$MLFLOW_EXPERIMENT_NAME \
-P data_url=https://minio.lab.sspcloud.fr/pengfei/mlflow-demo/pokemon-partial.csv \
-P n_estimator=50 -P max_depth=30 -P min_samples_split=2