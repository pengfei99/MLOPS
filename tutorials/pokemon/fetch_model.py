import pandas as pd
import os
import mlflow.sklearn


def prepare_sample_data(data_url):
    input_df = pd.read_csv(data_url, index_col=0)

    ## prepare sample data
    # Prepare data for ml model testing
    legendary_pokemon = input_df[input_df["legendary"] == True]
    legendary_pokemon_sample = legendary_pokemon.sample(5).drop(['legendary', 'generation', 'total'],
                                                                axis=1).select_dtypes(
        exclude=['object'])
    normal_pokemon = input_df[input_df["legendary"] == False]
    normal_pokemon_sample = normal_pokemon.sample(5).drop(['legendary', 'generation', 'total'], axis=1).select_dtypes(
        exclude=['object'])
    return legendary_pokemon_sample, normal_pokemon_sample


# fetch the trained model from mlflow server by using its version
def fetch_model(server_uri: str, experiment_name: str, model_version: str):
    os.environ["MLFLOW_TRACKING_URI"] = server_uri
    model = mlflow.pyfunc.load_model(model_uri=f"models:/{experiment_name}/{model_version}")
    return model


def test_model(data_url: str, server_uri: str, experiment_name: str, model_version: str):
    # step1: prepare sample data
    legendary_sample, normal_sample = prepare_sample_data(data_url)

    # step2: fetch the model
    model = fetch_model(server_uri, experiment_name, model_version)

    # step3: predict the sample data
    print(model.predict(legendary_sample))
    print(model.predict(normal_sample))


def main():
    data_url = "https://minio.lab.sspcloud.fr/pengfei/sspcloud-demo/pokemon-cleaned.csv"
    mlflow_server_uri = "https://user-pengfei-42041.kub.sspcloud.fr/"
    experiment_name = "pokemon"
    version = '4'

    test_model(data_url, mlflow_server_uri, experiment_name, version)


if __name__ == "__main__":
    main()
