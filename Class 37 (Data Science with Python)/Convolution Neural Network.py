{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8c76ce7b-411d-49ac-80ae-33953bbc668d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# importing the necessary libraries \n",
    "\n",
    "import numpy as np, pandas as pd\n",
    "import matplotlib.pyplot as plt, seaborn as sns\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "13ddebaa-9aed-4d1d-b894-92339fd66f46",
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
       "      <th>label</th>\n",
       "      <th>pixel0</th>\n",
       "      <th>pixel1</th>\n",
       "      <th>pixel2</th>\n",
       "      <th>pixel3</th>\n",
       "      <th>pixel4</th>\n",
       "      <th>pixel5</th>\n",
       "      <th>pixel6</th>\n",
       "      <th>pixel7</th>\n",
       "      <th>pixel8</th>\n",
       "      <th>...</th>\n",
       "      <th>pixel774</th>\n",
       "      <th>pixel775</th>\n",
       "      <th>pixel776</th>\n",
       "      <th>pixel777</th>\n",
       "      <th>pixel778</th>\n",
       "      <th>pixel779</th>\n",
       "      <th>pixel780</th>\n",
       "      <th>pixel781</th>\n",
       "      <th>pixel782</th>\n",
       "      <th>pixel783</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 785 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   label  pixel0  pixel1  pixel2  pixel3  pixel4  pixel5  pixel6  pixel7  \\\n",
       "0      1       0       0       0       0       0       0       0       0   \n",
       "1      0       0       0       0       0       0       0       0       0   \n",
       "2      1       0       0       0       0       0       0       0       0   \n",
       "3      4       0       0       0       0       0       0       0       0   \n",
       "4      0       0       0       0       0       0       0       0       0   \n",
       "\n",
       "   pixel8  ...  pixel774  pixel775  pixel776  pixel777  pixel778  pixel779  \\\n",
       "0       0  ...         0         0         0         0         0         0   \n",
       "1       0  ...         0         0         0         0         0         0   \n",
       "2       0  ...         0         0         0         0         0         0   \n",
       "3       0  ...         0         0         0         0         0         0   \n",
       "4       0  ...         0         0         0         0         0         0   \n",
       "\n",
       "   pixel780  pixel781  pixel782  pixel783  \n",
       "0         0         0         0         0  \n",
       "1         0         0         0         0  \n",
       "2         0         0         0         0  \n",
       "3         0         0         0         0  \n",
       "4         0         0         0         0  \n",
       "\n",
       "[5 rows x 785 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# load the train data \n",
    "train = pd.read_csv(\"train.csv\")\n",
    "train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "014680e1-ee32-472d-adab-9199b44b11be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(42000, 785)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c8486b8c-8d2c-430a-961c-c50dc3f64476",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 42000 entries, 0 to 41999\n",
      "Columns: 785 entries, label to pixel783\n",
      "dtypes: int64(785)\n",
      "memory usage: 251.5 MB\n"
     ]
    }
   ],
   "source": [
    "train.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "069c2bae-3df3-4bd9-a695-ccab8128891f",
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
       "      <th>pixel0</th>\n",
       "      <th>pixel1</th>\n",
       "      <th>pixel2</th>\n",
       "      <th>pixel3</th>\n",
       "      <th>pixel4</th>\n",
       "      <th>pixel5</th>\n",
       "      <th>pixel6</th>\n",
       "      <th>pixel7</th>\n",
       "      <th>pixel8</th>\n",
       "      <th>pixel9</th>\n",
       "      <th>...</th>\n",
       "      <th>pixel774</th>\n",
       "      <th>pixel775</th>\n",
       "      <th>pixel776</th>\n",
       "      <th>pixel777</th>\n",
       "      <th>pixel778</th>\n",
       "      <th>pixel779</th>\n",
       "      <th>pixel780</th>\n",
       "      <th>pixel781</th>\n",
       "      <th>pixel782</th>\n",
       "      <th>pixel783</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 784 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   pixel0  pixel1  pixel2  pixel3  pixel4  pixel5  pixel6  pixel7  pixel8  \\\n",
       "0       0       0       0       0       0       0       0       0       0   \n",
       "1       0       0       0       0       0       0       0       0       0   \n",
       "2       0       0       0       0       0       0       0       0       0   \n",
       "3       0       0       0       0       0       0       0       0       0   \n",
       "4       0       0       0       0       0       0       0       0       0   \n",
       "\n",
       "   pixel9  ...  pixel774  pixel775  pixel776  pixel777  pixel778  pixel779  \\\n",
       "0       0  ...         0         0         0         0         0         0   \n",
       "1       0  ...         0         0         0         0         0         0   \n",
       "2       0  ...         0         0         0         0         0         0   \n",
       "3       0  ...         0         0         0         0         0         0   \n",
       "4       0  ...         0         0         0         0         0         0   \n",
       "\n",
       "   pixel780  pixel781  pixel782  pixel783  \n",
       "0         0         0         0         0  \n",
       "1         0         0         0         0  \n",
       "2         0         0         0         0  \n",
       "3         0         0         0         0  \n",
       "4         0         0         0         0  \n",
       "\n",
       "[5 rows x 784 columns]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test = pd.read_csv('test.csv')\n",
    "test.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9a4aa4e6-09d1-4ea0-ae08-59a1eaf33143",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(28000, 784)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c73961ac-1ba1-46bd-9c9d-5ffddcf347ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 28000 entries, 0 to 27999\n",
      "Columns: 784 entries, pixel0 to pixel783\n",
      "dtypes: int64(784)\n",
      "memory usage: 167.5 MB\n"
     ]
    }
   ],
   "source": [
    "test.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f08dcd9a-64c7-434c-a54a-cf4025447f21",
   "metadata": {},
   "outputs": [],
   "source": [
    "# put the labels columns as y_train \n",
    "\n",
    "y_train = train['label']\n",
    "X_train = train.drop(labels = ['label'], axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "653e55ba-d8d9-4d5d-9bab-edfb844e3abd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1\n",
       "1    0\n",
       "2    1\n",
       "3    4\n",
       "4    0\n",
       "Name: label, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "966fbcd8-5c20-4563-9924-d56313f493a2",
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
       "      <th>pixel0</th>\n",
       "      <th>pixel1</th>\n",
       "      <th>pixel2</th>\n",
       "      <th>pixel3</th>\n",
       "      <th>pixel4</th>\n",
       "      <th>pixel5</th>\n",
       "      <th>pixel6</th>\n",
       "      <th>pixel7</th>\n",
       "      <th>pixel8</th>\n",
       "      <th>pixel9</th>\n",
       "      <th>...</th>\n",
       "      <th>pixel774</th>\n",
       "      <th>pixel775</th>\n",
       "      <th>pixel776</th>\n",
       "      <th>pixel777</th>\n",
       "      <th>pixel778</th>\n",
       "      <th>pixel779</th>\n",
       "      <th>pixel780</th>\n",
       "      <th>pixel781</th>\n",
       "      <th>pixel782</th>\n",
       "      <th>pixel783</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 784 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   pixel0  pixel1  pixel2  pixel3  pixel4  pixel5  pixel6  pixel7  pixel8  \\\n",
       "0       0       0       0       0       0       0       0       0       0   \n",
       "1       0       0       0       0       0       0       0       0       0   \n",
       "2       0       0       0       0       0       0       0       0       0   \n",
       "3       0       0       0       0       0       0       0       0       0   \n",
       "4       0       0       0       0       0       0       0       0       0   \n",
       "\n",
       "   pixel9  ...  pixel774  pixel775  pixel776  pixel777  pixel778  pixel779  \\\n",
       "0       0  ...         0         0         0         0         0         0   \n",
       "1       0  ...         0         0         0         0         0         0   \n",
       "2       0  ...         0         0         0         0         0         0   \n",
       "3       0  ...         0         0         0         0         0         0   \n",
       "4       0  ...         0         0         0         0         0         0   \n",
       "\n",
       "   pixel780  pixel781  pixel782  pixel783  \n",
       "0         0         0         0         0  \n",
       "1         0         0         0         0  \n",
       "2         0         0         0         0  \n",
       "3         0         0         0         0  \n",
       "4         0         0         0         0  \n",
       "\n",
       "[5 rows x 784 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "af85817c-9ead-4b8d-a55c-f81f3372a40d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAGZCAYAAABmNy2oAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAPqElEQVR4nO3cfazW8//A8delU51yXym5aeWshlIY1kFWytyG3G3JzWn8wdzMP23ummRm2dhCf7FGJeYmd2HsoJhzkNwsUo2tTNpCWLOD1PX9w3r99Dtxrs/lOqIej7+4rs/r83lff3Q9r/d1zvmUyuVyOQAgInbb0QsA4N9DFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFCikpaUlpk2bFj/88EPNz93U1BQDBw6s2flWr14dpVIpHn744Xzs4YcfjlKpFKtXr67Zdf6oqakpSqVSlEqlGDZsWLvnm5ubo7GxMXr27Bl9+vSJpqamWL9+fcXnr2T+o48+yjWUSqV46qmn/vbrYtchChTS0tISt99+e6dEYerUqfHMM8/U7Hz9+/eP1tbWOPPMM2t2zkrsv//+0draGvPnz9/m8cWLF8fpp58e/fr1i+eeey5mzpwZzc3NMXbs2Pjll186PG+l80OGDInW1taYNWtWzV8bO7+6Hb0Adl5tbW3Ro0ePio9vaGio6fW7d+8eI0eOrOk5/851p0yZEkOGDImnnnoq6up+/6c3aNCgOOGEE2L27Nlx9dVX/+V5K53v2bNnjBw5Mn7++ecavzJ2BXYKVGzatGkxZcqUiPj9zWjr1xOLFi2KgQMHxllnnRULFiyIo446Kurr6+P222+PiIhZs2bFSSedFH379o3dd989jjjiiLj77rtj06ZN25x/e18flUqluPbaa2Pu3Llx2GGHRc+ePWPEiBGxcOHCDte7va+P/szs2bNjxIgRUV9fH7169YoJEybEZ5991u64d999N8aPHx+9e/eO+vr6aGhoiBtuuKHD869duzaWLFkSl156ab6hR0Qcf/zxMWTIkA53SH93Hiplp0DFrrzyytiwYUPcf//9sWDBgujfv39ERBx++OEREfHBBx/EZ599FrfeemsMGjQodt9994iI+OKLL+Liiy+OQYMGRbdu3eLjjz+OO++8M1asWBGzZ8/u8LovvvhiLFmyJKZPnx577LFH3H333TFhwoRYuXJlHHLIIX/7dd11111x8803x8SJE+Ouu+6K7777LqZNmxaNjY2xZMmSGDx4cEREvPLKKzF+/Pg47LDD4t57740BAwbE6tWr49VXX+3wGp988klERAwfPrzdc8OHD4+33367U+ehUqJAxQ466KAYMGBAREQcddRR7T7Vr1+/PpYvXx5DhgzZ5vF77703/3vLli0xatSo6N27d0yePDnuueee2Hffff/yum1tbdHc3Bx77rlnREQcffTRccABB8QTTzwRN9544996TT/88EPccccdccYZZ2zzM4DRo0fH4MGDY9q0afHoo49GRMQ111wTAwYMiHfffTfq6+vz2MmTJ3d4ne+++y4iInr16tXuuV69euXznTUPlfL1ETUzfPjwdkGIiPjwww/j7LPPjt69e0eXLl2ia9eucdlll8XmzZtj1apVHZ53zJgxGYSIiH79+kXfvn1jzZo1f3vNra2t0dbWFk1NTds8fvDBB8fJJ58cr732WkRErFq1Kr744ou44oortglCUaVSqdDjtZ6HjogCNbP166Q/+vLLL2PUqFGxdu3amDlzZrz11luxZMmS/M2Ytra2Ds/bu3fvdo917969otmObP2Evb21H3DAAfn8N998ExG/75aqsfU1bO8T/YYNG7a7A6jlPFRKFKiZ7X1affbZZ+Onn36KBQsWxCWXXBInnnhiHHPMMdGtW7cdsML2tr7Zrlu3rt1zX3/9dfTp0yciIvbbb7+IiPjqq6+qus7Wv1lYtmxZu+eWLVu23b9pqOU8VEoUKKR79+4RUdkn/Ij/C8XWuYiIcrkcDz74YO0XV4XGxsbo0aNHzJs3b5vHv/rqq3j99ddj7NixEfH77/43NDTE7NmzK/qbgv/vwAMPjOOOOy7mzZsXmzdvzsffeeedWLlyZZx33nmdOg+VEgUKOeKIIyIiYubMmdHa2hrvv/9+bNy48U+PP+WUU6Jbt24xceLEePnll+OZZ56JU089Nb7//vuarmvx4sVRV1cX06dPLzS3zz77xNSpU+P555+Pyy67LF5++eWYN29ejBkzJurr6+O2227LY2fNmhVr1qyJkSNHxpw5c2LRokUxZ86cmDRpUkXXmjFjRqxYsSIuvPDCaG5ujvnz58dFF10Uw4YNa/fD6oEDB7b7QX6ReaiWKFDI6NGj46abbooXXnghTjzxxDj22GNj6dKlf3r8oYceGk8//XR8//33cd5558V1110XRx55ZNx33301XVe5XI7NmzfHli1bCs/edNNN8dBDD8XHH38c5557blx77bUxdOjQaGlpyV9HjYg49dRT480334z+/fvH9ddfH6eddlpMnz49+vXrV9F1Ro8eHS+99FKsW7cuxo8fH9ddd12MGTMmXnvttW12UhERP/30U7ufcxSZh2qVyuVyeUcvAnYWTU1NsWjRovj888+jVCpFly5dCp9j+fLlMXTo0Fi4cGHVt+j47bffYvHixTFu3Lh48skn44ILLqjqPOx67BSgxtasWRNdu3aNESNGVDX/xhtvRGNjY9VB+Oijj6Jr164xbty4qubZtdkpQA2tXr06vv3224iI6NGjRwwdOvQfX0NbW1t8+umn+f8NDQ0d/oEgbCUKACRfHwGQRAGAJAoApIrvkuqGWwD/bZX8CNlOAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIAqW5HLwD472tubi48M3bs2KqudfnllxeemTNnTlXX2hXZKQCQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAILkhHrCNN954o/DMCSecUHhmy5YthWciIsrlclVzVMZOAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIAyQ3xYCd2yy23FJ5pbGwsPNOlS5fCM0888UThmYiIp59+uqo5KmOnAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAVCqXy+WKDiyVOnstwF8499xzC8889thjhWe6detWeGbZsmWFZ0aNGlV4JiJi48aNVc0RUcnbvZ0CAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQ6nb0AmBXc/DBB1c1d9tttxWeqeaOpxs2bCg8M3Xq1MIz7nb672SnAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAVCqXy+WKDiyVOnst8J9z3HHHFZ558MEHq7rWsGHDqporatKkSYVnHn/88U5YCbVWydu9nQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAFLdjl4A/FtceumlhWceeeSRwjMV3oOynR9//LHwTHNzc+GZV155pfAMOw87BQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJDfEY6fUr1+/wjNTpkzphJXUznPPPVd4ZvLkyZ2wEnZmdgoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEByl1T+9fbZZ5/CM6+++mrhmaFDhxaeqcbGjRurmnv++edrvBJoz04BgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgCpVC6XyxUdWCp19lpguw488MDCM19++WUnrKS9av5d7L333lVdq9ob6cFWlbzd2ykAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACDV7egFsOvo06dPVXMvvPBC4Zl/6gaO77zzTuGZX3/9tRNWArVhpwBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgOSGePxjHnjggarmRowYUXimXC4XnmlpaSk8M27cuMIzv/zyS+EZ+KfYKQCQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAILkhHlXp06dP4ZmGhoZOWMn2bdq0qfDMjBkzCs+4uR07GzsFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAguUsq0bdv38Iz8+fPLzxz9NFHF56JiPj5558Lz1x11VWFZxYuXFh4BnY2dgoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEhuiEdMmDCh8MyYMWM6YSXb99577xWemTt3biesBHZ+dgoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEhuiLeTmThxYuGZGTNmdMJK2mtpaalq7uKLL67xSoA/Y6cAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYBUKpfL5YoOLJU6ey38wd57713V3NKlSwvPDBo0qKprFXX++edXNffss8/WdiGwi6rk7d5OAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIAqW5HL4DtO+ecc6qa+6dubleNvfbaa0cvAeiAnQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJDcJfVfatOmTVXNbdmypfDMbrsV/2ywefPmwjODBw8uPAP8s+wUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQSuVyuVzRgaVSZ6+FGli+fHnhmbq64vdFvPPOOwvPPPLII4VngNqp5O3eTgGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAMkN8QB2EW6IB0AhogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkOoqPbBcLnfmOgD4F7BTACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACD9DzqsUpuUQtNrAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot some samples in the train\n",
    "\n",
    "img = X_train.iloc[0].values\n",
    "img = img.reshape((28,28))\n",
    "plt.imshow(img, cmap = 'gray')\n",
    "plt.title('train.iloc[0,0]')\n",
    "plt.axis('off')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f3303472-652b-44f6-9856-f7f6607eae5b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAGZCAYAAABmNy2oAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAT+0lEQVR4nO3dfZBVdf3A8c8VFpaHRB7SZVWwQIohQJ1GZJLaldnK1FQcKhzQdaSxMk2dQGvS3bUxCSaLMaeZfB4VrUlsUvMp2SUmwRyt0dRGRWA1mTDChMSSOL8/is+PdVe4rAsLy+s140yce865H5a7+77n3r3fSkVRFAEAEXFAdw8AwN5DFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFHqwxx57LBobG+ONN97o8nPX19fHEUcc0WXnW716dZRKpbjlllty2y233BKlUilWr17dZfezvfr6+iiVSlEqleJjH/tYbn/zzTfjqquuipqamqiqqoqBAwfG+PHj4/vf/368/fbbHc7d0X933XVXu/t8+eWXY9q0aXHQQQfFwIEDo66uLp566qmy5m1sbOzwfiorKzvc/6677oqjjjoqKisro7q6Oi666KLYtGlTu/02bdoUF110UVRXV0dlZWUcddRRHc5+2mmndfj1omfp3d0DsPs89thj0dTUFPX19XHQQQd16bkvv/zy+MY3vtFl5xs+fHgsX748Ro0a1WXnLEdVVVXcc8890b9//9zW2toaP/rRj2LWrFlxySWXxMCBA2PZsmXR2NgYjzzySDzyyCNRKpXanOeCCy6IM888s822I488ss2fX3/99ZgyZUoMHjw4brrppqisrIyrr746ampq4oknnoiPfOQjZc384IMPxqBBg/LPBxzQ/rndHXfcETNnzozZs2fHD3/4w3jhhRfi0ksvjeeeey4efvjhNvtOmzYtnnjiiZg3b16MGTMmFi1aFDNmzIitW7e2+TvNnz8/Lrvssvja174W//73v8ualX1QQY+1YMGCIiKKVatW7XTft956a/cPtItuvvnmsufvjLPPPrsYOXJku+2bNm0qNm3a1G77tq/nsmXLctuqVauKiCgWLFiw0/ubM2dOUVFRUaxevTq3/eMf/yiGDRtWfOELX9jp8Q0NDUVEFK+//voO99uyZUsxfPjw4tOf/nSb7XfccUcREcWvf/3r3Hb//fcXEVEsWrSozb51dXVFdXV1sWXLlnbn/9SnPlWMGzdup/Oyb/LyUQ/V2NgYc+bMiYiID33oQ3nZ39LSEkcccUScfPLJsXjx4jj66KOjsrIympqaIiLiuuuui09+8pNx8MEHx4ABA2L8+PExf/78eOedd9qcv6OXj0qlUnz961+P2267LcaOHRv9+/ePiRMnxn333bfTeTt6+ei93HTTTTFx4sSorKyMIUOGxOmnnx7PP/98u/0ef/zxOOWUU2Lo0KFRWVkZo0aNiosuumin5x8wYEAMGDCg3fZjjz02IiJeeeWVnZ6jI/fcc0+ccMIJMXLkyNx24IEHxrRp0+Lee++NLVu2dOq877ZixYpYu3ZtnHPOOW22T58+PQYOHBj33HNPm5kGDhwY06dPb7PvOeecE6+99lo8/vjjXTIT+w5R6KFmz54dF1xwQURELF68OJYvXx7Lly+PY445JiIinnrqqZgzZ05ceOGF8eCDD8YZZ5wRERErV66MM888M2677ba477774txzz40FCxbEeeedV9b93n///fHjH/84rrzyyrj77rvzh/bLL7/cJX+vq6++Os4999wYN25cLF68OBYuXBhPP/10TJ48OV588cXc76GHHoopU6ZEa2trXHPNNfHAAw/Ed77znfjrX//a6ftesmRJRESMGzeu3W3z5s2LPn36RP/+/eP444+PX/3qV21u37x5c6xcuTImTJjQ7tgJEybE5s2by/4ajR8/Pnr16hWHHHJInHXWWdHa2trm9j/96U953u1VVFTERz/60bx9275jx46N3r3bvpK87djt92X/4D2FHuqwww6LESNGRETE0Ucf3e5Z/bp16+K5556LMWPGtNl+zTXX5P/eunVrTJkyJYYOHRrnnHNO/OAHP4jBgwfv8H43b94cv/nNb+IDH/hAREQcc8wxUV1dHT//+c/jsssue19/pzfeeCO++93vxuc+97lYtGhRbq+pqYkjjzwyGhsb44477oiIiPPPPz9GjBgRjz/+eJs3Yt/97LlcTz/9dMyfPz9OP/30Nj9s+/btG1/+8pejrq4uhg8fHq2trXHttdfGqaeeGtdff33Mnj07IiI2bNgQRVHEkCFD2p1727b169fvcIZRo0bFVVddlVd3v//972P+/Pnx8MMPx5NPPhmHHnpom/O8131t/8b9+vXr48Mf/nCnZ6LnEYX91IQJE9oFISLiD3/4QzQ0NMTvfve7+Pvf/97mthdeeCEmTZq0w/PW1tZmECIiDjnkkDj44INjzZo173vm5cuXx+bNm6O+vr7N9sMPPzxOOOGEePTRR3POlStXxve+9733/M2cXbF69eo4+eST4/DDD48bbrihzW3Dhw+Pn/70p222TZ8+PSZNmhSXXXZZ1NfXt3kW/u43qLe3o9siImbNmtXmz7W1tVFbWxuTJ0+O+fPnx8KFC8s637u3v5+Z6Hm8fLSfGj58eLttra2tMWXKlPjLX/4SCxcujGXLlsUTTzwR1113XUT89ypgZ4YOHdpuW9++fcs6dme2PWvtaPbq6uq8/fXXX4+I/14tvV9r1qyJ2tra6N27dzz66KMdPvt+t4qKivjiF78Y69evz5e0Bg8eHKVSqcNn3tviW8653+3YY4+NMWPGxIoVK3Lbtn+D97qv7e9n6NChXT4T+zZR2E919Azwl7/8Zfzzn/+MxYsXx8yZM+P444+Pj3/849GnT59umLC9bT/s1q5d2+621157LYYNGxYRER/84AcjIuLVV199X/e3Zs2aqKmpiaIoorm5eZciU/zv/9Bw26+L9uvXL0aPHh3PPPNMu32feeaZ6NevX4cv45R7X9v/Wur48ePzvNvbsmVL/PnPf27zGYPx48fH888/3+5N7m3H+jzC/kcUerC+fftGRHnP8CP+PxTbjov47w+c66+/vuuH64TJkydHv3794vbbb2+z/dVXX40lS5bE1KlTIyJizJgxMWrUqLjpppviX//6V6fuq7W1NWpqauI///lPLFmypM1vDO3MO++8Ez/72c9i2LBhMXr06Nx++umnx5IlS9r89tLGjRtj8eLF8fnPf77dm73lWLFiRbz44otx3HHH5bZJkybF8OHD2/0m1y9+8YvYtGlTTJs2rc1MmzZtirvvvrvNvrfeemtUV1fv9OVCeh7vKfRg254xLly4MM4+++yoqKjY4Qek6urqok+fPjFjxoyYO3duvP322/GTn/wkNmzY0KVzLV26NKZOnRpXXHFFXHHFFWUfd9BBB8Xll18e3/72t+Oss86KGTNmxPr166OpqSkqKyujoaEh973uuuvilFNOieOOOy4uvvjiGDFiRLS2tsZDDz2Ub0a/l3Xr1kVtbW2sXbs2brzxxli3bl2sW7cubz/ssMPyquGSSy6Jd955Jz7xiU9EVVVVvPLKK3HttdfGH//4x7j55pujV69eedw3v/nNuO222+Kkk06KK6+8Mvr27Rvz5s2Lt99+OxobG9vMUF9fH7feemusWrUqf0lg4sSJMXPmzBg7dmy+0bxgwYKoqqqKuXPn5rG9evWK+fPnx6xZs+K8886LGTNmxIsvvhhz586Nurq6+OxnP5v7nnjiiVFXVxdf/epX480334zRo0fHnXfeGQ8++GDcfvvtbeZnP9Gtn5Jgt/vWt75VVFdXFwcccEAREUVzc3MxcuTI4qSTTupw/3vvvbeYOHFiUVlZWRx66KHFnDlzigceeCCP3aajD35FRHH++ee3O+fIkSOLs88+O//c3NxcRETR0NCQ27Z9COzmm2/Obe/14bUbbrihmDBhQtGnT59i0KBBxamnnlo8++yz7e53+fLlxYknnlgMGjSo6Nu3bzFq1Kji4osv3uHfYfv53uu/7ee+8cYbi2OPPbYYMmRI0bt372Lw4MHFZz7zmeKhhx5qd96iKIqXXnqpOO2004oDDzyw6N+/fzF16tTiySefbLffGWecUfTr16/YsGFDbvvSl75UjB49uhgwYEBRUVFRjBw5svjKV75SvPbaax3e16JFi/LrVFVVVVx44YXFxo0b2+23cePG4sILLyyqqqqKPn36FBMmTCjuvPPODs9ZFD681tOViuJ/L37Cfqa+vj5aWlripZdeilKptFc9K66qqopZs2bFggULunuUtHXr1ti6dWtMnTo11q9f7zMMPZT3FNivrVmzJioqKmLixIndPUp69tln46233opLL720u0dpY9q0aVFRURG//e1vu3sUdiNXCuy3Vq9eHX/7298i4r+/HdTRJ5X5fytXrsz3l3y9ei5RACB5+QiAJAoAJFEAIJX94TULYwHs28p5C9mVAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJ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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "img = X_train.iloc[250].values\n",
    "img = img.reshape((28,28))\n",
    "plt.imshow(img, cmap = 'gray')\n",
    "plt.title('train.iloc[250,500]')\n",
    "plt.axis('off')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d518dcab-ff8f-4762-9e84-7dad50bd959c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1    4684\n",
       "7    4401\n",
       "3    4351\n",
       "9    4188\n",
       "2    4177\n",
       "6    4137\n",
       "0    4132\n",
       "4    4072\n",
       "8    4063\n",
       "5    3795\n",
       "Name: label, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "5129a72f-8350-45b7-b5d7-4b379ba2f69a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABN8AAAJuCAYAAACAKaRXAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAABciklEQVR4nO3debhVZd0H/O+RWYSjjAcSFREFB1SgEPJJVEQNRfN51dJIy6kccci5RFNQcirJAUMh0QefyimfIjAURxRRCs0wDacE0UQQVEDY7x+97Lcj4AAsDhw+n+va18W+12+t9bvPjjh+91r3qiiVSqUAAAAAAGvcRjXdAAAAAADUVsI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAoNYZOXJkKioq0rBhw7z66qvLbe/du3d23HHHGugseeihh1JRUZHf/OY3NXL+L+qVV15Jv3790qxZs1RUVGTgwIFf+BgVFRUZNGhQ+f2yz+eVV15ZpX4qKioycuTI8tjjjz+eQYMG5b333vvCx1uZ1ekRAOA/Cd8AgFpr4cKFufDCC2u6jfXa6aefnieffDK33HJLnnjiiZx++umrfcx+/frliSeeSJs2bb7wvm3atMkTTzyRfv36lccef/zxXHzxxWs0fAMAWFPq1nQDAABF2W+//XLHHXfkrLPOys4771zT7axVH374YRo2bJiKiorVOs5zzz2Xr3zlKzn44IPXTGNJWrZsmZYtW67Svg0aNMhuu+22xnoBACiaK98AgFrr7LPPTvPmzXPOOed8at2KbmVc5pO3TA4aNCgVFRX5y1/+kkMPPTSVlZVp1qxZzjjjjHz88ceZPn169ttvvzRp0iRbbbVVhg4dusJzfvTRRznjjDNSVVWVRo0aZY899sizzz67XN3TTz+d/v37p1mzZmnYsGF23XXX/O///m+1mmW3SI4bNy7f+9730rJly2y88cZZuHDhSuf82muv5dvf/nZatWqVBg0apHPnzrnqqquydOnSJP//7bEvvfRS/vCHP6SiouIzb8OcN29ejjvuuDRv3jybbLJJ9ttvv7z44ovL1a3ols5SqZTBgwdnyy23TMOGDdO9e/eMHz8+vXv3Tu/evct1n/ysBg0alB/+8IdJkvbt25f7fOihh1baZ5I8+eSTOfDAA9O8efM0bNgwHTp0+MxbasePH5+DDjoom2++eRo2bJhtttkmJ5xwQt55551qdW+//XaOP/74tGvXLg0aNEjLli3z1a9+NQ888EC55tlnn80BBxxQ/vm3bds2/fr1yxtvvPGpPQAA6x9XvgEAtVaTJk1y4YUX5rTTTsuECROy1157rbFjH3bYYfn2t7+dE044IePHj8/QoUOzePHiPPDAAznxxBNz1lln5Y477sg555yTbbbZJocccki1/c8///x07do1v/zlLzN37twMGjQovXv3zrPPPputt946SfLggw9mv/32S48ePXLjjTemsrIyY8aMyeGHH54PPvggRx99dLVjfu9730u/fv1y2223ZcGCBalXr94Ke3/77bfTq1evLFq0KD/5yU+y1VZb5f77789ZZ52Vl19+Oddff326du2aJ554It/4xjfSoUOHXHnllUmy0ltFS6VSDj744Dz++OP58Y9/nC9/+ct57LHHsv/++3+un+cFF1yQIUOG5Pjjj88hhxyS119/Pccee2wWL16cbbfddqX7HXvssXn33Xdz3XXX5a677ir3t/322690nz/+8Y858MAD07lz51x99dXZYost8sorr2TcuHGf2uPLL7+cnj175thjj01lZWVeeeWVXH311dl9990zbdq08s97wIABeeaZZ3LZZZdl2223zXvvvZdnnnkm//rXv5IkCxYsyD777JP27dvnF7/4RVq3bp1Zs2blwQcfzPvvv/+5fl4AwHqkBABQy9x6662lJKXJkyeXFi5cWNp6661L3bt3Ly1durRUKpVKe+yxR2mHHXYo18+YMaOUpHTrrbcud6wkpYsuuqj8/qKLLiolKV111VXV6nbZZZdSktJdd91VHlu8eHGpZcuWpUMOOaQ89uCDD5aSlLp27Vrup1QqlV555ZVSvXr1Sscee2x5rFOnTqVdd921tHjx4mrnOuCAA0pt2rQpLVmypNp8v/Od73yun8+5555bSlJ68sknq43/4Ac/KFVUVJSmT59eHttyyy1L/fr1+8xj/uEPfyglKf3sZz+rNn7ZZZct9zNc1u+MGTNKpVKp9O6775YaNGhQOvzww6vt+8QTT5SSlPbYY4/y2Io+q5/+9KfVjvdZOnToUOrQoUPpww8/XGnNJ3v8pKVLl5YWL15cevXVV0tJSvfee2952yabbFIaOHDgSo/99NNPl5KU7rnnns/VLwCwfnPbKQBQq9WvXz+XXnppnn766eVu11wdBxxwQLX3nTt3TkVFRbUrverWrZttttlmhU9cPeKII6qtx7blllumV69eefDBB5MkL730Uv72t7/lyCOPTJJ8/PHH5dfXv/71zJw5M9OnT692zP/+7//+XL1PmDAh22+/fb7yla9UGz/66KNTKpUyYcKEz3Wc/7Ss72X9LnPEEUd85r6TJk3KwoULc9hhh1Ub32233bLVVlt94V4+zYsvvpiXX345xxxzTBo2bPiF9p09e3a+//3vp127dqlbt27q1auXLbfcMknywgsvlOu+8pWvZOTIkbn00kszadKkLF68uNpxttlmm2y22WY555xzcuONN+avf/3r6k8MAFhnCd8AgFrvm9/8Zrp27ZoLLrhguSBkVTVr1qza+/r162fjjTdeLtCpX79+Pvroo+X2r6qqWuHYslsT33rrrSTJWWedlXr16lV7nXjiiUmy3Fpjn/fpof/6179WWNu2bdvy9i/qX//6V+rWrZvmzZtXG1/RPFe0b5K0bt16uW0rGlsdb7/9dpJk8803/0L7LV26NH379s1dd92Vs88+O3/605/y1FNPZdKkSUn+/YCLZe68884cddRR+eUvf5mePXumWbNm+c53vpNZs2YlSSorKzNx4sTssssuOf/887PDDjukbdu2ueiii9bY/z4BgHWHNd8AgFqvoqIiV1xxRfbZZ58MHz58ue3LArNPPqBgVUKoz2tZEPPJsWXhVYsWLZIk55133nLrxS2z3XbbVXv/eZ9s2rx588ycOXO58TfffLPaub+I5s2b5+OPP86//vWvagHciua5on2T/z9w/E+zZs1ao1e/LXvK6hd9sMFzzz2XP//5zxk5cmSOOuqo8vhLL720XG2LFi1y7bXX5tprr81rr72W++67L+eee25mz56dsWPHJkl22mmnjBkzJqVSKX/5y18ycuTIXHLJJWnUqFHOPffc1ZghALCuceUbALBB6NOnT/bZZ59ccsklmT9/frVtrVu3TsOGDfOXv/yl2vi9995bWD//8z//k1KpVH7/6quv5vHHHy8/2XO77bZLx44d8+c//zndu3df4atJkyardO699947f/3rX/PMM89UG//Vr36VioqK7Lnnnl/4mMv2uf3226uN33HHHZ+5b48ePdKgQYPceeed1cYnTZq0wlt2P6lBgwZJql99tjLbbrttOnTokFtuueVTnwb7ScuCzWXnWuamm2761P222GKLnHzyydlnn32W+3kvO+7OO++ca665JptuuukKawCA9Zsr3wCADcYVV1yRbt26Zfbs2dlhhx3K4xUVFfn2t7+dW265JR06dMjOO++cp5566nMFR6tq9uzZ+cY3vpHjjjsuc+fOzUUXXZSGDRvmvPPOK9fcdNNN2X///bPvvvvm6KOPzpe+9KW8++67eeGFF/LMM8/k17/+9Sqd+/TTT8+vfvWr9OvXL5dcckm23HLL/N///V+uv/76/OAHP/jUp4uuTN++ffO1r30tZ599dhYsWJDu3bvnsccey2233faZ+zZr1ixnnHFGhgwZks022yzf+MY38sYbb+Tiiy9OmzZtstFGn/598U477ZQk+dnPfpajjjoq9erVy3bbbbfScPIXv/hFDjzwwOy22245/fTTs8UWW+S1117LH//4x+XCw2U6deqUDh065Nxzz02pVEqzZs3yu9/9LuPHj69WN3fu3Oy555454ogj0qlTpzRp0iSTJ0/O2LFjy1cw3n///bn++utz8MEHZ+utt06pVMpdd92V9957L/vss89n/rwAgPWL8A0A2GDsuuuu+da3vrXCUO2qq65KkgwdOjTz58/PXnvtlfvvv3+NL/i/zODBgzN58uR897vfzbx58/KVr3wlY8aMSYcOHco1e+65Z5566qlcdtllGThwYObMmZPmzZtn++23X+7hBF9Ey5Yt8/jjj+e8887Leeedl3nz5mXrrbfO0KFDc8YZZ6zSMTfaaKPcd999OeOMMzJ06NAsWrQoX/3qV/P73/8+nTp1+sz9L7vssjRu3Dg33nhjbr311nTq1Ck33HBDLrjggmy66aafum/v3r1z3nnnZdSoUbn55puzdOnSPPjgg+WrCD9p3333zcMPP5xLLrkkp556aj766KNsvvnm6d+//0rPUa9evfzud7/LaaedlhNOOCF169ZNnz598sADD2SLLbYo1zVs2DA9evTIbbfdlldeeSWLFy/OFltskXPOOSdnn312kqRjx47ZdNNNM3To0Lz55pupX79+tttuu+VuaQUAaoeK0n/e7wAAAOuIGTNmpFOnTrnoooty/vnn13Q7AACrRPgGAECN+/Of/5z/+Z//Sa9evdK0adNMnz49Q4cOzbx58/Lcc8+t8aeeAgCsLW47BQCgxjVu3DhPP/10RowYkffeey+VlZXp3bt3LrvsMsEbALBec+UbAAAAABTk0x8dBQAAAACsMuEbAAAAABRE+AYAAAAABfHAhc9p6dKlefPNN9OkSZNUVFTUdDsAAAAA1JBSqZT3338/bdu2zUYbffq1bcK3z+nNN99Mu3btaroNAAAAANYRr7/+ejbffPNPrRG+fU5NmjRJ8u8fatOmTWu4GwAAAABqyrx589KuXbtyXvRphG+f07JbTZs2bSp8AwAAAOBzLU3mgQsAAAAAUBDhGwAAAAAURPgGAAAAAAURvgEAAABAQYRvAAAAAFAQ4RsAAAAAFET4BgAAAAAFEb4BAAAAQEGEbwAAAABQEOEbAAAAABRE+AbrkSFDhqSioiIDBw6sNv7CCy+kf//+qaysTJMmTbLbbrvltddeK2+fNWtWBgwYkKqqqjRu3Dhdu3bNb37zmxWeY+HChdlll11SUVGRqVOnFjgbAAAAqP2Eb7CemDx5coYPH54uXbpUG3/55Zez++67p1OnTnnooYfy5z//OT/60Y/SsGHDcs2AAQMyffr03HfffZk2bVoOOeSQHH744Xn22WeXO8/ZZ5+dtm3bFj4fAAAA2BAI32A9MH/+/Bx55JG5+eabs9lmm1XbdsEFF+TrX/96hg4dml133TVbb711+vXrl1atWpVrnnjiiZxyyin5yle+kq233joXXnhhNt100zzzzDPVjvWHP/wh48aNy5VXXrlW5gUAAAC1nfAN1gMnnXRS+vXrlz59+lQbX7p0af7v//4v2267bfbdd9+0atUqPXr0yD333FOtbvfdd8+dd96Zd999N0uXLs2YMWOycOHC9O7du1zz1ltv5bjjjsttt92WjTfeeC3MCgAAAGo/4Rus48aMGZNnnnkmQ4YMWW7b7NmzM3/+/Fx++eXZb7/9Mm7cuHzjG9/IIYcckokTJ5br7rzzznz88cdp3rx5GjRokBNOOCF33313OnTokCQplUo5+uij8/3vfz/du3dfa3MDAACA2q5uTTcArNzrr7+e0047LePGjau2htsyS5cuTZIcdNBBOf3005Mku+yySx5//PHceOON2WOPPZIkF154YebMmZMHHnggLVq0yD333JNDDz00jzzySHbaaadcd911mTdvXs4777y1NzkAAADYAAjfYB02ZcqUzJ49O926dSuPLVmyJA8//HCGDRuWBQsWpG7dutl+++2r7de5c+c8+uijSf79QIZhw4blueeeyw477JAk2XnnnfPII4/kF7/4RW688cZMmDAhkyZNSoMGDaodp3v37jnyyCMzatSogmcKAAAAtZPwDdZhe++9d6ZNm1Zt7Lvf/W46deqUc845Jw0aNMiXv/zlTJ8+vVrNiy++mC233DJJ8sEHHyRJNtqo+l3mderUKV859/Of/zyXXnppedubb76ZfffdN3feeWd69OixxucFAAAAGwrhG6zDmjRpkh133LHaWOPGjdO8efPy+A9/+MMcfvjh+drXvpY999wzY8eOze9+97s89NBDSZJOnTplm222yQknnJArr7wyzZs3zz333JPx48fn/vvvT5JsscUW1c6xySabJEk6dOiQzTffvOBZAgAAQO3lgQuwnvvGN76RG2+8MUOHDs1OO+2UX/7yl/ntb3+b3XffPUlSr169/P73v0/Lli1z4IEHpkuXLvnVr36VUaNG5etf/3oNdw8AAAC1W0WpVCrVdBPrg3nz5qWysjJz585N06ZNa7odAAAAAGrIF8mJXPkGAAAAAAWx5ht8TodcM6GmW9jg3HX6XjXdAgAAAKwWV74BAAAAQEGEbwAAAABQEOEbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAAAAURPgGAAAAAAURvgEAAABAQYRvAAAAAFAQ4RsAAAAAFET4BgAAAAAFEb4BAAAAQEGEbwAAAABQEOEbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAADVqyJAhqaioyMCBA1e4/YQTTkhFRUWuvfbaauMLFy7MKaeckhYtWqRx48bp379/3njjjWo1l112WXr16pWNN944m266aTETAPgUwjcAAABqzOTJkzN8+PB06dJlhdvvueeePPnkk2nbtu1y2wYOHJi77747Y8aMyaOPPpr58+fngAMOyJIlS8o1ixYtyqGHHpof/OAHhc0B4NMI3wAAAKgR8+fPz5FHHpmbb745m2222XLb//nPf+bkk0/O7bffnnr16lXbNnfu3IwYMSJXXXVV+vTpk1133TWjR4/OtGnT8sADD5TrLr744px++unZaaedCp8PwIoI3wAAAKgRJ510Uvr165c+ffost23p0qUZMGBAfvjDH2aHHXZYbvuUKVOyePHi9O3btzzWtm3b7Ljjjnn88ccL7Rvgi6hb0w0AAACw4RkzZkyeeeaZTJ48eYXbr7jiitStWzennnrqCrfPmjUr9evXX+6KudatW2fWrFlrvF+AVeXKNwBYQ1a0WPSgQYPSqVOnNG7cOJtttln69OmTJ598stp+vXv3TkVFRbXXN7/5zWo1FosGoDZ5/fXXc9ppp2X06NFp2LDhctunTJmSn/3sZxk5cmQqKiq+0LFLpdIX3gegSMI3AFgDVrZY9Lbbbpthw4Zl2rRpefTRR7PVVlulb9++efvtt6vVHXfccZk5c2b5ddNNN1XbbrFoAGqTKVOmZPbs2enWrVvq1q2bunXrZuLEifn5z3+eunXr5qGHHsrs2bOzxRZblLe/+uqrOfPMM7PVVlslSaqqqrJo0aLMmTOn2rFnz56d1q1b18CsAFbMbacAsJr+c7HoSy+9tNq2I444otr7q6++OiNGjMhf/vKX7L333uXxjTfeOFVVVSs9x8UXX5wkGTly5JprHABqyN57751p06ZVG/vud7+bTp065ZxzzkmbNm2y7777Vtu+7777ZsCAAfnud7+bJOnWrVvq1auX8ePH57DDDkuSzJw5M88991yGDh26diYC8DkI3wBgNf3nYtGfDN/+06JFizJ8+PBUVlZm5513rrbt9ttvz+jRo9O6devsv//+ueiii9KkSZOiWweAGtGkSZPsuOOO1cYaN26c5s2bl8ebN29ebXu9evVSVVWV7bbbLklSWVmZY445JmeeeWaaN2+eZs2a5ayzzspOO+1U7QEOr732Wt5999289tprWbJkSaZOnZok2WabbbLJJpsUOEuAfxO+AcBq+KzFopPk/vvvzze/+c188MEHadOmTcaPH58WLVqUtx955JFp3759qqqq8txzz+W8887Ln//854wfP35tTAEA1lvXXHNN6tatm8MOOywffvhh9t5774wcOTJ16tQp1/z4xz/OqFGjyu933XXXJMmDDz6Y3r17r+2WgQ1QRalUKtV0E+uDefPmpbKyMnPnzk3Tpk1ruh1qwCHXTKjpFjY4d52+V023AJ/q9ddfT/fu3TNu3LjylWy9e/fOLrvskmuvvbZct2DBgsycOTPvvPNObr755kyYMCFPPvlkWrVqtcLjTpkyJd27d8+UKVPStWvXattGjhyZgQMH5r333itqWgAAwGf4IjmRBy4AwCr6rMWilyxZkuTft9Fss8022W233TJixIjUrVs3I0aMWOlxu3btmnr16uXvf//72poKAABQELedAsAq+qzFov/zlpf/VCqVsnDhwpUe9/nnn8/ixYvTpk2bNdovAHzS8N4H1XQLG5zjH7q3plsA1jLhGwCsos9aLHrBggW57LLL0r9//7Rp0yb/+te/cv311+eNN97IoYcemiR5+eWXc/vtt+frX/96WrRokb/+9a8588wzs+uuu+arX/1q+bgWiwYAgPWT8A0AClKnTp387W9/y6hRo/LOO++kefPm+fKXv5xHHnkkO+ywQ5Kkfv36+dOf/pSf/exnmT9/ftq1a5d+/frloosuslg0AADUAsI3AFiDHnroofKfGzZsmLvuuutT69u1a5eJEyd+5nFHjhyZkSNHrmZ3AADA2uaBCwAAAABQEOEbAAAAABTEbacArPf23OO7Nd3CBufBibfWdAsAALBecOUbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAAAArNGTIkFRUVGTgwIHlsbvuuiv77rtvWrRokYqKikydOnW5/WbNmpUBAwakqqoqjRs3TteuXfOb3/ymWs2LL76Ygw46KC1atEjTpk3z1a9+NQ8++GDBM1r7hG8AAAAALGfy5MkZPnx4unTpUm18wYIF+epXv5rLL798pfsOGDAg06dPz3333Zdp06blkEMOyeGHH55nn322XNOvX798/PHHmTBhQqZMmZJddtklBxxwQGbNmlXYnGqC8A2ghqzKN0ivvPJKKioqVvj69a9/nSR56KGHVlozefLktThDAABgfTV//vwceeSRufnmm7PZZptV2zZgwID8+Mc/Tp8+fVa6/xNPPJFTTjklX/nKV7L11lvnwgsvzKabbppnnnkmSfLOO+/kpZdeyrnnnpsuXbqkY8eOufzyy/PBBx/k+eefL3Rua5vwDaAGrOo3SO3atcvMmTOrvS6++OI0btw4+++/f5KkV69ey9Uce+yx2WqrrdK9e/fC5wYAAKz/TjrppPTr1+9TA7ZPs/vuu+fOO+/Mu+++m6VLl2bMmDFZuHBhevfunSRp3rx5OnfunF/96ldZsGBBPv7449x0001p3bp1unXrtgZnUvPq1nQDABua//wG6dJLL622bcCAAUn+fYXbitSpUydVVVXVxu6+++4cfvjh2WSTTZIk9evXr1azePHi3HfffTn55JNTUVGxBmcCAADURmPGjMkzzzyzWnfO3HnnnTn88MPTvHnz1K1bNxtvvHHuvvvudOjQIUlSUVGR8ePH56CDDkqTJk2y0UYbpXXr1hk7dmw23XTTNTSTdYMr3wDWstX9Buk/TZkyJVOnTs0xxxyz0pr77rsv77zzTo4++ujVPh8AAFC7vf766znttNMyevToNGzYcJWPc+GFF2bOnDl54IEH8vTTT+eMM87IoYcemmnTpiVJSqVSTjzxxLRq1SqPPPJInnrqqRx00EE54IADMnPmzDU1nXWC8K2WW9Wnkpxwwgnp0KFDGjVqlJYtW+aggw7K3/72t/L2V155Jcccc0zat2+fRo0apUOHDrnooouyaNGitTArWH8t+wZpyJAha+R4I0aMSOfOndOrV69Prdl3333Trl27NXJOAKhpRf2Oa91UgH9/wT979ux069YtdevWTd26dTNx4sT8/Oc/T926dbNkyZLPPMbLL7+cYcOG5ZZbbsnee++dnXfeORdddFG6d++eX/ziF0mSCRMm5P7778+YMWPy1a9+NV27ds3111+fRo0aZdSoUUVPc60SvtViq/NUkm7duuXWW2/NCy+8kD/+8Y8plUrp27dv+S/Z3/72tyxdujQ33XRTnn/++VxzzTW58cYbc/755xc6J1ifralvkJb58MMPc8cdd3zqVW9vvPFG/vjHP35qDQCsT4r8Hde6qQDJ3nvvnWnTpmXq1KnlV/fu3XPkkUdm6tSpqVOnzmce44MPPkiSbLRR9dipTp06Wbp06afWbLTRRuWa2sKab7XU6qwplSTHH398+c9bbbVVLr300uy888555ZVX0qFDh+y3337Zb7/9yjVbb711pk+fnhtuuCFXXnnlmp0M1BL/+Q3SMkuWLMnDDz+cYcOGZeHChZ/rH7JlfvOb3+SDDz7Id77znZXW3HrrrWnevHn69++/Wr0DwLqg6N9xrZsKkDRp0iQ77rhjtbHGjRunefPm5fF33303r732Wt58880kyfTp05MkVVVVqaqqSqdOnbLNNtvkhBNOyJVXXpnmzZvnnnvuyfjx43P//fcnSXr27JnNNtssRx11VH784x+nUaNGufnmmzNjxoz069dvLc64eK58q6XW5JpSCxYsyK233pr27dt/6m1rc+fOTbNmzVb7fFBbrYlvkP7TiBEj0r9//7Rs2XKF20ulUm699dZ85zvfSb169dbEFACgRq3t33GtmwqwYvfdd1923XXXckj2zW9+M7vuumtuvPHGJEm9evXy+9//Pi1btsyBBx6YLl265Fe/+lVGjRqVr3/960mSFi1aZOzYsZk/f3722muvdO/ePY8++mjuvffe7LzzzjU2tyK48q0WWhNPJUmS66+/PmeffXYWLFiQTp06Zfz48alfv/4Ka19++eVcd911ueqqq1brnFCbrYlvkJZ56aWX8vDDD+f3v//9Ss83YcKEzJgxwy2nANQKNfE7rnVTAf7toYceqvb+6KOP/swvJjp27Jjf/va3n1rTvXv3/PGPf1zN7tZ9rnyrZdbkmlJHHnlknn322UycODEdO3bMYYcdlo8++mi5ujfffDP77bdfDj300Bx77LGrdU7Y0H3WN0jL3HLLLfnSl76Uvn37rvRYI0aMSK9evdK5c+dCewaAotXE77jWTQVgTakolUqlmm5ifTBv3rxUVlZm7ty5adq0aU23s1L33HNPvvGNb1S7fW3JkiWpqKjIRhttVG1NqVdeeSXt27fPs88+m1122eVTj7to0aJsttlm+eUvf5lvfetb5fE333wze+65Z3r06JGRI0cut1BibXLINRNquoUNzl2n71XTLbCe2HOP79Z0CxucByfeWtMtABuQtf07bpL85Cc/yXXXXZd//vOftXr5huG9D6rpFjY4xz90b023AKwBXyQncttpLbNsTan/9N3vfjedOnXKOeec84XXlPpPpVIpCxcuLL//5z//mT333LP81KjaHLwBsOEZMmRIzj///Jx22mm59tprk/z738KLL744w4cPz5w5c9KjR4/84he/yA477JDk//+P/hX53//93xx66KF55ZVX8pOf/CQTJkzIrFmz0rZt23z729/OBRdcsNJb32BDtzZ/x102Zt1UYF3wyvCTa7qFDc5Wxw9b48cUvtUya2JNqX/84x+5884707dv37Rs2TL//Oc/c8UVV6RRo0blhRHffPPN9O7dO1tssUWuvPLKvP322+Xz/ee6VLCuOuz4u2q6hQ3O/w4/pKZbgM9t8uTJGT58eLp06VJtfOjQobn66qszcuTIbLvttrn00kuzzz77ZPr06WnSpEnatWuXmTNnVttn+PDhGTp0aPbff/8kyd/+9rcsXbo0N910U7bZZps899xzOe6447JgwQJPDIeVWFu/4y5j3VRYPavyBdYyTzzxRC644II8+eSTqVevXnbZZZf84Q9/SKNGjZIk/fv3z9SpUzN79uxsttlm6dOnT6644oq0bdt2bU8TPjeXKm2APmtNqYYNG+aRRx7J17/+9WyzzTY57LDD0rhx4zz++ONp1apVkmTcuHF56aWXMmHChGy++eZp06ZN+QUA67P58+fnyCOPzM0335zNNtusPF4qlXLttdfmggsuyCGHHJIdd9wxo0aNygcffJA77rgjSVKnTp3yf+gve9199905/PDDs8kmmyRJ9ttvv9x6663p27dvtt566/Tv3z9nnXVW7rrLlwKwOtbE77jLWDcVVt1nfYE1bNiwTJ48OVVVVdlnn33y/vvvl2ueeOKJ7Lfffunbt2+eeuqpTJ48OSeffHK1u6z23HPP/O///m+mT5+e3/72t3n55Zfz//w//89amx+sCmu+fU7ry5pvFMeab2tfkWu+ufJt7Svyyjdrvq19tXnNt6OOOirNmjXLNddck969e2eXXXbJtddem3/84x/p0KFDnnnmmey6667l+oMOOiibbrppRo0atdyxpkyZku7du+exxx5Lr169VnrOCy+8MGPHjs3TTz9dyJwAVsaab2tfbV7zbf78+enatWuuv/76XHrppeV/Q0ulUtq2bZuBAwfmnHPOSZIsXLgwrVu3zhVXXJETTjghSbLbbrtln332yU9+8pPPfc777rsvBx98cBYuXFgrbxN32+na93lvO/0iOZEr3wAA/j9jxozJM888kyFDhiy3bdasWUmS1q1bVxtv3bp1edsnjRgxIp07d/7U4O3ll1/Oddddl+9///ur0TkA1LyTTjop/fr1S58+faqNz5gxI7NmzUrfvn3LYw0aNMgee+yRxx9/PEkye/bsPPnkk2nVqlV69eqV1q1bZ4899sijjz660vO9++67uf3229OrV69aGbxRe1jzDQAgyeuvv57TTjst48aNS8OGDVdaV1FRUe19qVRabixJPvzww9xxxx350Y9+tNJjvfnmm9lvv/1y6KGH5thjj1315mEt+vauu9d0Cxuc0c+uPHyAdcWyL7AmT5683LZP+wLr1VdfTZL84x//SJIMGjQoV155ZXbZZZf86le/yt57753nnnsuHTt2LO93zjnnZNiwYfnggw+y22675f777y9qWrBGCN8KMvgPj9V0Cxuc8/f/ak23AMB6bMqUKZk9e3a6detWHluyZEkefvjhDBs2rLx4+6xZs6qtcTp79uzl/mMiSX7zm9/kgw8+yHe+850Vnu/NN9/MnnvumZ49e2b48OFreDYAsPasiS+wli5dmiQ54YQT8t3v/ntJkV133TV/+tOfcsstt1S7Kv2HP/xhjjnmmLz66qu5+OKL853vfCf333//Cr8Mg3WB8A0AIMnee++dadOmVRv77ne/m06dOuWcc87J1ltvnaqqqowfP7685tuiRYsyceLEXHHFFcsdb8SIEenfv39atmy53LZ//vOf2XPPPdOtW7fceuut1RaSBoD1zZr4AmvZ+Pbbb1/t2J07d85rr71WbaxFixZp0aJFtt1223Tu3Dnt2rXLpEmT0rNnz0LmB6tL+AYAkKRJkybZcccdq401btw4zZs3L48PHDgwgwcPTseOHdOxY8cMHjw4G2+8cY444ohq+7300kt5+OGH8/vf/36587z55pvp3bt3tthii1x55ZV5++23y9uqqqoKmBkAFGtNfIG11VZbpW3btuWgbpkXX3wx+++//0rPvewZkgsXLlyTU4I1SvgGAPA5nX322fnwww9z4oknZs6cOenRo0fGjRuXJk2aVKu75ZZb8qUvfanawtLLjBs3Li+99FJeeumlbL755tW2eQg9AOujNfEFVkVFRX74wx/moosuys4775xddtklo0aNyt/+9rf85je/SZI89dRTeeqpp7L77rtns802yz/+8Y/8+Mc/TocOHVz1xjpN+AYAsBIPPfRQtfcVFRUZNGhQBg0a9Kn7DR48OIMHD17htqOPPjpHH330mmkQANYTn+cLrIEDB+ajjz7K6aefnnfffTc777xzxo8fnw4dOiRJGjVqlLvuuisXXXRRFixYkDZt2mS//fbLmDFj0qBBg5qaGnwm4RsAAACwRq3qF1jnnntuzj333BVu22mnnTJhwoQ11CGsPcI3AGCdss02O9R0Cxucl156vqZbAACotYRvAAAAUAtMOubrNd3CBme3Ecs/XAk+yXPtAQAAAKAgwjcAAAAAKMg6E74NGTIkFRUVGThwYHmsVCpl0KBBadu2bRo1apTevXvn+eerr0mycOHCnHLKKWnRokUaN26c/v3754033qhWM2fOnAwYMCCVlZWprKzMgAED8t57762FWQEAAACwIVsnwrfJkydn+PDh6dKlS7XxoUOH5uqrr86wYcMyefLkVFVVZZ999sn7779frhk4cGDuvvvujBkzJo8++mjmz5+fAw44IEuWLCnXHHHEEZk6dWrGjh2bsWPHZurUqRkwYMBamx8AAAAAG6YaD9/mz5+fI488MjfffHM222yz8nipVMq1116bCy64IIccckh23HHHjBo1Kh988EHuuOOOJMncuXMzYsSIXHXVVenTp0923XXXjB49OtOmTcsDDzyQJHnhhRcyduzY/PKXv0zPnj3Ts2fP3Hzzzbn//vszffr0GpkzAAAAABuGGg/fTjrppPTr1y99+vSpNj5jxozMmjUrffv2LY81aNAge+yxRx5//PEkyZQpU7J48eJqNW3bts2OO+5YrnniiSdSWVmZHj16lGt22223VFZWlmtWZOHChZk3b161FwAAAAB8EXVr8uRjxozJM888k8mTJy+3bdasWUmS1q1bVxtv3bp1Xn311XJN/fr1q10xt6xm2f6zZs1Kq1atljt+q1atyjUrMmTIkFx88cVfbEIAAAAA8B9q7Mq3119/PaeddlpGjx6dhg0brrSuoqKi2vtSqbTc2Cd9smZF9Z91nPPOOy9z584tv15//fVPPScAAAAAfFKNhW9TpkzJ7Nmz061bt9StWzd169bNxIkT8/Of/zx169YtX/H2yavTZs+eXd5WVVWVRYsWZc6cOZ9a89Zbby13/rfffnu5q+r+U4MGDdK0adNqLwAAAAD4ImosfNt7770zbdq0TJ06tfzq3r17jjzyyEydOjVbb711qqqqMn78+PI+ixYtysSJE9OrV68kSbdu3VKvXr1qNTNnzsxzzz1XrunZs2fmzp2bp556qlzz5JNPZu7cueUaAAAAAChCja351qRJk+y4447Vxho3bpzmzZuXxwcOHJjBgwenY8eO6dixYwYPHpyNN944RxxxRJKksrIyxxxzTM4888w0b948zZo1y1lnnZWddtqp/ACHzp07Z7/99stxxx2Xm266KUly/PHH54ADDsh22223FmcMAAAAwIamRh+48FnOPvvsfPjhhznxxBMzZ86c9OjRI+PGjUuTJk3KNddcc03q1q2bww47LB9++GH23nvvjBw5MnXq1CnX3H777Tn11FPLT0Xt379/hg0bttbnAwAAAMCGZZ0K3x566KFq7ysqKjJo0KAMGjRopfs0bNgw1113Xa677rqV1jRr1iyjR49eQ10CAAAAwOdTY2u+AQAAAEBtJ3wDAAAAgIII3wAAAACgIMI3AABqnRtuuCFdunRJ06ZN07Rp0/Ts2TN/+MMfytsrKipW+PrpT39arnn55ZfzjW98Iy1btkzTpk1z2GGH5a233qp2nq222mq5Y5x77rlrbZ4AwLpP+AYAQK2z+eab5/LLL8/TTz+dp59+OnvttVcOOuigPP/880mSmTNnVnvdcsstqaioyH//938nSRYsWJC+ffumoqIiEyZMyGOPPZZFixblwAMPzNKlS6ud65JLLql2rAsvvHCtzxcAWHetU087BQCANeHAAw+s9v6yyy7LDTfckEmTJmWHHXZIVVVVte333ntv9txzz2y99dZJksceeyyvvPJKnn322TRt2jRJcuutt6ZZs2aZMGFC+vTpU963SZMmyx0PAGAZV74BAFCrLVmyJGPGjMmCBQvSs2fP5ba/9dZb+b//+78cc8wx5bGFCxemoqIiDRo0KI81bNgwG220UR599NFq+19xxRVp3rx5dtlll1x22WVZtGhRcZMBANY7rnwDAKBWmjZtWnr27JmPPvoom2yySe6+++5sv/32y9WNGjUqTZo0ySGHHFIe22233dK4ceOcc845GTx4cEqlUs4555wsXbo0M2fOLNeddtpp6dq1azbbbLM89dRTOe+88zJjxoz88pe/XCtzBADWfa58AwCgVtpuu+0yderUTJo0KT/4wQ9y1FFH5a9//etydbfcckuOPPLINGzYsDzWsmXL/PrXv87vfve7bLLJJqmsrMzcuXPTtWvX1KlTp1x3+umnZ4899kiXLl1y7LHH5sYbb8yIESPyr3/9a63MEQBY97nyDQCAWql+/frZZpttkiTdu3fP5MmT87Of/Sw33XRTueaRRx7J9OnTc+eddy63f9++ffPyyy/nnXfeSd26dbPpppumqqoq7du3X+k5d9tttyTJSy+9lObNm6/hGQEA6yPhGwAAG4RSqZSFCxdWGxsxYkS6deuWnXfeeaX7tWjRIkkyYcKEzJ49O/37919p7bPPPpskadOmzRroGACoDYRvAADUOueff37233//tGvXLu+//37GjBmThx56KGPHji3XzJs3L7/+9a9z1VVXrfAYt956azp37pyWLVvmiSeeyGmnnZbTTz892223XZLkiSeeyKRJk7LnnnumsrIykydPzumnn57+/ftniy22WCvzBADWfcI3AABqnbfeeisDBgzIzJkzU1lZmS5dumTs2LHZZ599yjVjxoxJqVTKt771rRUeY/r06TnvvPPy7rvvZquttsoFF1yQ008/vby9QYMGufPOO3PxxRdn4cKF2XLLLXPcccfl7LPPLnx+AMD6Q/gGAECtM2LEiM+sOf7443P88cevdPvll1+eyy+/fKXbu3btmkmTJq1SfwDAhsPTTgEAAACgIMI3AAAAACiI204BACjUTu071HQLG5xpM16u6RYAgP+PK98AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAAChIjYZvN9xwQ7p06ZKmTZumadOm6dmzZ/7whz+Ut5dKpQwaNCht27ZNo0aN0rt37zz//PPVjrFw4cKccsopadGiRRo3bpz+/fvnjTfeqFYzZ86cDBgwIJWVlamsrMyAAQPy3nvvrY0pAgAAALABq9HwbfPNN8/ll1+ep59+Ok8//XT22muvHHTQQeWAbejQobn66qszbNiwTJ48OVVVVdlnn33y/vvvl48xcODA3H333RkzZkweffTRzJ8/PwcccECWLFlSrjniiCMyderUjB07NmPHjs3UqVMzYMCAtT5fAAAAADYsdWvy5AceeGC195dddlluuOGGTJo0Kdtvv32uvfbaXHDBBTnkkEOSJKNGjUrr1q1zxx135IQTTsjcuXMzYsSI3HbbbenTp0+SZPTo0WnXrl0eeOCB7LvvvnnhhRcyduzYTJo0KT169EiS3HzzzenZs2emT5+e7bbbbu1OGgAAAIANxjqz5tuSJUsyZsyYLFiwID179syMGTMya9as9O3bt1zToEGD7LHHHnn88ceTJFOmTMnixYur1bRt2zY77rhjueaJJ55IZWVlOXhLkt122y2VlZXlmhVZuHBh5s2bV+0FAAAAAF9EjYdv06ZNyyabbJIGDRrk+9//fu6+++5sv/32mTVrVpKkdevW1epbt25d3jZr1qzUr18/m2222afWtGrVarnztmrVqlyzIkOGDCmvEVdZWZl27dqt1jwBAAAA2PDUePi23XbbZerUqZk0aVJ+8IMf5Kijjspf//rX8vaKiopq9aVSabmxT/pkzYrqP+s45513XubOnVt+vf766593SgAAAACQZB0I3+rXr59tttkm3bt3z5AhQ7LzzjvnZz/7WaqqqpJkuavTZs+eXb4arqqqKosWLcqcOXM+teatt95a7rxvv/32clfV/acGDRqUn8K67AUAAAAAX0SNh2+fVCqVsnDhwrRv3z5VVVUZP358eduiRYsyceLE9OrVK0nSrVu31KtXr1rNzJkz89xzz5Vrevbsmblz5+app54q1zz55JOZO3duuQYAAAAAilCjTzs9//zzs//++6ddu3Z5//33M2bMmDz00EMZO3ZsKioqMnDgwAwePDgdO3ZMx44dM3jw4Gy88cY54ogjkiSVlZU55phjcuaZZ6Z58+Zp1qxZzjrrrOy0007lp5927tw5++23X4477rjcdNNNSZLjjz8+BxxwgCedAgAAAFCoGg3f3nrrrQwYMCAzZ85MZWVlunTpkrFjx2afffZJkpx99tn58MMPc+KJJ2bOnDnp0aNHxo0blyZNmpSPcc0116Ru3bo57LDD8uGHH2bvvffOyJEjU6dOnXLN7bffnlNPPbX8VNT+/ftn2LBha3eyAAAAAGxwajR8GzFixKdur6ioyKBBgzJo0KCV1jRs2DDXXXddrrvuupXWNGvWLKNHj17VNgEAAABglaxza74BAAAAQG0hfAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCCrFL7ttddeee+995YbnzdvXvbaa6/V7QkAAAAAaoVVCt8eeuihLFq0aLnxjz76KI888shqNwUAAAAAtUHdL1L8l7/8pfznv/71r5k1a1b5/ZIlSzJ27Nh86UtfWnPdAQAAAMB67AuFb7vssksqKipSUVGxwttLGzVqlOuuu26NNQcAAAAA67MvFL7NmDEjpVIpW2+9dZ566qm0bNmyvK1+/fpp1apV6tSps8abBAAAAID10RcK37bccsskydKlSwtpBgAAAABqky8Uvv2nF198MQ899FBmz569XBj34x//eLUbAwAAAID13SqFbzfffHN+8IMfpEWLFqmqqkpFRUV5W0VFhfANAAAAALKK4dull16ayy67LOecc86a7gcAAAAAao2NVmWnOXPm5NBDD13TvQAAAABArbJK4duhhx6acePGreleAAAAAKBWWaXbTrfZZpv86Ec/yqRJk7LTTjulXr161bafeuqpa6Q5AAAAAFifrVL4Nnz48GyyySaZOHFiJk6cWG1bRUWF8A0AAAAAsorh24wZM9Z0HwAAAABQ66zSmm8AAAAAwGdbpSvfvve9733q9ltuuWWVmgEAAACA2mSVwrc5c+ZUe7948eI899xzee+997LXXnutkcYAAAAAYH23SuHb3XffvdzY0qVLc+KJJ2brrbde7aYAAAAAoDZYY2u+bbTRRjn99NNzzTXXrKlDAgAAAMB6bY0+cOHll1/Oxx9/vCYPCQAAAADrrVW67fSMM86o9r5UKmXmzJn5v//7vxx11FFrpDEAAAAAWN+tUvj27LPPVnu/0UYbpWXLlrnqqqs+80moAAAAALChWKXw7cEHH1zTfQAAAABArbNK4dsyb7/9dqZPn56Kiopsu+22admy5ZrqCwAAAADWe6v0wIUFCxbke9/7Xtq0aZOvfe1r+a//+q+0bds2xxxzTD744IM13SMAAAAArJdWKXw744wzMnHixPzud7/Le++9l/feey/33ntvJk6cmDPPPHNN9wgAAAAA66VVuu30t7/9bX7zm9+kd+/e5bGvf/3radSoUQ477LDccMMNa6o/AAAAAFhvrdKVbx988EFat2693HirVq3cdgoAAAAA/59VCt969uyZiy66KB999FF57MMPP8zFF1+cnj17rrHmAAAAAGB9tkq3nV577bXZf//9s/nmm2fnnXdORUVFpk6dmgYNGmTcuHFrukcAAAAAWC+tUvi200475e9//3tGjx6dv/3tbymVSvnmN7+ZI488Mo0aNVrTPQIAAADAemmVwrchQ4akdevWOe6446qN33LLLXn77bdzzjnnrJHmAAAAAGB9tkprvt10003p1KnTcuM77LBDbrzxxtVuCgAAAABqg1UK32bNmpU2bdosN96yZcvMnDlztZsCAAAAgNpglcK3du3a5bHHHltu/LHHHkvbtm1XuykAAAAAqA1Wac23Y489NgMHDszixYuz1157JUn+9Kc/5eyzz86ZZ565RhsEAAAAgPXVKoVvZ599dt59992ceOKJWbRoUZKkYcOGOeecc3Leeeet0QYBAAAAYH21SuFbRUVFrrjiivzoRz/KCy+8kEaNGqVjx45p0KDBmu4PAAAAANZbqxS+LbPJJpvky1/+8prqBQAAAABqlVV64AIAAAAA8NmEbwAAAABQEOEbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAAAAURPgGAAAAAAURvgEAAABAQYRvAAAAAFAQ4RsAAAAAFET4BgAAAAAFEb4BAAAAQEGEbwAAAABQEOEbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAAAAURPgGAAAAAAURvgEAAABAQYRvAAAAAFAQ4RsAAAAAFET4BgAAAAAFEb4BAAAAQEFqNHwbMmRIvvzlL6dJkyZp1apVDj744EyfPr1aTalUyqBBg9K2bds0atQovXv3zvPPP1+tZuHChTnllFPSokWLNG7cOP37988bb7xRrWbOnDkZMGBAKisrU1lZmQEDBuS9994reooAAAAAbMBqNHybOHFiTjrppEyaNCnjx4/Pxx9/nL59+2bBggXlmqFDh+bqq6/OsGHDMnny5FRVVWWfffbJ+++/X64ZOHBg7r777owZMyaPPvpo5s+fnwMOOCBLliwp1xxxxBGZOnVqxo4dm7Fjx2bq1KkZMGDAWp0vAAAAABuWujV58rFjx1Z7f+utt6ZVq1aZMmVKvva1r6VUKuXaa6/NBRdckEMOOSRJMmrUqLRu3Tp33HFHTjjhhMydOzcjRozIbbfdlj59+iRJRo8enXbt2uWBBx7IvvvumxdeeCFjx47NpEmT0qNHjyTJzTffnJ49e2b69OnZbrvt1u7EAQAAANggrFNrvs2dOzdJ0qxZsyTJjBkzMmvWrPTt27dc06BBg+yxxx55/PHHkyRTpkzJ4sWLq9W0bds2O+64Y7nmiSeeSGVlZTl4S5LddtstlZWV5ZpPWrhwYebNm1ftBQAAAABfxDoTvpVKpZxxxhnZfffds+OOOyZJZs2alSRp3bp1tdrWrVuXt82aNSv169fPZptt9qk1rVq1Wu6crVq1Ktd80pAhQ8rrw1VWVqZdu3arN0EAAAAANjjrTPh28skn5y9/+Uv+53/+Z7ltFRUV1d6XSqXlxj7pkzUrqv+045x33nmZO3du+fX6669/nmkAAAAAQNk6Eb6dcsopue+++/Lggw9m8803L49XVVUlyXJXp82ePbt8NVxVVVUWLVqUOXPmfGrNW2+9tdx533777eWuqlumQYMGadq0abUXAAAAAHwRNRq+lUqlnHzyybnrrrsyYcKEtG/fvtr29u3bp6qqKuPHjy+PLVq0KBMnTkyvXr2SJN26dUu9evWq1cycOTPPPfdcuaZnz56ZO3dunnrqqXLNk08+mblz55ZrAAAAAGBNq9GnnZ500km54447cu+996ZJkyblK9wqKyvTqFGjVFRUZODAgRk8eHA6duyYjh07ZvDgwdl4441zxBFHlGuPOeaYnHnmmWnevHmaNWuWs846KzvttFP56aedO3fOfvvtl+OOOy433XRTkuT444/PAQcc4EmnAAAAABSmRsO3G264IUnSu3fvauO33nprjj766CTJ2WefnQ8//DAnnnhi5syZkx49emTcuHFp0qRJuf6aa65J3bp1c9hhh+XDDz/M3nvvnZEjR6ZOnTrlmttvvz2nnnpq+amo/fv3z7Bhw4qdIAAAAAAbtBoN30ql0mfWVFRUZNCgQRk0aNBKaxo2bJjrrrsu11133UprmjVrltGjR69KmwAAAACwStaJBy4AAAAAQG0kfAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAgtRo+Pbwww/nwAMPTNu2bVNRUZF77rmn2vZSqZRBgwalbdu2adSoUXr37p3nn3++Ws3ChQtzyimnpEWLFmncuHH69++fN954o1rNnDlzMmDAgFRWVqaysjIDBgzIe++9V/DsAAAAANjQ1Wj4tmDBguy8884ZNmzYCrcPHTo0V199dYYNG5bJkyenqqoq++yzT95///1yzcCBA3P33XdnzJgxefTRRzN//vwccMABWbJkSbnmiCOOyNSpUzN27NiMHTs2U6dOzYABAwqfHwAAAAAbtro1efL9998/+++//wq3lUqlXHvttbngggtyyCGHJElGjRqV1q1b54477sgJJ5yQuXPnZsSIEbntttvSp0+fJMno0aPTrl27PPDAA9l3333zwgsvZOzYsZk0aVJ69OiRJLn55pvTs2fPTJ8+Pdttt93amSwAAAAAG5x1ds23GTNmZNasWenbt295rEGDBtljjz3y+OOPJ0mmTJmSxYsXV6tp27Ztdtxxx3LNE088kcrKynLwliS77bZbKisryzUrsnDhwsybN6/aCwAAAAC+iHU2fJs1a1aSpHXr1tXGW7duXd42a9as1K9fP5ttttmn1rRq1Wq547dq1apcsyJDhgwprxFXWVmZdu3ardZ8AAAAANjwrLPh2zIVFRXV3pdKpeXGPumTNSuq/6zjnHfeeZk7d2759frrr3/BzgEAAADY0K2z4VtVVVWSLHd12uzZs8tXw1VVVWXRokWZM2fOp9a89dZbyx3/7bffXu6quv/UoEGDNG3atNoLAAAAAL6IdTZ8a9++faqqqjJ+/Pjy2KJFizJx4sT06tUrSdKtW7fUq1evWs3MmTPz3HPPlWt69uyZuXPn5qmnnirXPPnkk5k7d265BgAAAACKUKNPO50/f35eeuml8vsZM2Zk6tSpadasWbbYYosMHDgwgwcPTseOHdOxY8cMHjw4G2+8cY444ogkSWVlZY455piceeaZad68eZo1a5azzjorO+20U/npp507d85+++2X4447LjfddFOS5Pjjj88BBxzgSacAAAAAFKpGw7enn346e+65Z/n9GWeckSQ56qijMnLkyJx99tn5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u2TKlCk13RarYKuttlru72dFRUVOOumkmm6NVfDxxx/nwgsvTPv27dOoUaNsvfXWueSSS7J06dKabo3V8P7772fgwIHZcsst06hRo/Tq1SuTJ0+u6bZqnPCNJMmdd96ZgQMH5oILLsizzz6b//qv/8r++++f1157raZbYxUsWLAgO++8c4YNG1bTrbAGTJw4MSeddFImTZqU8ePH5+OPP07fvn2zYMGCmm6NVbD55pvn8ssvz9NPP52nn346e+21Vw466KA8//zzNd0aq2ny5MkZPnx4unTpUtOtsJp22GGHzJw5s/yaNm1aTbfEKpozZ06++tWvpl69evnDH/6Qv/71r7nqqquy6aab1nRrrILJkydX+7s5fvz4JMmhhx5aw52xKq644orceOONGTZsWF544YUMHTo0P/3pT3PdddfVdGushmOPPTbjx4/PbbfdlmnTpqVv377p06dP/vnPf9Z0azWqolQqlWq6CWpejx490rVr19xwww3lsc6dO+fggw/OkCFDarAzVldFRUXuvvvuHHzwwTXdCmvI22+/nVatWmXixIn52te+VtPtsAY0a9YsP/3pT3PMMcfUdCusovnz56dr1665/vrrc+mll2aXXXbJtddeW9NtsQoGDRqUe+65J1OnTq3pVlgDzj333Dz22GPu6KilBg4cmPvvvz9///vfU1FRUdPt8AUdcMABad26dUaMGFEe++///u9svPHGue2222qwM1bVhx9+mCZNmuTee+9Nv379yuO77LJLDjjggFx66aU12F3NcuUbWbRoUaZMmZK+fftWG+/bt28ef/zxGuoKWJm5c+cm+Xdgw/ptyZIlGTNmTBYsWJCePXvWdDushpNOOin9+vVLnz59aroV1oC///3vadu2bdq3b59vfvOb+cc//lHTLbGK7rvvvnTv3j2HHnpoWrVqlV133TU333xzTbfFGrBo0aKMHj063/ve9wRv66ndd989f/rTn/Liiy8mSf785z/n0Ucfzde//vUa7oxV9fHHH2fJkiVp2LBhtfFGjRrl0UcfraGu1g11a7oBat4777yTJUuWpHXr1tXGW7dunVmzZtVQV8CKlEqlnHHGGdl9992z44471nQ7rKJp06alZ8+e+eijj7LJJpvk7rvvzvbbb1/TbbGKxowZk2eeecZ6JrVEjx498qtf/Srbbrtt3nrrrVx66aXp1atXnn/++TRv3rym2+ML+sc//pEbbrghZ5xxRs4///w89dRTOfXUU9OgQYN85zvfqen2WA333HNP3nvvvRx99NE13Qqr6JxzzsncuXPTqVOn1KlTJ0uWLMlll12Wb33rWzXdGquoSZMm6dmzZ37yk5+kc+fOad26df7nf/4nTz75ZDp27FjT7dUo4Rtln/zGqFQq+RYJ1jEnn3xy/vKXv2zw3xyt77bbbrtMnTo17733Xn7729/mqKOOysSJEwVw66HXX389p512WsaNG7fct7ysn/bff//yn3faaaf07NkzHTp0yKhRo3LGGWfUYGesiqVLl6Z79+4ZPHhwkmTXXXfN888/nxtuuEH4tp4bMWJE9t9//7Rt27amW2EV3XnnnRk9enTuuOOO7LDDDpk6dWoGDhyYtm3b5qijjqrp9lhFt912W773ve/lS1/6UurUqZOuXbvmiCOOyDPPPFPTrdUo4Rtp0aJF6tSps9xVbrNnz17uajig5pxyyim577778vDDD2fzzTev6XZYDfXr188222yTJOnevXsmT56cn/3sZ7nppptquDO+qClTpmT27Nnp1q1beWzJkiV5+OGHM2zYsCxcuDB16tSpwQ5ZXY0bN85OO+2Uv//97zXdCqugTZs2y32x0blz5/z2t7+toY5YE1599dU88MADueuuu2q6FVbDD3/4w5x77rn55je/meTfX3i8+uqrGTJkiPBtPdahQ4dMnDgxCxYsyLx589KmTZscfvjhad++fU23VqOs+Ubq16+fbt26lZ8WtMz48ePTq1evGuoKWKZUKuXkk0/OXXfdlQkTJmzw/3DVRqVSKQsXLqzpNlgFe++9d6ZNm5apU6eWX927d8+RRx6ZqVOnCt5qgYULF+aFF15ImzZtaroVVsFXv/rVTJ8+vdrYiy++mC233LKGOmJNuPXWW9OqVatqC7qz/vnggw+y0UbVI4k6depk6dKlNdQRa1Ljxo3Tpk2bzJkzJ3/84x9z0EEH1XRLNcqVbyRJzjjjjAwYMCDdu3dPz549M3z48Lz22mv5/ve/X9OtsQrmz5+fl156qfx+xowZmTp1apo1a5YtttiiBjtjVZx00km54447cu+996ZJkyblq1QrKyvTqFGjGu6OL+r888/P/vvvn3bt2uX999/PmDFj8tBDD2Xs2LE13RqroEmTJsutv9i4ceM0b97cuozrqbPOOisHHnhgtthii8yePTuXXnpp5s2b5yqM9dTpp5+eXr16ZfDgwTnssMPy1FNPZfjw4Rk+fHhNt8YqWrp0aW699dYcddRRqVvXf86uzw488MBcdtll2WKLLbLDDjvk2WefzdVXX53vfe97Nd0aq+GPf/xjSqVStttuu7z00kv54Q9/mO222y7f/e53a7q1GuX/rUiSHH744fnXv/6VSy65JDNnzsyOO+6Y3//+974VXE89/fTT2XPPPcvvl61Rc9RRR2XkyJE11BWr6oYbbkiS9O7du9r4rbfeapHh9dBbb72VAQMGZObMmamsrEyXLl0yduzY7LPPPjXdGpDkjTfeyLe+9a288847admyZXbbbbdMmjTJ70TrqS9/+cu5++67c9555+WSSy5J+/btc+211+bII4+s6dZYRQ888EBee+01AU0tcN111+VHP/pRTjzxxMyePTtt27bNCSeckB//+Mc13RqrYe7cuTnvvPPyxhtvpFmzZvnv//7vXHbZZalXr15Nt1ajKkqlUqmmmwAAAACA2siabwAAAABQEOEbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAAAAURPgGAAAAAAURvgEAAABAQYRvAAAbmN69e2fgwIGfq/ahhx5KRUVF3nvvvdU651ZbbZVrr712tY4BALA+Er4BAAAAQEGEbwAAAABQEOEbAMAGbPTo0enevXuaNGmSqqqqHHHEEZk9e/ZydY899lh23nnnNGzYMD169Mi0adOqbX/88cfzta99LY0aNUq7du1y6qmnZsGCBWtrGgAA6yzhGwDABmzRokX5yU9+kj//+c+55557MmPGjBx99NHL1f3whz/MlVdemcmTJ6dVq1bp379/Fi9enCSZNm1a9t133xxyyCH5y1/+kjvvvDOPPvpoTj755LU8GwCAdU/dmm4AAICa873vfa/856233jo///nP85WvfCXz58/PJptsUt520UUXZZ999kmSjBo1KptvvnnuvvvuHHbYYfnpT3+aI444ovwQh44dO+bnP/959thjj9xwww1p2LDhWp0TAMC6xJVvAAAbsGeffTYHHXRQttxyyzRp0iS9e/dOkrz22mvV6nr27Fn+c7NmzbLddtvlhRdeSJJMmTIlI0eOzCabbFJ+7bvvvlm6dGlmzJix1uYCALAucuUbAMAGasGCBenbt2/69u2b0aNHp2XLlnnttdey7777ZtGiRZ+5f0VFRZJk6dKlOeGEE3LqqacuV7PFFlus8b4BANYnwjcAgA3U3/72t7zzzju5/PLL065duyTJ008/vcLaSZMmlYO0OXPm5MUXX0ynTp2SJF27ds3zzz+fbbbZZu00DgCwHnHbKQDABmqLLbZI/fr1c9111+Uf//hH7rvvvvzkJz9ZYe0ll1ySP/3pT3nuuedy9NFHp0WLFjn44IOTJOecc06eeOKJnHTSSZk6dWr+/ve/57777sspp5yyFmcDALBuEr4BAGygWrZsmZEjR+bXv/51tt9++1x++eW58sorV1h7+eWX57TTTku3bt0yc+bM3Hfffalfv36SpEuXLpk4cWL+/ve/57/+67+y66675kc/+lHatGmzNqcDALBOqiiVSqWabgIAAAAAaiNXvgEAAABAQYRvAAAAAFAQ4RsAAAAAFET4BgAAAAAFEb4BAAAAQEGEbwAAAABQEOEbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAAAAU5P8FkPnad3On3ewAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1500x700 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# plot the number of digits in the label columns \n",
    "\n",
    "plt.figure(figsize = (15,7))\n",
    "g = sns.countplot(x = y_train, palette = 'icefire')\n",
    "\n",
    "\n",
    "# add labels to the bar\n",
    "for patch in g.patches:\n",
    "    height = patch.get_height()\n",
    "    g.text(patch.get_x() + patch.get_width()/2, height + 0.5, int(height), ha = 'center', va = 'bottom')\n",
    "plt.title(\"Number of digit class\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c6abbc56-b339-4642-823b-5fbef119f3a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# check for missing values in any rows \n",
    "\n",
    "missing_values = train.isnull().any(axis=1)\n",
    "count_missing_values = missing_values.sum()\n",
    "count_missing_values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "203bbe15-75ec-4202-871a-dcc16e778cfc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "missing_values = test.isnull().any(axis=1)\n",
    "count_missing_values = missing_values.sum()\n",
    "count_missing_values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "882b7a06-220f-4aa2-9caa-6f5b338084f4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((42000, 784), (28000, 784))"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Both train and test does not have any missing values \n",
    "# Normalize the image data \n",
    "X_train = X_train/255.0\n",
    "test = test/255.0\n",
    "\n",
    "X_train.shape, test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "8616be13-b6c4-4868-913c-46448c356726",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((42000, 28, 28, 1), (28000, 28, 28, 1))"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# we need to reshape the images and perform a grayscale to reduce the efefct of illumination and perform normalization for all data\n",
    "\n",
    "X_train = X_train.values.reshape(-1,28,28,1)\n",
    "test = test.values.reshape(-1,28,28,1)\n",
    "X_train.shape, test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "3df5db8a-e6dc-4b85-8464-16a7f4530c76",
   "metadata": {},
   "outputs": [],
   "source": [
    "#pip install tensorflow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "db861f4a-e6ed-4562-8bc9-8c89acdbe886",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-29 03:27:06.590722: I external/local_xla/xla/tsl/cuda/cudart_stub.cc:32] Could not find cuda drivers on your machine, GPU will not be used.\n",
      "2024-10-29 03:27:06.596146: I external/local_xla/xla/tsl/cuda/cudart_stub.cc:32] Could not find cuda drivers on your machine, GPU will not be used.\n",
      "2024-10-29 03:27:06.613622: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered\n",
      "2024-10-29 03:27:06.640894: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered\n",
      "2024-10-29 03:27:06.649280: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered\n",
      "2024-10-29 03:27:06.669800: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\n",
      "To enable the following instructions: AVX2 AVX512F FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\n",
      "2024-10-29 03:27:08.986135: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT\n"
     ]
    }
   ],
   "source": [
    "# We will train_test_split\n",
    "\n",
    "# Convert the lables to one-hot encoding \n",
    "from sklearn.model_selection import train_test_split\n",
    "from tensorflow.keras.utils import to_categorical\n",
    "num_classes = 10\n",
    "y_train = to_categorical(y_train,num_classes = num_classes)\n",
    "X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size = 0.1, random_state=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1659d280-f0e7-4911-9303-2a581a1b78c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((37800, 28, 28, 1), (4200, 28, 28, 1), (37800, 10), (4200, 10))"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.shape, X_val.shape, y_train.shape, y_val.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "2717d52e-6c6a-4a23-a0e2-d243216ce222",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "plt.imshow(X_train[2][:,:,0], cmap = 'gray')\n",
    "plt.title('Sample Image')\n",
    "plt.axis('off')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "4cd21efe-c5f0-4dd6-ab27-18e1e46d1188",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix \n",
    "from tensorflow.keras.models import Sequential\n",
    "from tensorflow.keras.layers import Dropout, Dense, Flatten, Conv2D, MaxPool2D\n",
    "from tensorflow.keras.optimizers import Adam\n",
    "from tensorflow.keras.preprocessing.image import ImageDataGenerator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "fcafc607-3f5c-4496-ad3a-f18ae5f16a6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Build the CNN model \n",
    "\n",
    "model = Sequential()\n",
    "model.add(Conv2D(filters = 8, kernel_size=(5,5), padding = 'Same', activation = 'relu', input_shape = (28,28,1)))\n",
    "model.add(MaxPool2D(pool_size=(2,2)))\n",
    "model.add(Dropout(0.25))\n",
    "\n",
    "\n",
    "model.add(Conv2D(filters = 16, kernel_size=(3,3), padding = 'Same', activation = 'relu'))\n",
    "model.add(MaxPool2D(pool_size=(2,2), strides = (2,2)))\n",
    "model.add(Dropout(0.25))\n",
    "\n",
    "model.add(Flatten())\n",
    "model.add(Dense(256, activation = 'relu'))\n",
    "model.add(Dropout(0.5))\n",
    "model.add(Dense(10, activation = 'softmax'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18f2961b-b1e4-4586-bf82-0ea0fe14ab60",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the optimizer , To be continued"
   ]
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
