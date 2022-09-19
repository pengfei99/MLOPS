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
def fetch_model(experiment_name: str, model_version: str):
    model = mlflow.pyfunc.load_model(model_uri=f"models:/{experiment_name}/{model_version}")
    return model


def test_model(data_url: str, experiment_name: str, model_version: str):
    # step1: prepare sample data
    legendary_sample, normal_sample = prepare_sample_data(data_url)

    # step2: fetch the model
    model = fetch_model(experiment_name, model_version)

    # step3: predict the sample data
    print(f"The prediction of 5 five legendary pokemon: {model.predict(legendary_sample)}")
    print(f"The prediction of 5 five normal pokemon: {model.predict(normal_sample)}")


def main():
    data_url = "https://minio.lab.sspcloud.fr/pengfei/sspcloud-demo/pokemon-cleaned.csv"
    # setup experiment name      
    experiment_name = "pokemon"
    # setup model version      
    version = '4'
    # test model with test data      
    test_model(data_url, experiment_name, version)


if __name__ == "__main__":
    main()
