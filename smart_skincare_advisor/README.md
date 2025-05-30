# Smart Skincare Advisor

A simple Streamlit app that simulates facial skin concern detection and recommends ingredients and DIY remedies.

## 🧰 Requirements

- Python 3.8+
- pip

## 🚀 Setup & Run (VS Code Terminal)

1. **Open VS Code** and open the folder `smart_skincare_advisor`.
2. Open the terminal: View > Terminal (or press Ctrl + `).
3. Create a virtual environment:

   On Windows:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the app:
   ```
   streamlit run app.py
   ```

6. The app will open in your browser at http://localhost:8501

## 📁 Project Structure

- `app.py`: Main Streamlit app
- `skin_analysis.py`: Simulated concern detection
- `recommendations.py`: Concern to recommendation logic
- `sample_data/`: JSON files with sample data