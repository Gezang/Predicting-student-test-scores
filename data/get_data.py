
import kaggle as kg

COMPETITION = "playground-series-s6e1"
OUT_DIR = "./data/"

# Download data from Kaggle into ./data/.
# Requires KAGGLE_USERNAME and KAGGLE_KEY in your environment.
# https://www.kaggle.com/competitions/playground-series-s6e1/overview
kg.api.competition_download_files(COMPETITION, path=OUT_DIR, quiet=False)
