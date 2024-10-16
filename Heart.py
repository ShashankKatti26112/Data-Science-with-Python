{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fd2a0604-0ca9-4cf2-b00b-f06c24fda32f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt  \n",
    "import seaborn as sns \n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import accuracy_score, confusion_matrix, classification_report"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "240faee9-7fe6-4e52-80fb-7534bb0a34f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load the dataset into a DataFrame\n",
    "df = pd.read_csv(\"C:/Users/hp/Downloads/heart_v2.csv\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
