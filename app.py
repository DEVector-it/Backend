import os
import json
from flask import Flask, Response, request, stream_with_context
import google.generativeai as genai

# --- 1. Configure your API Key ---
# The API key is loaded from an environment variable for security.
# Before running this script, set the environment variable:
# On macOS/Linux: export GEMINI_API_KEY="YOUR_API_KEY"
# On Windows: set GEMINI_API_KEY="YOUR_API_KEY"
try:
    # Replace "YOUR_API_KEY" with your actual key if you are not using environment variables
    # For example: api_key = "AIza..."
    api_key = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY") # Fallback for simplicity
    if api_key == "YOUR_API_KEY":
        print("WARNING: Using a placeholder API key. Please set your GEMINI_API_KEY.")
    genai.configure(api_key=api_key)
except KeyError:
    print("FATAL ERROR: GEMINI_API_KEY environment variable not set.")
    print("Please set the key before running the script.")
    exit()

# --- 2. HTML, CSS, and JavaScript Frontend ---
# All the frontend code is stored in this single string.