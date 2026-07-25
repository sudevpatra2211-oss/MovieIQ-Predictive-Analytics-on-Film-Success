# 🎬 MovieIQ — Movie Success Predictor

**Predictive Analytics Dashboard | Streamlit | Machine Learning**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movieiq-predictor.streamlit.app/)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Overview

MovieIQ is an interactive Streamlit dashboard that predicts movie success using machine learning. The application analyzes movie features (budget, popularity, genre, runtime, ratings) to predict whether a movie's revenue will exceed its budget.

**Key Metrics:**
- **Dataset:** 600+ movies with comprehensive features
- **Model:** Random Forest Classifier
- **Features:** Budget, Popularity, Runtime, Vote Average, Genre
- **Target:** Binary classification (Success/Failure)

---

## ✨ Features

### 📊 **Overview Tab**
- Dataset statistics and KPIs
- Movie count, success rate, average budget/revenue
- Sample data preview (first 20 movies)
- Detailed dataset information

### 📈 **EDA Tab (Exploratory Data Analysis)**
- Genre distribution chart
- Success rate by genre
- Budget vs. Revenue scatter plot
- Feature distribution histograms
- Interactive feature selection

### 🧪 **Statistical Tests Tab**
- T-tests for numeric features
- Chi-square test for categorical data
- P-value significance testing
- Statistical interpretation

### 🎯 **Prediction Tab**
- Interactive input controls
- Real-time movie success prediction
- Probability estimation
- Input validation and error handling

---

## 🚀 Quick Start

### Local Installation

```bash
# Clone the repository
git clone https://github.com/sudevpatra2211-oss/MovieIQ-Predictive-Analytics-on-Film-Success.git
cd MovieIQ-Predictive-Analytics-on-Film-Success

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## ☁️ Streamlit Cloud Deployment

### Automatic Deployment

1. **Go to [Streamlit Cloud](https://share.streamlit.io/)**
2. **Click "New app"**
3. **Fill in the details:**
   - Repository: `sudevpatra2211-oss/MovieIQ-Predictive-Analytics-on-Film-Success`
   - Branch: `main`
   - Main file: `app.py`
4. **Click "Deploy"**

### Manual Alternative

```bash
# Install Streamlit CLI
pip install streamlit

# Deploy
streamlit deploy --repository https://github.com/sudevpatra2211-oss/MovieIQ-Predictive-Analytics-on-Film-Success
```

---

## 📁 Project Structure

```
MovieIQ-Predictive-Analytics-on-Film-Success/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── movies_cleaned.csv             # Dataset
├── README.md                       # This file
├── DEPLOYMENT.md                   # Deployment guide
├── Procfile                        # Heroku deployment config
├── setup.sh                        # Environment setup script
├── runtime.txt                     # Python version
├── streamlit_app.py               # Cloud deployment alias
└── .gitignore                      # Git ignore patterns
```

---

## 📊 Dataset

**movies_cleaned.csv** contains the following features:

| Feature | Type | Description |
|---------|------|-------------|
| title | String | Movie title |
| genre | Categorical | Movie genre |
| budget | Numeric | Production budget ($) |
| revenue | Numeric | Box office revenue ($) |
| roi | Numeric | Return on investment |
| success | Binary | Revenue > Budget (1/0) |
| popularity | Numeric | Popularity score |
| runtime | Numeric | Movie duration (minutes) |
| vote_average | Numeric | IMDb-like rating (0-10) |
| has_missing | Boolean | Data quality flag |

---

## 🤖 Machine Learning Model

**Model Type:** Random Forest Classifier

**Input Features:**
- Budget
- Popularity
- Runtime
- Vote Average
- Genre (encoded)

**Output:** Binary prediction (Success/Failure)

**Performance Notes:**
- Test ROC-AUC: ~0.47 (near chance level)
- Predictions are illustrative; not reliable for production use
- Model files required: `movieiq_rf_model.pkl`, `genre_encoder.pkl`

---

## 📋 Requirements

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
scikit-learn>=1.3.0
scipy>=1.10.0
matplotlib>=3.7.0
pillow>=10.0.0
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 🔧 Configuration

### Streamlit Configuration (.streamlit/config.toml)

```toml
[theme]
primaryColor = "#3498db"
backgroundColor = "#f5f5f5"
secondaryBackgroundColor = "#ffffff"
textColor = "#2c3e50"
font = "sans serif"

[client]
showErrorDetails = true

[server]
port = 8501
headless = true
```

---

## 🐛 Troubleshooting

### Issue: "FileNotFoundError: movies_cleaned.csv"
**Solution:** Ensure `movies_cleaned.csv` is in the project root directory.

### Issue: "Model files not found"
**Solution:** The app works in demo mode without model files. To enable predictions:
1. Train the model locally
2. Save as `movieiq_rf_model.pkl` and `genre_encoder.pkl`
3. Upload to repository

### Issue: Slow performance on Streamlit Cloud
**Solution:**
- Streamlit Cloud has resource limits
- App uses `@st.cache_data` and `@st.cache_resource` for optimization
- Consider upgrading to Streamlit Community Cloud paid tier if needed

### Issue: "ModuleNotFoundError"
**Solution:** Reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

---

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Cloud Deploy Guide](https://docs.streamlit.io/streamlit-cloud/get-started)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

## 👤 Author

**sudevpatra2211-oss**
- GitHub: [@sudevpatra2211-oss](https://github.com/sudevpatra2211-oss)
- Email: sudevpatra2211@gmail.com

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📞 Support

For issues, questions, or suggestions:
- Open a [GitHub Issue](https://github.com/sudevpatra2211-oss/MovieIQ-Predictive-Analytics-on-Film-Success/issues)
- Contact the author

---

## 🌟 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Machine Learning with [scikit-learn](https://scikit-learn.org/)
- Data analysis with [pandas](https://pandas.pydata.org/)
- Visualization with [matplotlib](https://matplotlib.org/)

---

**Last Updated:** July 2026
**Version:** 1.0.0
