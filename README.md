# Mobile Price Classification Project: Project Overview
* Developed a tool facilitating users in estimating the price class of their desired mobile phones.
* Conducted an analysis on how the price class correlates with various criteria, such as RAM and battery power.
* Employed hypothesis tests (1-way ANOVA, chi-squared tests) to quantify the relationships between features and the target variable.
* Optimized Logistic Regression, Random Forest, and SVC using GridSearchCV and Bayesian Optimization to attain the best-performing model.
* Constructed a Streamlit user interface allowing users to select desired phone features and receive price class predictions.
* Containerized the model using Docker for efficient deployment.

## Code and Resources Used 
**Python Version:** 3.11
**Dataset (Kaggle):** https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification
**Skopt Tutorial:** https://www.youtube.com/watch?v=5nYqK-HaoKY&t=2320s
**Deployment of Streamlit UI:** https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker

## Model Building 

I First performed EDA and statistical tests to gain insights on the most informative features, below are the prevalent ones and how they split the target variable:
![alt text](https://github.com/MrAnasAbid/MobilePhoneClassif/tree/main/Informative_features.png "Most informative predictors")  

Since no binary features were informative enough, I decided to only keep the ordinal and continuous ones before the modeling phase.
I experimented with three different models, evaluating their performance based on accuracy, given the absence of class privilege:
* **Logistic Regression** - Since linear relationships were noticed during the EDA phase
* **Random Forest** - For comparison with the linear model, it didn't perform well since there were no binary features
* **Support Vector Machines:** - Utilized for its flexibility in handling complex relationships

Preprocessing (Standardization) was used for Logistic Regression (necessity of scaling) and SVM (convergence speed), Hyperparameter optimization was also used to tune the models, resulting in the following scores on a 5-fold cross validation:
'5-Fold Accuracy': ['97.50%', '90.05%', '97.30%']
*	**Logistic Regression:** : accuracy: 97.50%
*	**Random Forest:**: accuracy: 90.05%
*	**Support Vector Machines:**: accuracy: 97.30%

Logistic Regression was the best performing model, slightly edging out SVM, it was also preferred due to its faster computing time, the resulting confusion matrix on a 80/20 train test split is the following:
![alt text](https://github.com/MrAnasAbid/MobilePhoneClassif/tree/main/LogRegConfusionMatrix.png "Confusion Matrix for the model") 
 
## User Interface
A streamlit UI was developed to facilitate end users experience with the model, providing a comprehensive and easy tool to use
![alt text](https://github.com/MrAnasAbid/MobilePhoneClassif/tree/main/UI_preview.png "UI preview") 

## Deployment
In this step, I listed dependancies and packaged the project using Docker for efficient deployment on a server or cloud infrastructure

## How to Use the Project

```bash
# Step 1: Clone the GitHub repo
git clone https://github.com/MrAnasAbid/MobilePhoneClassif.git

# Step 2: Navigate to the project's directory and install dependencies
pip install -r requirements.txt

# Step 3a: Run the project locally
python wsgi.py

# Step 3b: Deploy the Docker container
docker build -t <image_name> .
docker run -p 8501:8501 <container_name>
```

## Contributing
Feel free to contribute to this project! If you have questions, feedback, or would like to report issues, please reach out:
- **Email:** your.email@example.com
- **GitHub:** [Your GitHub Profile](https://github.com/YourUsername)
- **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/yourusername/)