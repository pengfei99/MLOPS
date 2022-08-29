# MLOPS

## 1. Introduction

### 1.1 What is MLOps?

**MLOps** stands for `Machine Learning Operations`. It contains a set of practices that aims to deploy and 
maintain machine learning models in production reliably and efficiently


Machine learning models are developed, trained and tested in isolated experimental systems. When a model is ready to 
be deployed in a production environment, we need a standard operation procedure that can deploy the model efficiently 
and then maintaining and monitoring the model, or even retrain the model.

MLOps is a set of best practices that seeks to increase automation and improve the efficiency of models during
the whole ml lifecycle, while also focusing on business and regulatory requirements. It also aims to shorten and 
manage the complete development life-cycle and provide continuous delivery of predictive services. 

MLOps applies to the entire lifecycle - from integrating with model code development ( 
continuous integration/continuous delivery), orchestration, and deployment, to health, diagnostics, governance, 
and business metrics. 



### 1.2 Why do we need MLOps?

Put a machine learning model into production is difficult. It envoles many complex components such as 
- data collection/ingest, 
- data prep (e.g. cleaning, feature engineering, etc), 
- model development
- model training, 
- model tuning
- model deployment
- model monitoring, 
- model explainability
- ETC. 

Below figure shows the mlops competence requirement:

![ML_Ops_Venn_Diagram.svg](img/ML_Ops_Venn_Diagram.svg)

![ml_technical_debt.PNG](img/ml_technical_debt.PNG)

These components require the collaboration and hand-offs across teams, from Data Engineering to Data Science to ML Engineering. 
Naturally, it requires stringent operational rigor to keep all these processes synchronous and working in tandem. 
MLOps encompasses the experimentation, iteration, and continuous improvement of the machine learning lifecycle. 


By adopting an MLOps approach, data scientists and machine learning engineers can collaborate and `increase the pace 
of model development and production`, by implementing continuous integration and deployment (CI/CD) practices with 
proper monitoring, validation, and governance of ML models.


### 1.3 What are the benefits of MLOps?

The primary benefits of MLOps are 
- efficiency: MLOps allows data teams to achieve faster model development, deliver higher quality ML models, and 
               faster deployment and production
- scalability: MLOps also enables vast scalability and management where thousands of models can be overseen, controlled, 
               managed, and monitored for continuous integration, continuous delivery, and continuous deployment. 
                Specifically, MLOps provides reproducibility of ML pipelines, enabling more tightly-coupled 
              collaboration across data teams, reducing conflict with devops and IT, and accelerating release velocity
- risk reduction: Machine learning models often need regulatory scrutiny and drift-check, and MLOps enables greater 
               transparency and faster response to such requests and ensures greater compliance with an organization’s 
               or industry’s policies.


## 2. Key steps in MLOps

The complete MLOps process includes three broad phases of 
1. Designing the ML-powered application
2. ML Experimentation and Development
3. ML Operations

### 2.1 Designing the ML-powered application

The first phase is devoted to business understanding, data understanding and designing the ML-powered software. 
In this stage, we identify our potential user and use case, design the machine learning solution to solve its problem, 
and assess the further development of the project. Mostly, we would act within two categories of problems:
- increasing the productivity of the user
- increasing the interactivity of our application.

Initially, we define ML use-cases and prioritize them. The best practice for ML projects is to work on one ML use case 
at a time. Furthermore, the design phase aims to inspect the available data that will be needed to train our model and 
to specify the functional and non-functional requirements of our ML model. We should use these requirements to design 
the architecture of the ML-application, establish the serving strategy, and create a test suite for the future ML model.

### 2.2 ML Experimentation and Development

The second phase is devoted to verifying the applicability of ML for our problem by implementing Proof-of-Concept for 
ML Model. Here, we run iteratively below steps:
1. Exploratory data analysis (EDA)
2. identifying or polishing the suitable ML algorithm for our problem, 
3. data engineering (e.g. data cleaning, feature engineering)
4. model engineering (e.g. model training and tuning). 

The primary goal in this phase is to deliver a stable quality ML model that we will run in production.

### 2.3 ML Operations

The third phase is devoted to deliver the previously developed ML model into production. Here, we need to address the
following MLOps principals:
- **Model tracking**: track all the necessary element to reproduce the model such as code, hyperparameter and training data.
- **Model review**: Test model and produce quality assurance report. Inference model production-specifics properties such as 
                model response times.
- **Model Governance** : manage model versions, model artifacts and transitions through their lifecycle (e.g. staging, production, archived,etc.).
                     
- **Model deployment**: Automate the process of deploying registered models (e.g. permissions, cluster creation, API management, etc.)
- **Model monitoring**: Monitor the state of model production server (e.g. number of request, response time, serving data anomalies, etc.)
- **Model retraining**: Create alerts and automation to take corrective action in case of **model drift** due to 
                    differences in training and inference data or `data evolution`.

## 3. Different level of MLOps maturity

Google defines three levels of maturity of the ML process:
- Level 0 : Manual process
- Level 1 : ML pipeline automation
- Level 2 : CI/CD pipeline automation

### 3.1 Manual process (Level 0 maturity)

This is a typical data science process, which is performed at the beginning of 
implementing ML. This level has an experimental and iterative nature. Every step in each 
pipeline, such as data preparation and validation, model training and testing, are executed 
manually. The common way to process is to use Rapid Application Development (RAD) tools, 
such as Jupyter Notebooks.

Below figure shows the main steps:
![mlops_level_0_manual.svg](img/mlops_level_0_manual.svg)

### 3.2 ML pipeline automation (Level 1 maturity)

The goal of level 1 is to perform `continuous training` of the model by automating the ML pipeline; this lets you 
achieve `continuous delivery` of model prediction service.

To automate the process of using new data to retrain models in production, you need to introduce 
**automated data and model validation** steps to the pipeline, as well as pipeline triggers and metadata management.

![mlops_level_1_ml-automation.svg](img/mlops_level_1_ml-automation.svg)
### 3.3 CI/CD pipeline automation (Level 2 maturity)

In this level, we introduce a CI/CD system to perform fast and reliable ML model deployments in production. This 
automated CI/CD system lets your data scientists rapidly explore new ideas around feature engineering, model 
architecture, and hyper-parameters. They can implement these ideas and automatically build, test, and deploy the 
new pipeline components to the target environment.

![mlops_level_2_ml-automation.svg](img/mlops_level_2_ml-automation.svg)


For more information, you can visit this [page](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)

## 4. Continuous X

To understand Model deployment, we first specify the “ML assets” as ML model, its parameters and hyperparameters, 
training scripts, training and testing data. We are interested in the identity, components, versioning, and 
dependencies of these ML artifacts. The target destination for an ML artifact may be a (micro-) service or some 
infrastructure components. A deployment service provides orchestration, logging, monitoring, and notification to 
ensure that the ML models, code and data artifacts are stable.

MLOps is an ML engineering culture that includes the following practices:

- **Continuous Integration (CI)** extends the testing and validating code and components by adding testing and validating data and models.
- **Continuous Delivery (CD)** concerns with delivery of an ML training pipeline that automatically deploys another the ML model prediction service.
- **Continuous Training (CT)** is unique to ML systems property, which automatically retrains ML models for re-deployment.
- **Continuous Monitoring (CM)** concerns with monitoring production data and model performance metrics, which are bound to business metrics.

## 5. MLOps platform

An MLOps platform provides data scientists and software engineers with a collaborative environment that facilitates 
iterative data exploration, real-time co-working capabilities for experiment tracking, feature engineering, and 
model management, as well as controlled model transitioning, deployment, and monitoring. An MLOps automates the 
operational and synchronization aspects of the machine learning lifecycle.

For example, [mlflow](https://mlflow.org/) can be considered as a mlops platform

![mlflow_for_mlops.png](img/mlflow_for_mlops.png)

## Related sources

- [MLOps project example](https://github.com/pengfei99/mlflow-pokemon-example.git) 
- [Feature engineering/store](https://github.com/pengfei99/FeatureEngineering.git)