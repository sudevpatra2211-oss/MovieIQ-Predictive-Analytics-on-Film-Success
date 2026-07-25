# MovieIQ Deployment Guide

## 🚀 Quick Start

### Local Deployment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sudevpatra2211-oss/MovieIQ-Predictive-Analytics-on-Film-Success.git
   cd MovieIQ-Predictive-Analytics-on-Film-Success
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

4. Open your browser to `http://localhost:8501`

---

## ☁️ Streamlit Cloud Deployment

### Step 1: Prepare Your Repository
- Ensure all files are committed to GitHub
- Repository must be public

### Step 2: Deploy on Streamlit Cloud

1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Click **"New app"**
3. Select your repository:
   - **Repository:** `sudevpatra2211-oss/MovieIQ-Predictive-Analytics-on-Film-Success`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **"Deploy"**

### Step 3: Monitor Deployment
- Streamlit will automatically build and deploy your app
- View logs in the admin panel
- Access your app via the provided URL

---

## 🔑 Environment Variables (Optional)

For sensitive data, add secrets in Streamlit Cloud:
1. Go to your app's settings
2. Click **"Secrets"**
3. Add your secrets in TOML format

---

## 📊 Required Files

Make sure these files are in the repository root:
- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `movies_cleaned.csv` - Dataset
- `movieiq_rf_model.pkl` - Trained model (optional for demo)
- `genre_encoder.pkl` - Encoder (optional for demo)
- `.streamlit/config.toml` - Streamlit configuration

---

## 🐛 Troubleshooting

### Issue: "File not found" error
- Ensure all data files are in the root directory
- Check file permissions on the server
- Verify paths in the code use relative paths

### Issue: Memory errors
- Streamlit Cloud limits memory usage
- Consider caching with `@st.cache_data` and `@st.cache_resource`
- Use data sampling for large datasets

### Issue: Slow performance
- Optimize data loading with caching
- Reduce DataFrame size
- Use lazy loading for heavy computations

---

## 📞 Support

For issues, create a GitHub issue or contact the maintainer.

---

**Deployment URL:** Will be provided after successful deployment on Streamlit Cloud
