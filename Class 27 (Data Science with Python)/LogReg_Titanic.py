{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a85fb38e-be27-4619-bd46-dee2bee462d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>survived</th>\n",
       "      <th>pclass</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>sibsp</th>\n",
       "      <th>parch</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>class</th>\n",
       "      <th>who</th>\n",
       "      <th>adult_male</th>\n",
       "      <th>deck</th>\n",
       "      <th>embark_town</th>\n",
       "      <th>alive</th>\n",
       "      <th>alone</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>S</td>\n",
       "      <td>Third</td>\n",
       "      <td>man</td>\n",
       "      <td>True</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C</td>\n",
       "      <td>First</td>\n",
       "      <td>woman</td>\n",
       "      <td>False</td>\n",
       "      <td>C</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>S</td>\n",
       "      <td>Third</td>\n",
       "      <td>woman</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>S</td>\n",
       "      <td>First</td>\n",
       "      <td>woman</td>\n",
       "      <td>False</td>\n",
       "      <td>C</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>S</td>\n",
       "      <td>Third</td>\n",
       "      <td>man</td>\n",
       "      <td>True</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   survived  pclass     sex   age  sibsp  parch     fare embarked  class  \\\n",
       "0         0       3    male  22.0      1      0   7.2500        S  Third   \n",
       "1         1       1  female  38.0      1      0  71.2833        C  First   \n",
       "2         1       3  female  26.0      0      0   7.9250        S  Third   \n",
       "3         1       1  female  35.0      1      0  53.1000        S  First   \n",
       "4         0       3    male  35.0      0      0   8.0500        S  Third   \n",
       "\n",
       "     who  adult_male deck  embark_town alive  alone  \n",
       "0    man        True  NaN  Southampton    no  False  \n",
       "1  woman       False    C    Cherbourg   yes  False  \n",
       "2  woman       False  NaN  Southampton   yes   True  \n",
       "3  woman       False    C  Southampton   yes  False  \n",
       "4    man        True  NaN  Southampton    no   True  "
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd, numpy as np\n",
    "import matplotlib.pyplot as plt, seaborn as sns\n",
    "\n",
    "titanic = sns.load_dataset('titanic')\n",
    "titanic.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7d9dba68-f886-47e5-8944-63356b936232",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(891, 15)"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "583657be-65cd-4b9c-a269-833e3426cfa8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "survived         0\n",
       "pclass           0\n",
       "sex              0\n",
       "age            177\n",
       "sibsp            0\n",
       "parch            0\n",
       "fare             0\n",
       "embarked         2\n",
       "class            0\n",
       "who              0\n",
       "adult_male       0\n",
       "deck           688\n",
       "embark_town      2\n",
       "alive            0\n",
       "alone            0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ea0e83bf-74ae-4a9d-a6fa-e34307682656",
   "metadata": {},
   "outputs": [],
   "source": [
    "titanic = titanic.dropna(subset=['age','embarked', 'deck','embark_town'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d38b9fe7-0d1a-467e-94a7-a5a97e77af66",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>survived</th>\n",
       "      <th>pclass</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>sibsp</th>\n",
       "      <th>parch</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>class</th>\n",
       "      <th>who</th>\n",
       "      <th>adult_male</th>\n",
       "      <th>deck</th>\n",
       "      <th>embark_town</th>\n",
       "      <th>alive</th>\n",
       "      <th>alone</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C</td>\n",
       "      <td>First</td>\n",
       "      <td>woman</td>\n",
       "      <td>False</td>\n",
       "      <td>C</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>S</td>\n",
       "      <td>First</td>\n",
       "      <td>woman</td>\n",
       "      <td>False</td>\n",
       "      <td>C</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>male</td>\n",
       "      <td>54.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>51.8625</td>\n",
       "      <td>S</td>\n",
       "      <td>First</td>\n",
       "      <td>man</td>\n",
       "      <td>True</td>\n",
       "      <td>E</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>female</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>16.7000</td>\n",
       "      <td>S</td>\n",
       "      <td>Third</td>\n",
       "      <td>child</td>\n",
       "      <td>False</td>\n",
       "      <td>G</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>58.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>26.5500</td>\n",
       "      <td>S</td>\n",
       "      <td>First</td>\n",
       "      <td>woman</td>\n",
       "      <td>False</td>\n",
       "      <td>C</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    survived  pclass     sex   age  sibsp  parch     fare embarked  class  \\\n",
       "1          1       1  female  38.0      1      0  71.2833        C  First   \n",
       "3          1       1  female  35.0      1      0  53.1000        S  First   \n",
       "6          0       1    male  54.0      0      0  51.8625        S  First   \n",
       "10         1       3  female   4.0      1      1  16.7000        S  Third   \n",
       "11         1       1  female  58.0      0      0  26.5500        S  First   \n",
       "\n",
       "      who  adult_male deck  embark_town alive  alone  \n",
       "1   woman       False    C    Cherbourg   yes  False  \n",
       "3   woman       False    C  Southampton   yes  False  \n",
       "6     man        True    E  Southampton    no   True  \n",
       "10  child       False    G  Southampton   yes  False  \n",
       "11  woman       False    C  Southampton   yes   True  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ace153dd-7b24-46b0-92e0-9891de787669",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(182, 15)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4d1499b0-a510-43a8-99eb-d07d4fde7d4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "male      94\n",
       "female    88\n",
       "Name: sex, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.sex.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5ed93c69-0d15-46fc-aec5-0d79e840678e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "S    115\n",
       "C     65\n",
       "Q      2\n",
       "Name: embarked, dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.embarked.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bdf99055-778a-4307-9dd9-f872d1b3dc0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Converting the categorical cols into numerical\n",
    "\n",
    "titanic['sex'] = titanic['sex'].map({'male':0, 'female':1})\n",
    "titanic['embarked'] = titanic['embarked'].map({'S':0,'C':1,'Q':2})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ab67b050-fd1c-48b1-bd5b-983111c99f8a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>survived</th>\n",
       "      <th>pclass</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>sibsp</th>\n",
       "      <th>parch</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>class</th>\n",
       "      <th>who</th>\n",
       "      <th>adult_male</th>\n",
       "      <th>deck</th>\n",
       "      <th>embark_town</th>\n",
       "      <th>alive</th>\n",
       "      <th>alone</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>1</td>\n",
       "      <td>First</td>\n",
       "      <td>woman</td>\n",
       "      <td>False</td>\n",
       "      <td>C</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>0</td>\n",
       "      <td>First</td>\n",
       "      <td>woman</td>\n",
       "      <td>False</td>\n",
       "      <td>C</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>54.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>51.8625</td>\n",
       "      <td>0</td>\n",
       "      <td>First</td>\n",
       "      <td>man</td>\n",
       "      <td>True</td>\n",
       "      <td>E</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>16.7000</td>\n",
       "      <td>0</td>\n",
       "      <td>Third</td>\n",
       "      <td>child</td>\n",
       "      <td>False</td>\n",
       "      <td>G</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>58.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>26.5500</td>\n",
       "      <td>0</td>\n",
       "      <td>First</td>\n",
       "      <td>woman</td>\n",
       "      <td>False</td>\n",
       "      <td>C</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    survived  pclass  sex   age  sibsp  parch     fare  embarked  class  \\\n",
       "1          1       1    1  38.0      1      0  71.2833         1  First   \n",
       "3          1       1    1  35.0      1      0  53.1000         0  First   \n",
       "6          0       1    0  54.0      0      0  51.8625         0  First   \n",
       "10         1       3    1   4.0      1      1  16.7000         0  Third   \n",
       "11         1       1    1  58.0      0      0  26.5500         0  First   \n",
       "\n",
       "      who  adult_male deck  embark_town alive  alone  \n",
       "1   woman       False    C    Cherbourg   yes  False  \n",
       "3   woman       False    C  Southampton   yes  False  \n",
       "6     man        True    E  Southampton    no   True  \n",
       "10  child       False    G  Southampton   yes  False  \n",
       "11  woman       False    C  Southampton   yes   True  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "961045d1-f76c-4a0d-8140-d8e9fcf6f13e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/tmp/ipykernel_6220/3283234111.py:1: FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.\n",
      "  sns.heatmap(titanic.corr(), annot = True)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(titanic.corr(), annot = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d9ce55fe-1a5f-4e73-bf85-8aae3aae04de",
   "metadata": {},
   "outputs": [],
   "source": [
    "# identify which is X and y \n",
    "\n",
    "X = titanic[['sex', 'age', 'pclass', 'sibsp', 'parch', 'fare','embarked']]\n",
    "y = titanic['survived']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "03fa665c-b205-46a0-870d-96dddbea30aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# train test split\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import accuracy_score, confusion_matrix, classification_report"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "bb5abebd-d9f1-49b8-8c26-a511d50903f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "daa99517-2f4f-4fb9-816a-ab806232a0d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression(max_iter=1000)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression(max_iter=1000)</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LogisticRegression(max_iter=1000)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Initialize and fit the Logistic regression model\n",
    "\n",
    "logreg = LogisticRegression(max_iter = 1000)\n",
    "logreg.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "d555cb5e-39b3-4e65-ab73-3ea8dffa5fbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0,\n",
       "       0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1])"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred = logreg.predict(X_test)\n",
    "y_pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "c15b542d-5d74-48a8-8281-a2a013c8b739",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy : 62.16%\n"
     ]
    }
   ],
   "source": [
    "# Evalute the model \n",
    "\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "print(f'Accuracy : {accuracy *100:.2f}%')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "ee8fa521-8151-4ebd-a345-08c0139e3608",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 8  5]\n",
      " [ 9 15]]\n"
     ]
    }
   ],
   "source": [
    "# confusion matrix\n",
    "\n",
    "conf_matrix = confusion_matrix(y_test, y_pred)\n",
    "print(conf_matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "78328619-21ba-462f-bc87-ba51fe84c982",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Classification Report:               precision    recall  f1-score   support\n",
      "\n",
      "           0       0.47      0.62      0.53        13\n",
      "           1       0.75      0.62      0.68        24\n",
      "\n",
      "    accuracy                           0.62        37\n",
      "   macro avg       0.61      0.62      0.61        37\n",
      "weighted avg       0.65      0.62      0.63        37\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"Classification Report:\",classification_report(y_test, y_pred) )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "6079baa7-3142-4f92-9e06-573f49b66885",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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A+DCRpAAKln16tXVrFmzCr33iiuuUG5urqpUqaLGjRuX+55WrVppx44duu2228rO7dix46z3bN68uaKiorRx40aNHDnyjOu/rIkoKSkpOxcXF6eGDRtq3759GjZsWLn3bd26tVasWKFTp06VhZVz1QHAHRhtACHsmmuuUdeuXZWcnKy3335b+/fv1/bt2/Xwww8rIyNDkjR27FgtXbpUS5cu1e7duzVt2jR99tlnZ71n1apVNXnyZD3wwAN64YUXtHfvXu3YsUP/+Mc/JEn16tVTVFSU3nrrLX333Xc6ceKEpJ8/5Co1NVXPPPOMdu/erU8++UTLli3T008/LUkaOnSowsLCdNddd2nXrl1at26dnnrqKcO/QwCcRpAAQpjH49G6det05ZVX6s4771SLFi108803a//+/YqLi5MkDRkyRFOnTtXkyZPVsWNHHThwQPfcc8857ztlyhRNnDhRU6dOVatWrTRkyBDl5eVJkqpUqaJnn31WCxcuVHx8vAYNGiRJGjlypJYsWaLly5erXbt26tWrl5YvX162XbRGjRp6/fXXtWvXLnXo0EEPPfSQZs6cafB3B0Ao8PgZbAIAAIvoSAAAAMsIEgAAwDKCBAAAsIwgAQAALCNIAAAAywgSAADAMoIEAACwjCABAAAsI0gAAADLCBIAAMAyggQAALDs/wMxNQoZTSUdOgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = 'Blues')\n",
    "plt.ylabel(\"Actual\")\n",
    "plt.xlabel(\"Predicted\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "248d627d-519e-4410-b934-91bf699c58d4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-panel-2023.05-py310",
   "language": "python",
   "name": "conda-env-anaconda-panel-2023.05-py310-py"
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
