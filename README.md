# Predicting Student Test Scores

This project explores classical ML and neural network approaches for the Kaggle Playground Series S6E1 competition: predicting student test scores from demographic and school-related features.

## Dataset

- Source: Kaggle Playground Series S6E1
- Competition page: https://www.kaggle.com/competitions/playground-series-s6e1/overview
- Data is not stored in this repo. Use the download script below.

## Project structure

```
Notebooks/
  XGBoost.ipynb
  Neural_network.ipynb
data/
  get_data.py
README.md
```

## Setup

1. Create a Python environment (3.10+ recommended).
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Configure Kaggle credentials:
   - Set `KAGGLE_USERNAME` and `KAGGLE_KEY` environment variables, or
   - Follow Kaggle API setup instructions in the Kaggle docs.

## Download data

```
python data/get_data.py
```

## Notebooks

- `Notebooks/XGBoost.ipynb`: feature engineering + XGBoost model.
- `Notebooks/Neural_network.ipynb`: (Under development) PyTorch-based neural network model.

## Results

Results can be found in the notebooks.
