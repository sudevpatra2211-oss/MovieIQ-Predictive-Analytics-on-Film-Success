# 🎬 MovieIQ — Movie Success Predictor

A Streamlit dashboard for predictive analytics on film success, using Random Forest classification to predict whether a movie's revenue exceeds its budget.

## Features

- **Overview Tab**: Dataset statistics and data preview
- **EDA Tab**: Genre distribution, success rates, budget vs. revenue scatter plots, and feature distributions
- **Statistical Tests Tab**: T-tests for numeric features and Chi-square test for genre associations
- **Prediction Tab**: Interactive tool to predict movie success based on input parameters

## Setup & Deployment

### Prerequisites

- Python 3.9+
- Required data and model files (see below)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sudevpatra2211-oss/MovieIQ-Predictive-Analytics-on-Film-Success.git
cd MovieIQ-Predictive-Analytics-on-Film-Success
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Required Files

Before running the app, ensure these files are in the project root:

- **`movies_cleaned.csv`** - Cleaned dataset with columns: `genre`, `budget`, `revenue`, `success`, `popularity`, `runtime`, `vote_average`
- **`movieiq_rf_model.joblib`** - Trained Random Forest model
- **`genre_encoder.joblib`** - Fitted LabelEncoder for genre encoding

### Running Locally

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Deployment on Streamlit Cloud

1. Push your repository to GitHub (including all required files)
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Connect your GitHub repository and select the `main` branch
5. Set the main file path to `app.py`
6. Deploy!

**Note**: Ensure the data and model files are available in the repository.

## Model Performance

- **Test-set ROC-AUC**: 0.47 (near chance level)
- **Note**: Predictions should be treated as illustrative of the ML pipeline rather than reliable forecasts

## Tech Stack

- **Streamlit** - Web app framework
- **pandas & numpy** - Data manipulation
- **scikit-learn** - Machine learning
- **scipy** - Statistical testing
- **matplotlib** - Visualizations
- **joblib** - Model serialization

## License

Open source - feel free to modify and distribute.
