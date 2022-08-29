import logging
import sys
import warnings

import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


# calculate an accuracy from the confusion matrix
def get_model_accuracy(cf_matrix):
    diagonal_sum = cf_matrix.trace()
    sum_of_all_elements = cf_matrix.sum()
    return diagonal_sum / sum_of_all_elements


def train_model_with_mlflow_tracking(mlflow_experiment_name: str, mlflow_run_name: str, data_url: str, n_estimator: int,
                                     max_depth: int, min_samples_split: int):
    # Step1: Prepare data
    feature_data, label_data = prepare_data(data_url)
    train_X, test_X, train_y, test_y = train_test_split(feature_data, label_data, train_size=0.8, test_size=0.2,
                                                        random_state=0)
    # set up mlflow context
    mlflow.set_experiment(mlflow_experiment_name)
    with mlflow.start_run(run_name=mlflow_run_name):
        # create a random forest classifier
        rf_clf = RandomForestClassifier(n_estimators=n_estimator, max_depth=max_depth,
                                        min_samples_split=min_samples_split,
                                        n_jobs=2, random_state=0)
        # train the model with training_data
        rf_clf.fit(train_X, train_y)
        # predict testing data
        predicts_val = rf_clf.predict(test_X)

        # Generate a cm
        cm = confusion_matrix(test_y, predicts_val)
        model_accuracy = get_model_accuracy(cm)
        print("RandomForest model with hyper-parameters: (n_estimator=%f, max_depth=%f, min_samples_split=%f):" % (
        n_estimator, max_depth,
        min_samples_split))
        print("accuracy: %f" % model_accuracy)
        # log the model hyper-parameters to the mlflow server
        mlflow.log_param("data_url", data_url)
        mlflow.log_param("n_estimator", n_estimator)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("min_samples_split", min_samples_split)

        # log shap feature explanation extension. This will generate a graph of feature importance of the model
        # mlflow.shap.log_explanation(rf_clf.predict, test_X.sample(70))

        # log the model accuracy to the mlflow server
        mlflow.log_metric("model_accuracy", model_accuracy)

        # log the model to the mlflow server
        mlflow.sklearn.log_model(rf_clf, "model")


def prepare_data(data_url):
    input_df = None
    # read data as df
    try:
        input_df = pd.read_csv(data_url, index_col=0)
        input_df.head()
    except Exception as e:
        print(
            "Unable to read data from the giving path, check your data location. Error: %s", e
        )
    # Prepare data for ml model
    label = input_df.legendary
    feature = input_df.drop(['legendary', 'generation', 'total'], axis=1).select_dtypes(exclude=['object'])
    return feature, label


def main():
    warnings.filterwarnings("ignore")
    np.random.seed(40)
    # default configuration

    default_data_url = "https://minio.lab.sspcloud.fr/pengfei/sspcloud-demo/pokemon-cleaned.csv"
    default_run_name = "default"

    default_n_estimator = 10
    default_max_depth = 5
    default_samples_split = 2

    # Get experiment setting from cli
    experiment_name = str(sys.argv[1]) if len(sys.argv) > 1 else sys.exit("Must provide a mlflow experiment name ")
    run_name = str(sys.argv[2]) if len(sys.argv) > 2 else default_run_name

    # Get data path
    data_url = str(sys.argv[3]) if len(
        sys.argv) > 3 else default_data_url

    # Get hyper parameters from cli arguments
    n_estimator = int(sys.argv[4]) if len(sys.argv) > 4 else default_n_estimator
    max_depth = int(sys.argv[5]) if len(sys.argv) > 5 else default_max_depth
    min_samples_split = int(sys.argv[6]) if len(sys.argv) > 6 else default_samples_split

    # run the main model training pipeline

    train_model_with_mlflow_tracking(experiment_name, run_name, data_url, n_estimator, max_depth, min_samples_split)


if __name__ == "__main__":
    main()
