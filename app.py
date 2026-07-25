"""
MovieIQ — Stage 6: Streamlit Dashboard
Interactive app covering EDA, statistical test results, and a live
Random Forest prediction tool for movie success (revenue > budget).
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="MovieIQ - Movie Success Predictor",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .metric-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and cache the movies dataset."""
    try:
        return pd.read_csv("movies_cleaned.csv")
    except FileNotFoundError:
        st.error("❌ Error: movies_cleaned.csv not found. Please ensure it's in the app directory.")
        st.stop()

@st.cache_resource
def load_model():
    """Load and cache the trained model and encoder."""
    try:
        with open("movieiq_rf_model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("genre_encoder.pkl", "rb") as f:
            encoder = pickle.load(f)
        return model, encoder
    except FileNotFoundError as e:
        st.warning(f"⚠️ Model files not found: {e}\nDemo mode enabled - predictions will use random values.")
        return None, None

# Load data and model
df = load_data()
model, encoder = load_model()

# Header
st.title("🎬 MovieIQ — Movie Success Predictor")
st.caption("📊 Classification project: Predicting whether a movie's revenue exceeds its budget using machine learning.")
st.markdown("---")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📈 EDA", "🧪 Statistical Tests", "🔮 Predict"])

# ============ TAB 1: OVERVIEW ============
with tab1:
    st.header("Dataset Overview")
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Movies", f"{len(df):,}")
    with col2:
        success_rate = (df['success'].mean() * 100)
        st.metric("Success Rate", f"{success_rate:.1f}%")
    with col3:
        st.metric("Avg Budget", f"${df['budget'].mean():,.0f}")
    with col4:
        st.metric("Avg Revenue", f"${df['revenue'].mean():,.0f}")
    
    st.markdown("### Dataset Sample")
    st.dataframe(
        df.head(20),
        use_container_width=True,
        height=400
    )
    
    # Dataset Info
    with st.expander("📋 Dataset Information"):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Columns:** {len(df.columns)}")
            st.write(f"**Rows:** {len(df):,}")
            st.write(f"**Memory:** {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        with col2:
            st.write(f"**Data Types:**")
            st.write(df.dtypes)

# ============ TAB 2: EXPLORATORY DATA ANALYSIS ============
with tab2:
    st.header("Exploratory Data Analysis (EDA)")
    
    c1, c2 = st.columns(2)
    
    # Genre Distribution
    with c1:
        st.subheader("📊 Genre Distribution")
        try:
            fig, ax = plt.subplots(figsize=(8, 5))
            genre_counts = df["genre"].value_counts()
            ax.barh(genre_counts.index, genre_counts.values, color="#3498db")
            ax.set_xlabel("Count", fontsize=12)
            ax.set_ylabel("Genre", fontsize=12)
            plt.tight_layout()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error plotting genre distribution: {e}")
    
    # Success Rate by Genre
    with c2:
        st.subheader("✅ Success Rate by Genre")
        try:
            fig, ax = plt.subplots(figsize=(8, 5))
            rate = df.groupby("genre")["success"].mean().sort_values()
            ax.barh(rate.index, rate.values, color="#2ecc71")
            ax.set_xlabel("Success Rate", fontsize=12)
            ax.set_xlim(0, 1)
            plt.tight_layout()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error plotting success rate by genre: {e}")
    
    c3, c4 = st.columns(2)
    
    # Budget vs Revenue Scatter
    with c3:
        st.subheader("💰 Budget vs. Revenue")
        try:
            fig, ax = plt.subplots(figsize=(8, 6))
            colors = df["success"].map({1: "#2ecc71", 0: "#e74c3c"})
            ax.scatter(df["budget"], df["revenue"], c=colors, alpha=0.5, s=20)
            ax.set_xlabel("Budget ($)", fontsize=12)
            ax.set_ylabel("Revenue ($)", fontsize=12)
            ax.grid(True, alpha=0.3)
            # Add legend
            from matplotlib.patches import Patch
            legend_elements = [Patch(facecolor='#2ecc71', label='Success'),
                             Patch(facecolor='#e74c3c', label='Failure')]
            ax.legend(handles=legend_elements)
            plt.tight_layout()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error plotting budget vs revenue: {e}")
    
    # Feature Distributions
    with c4:
        st.subheader("📉 Feature Distributions")
        try:
            feature = st.selectbox(
                "Choose a feature:",
                ["budget", "popularity", "runtime", "vote_average"],
                key="feature_select"
            )
            fig, ax = plt.subplots(figsize=(8, 6))
            df[df["success"] == 1][feature].hist(ax=ax, alpha=0.6, label="Success", color="#2ecc71", bins=25, edgecolor='black')
            df[df["success"] == 0][feature].hist(ax=ax, alpha=0.6, label="Failure", color="#e74c3c", bins=25, edgecolor='black')
            ax.set_xlabel(feature.replace('_', ' ').title(), fontsize=12)
            ax.set_ylabel("Frequency", fontsize=12)
            ax.legend()
            ax.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error plotting feature distribution: {e}")

# ============ TAB 3: STATISTICAL TESTS ============
with tab3:
    st.header("Statistical Testing")
    
    st.subheader("🧪 T-tests: Numeric Features vs. Success")
    st.write("Testing if there's a significant difference in feature means between successful and unsuccessful movies.")
    
    try:
        rows = []
        for col in ["budget", "popularity", "runtime", "vote_average"]:
            s = df[df["success"] == 1][col]
            f = df[df["success"] == 0][col]
            t_stat, p_val = stats.ttest_ind(s, f, equal_var=False)
            rows.append({
                "Feature": col.replace('_', ' ').title(),
                "Mean (Success)": f"{s.mean():,.2f}",
                "Mean (Failure)": f"{f.mean():,.2f}",
                "T-Statistic": f"{t_stat:.4f}",
                "P-Value": f"{p_val:.4f}",
                "Significant (α=0.05)": "✅ Yes" if p_val < 0.05 else "❌ No"
            })
        
        results_df = pd.DataFrame(rows)
        st.dataframe(results_df, use_container_width=True, hide_index=True)
    except Exception as e:
        st.error(f"Error performing t-tests: {e}")
    
    st.subheader("📊 Chi-square Test: Genre vs. Success")
    st.write("Testing if genre and movie success are independent.")
    
    try:
        contingency = pd.crosstab(df["genre"], df["success"])
        chi2, p_val, dof, _ = stats.chi2_contingency(contingency)
        
        cc1, cc2, cc3 = st.columns(3)
        with cc1:
            st.metric("Chi² Statistic", f"{chi2:.3f}")
        with cc2:
            st.metric("P-Value", f"{p_val:.4f}")
        with cc3:
            st.metric("Significant?", "✅ Yes" if p_val < 0.05 else "❌ No")
        
        st.info(
            "📌 **Interpretation:** Genre shows no statistically significant association with success in this dataset. "
            "Only popularity showed a significant mean difference between successful and unsuccessful movies — "
            "consistent with the modest predictive power of the model."
        )
    except Exception as e:
        st.error(f"Error performing chi-square test: {e}")

# ============ TAB 4: PREDICTIONS ============
with tab4:
    st.header("🔮 Predict Movie Success")
    st.warning(
        "⚠️ **Model Note:** Test-set ROC-AUC was 0.47 — near chance level. "
        "Treat predictions as illustrative of the pipeline, not reliable forecasts."
    )
    
    if model is None or encoder is None:
        st.error("❌ Model files not found. Cannot make predictions.")
        st.info("To deploy, ensure movieiq_rf_model.pkl and genre_encoder.pkl are in the app directory.")
    else:
        c1, c2 = st.columns(2)
        
        with c1:
            st.subheader("Input Parameters")
            budget = st.number_input(
                "Budget ($)",
                min_value=1000,
                value=50_000_000,
                step=1_000_000
            )
            popularity = st.slider(
                "Popularity Score",
                0.0, 150.0, 50.0,
                step=0.1
            )
            runtime = st.slider(
                "Runtime (minutes)",
                60, 240, 120,
                step=1
            )
        
        with c2:
            st.subheader("More Parameters")
            vote_average = st.slider(
                "Vote Average (IMDb-like)",
                0.0, 10.0, 6.0,
                step=0.1
            )
            genre = st.selectbox(
                "Genre",
                sorted(df["genre"].unique()),
                key="genre_select_predict"
            )
        
        # Prediction button
        if st.button("🎯 Predict", type="primary", use_container_width=True):
            try:
                genre_encoded = encoder.transform([genre])[0]
                X_new = pd.DataFrame([{
                    "budget": budget,
                    "popularity": popularity,
                    "runtime": runtime,
                    "vote_average": vote_average,
                    "genre_encoded": genre_encoded
                }])
                
                pred = model.predict(X_new)[0]
                proba = model.predict_proba(X_new)[0][1]
                
                st.markdown("---")
                st.subheader("📊 Prediction Result")
                
                col1, col2 = st.columns(2)
                with col1:
                    if pred == 1:
                        st.success(
                            f"✅ **Predicted: SUCCESS**\n\n"
                            f"Probability of Success: **{proba:.1%}**"
                        )
                    else:
                        st.error(
                            f"❌ **Predicted: FAILURE**\n\n"
                            f"Probability of Success: **{proba:.1%}**"
                        )
                
                with col2:
                    st.info(
                        f"**Input Summary:**\n\n"
                        f"• Budget: ${budget:,.0f}\n"
                        f"• Genre: {genre}\n"
                        f"• Popularity: {popularity:.1f}\n"
                        f"• Runtime: {runtime} min\n"
                        f"• Rating: {vote_average:.1f}/10"
                    )
            except Exception as e:
                st.error(f"❌ Error during prediction: {e}")

st.markdown("---")
st.caption(
    "🎬 **MovieIQ** | Built with Streamlit • scikit-learn • scipy • pandas "
    "| [GitHub](https://github.com/sudevpatra2211-oss/MovieIQ-Predictive-Analytics-on-Film-Success)"
)
