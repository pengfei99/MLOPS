#! /bin/bash
export MLFLOW_S3_ENDPOINT_URL='https://minio.lab.sspcloud.fr'
export MLFLOW_TRACKING_URI='https://user-pengfei-531016.kub.sspcloud.fr/'
export MLFLOW_EXPERIMENT_NAME="pokemon"



python ../train_model.py {experiment_name} {run_name} {data_url} {n_estimator} {max_depth} {min_samples_split}