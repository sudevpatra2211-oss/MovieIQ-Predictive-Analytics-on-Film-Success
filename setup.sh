mkdir -p ~/.streamlit/

echo "\
[server]
\nheadless = true
\nport = $PORT
\nenableXsrfProtection = false
\n" > ~/.streamlit/config.toml
