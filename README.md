# Diabetes Prediction System

A lightweight Streamlit app that loads a trained machine-learning model from `model.pkl` and predicts whether a user is diabetic based on two inputs: glucose level and BMI.

## Features

- Simple Streamlit interface
- Predicts from two inputs: glucose and BMI
- Clear result feedback for diabetic and non-diabetic outcomes

## Requirements

- Python 3.12 or later
- `streamlit`
- A trained model saved as `model.pkl` in the project root

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install streamlit
```

If your model was trained with scikit-learn or another library, install the matching training-time packages as well.

## Run the app

```bash
streamlit run main.py
```

## Usage

1. Enter the glucose level.
2. Enter the BMI value.
3. Click Predict to see the result.

## Project Structure

```text
main.py
model.pkl
README.md
.gitignore
```

## Notes

- The app expects `model.pkl` to be present next to `main.py`.
- If you replace the model, make sure the new model exposes a compatible `predict()` method.
