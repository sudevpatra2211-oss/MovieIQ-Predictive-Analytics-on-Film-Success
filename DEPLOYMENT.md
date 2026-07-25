# 🚀 MovieIQ Deployment Guide

## Table of Contents
1. [Quick Start](#quick-start)
2. [Streamlit Cloud (Recommended)](#streamlit-cloud-recommended)
3. [Other Deployment Options](#other-deployment-options)
4. [Configuration](#configuration)
5. [Troubleshooting](#troubleshooting)
6. [Monitoring & Maintenance](#monitoring--maintenance)

---

## Quick Start

### Option 1: Streamlit Cloud (5 minutes, FREE)

1. Visit [share.streamlit.io](https://share.streamlit.io/)
2. Sign in with GitHub
3. Click **"New app"**
4. Select:
   - Repository: `sudevpatra2211-oss/MovieIQ-Predictive-Analytics-on-Film-Success`
   - Branch: `main`
   - Main file: `app.py`
5. Click **"Deploy"**

✅ Your app is now live!

### Option 2: Local Testing (2 minutes)

```bash
# Clone repo
git clone https://github.com/sudevpatra2211-oss/MovieIQ-Predictive-Analytics-on-Film-Success.git
cd MovieIQ-Predictive-Analytics-on-Film-Success

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

Access at: `http://localhost:8501`

---

## Streamlit Cloud (Recommended)

### Prerequisites
- GitHub account (free)
- Public repository
- `requirements.txt` in repo root
- `app.py` as main entry point

### Step-by-Step Deployment

#### 1. Prepare Repository

```bash
# Ensure all files are committed
git add .
git commit -m "Ready for deployment"
git push origin main
```

**Required files:**
- ✅ `app.py`
- ✅ `requirements.txt`
- ✅ `movies_cleaned.csv`
- ✅ `.streamlit/config.toml` (optional)

#### 2. Access Streamlit Cloud

- Go to: https://share.streamlit.io/
- Sign in with GitHub
- Authorize Streamlit to access your repositories

#### 3. Create New App

1. Click **"New app"** button (top right)
2. Fill deployment form:
   ```
   Repository: sudevpatra2211-oss/MovieIQ-Predictive-Analytics-on-Film-Success
   Branch: main
   Main file path: app.py
   ```
3. Click **"Deploy"**

#### 4. Monitor Deployment

- Streamlit will build and deploy automatically
- View real-time logs in admin panel
- App URL: `https://movieiq-[random-string].streamlit.app/`

### Post-Deployment

- **Share URL** with stakeholders
- **Monitor logs** for errors
- **Update frequently** by pushing to GitHub
- Changes auto-deploy within minutes

---

## Other Deployment Options

### Heroku (Legacy - No Longer Free)

```bash
# Login to Heroku
heroku login

# Create app
heroku create movieiq-app

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

**Requirements:**
- `Procfile`: `web: streamlit run app.py`
- `setup.sh`: Environment configuration
- `runtime.txt`: `python-3.11.0`

### AWS Elastic Beanstalk

```bash
# Install EB CLI
pip install awsebcli

# Initialize
eb init -p python-3.11 movieiq

# Deploy
eb create movieiq-env
eb deploy
```

### Azure App Service

```bash
# Login
az login

# Create resource group
az group create --name movieiq-rg --location eastus

# Deploy
az webapp deployment source config-zip --resource-group movieiq-rg \
  --name movieiq-app --src deploy.zip
```

### Google Cloud Run

```bash
# Create Dockerfile
cat > Dockerfile << EOF
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]
EOF

# Deploy
gcloud run deploy movieiq --source . --platform managed
```

---

## Configuration

### .streamlit/config.toml

```toml
[theme]
primaryColor = "#3498db"
backgroundColor = "#f5f5f5"
secondaryBackgroundColor = "#ffffff"
textColor = "#2c3e50"
font = "sans serif"

[client]
showErrorDetails = true
raiseOnScriptFileChangeWarning = false

[server]
port = 8501
headless = true
enableXsrfProtection = true
maxUploadSize = 200

[logger]
level = "info"

[browser]
gatherUsageStats = true
```

### Environment Variables (Streamlit Cloud Secrets)

1. Go to app settings → **Secrets**
2. Add in TOML format:

```toml
# .streamlit/secrets.toml
db_username = "admin"
db_password = "secret_password"
api_key = "your-api-key"
```

3. Access in code:

```python
import streamlit as st
username = st.secrets["db_username"]
password = st.secrets["db_password"]
```

---

## File Requirements Checklist

### Essential Files ✅

- [x] `app.py` - Main application
- [x] `requirements.txt` - Dependencies
- [x] `movies_cleaned.csv` - Dataset
- [x] `README.md` - Documentation
- [x] `.gitignore` - Git configuration

### Optional but Recommended ✅

- [x] `.streamlit/config.toml` - Streamlit config
- [x] `DEPLOYMENT.md` - Deployment guide
- [x] `LICENSE` - License file
- [x] `.github/workflows/` - CI/CD pipelines

### For Advanced Deployment

- [x] `Procfile` - Heroku config
- [x] `setup.sh` - Environment setup
- [x] `runtime.txt` - Python version
- [x] `Dockerfile` - Container config

---

## Troubleshooting

### "ModuleNotFoundError"

**Problem:** App crashes with missing module error

**Solutions:**
```bash
# Update requirements.txt
pip freeze > requirements.txt

# Commit and push
git add requirements.txt
git commit -m "Update dependencies"
git push origin main

# Redeploy (Streamlit Cloud auto-deploys)
```

### "FileNotFoundError: movies_cleaned.csv"

**Problem:** Dataset file not found

**Solutions:**
1. Ensure file is in repo root
2. Verify filename spelling (case-sensitive on Linux)
3. Check `.gitignore` isn't excluding it:
   ```
   # .gitignore should have:
   !movies_cleaned.csv
   ```
4. Commit and push:
   ```bash
   git add movies_cleaned.csv
   git commit -m "Add dataset"
   git push origin main
   ```

### "Memory exceeded"

**Problem:** Streamlit Cloud memory limit exceeded

**Solutions:**
1. Use `@st.cache_data` for expensive operations
2. Load only required data columns
3. Reduce dataset size
4. Upgrade to paid tier

### "Deployment stuck/slow"

**Problem:** Build taking too long or failing

**Solutions:**
1. Check deployment logs:
   - Click app settings → View logs
2. Verify `requirements.txt` syntax
3. Reduce dependency count
4. Try manual redeployment:
   - Settings → Reboot app

### "App shows blank page"

**Problem:** App deploys but shows nothing

**Solutions:**
1. Check browser console for errors (F12)
2. View app logs in Streamlit Cloud admin
3. Test locally:
   ```bash
   streamlit run app.py
   ```
4. Common fixes:
   ```python
   # Add debug output
   st.write("App loaded successfully!")
   
   # Force cache clear
   st.cache_data.clear()
   ```

### "CORS or connection errors"

**Problem:** API/database connection fails

**Solutions:**
1. Use environment variables for secrets
2. Whitelist Streamlit Cloud IP (if needed)
3. Verify credentials are correct
4. Test connection locally first

---

## Monitoring & Maintenance

### Monitor App Health

1. **Set up alerts:**
   - GitHub Actions for notifications
   - Streamlit Community alerts

2. **Check logs regularly:**
   ```bash
   # Streamlit Cloud admin panel
   # View → Logs
   ```

3. **Track usage:**
   - Streamlit Cloud dashboard
   - View daily active users
   - Monitor resource usage

### Update App

```bash
# Make changes locally
# Test with: streamlit run app.py

# Commit and push
git add .
git commit -m "Feature: Add new visualization"
git push origin main

# Streamlit Cloud auto-deploys within minutes!
```

### Scaling

**Free Tier Limits:**
- 3 public apps
- 1 GB storage
- 5 GB bandwidth/month
- ~100MB RAM per app

**Paid Tier ($5/month):**
- Unlimited apps
- 10 GB storage
- 100 GB bandwidth/month
- ~1 GB RAM per app
- Priority support

---

## Security Best Practices

1. **Never commit secrets:**
   ```bash
   # Use .streamlit/secrets.toml (in .gitignore)
   # OR Streamlit Cloud admin secrets
   ```

2. **Use HTTPS only:**
   - Streamlit Cloud provides automatic HTTPS

3. **Keep dependencies updated:**
   ```bash
   pip install --upgrade pip
   pip install --upgrade -r requirements.txt
   ```

4. **Validate user inputs:**
   ```python
   if not isinstance(budget, (int, float)):
       st.error("Invalid budget input")
   ```

5. **Add authentication (optional):**
   ```python
   import streamlit_authenticator as stauth
   ```

---

## Performance Optimization

### Caching Strategies

```python
# Cache expensive data operations
@st.cache_data
def load_data():
    return pd.read_csv("movies_cleaned.csv")

# Cache ML models
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")
```

### Reduce Load Time

```python
# Load only required columns
df = pd.read_csv("data.csv", usecols=['budget', 'revenue', 'success'])

# Use lazy loading
if st.button("Load detailed analysis"):
    # Heavy computation here
    pass
```

---

## Support & Resources

- **Streamlit Docs:** https://docs.streamlit.io/
- **Streamlit Cloud Guide:** https://docs.streamlit.io/streamlit-cloud/
- **Community Forum:** https://discuss.streamlit.io/
- **GitHub Issues:** https://github.com/streamlit/streamlit/issues
- **Stack Overflow:** Tag `streamlit`

---

## Quick Reference

| Task | Command |
|------|----------|
| Run locally | `streamlit run app.py` |
| Build requirements | `pip freeze > requirements.txt` |
| Test locally | `streamlit run app.py --logger.level=debug` |
| View Streamlit logs | Streamlit Cloud admin → Logs |
| Reboot app | Settings → Reboot app |
| Clear cache | Click "Always rerun" or restart |

---

**Last Updated:** July 2026
**Version:** 1.0
