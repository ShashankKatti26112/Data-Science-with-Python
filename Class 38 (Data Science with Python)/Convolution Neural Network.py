{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a9f8a240-5519-4005-bc9f-b22f69c3884e",
   "metadata": {},
   "source": [
    "A Convolutional Neural Network (CNN) is a type of deep learning model primarily used for processing structured grid data, such as images, and recognizing patterns. CNNs are widely applied in tasks like image recognition, object detection, video analysis, and natural language processing, thanks to their ability to capture spatial and hierarchical information from the data.\n",
    "\n",
    "### Key Components of CNNs\n",
    "\n",
    "### Convolutional Layers\n",
    "These layers apply filters (kernels) to the input data to detect features, such as edges, textures, and shapes in an image.\n",
    "The filter slides across the input, performing a convolution operation that produces a feature map, which highlights the presence of certain patterns in specific regions.\n",
    "\n",
    "### Pooling Layers\n",
    "Pooling layers reduce the spatial dimensions of the feature maps, which decreases the number of parameters, speeds up computation, and helps control overfitting.\n",
    "The most common pooling method is max pooling, which takes the maximum value in a region, retaining only the most significant feature.\n",
    "\n",
    "### Fully Connected Layers\n",
    "After a series of convolutional and pooling layers, the output is often flattened and passed through fully connected (dense) layers.\n",
    "These layers combine all features detected by the convolutional layers to make final predictions.\n",
    "\n",
    "### Activation Functions\n",
    "Activation functions introduce non-linearity into the network, allowing it to learn complex patterns.\n",
    "ReLU (Rectified Linear Unit) is the most common activation function in CNNs, setting all negative values to zero to enhance computational efficiency.\n",
    "\n",
    "### Dropout (Optional)\n",
    "Dropout is a regularization technique that randomly \"drops\" (sets to zero) a fraction of the neurons during training, which helps prevent overfitting by ensuring that the network does not rely too heavily on specific neurons.\n",
    "\n",
    "### How CNNs Work for Image Classification\n",
    "In an image classification task, a CNN might take an image as input and perform the following steps:\n",
    "\n",
    "1. Extract Low-Level Features: The first layers typically detect simple patterns, like edges and corners.\n",
    "2. Detect Mid-Level Features: As data passes through deeper layers, the model learns more complex features, like shapes and textures.\n",
    "3. Recognize High-Level Features: In the final layers, the network learns abstract concepts (e.g., parts of objects) and combines them to classify the image.\n",
    "   \n",
    "### Advantages of CNNs\n",
    "1. Translation Invariance: CNNs can recognize patterns regardless of their position within the image.\n",
    "2. Parameter Efficiency: By using shared weights (filters), CNNs require fewer parameters than fully connected neural networks, making them more computationally efficient.\n",
    "3. Hierarchical Feature Learning: CNNs learn from simple to complex features, capturing intricate structures within data.\n",
    "\n",
    "### Applications of CNNs\n",
    "1. Image and Video Analysis: Face recognition, object detection, medical image analysis (e.g., MRI scans).\n",
    "2. Natural Language Processing: Text classification, sentiment analysis, and language translation.\n",
    "3. Self-Driving Cars: Detecting objects like pedestrians, road signs, and other vehicles.\n",
    "4. Healthcare: Diagnosing diseases from medical images, analyzing x-rays, and automating pathology.\n",
    "5. \n",
    "CNNs are a powerful tool in the deep learning field, especially for tasks involving images or spatial data, due to their ability to understand intricate patterns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3246c568-5ef7-412a-8264-aa01a1aa0679",
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
   "execution_count": 2,
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
     "execution_count": 2,
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
   "execution_count": 3,
   "id": "014680e1-ee32-472d-adab-9199b44b11be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(42000, 785)"
      ]
     },
     "execution_count": 3,
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
   "execution_count": 4,
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
   "execution_count": 5,
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
     "execution_count": 5,
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
   "execution_count": 6,
   "id": "9a4aa4e6-09d1-4ea0-ae08-59a1eaf33143",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(28000, 784)"
      ]
     },
     "execution_count": 6,
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
   "execution_count": 7,
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
   "execution_count": 8,
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
   "execution_count": 9,
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
     "execution_count": 9,
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
   "execution_count": 10,
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
     "execution_count": 10,
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
   "execution_count": 11,
   "id": "af85817c-9ead-4b8d-a55c-f81f3372a40d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAGZCAYAAABmNy2oAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAPqElEQVR4nO3cfazW8//A8delU51yXym5aeWshlIY1kFWytyG3G3JzWn8wdzMP23ummRm2dhCf7FGJeYmd2HsoJhzkNwsUo2tTNpCWLOD1PX9w3r99Dtxrs/lOqIej7+4rs/r83lff3Q9r/d1zvmUyuVyOQAgInbb0QsA4N9DFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFCikpaUlpk2bFj/88EPNz93U1BQDBw6s2flWr14dpVIpHn744Xzs4YcfjlKpFKtXr67Zdf6oqakpSqVSlEqlGDZsWLvnm5ubo7GxMXr27Bl9+vSJpqamWL9+fcXnr2T+o48+yjWUSqV46qmn/vbrYtchChTS0tISt99+e6dEYerUqfHMM8/U7Hz9+/eP1tbWOPPMM2t2zkrsv//+0draGvPnz9/m8cWLF8fpp58e/fr1i+eeey5mzpwZzc3NMXbs2Pjll186PG+l80OGDInW1taYNWtWzV8bO7+6Hb0Adl5tbW3Ro0ePio9vaGio6fW7d+8eI0eOrOk5/851p0yZEkOGDImnnnoq6up+/6c3aNCgOOGEE2L27Nlx9dVX/+V5K53v2bNnjBw5Mn7++ecavzJ2BXYKVGzatGkxZcqUiPj9zWjr1xOLFi2KgQMHxllnnRULFiyIo446Kurr6+P222+PiIhZs2bFSSedFH379o3dd989jjjiiLj77rtj06ZN25x/e18flUqluPbaa2Pu3Llx2GGHRc+ePWPEiBGxcOHCDte7va+P/szs2bNjxIgRUV9fH7169YoJEybEZ5991u64d999N8aPHx+9e/eO+vr6aGhoiBtuuKHD869duzaWLFkSl156ab6hR0Qcf/zxMWTIkA53SH93Hiplp0DFrrzyytiwYUPcf//9sWDBgujfv39ERBx++OEREfHBBx/EZ599FrfeemsMGjQodt9994iI+OKLL+Liiy+OQYMGRbdu3eLjjz+OO++8M1asWBGzZ8/u8LovvvhiLFmyJKZPnx577LFH3H333TFhwoRYuXJlHHLIIX/7dd11111x8803x8SJE+Ouu+6K7777LqZNmxaNjY2xZMmSGDx4cEREvPLKKzF+/Pg47LDD4t57740BAwbE6tWr49VXX+3wGp988klERAwfPrzdc8OHD4+33367U+ehUqJAxQ466KAYMGBAREQcddRR7T7Vr1+/PpYvXx5DhgzZ5vF77703/3vLli0xatSo6N27d0yePDnuueee2Hffff/yum1tbdHc3Bx77rlnREQcffTRccABB8QTTzwRN9544996TT/88EPccccdccYZZ2zzM4DRo0fH4MGDY9q0afHoo49GRMQ111wTAwYMiHfffTfq6+vz2MmTJ3d4ne+++y4iInr16tXuuV69euXznTUPlfL1ETUzfPjwdkGIiPjwww/j7LPPjt69e0eXLl2ia9eucdlll8XmzZtj1apVHZ53zJgxGYSIiH79+kXfvn1jzZo1f3vNra2t0dbWFk1NTds8fvDBB8fJJ58cr732WkRErFq1Kr744ou44oortglCUaVSqdDjtZ6HjogCNbP166Q/+vLLL2PUqFGxdu3amDlzZrz11luxZMmS/M2Ytra2Ds/bu3fvdo917969otmObP2Evb21H3DAAfn8N998ExG/75aqsfU1bO8T/YYNG7a7A6jlPFRKFKiZ7X1affbZZ+Onn36KBQsWxCWXXBInnnhiHHPMMdGtW7cdsML2tr7Zrlu3rt1zX3/9dfTp0yciIvbbb7+IiPjqq6+qus7Wv1lYtmxZu+eWLVu23b9pqOU8VEoUKKR79+4RUdkn/Ij/C8XWuYiIcrkcDz74YO0XV4XGxsbo0aNHzJs3b5vHv/rqq3j99ddj7NixEfH77/43NDTE7NmzK/qbgv/vwAMPjOOOOy7mzZsXmzdvzsffeeedWLlyZZx33nmdOg+VEgUKOeKIIyIiYubMmdHa2hrvv/9+bNy48U+PP+WUU6Jbt24xceLEePnll+OZZ56JU089Nb7//vuarmvx4sVRV1cX06dPLzS3zz77xNSpU+P555+Pyy67LF5++eWYN29ejBkzJurr6+O2227LY2fNmhVr1qyJkSNHxpw5c2LRokUxZ86cmDRpUkXXmjFjRqxYsSIuvPDCaG5ujvnz58dFF10Uw4YNa/fD6oEDB7b7QX6ReaiWKFDI6NGj46abbooXXnghTjzxxDj22GNj6dKlf3r8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wd57713V3NKlSwvPDBo0qKprFXX++edXNffss8/WdiGwi6rk7d5OAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIAqW5HL4DtO+ecc6qa+6dubleNvfbaa0cvAeiAnQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJDcJfVfatOmTVXNbdmypfDMbrsV/2ywefPmwjODBw8uPAP8s+wUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQSuVyuVzRgaVSZ6+FGli+fHnhmbq64vdFvPPOOwvPPPLII4VngNqp5O3eTgGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAMkN8QB2EW6IB0AhogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkOoqPbBcLnfmOgD4F7BTACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACD9DzqsUpuUQtNrAAAAAElFTkSuQmCC",
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
   "execution_count": 12,
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
   "execution_count": 13,
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
     "execution_count": 13,
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
   "execution_count": 14,
   "id": "5129a72f-8350-45b7-b5d7-4b379ba2f69a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABN8AAAJuCAYAAACAKaRXAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAABciklEQVR4nO3debhVZd0H/O+RWYSjjAcSFREFB1SgEPJJVEQNRfN51dJIy6kccci5RFNQcirJAUMh0QefyimfIjAURxRRCs0wDacE0UQQVEDY7x+97Lcj4AAsDhw+n+va18W+12+t9bvPjjh+91r3qiiVSqUAAAAAAGvcRjXdAAAAAADUVsI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAoNYZOXJkKioq0rBhw7z66qvLbe/du3d23HHHGugseeihh1JRUZHf/OY3NXL+L+qVV15Jv3790qxZs1RUVGTgwIFf+BgVFRUZNGhQ+f2yz+eVV15ZpX4qKioycuTI8tjjjz+eQYMG5b333vvCx1uZ1ekRAOA/Cd8AgFpr4cKFufDCC2u6jfXa6aefnieffDK33HJLnnjiiZx++umrfcx+/frliSeeSJs2bb7wvm3atMkTTzyRfv36lccef/zxXHzxxWs0fAMAWFPq1nQDAABF2W+//XLHHXfkrLPOys4771zT7axVH374YRo2bJiKiorVOs5zzz2Xr3zlKzn44IPXTGNJWrZsmZYtW67Svg0aNMhuu+22xnoBACiaK98AgFrr7LPPTvPmzXPOOed8at2KbmVc5pO3TA4aNCgVFRX5y1/+kkMPPTSVlZVp1qxZzjjjjHz88ceZPn169ttvvzRp0iRbbbVVhg4dusJzfvTRRznjjDNSVVWVRo0aZY899sizzz67XN3TTz+d/v37p1mzZmnYsGF23XXX/O///m+1mmW3SI4bNy7f+9730rJly2y88cZZuHDhSuf82muv5dvf/nZatWqVBg0apHPnzrnqqquydOnSJP//7bEvvfRS/vCHP6SiouIzb8OcN29ejjvuuDRv3jybbLJJ9ttvv7z44ovL1a3ols5SqZTBgwdnyy23TMOGDdO9e/eMHz8+vXv3Tu/evct1n/ysBg0alB/+8IdJkvbt25f7fOihh1baZ5I8+eSTOfDAA9O8efM0bNgwHTp0+MxbasePH5+DDjoom2++eRo2bJhtttkmJ5xwQt55551qdW+//XaOP/74tGvXLg0aNEjLli3z1a9+NQ888EC55tlnn80BBxxQ/vm3bds2/fr1yxtvvPGpPQAA6x9XvgEAtVaTJk1y4YUX5rTTTsuECROy1157rbFjH3bYYfn2t7+dE044IePHj8/QoUOzePHiPPDAAznxxBNz1lln5Y477sg555yTbbbZJocccki1/c8///x07do1v/zlLzN37twMGjQovXv3zrPPPputt946SfLggw9mv/32S48ePXLjjTemsrIyY8aMyeGHH54PPvggRx99dLVjfu9730u/fv1y2223ZcGCBalXr94Ke3/77bfTq1evLFq0KD/5yU+y1VZb5f77789ZZ52Vl19+Oddff326du2aJ554It/4xjfSoUOHXHnllUmy0ltFS6VSDj744Dz++OP58Y9/nC9/+ct57LHHsv/++3+un+cFF1yQIUOG5Pjjj88hhxyS119/Pccee2wWL16cbbfddqX7HXvssXn33Xdz3XXX5a677ir3t/322690nz/+8Y858MAD07lz51x99dXZYost8sorr2TcuHGf2uPLL7+cnj175thjj01lZWVeeeWVXH311dl9990zbdq08s97wIABeeaZZ3LZZZdl2223zXvvvZdnnnkm//rXv5IkCxYsyD777JP27dvnF7/4RVq3bp1Zs2blwQcfzPvvv/+5fl4AwHqkBABQy9x6662lJKXJkyeXFi5cWNp6661L3bt3Ly1durRUKpVKe+yxR2mHHXYo18+YMaOUpHTrrbcud6wkpYsuuqj8/qKLLiolKV111VXV6nbZZZdSktJdd91VHlu8eHGpZcuWpUMOOaQ89uCDD5aSlLp27Vrup1QqlV555ZVSvXr1Sscee2x5rFOnTqVdd921tHjx4mrnOuCAA0pt2rQpLVmypNp8v/Od73yun8+5555bSlJ68sknq43/4Ac/KFVUVJSmT59eHttyyy1L/fr1+8xj/uEPfyglKf3sZz+rNn7ZZZct9zNc1u+MGTNKpVKp9O6775YaNGhQOvzww6vt+8QTT5SSlPbYY4/y2Io+q5/+9KfVjvdZOnToUOrQoUPpww8/XGnNJ3v8pKVLl5YWL15cevXVV0tJSvfee2952yabbFIaOHDgSo/99NNPl5KU7rnnns/VLwCwfnPbKQBQq9WvXz+XXnppnn766eVu11wdBxxwQLX3nTt3TkVFRbUrverWrZttttlmhU9cPeKII6qtx7blllumV69eefDBB5MkL730Uv72t7/lyCOPTJJ8/PHH5dfXv/71zJw5M9OnT692zP/+7//+XL1PmDAh22+/fb7yla9UGz/66KNTKpUyYcKEz3Wc/7Ss72X9LnPEEUd85r6TJk3KwoULc9hhh1Ub32233bLVVlt94V4+zYsvvpiXX345xxxzTBo2bPiF9p09e3a+//3vp127dqlbt27q1auXLbfcMknywgsvlOu+8pWvZOTIkbn00kszadKkLF68uNpxttlmm2y22WY555xzcuONN+avf/3r6k8MAFhnCd8AgFrvm9/8Zrp27ZoLLrhguSBkVTVr1qza+/r162fjjTdeLtCpX79+Pvroo+X2r6qqWuHYslsT33rrrSTJWWedlXr16lV7nXjiiUmy3Fpjn/fpof/6179WWNu2bdvy9i/qX//6V+rWrZvmzZtXG1/RPFe0b5K0bt16uW0rGlsdb7/9dpJk8803/0L7LV26NH379s1dd92Vs88+O3/605/y1FNPZdKkSUn+/YCLZe68884cddRR+eUvf5mePXumWbNm+c53vpNZs2YlSSorKzNx4sTssssuOf/887PDDjukbdu2ueiii9bY/z4BgHWHNd8AgFqvoqIiV1xxRfbZZ58MHz58ue3LArNPPqBgVUKoz2tZEPPJsWXhVYsWLZIk55133nLrxS2z3XbbVXv/eZ9s2rx588ycOXO58TfffLPaub+I5s2b5+OPP86//vWvagHciua5on2T/z9w/E+zZs1ao1e/LXvK6hd9sMFzzz2XP//5zxk5cmSOOuqo8vhLL720XG2LFi1y7bXX5tprr81rr72W++67L+eee25mz56dsWPHJkl22mmnjBkzJqVSKX/5y18ycuTIXHLJJWnUqFHOPffc1ZghALCuceUbALBB6NOnT/bZZ59ccsklmT9/frVtrVu3TsOGDfOXv/yl2vi9995bWD//8z//k1KpVH7/6quv5vHHHy8/2XO77bZLx44d8+c//zndu3df4atJkyardO699947f/3rX/PMM89UG//Vr36VioqK7Lnnnl/4mMv2uf3226uN33HHHZ+5b48ePdKgQYPceeed1cYnTZq0wlt2P6lBgwZJql99tjLbbrttOnTokFtuueVTnwb7ScuCzWXnWuamm2761P222GKLnHzyydlnn32W+3kvO+7OO++ca665JptuuukKawCA9Zsr3wCADcYVV1yRbt26Zfbs2dlhhx3K4xUVFfn2t7+dW265JR06dMjOO++cp5566nMFR6tq9uzZ+cY3vpHjjjsuc+fOzUUXXZSGDRvmvPPOK9fcdNNN2X///bPvvvvm6KOPzpe+9KW8++67eeGFF/LMM8/k17/+9Sqd+/TTT8+vfvWr9OvXL5dcckm23HLL/N///V+uv/76/OAHP/jUp4uuTN++ffO1r30tZ599dhYsWJDu3bvnsccey2233faZ+zZr1ixnnHFGhgwZks022yzf+MY38sYbb+Tiiy9OmzZtstFGn/598U477ZQk+dnPfpajjjoq9erVy3bbbbfScPIXv/hFDjzwwOy22245/fTTs8UWW+S1117LH//4x+XCw2U6deqUDh065Nxzz02pVEqzZs3yu9/9LuPHj69WN3fu3Oy555454ogj0qlTpzRp0iSTJ0/O2LFjy1cw3n///bn++utz8MEHZ+utt06pVMpdd92V9957L/vss89n/rwAgPWL8A0A2GDsuuuu+da3vrXCUO2qq65KkgwdOjTz58/PXnvtlfvvv3+NL/i/zODBgzN58uR897vfzbx58/KVr3wlY8aMSYcOHco1e+65Z5566qlcdtllGThwYObMmZPmzZtn++23X+7hBF9Ey5Yt8/jjj+e8887Leeedl3nz5mXrrbfO0KFDc8YZZ6zSMTfaaKPcd999OeOMMzJ06NAsWrQoX/3qV/P73/8+nTp1+sz9L7vssjRu3Dg33nhjbr311nTq1Ck33HBDLrjggmy66aafum/v3r1z3nnnZdSoUbn55puzdOnSPPjgg+WrCD9p3333zcMPP5xLLrkkp556aj766KNsvvnm6d+//0rPUa9evfzud7/LaaedlhNOOCF169ZNnz598sADD2SLLbYo1zVs2DA9evTIbbfdlldeeSWLFy/OFltskXPOOSdnn312kqRjx47ZdNNNM3To0Lz55pupX79+tttuu+VuaQUAaoeK0n/e7wAAAOuIGTNmpFOnTrnoooty/vnn13Q7AACrRPgGAECN+/Of/5z/+Z//Sa9evdK0adNMnz49Q4cOzbx58/Lcc8+t8aeeAgCsLW47BQCgxjVu3DhPP/10RowYkffeey+VlZXp3bt3LrvsMsEbALBec+UbAAAAABTk0x8dBQAAAACsMuEbAAAAABRE+AYAAAAABfHAhc9p6dKlefPNN9OkSZNUVFTUdDsAAAAA1JBSqZT3338/bdu2zUYbffq1bcK3z+nNN99Mu3btaroNAAAAANYRr7/+ejbffPNPrRG+fU5NmjRJ8u8fatOmTWu4GwAAAABqyrx589KuXbtyXvRphG+f07JbTZs2bSp8AwAAAOBzLU3mgQsAAAAAUBDhGwAAAAAURPgGAAAAAAURvgEAAABAQYRvAAAAAFAQ4RsAAAAAFET4BgAAAAAFEb4BAAAAQEGEbwAAAABQEOEbAAAAABRE+AbrkSFDhqSioiIDBw6sNv7CCy+kf//+qaysTJMmTbLbbrvltddeK2+fNWtWBgwYkKqqqjRu3Dhdu3bNb37zmxWeY+HChdlll11SUVGRqVOnFjgbAAAAqP2Eb7CemDx5coYPH54uXbpUG3/55Zez++67p1OnTnnooYfy5z//OT/60Y/SsGHDcs2AAQMyffr03HfffZk2bVoOOeSQHH744Xn22WeXO8/ZZ5+dtm3bFj4fAAAA2BAI32A9MH/+/Bx55JG5+eabs9lmm1XbdsEFF+TrX/96hg4dml133TVbb711+vXrl1atWpVrnnjiiZxyyin5yle+kq233joXXnhhNt100zzzzDPVjvWHP/wh48aNy5VXXrlW5gUAAAC1nfAN1gMnnXRS+vXrlz59+lQbX7p0af7v//4v2267bfbdd9+0atUqPXr0yD333FOtbvfdd8+dd96Zd999N0uXLs2YMWOycOHC9O7du1zz1ltv5bjjjsttt92WjTfeeC3MCgAAAGo/4Rus48aMGZNnnnkmQ4YMWW7b7NmzM3/+/Fx++eXZb7/9Mm7cuHzjG9/IIYcckokTJ5br7rzzznz88cdp3rx5GjRokBNOOCF33313OnTokCQplUo5+uij8/3vfz/du3dfa3MDAACA2q5uTTcArNzrr7+e0047LePGjau2htsyS5cuTZIcdNBBOf3005Mku+yySx5//PHceOON2WOPPZIkF154YebMmZMHHnggLVq0yD333JNDDz00jzzySHbaaadcd911mTdvXs4777y1NzkAAADYAAjfYB02ZcqUzJ49O926dSuPLVmyJA8//HCGDRuWBQsWpG7dutl+++2r7de5c+c8+uijSf79QIZhw4blueeeyw477JAk2XnnnfPII4/kF7/4RW688cZMmDAhkyZNSoMGDaodp3v37jnyyCMzatSogmcKAAAAtZPwDdZhe++9d6ZNm1Zt7Lvf/W46deqUc845Jw0aNMiXv/zlTJ8+vVrNiy++mC233DJJ8sEHHyRJNtqo+l3mderUKV859/Of/zyXXnppedubb76ZfffdN3feeWd69OixxucFAAAAGwrhG6zDmjRpkh133LHaWOPGjdO8efPy+A9/+MMcfvjh+drXvpY999wzY8eOze9+97s89NBDSZJOnTplm222yQknnJArr7wyzZs3zz333JPx48fn/vvvT5JsscUW1c6xySabJEk6dOiQzTffvOBZAgAAQO3lgQuwnvvGN76RG2+8MUOHDs1OO+2UX/7yl/ntb3+b3XffPUlSr169/P73v0/Lli1z4IEHpkuXLvnVr36VUaNG5etf/3oNdw8AAAC1W0WpVCrVdBPrg3nz5qWysjJz585N06ZNa7odAAAAAGrIF8mJXPkGAAAAAAWx5ht8TodcM6GmW9jg3HX6XjXdAgAAAKwWV74BAAAAQEGEbwAAAABQEOEbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAAAAURPgGAAAAAAURvgEAAABAQYRvAAAAAFAQ4RsAAAAAFET4BgAAAAAFEb4BAAAAQEGEbwAAAABQEOEbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAADVqyJAhqaioyMCBA1e4/YQTTkhFRUWuvfbaauMLFy7MKaeckhYtWqRx48bp379/3njjjWo1l112WXr16pWNN944m266aTETAPgUwjcAAABqzOTJkzN8+PB06dJlhdvvueeePPnkk2nbtu1y2wYOHJi77747Y8aMyaOPPpr58+fngAMOyJIlS8o1ixYtyqGHHpof/OAHhc0B4NMI3wAAAKgR8+fPz5FHHpmbb745m2222XLb//nPf+bkk0/O7bffnnr16lXbNnfu3IwYMSJXXXVV+vTpk1133TWjR4/OtGnT8sADD5TrLr744px++unZaaedCp8PwIoI3wAAAKgRJ510Uvr165c+ffost23p0qUZMGBAfvjDH2aHHXZYbvuUKVOyePHi9O3btzzWtm3b7Ljjjnn88ccL7Rvgi6hb0w0AAACw4RkzZkyeeeaZTJ48eYXbr7jiitStWzennnrqCrfPmjUr9evXX+6KudatW2fWrFlrvF+AVeXKNwBYQ1a0WPSgQYPSqVOnNG7cOJtttln69OmTJ598stp+vXv3TkVFRbXXN7/5zWo1FosGoDZ5/fXXc9ppp2X06NFp2LDhctunTJmSn/3sZxk5cmQqKiq+0LFLpdIX3gegSMI3AFgDVrZY9Lbbbpthw4Zl2rRpefTRR7PVVlulb9++efvtt6vVHXfccZk5c2b5ddNNN1XbbrFoAGqTKVOmZPbs2enWrVvq1q2bunXrZuLEifn5z3+eunXr5qGHHsrs2bOzxRZblLe/+uqrOfPMM7PVVlslSaqqqrJo0aLMmTOn2rFnz56d1q1b18CsAFbMbacAsJr+c7HoSy+9tNq2I444otr7q6++OiNGjMhf/vKX7L333uXxjTfeOFVVVSs9x8UXX5wkGTly5JprHABqyN57751p06ZVG/vud7+bTp065ZxzzkmbNm2y7777Vtu+7777ZsCAAfnud7+bJOnWrVvq1auX8ePH57DDDkuSzJw5M88991yGDh26diYC8DkI3wBgNf3nYtGfDN/+06JFizJ8+PBUVlZm5513rrbt9ttvz+jRo9O6devsv//+ueiii9KkSZOiWweAGtGkSZPsuOOO1cYaN26c5s2bl8ebN29ebXu9evVSVVWV7bbbLklSWVmZY445JmeeeWaaN2+eZs2a5ayzzspOO+1U7QEOr732Wt5999289tprWbJkSaZOnZok2WabbbLJJpsUOEuAfxO+AcBq+KzFopPk/vvvzze/+c188MEHadOmTcaPH58WLVqUtx955JFp3759qqqq8txzz+W8887Ln//854wfP35tTAEA1lvXXHNN6tatm8MOOywffvhh9t5774wcOTJ16tQp1/z4xz/OqFGjyu933XXXJMmDDz6Y3r17r+2WgQ1QRalUKtV0E+uDefPmpbKyMnPnzk3Tpk1ruh1qwCHXTKjpFjY4d52+V023AJ/q9ddfT/fu3TNu3LjylWy9e/fOLrvskmuvvbZct2DBgsycOTPvvPNObr755kyYMCFPPvlkWrVqtcLjTpkyJd27d8+UKVPStWvXattGjhyZgQMH5r333itqWgAAwGf4IjmRBy4AwCr6rMWilyxZkuTft9Fss8022W233TJixIjUrVs3I0aMWOlxu3btmnr16uXvf//72poKAABQELedAsAq+qzFov/zlpf/VCqVsnDhwpUe9/nnn8/ixYvTpk2bNdovAHzS8N4H1XQLG5zjH7q3plsA1jLhGwCsos9aLHrBggW57LLL0r9//7Rp0yb/+te/cv311+eNN97IoYcemiR5+eWXc/vtt+frX/96WrRokb/+9a8588wzs+uuu+arX/1q+bgWiwYAgPWT8A0AClKnTp387W9/y6hRo/LOO++kefPm+fKXv5xHHnkkO+ywQ5Kkfv36+dOf/pSf/exnmT9/ftq1a5d+/frloosuslg0AADUAsI3AFiDHnroofKfGzZsmLvuuutT69u1a5eJEyd+5nFHjhyZkSNHrmZ3AADA2uaBCwAAAABQEOEbAAAAABTEbacArPf23OO7Nd3CBufBibfWdAsAALBecOUbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAAAArNGTIkFRUVGTgwIHlsbvuuiv77rtvWrRokYqKikydOnW5/WbNmpUBAwakqqoqjRs3TteuXfOb3/ymWs2LL76Ygw46KC1atEjTpk3z1a9+NQ8++GDBM1r7hG8AAAAALGfy5MkZPnx4unTpUm18wYIF+epXv5rLL798pfsOGDAg06dPz3333Zdp06blkEMOyeGHH55nn322XNOvX798/PHHmTBhQqZMmZJddtklBxxwQGbNmlXYnGqC8A2ghqzKN0ivvPJKKioqVvj69a9/nSR56KGHVlozefLktThDAABgfTV//vwceeSRufnmm7PZZptV2zZgwID8+Mc/Tp8+fVa6/xNPPJFTTjklX/nKV7L11lvnwgsvzKabbppnnnkmSfLOO+/kpZdeyrnnnpsuXbqkY8eOufzyy/PBBx/k+eefL3Rua5vwDaAGrOo3SO3atcvMmTOrvS6++OI0btw4+++/f5KkV69ey9Uce+yx2WqrrdK9e/fC5wYAAKz/TjrppPTr1+9TA7ZPs/vuu+fOO+/Mu+++m6VLl2bMmDFZuHBhevfunSRp3rx5OnfunF/96ldZsGBBPv7449x0001p3bp1unXrtgZnUvPq1nQDABua//wG6dJLL622bcCAAUn+fYXbitSpUydVVVXVxu6+++4cfvjh2WSTTZIk9evXr1azePHi3HfffTn55JNTUVGxBmcCAADURmPGjMkzzzyzWnfO3HnnnTn88MPTvHnz1K1bNxtvvHHuvvvudOjQIUlSUVGR8ePH56CDDkqTJk2y0UYbpXXr1hk7dmw23XTTNTSTdYMr3wDWstX9Buk/TZkyJVOnTs0xxxyz0pr77rsv77zzTo4++ujVPh8AAFC7vf766znttNMyevToNGzYcJWPc+GFF2bOnDl54IEH8vTTT+eMM87IoYcemmnTpiVJSqVSTjzxxLRq1SqPPPJInnrqqRx00EE54IADMnPmzDU1nXWC8K2WW9Wnkpxwwgnp0KFDGjVqlJYtW+aggw7K3/72t/L2V155Jcccc0zat2+fRo0apUOHDrnooouyaNGitTArWH8t+wZpyJAha+R4I0aMSOfOndOrV69Prdl3333Trl27NXJOAKhpRf2Oa91UgH9/wT979ux069YtdevWTd26dTNx4sT8/Oc/T926dbNkyZLPPMbLL7+cYcOG5ZZbbsnee++dnXfeORdddFG6d++eX/ziF0mSCRMm5P7778+YMWPy1a9+NV27ds3111+fRo0aZdSoUUVPc60SvtViq/NUkm7duuXWW2/NCy+8kD/+8Y8plUrp27dv+S/Z3/72tyxdujQ33XRTnn/++VxzzTW58cYbc/755xc6J1ifralvkJb58MMPc8cdd3zqVW9vvPFG/vjHP35qDQCsT4r8Hde6qQDJ3nvvnWnTpmXq1KnlV/fu3XPkkUdm6tSpqVOnzmce44MPPkiSbLRR9dipTp06Wbp06afWbLTRRuWa2sKab7XU6qwplSTHH398+c9bbbVVLr300uy888555ZVX0qFDh+y3337Zb7/9yjVbb711pk+fnhtuuCFXXnnlmp0M1BL/+Q3SMkuWLMnDDz+cYcOGZeHChZ/rH7JlfvOb3+SDDz7Id77znZXW3HrrrWnevHn69++/Wr0DwLqg6N9xrZsKkDRp0iQ77rhjtbHGjRunefPm5fF33303r732Wt58880kyfTp05MkVVVVqaqqSqdOnbLNNtvkhBNOyJVXXpnmzZvnnnvuyfjx43P//fcnSXr27JnNNtssRx11VH784x+nUaNGufnmmzNjxoz069dvLc64eK58q6XW5JpSCxYsyK233pr27dt/6m1rc+fOTbNmzVb7fFBbrYlvkP7TiBEj0r9//7Rs2XKF20ulUm699dZ85zvfSb169dbEFACgRq3t33GtmwqwYvfdd1923XXXckj2zW9+M7vuumtuvPHGJEm9evXy+9//Pi1btsyBBx6YLl265Fe/+lVGjRqVr3/960mSFi1aZOzYsZk/f3722muvdO/ePY8++mjuvffe7LzzzjU2tyK48q0WWhNPJUmS66+/PmeffXYWLFiQTp06Zfz48alfv/4Ka19++eVcd911ueqqq1brnFCbrYlvkJZ56aWX8vDDD+f3v//9Ss83YcKEzJgxwy2nANQKNfE7rnVTAf7toYceqvb+6KOP/swvJjp27Jjf/va3n1rTvXv3/PGPf1zN7tZ9rnyrZdbkmlJHHnlknn322UycODEdO3bMYYcdlo8++mi5ujfffDP77bdfDj300Bx77LGrdU7Y0H3WN0jL3HLLLfnSl76Uvn37rvRYI0aMSK9evdK5c+dCewaAotXE77jWTQVgTakolUqlmm5ifTBv3rxUVlZm7ty5adq0aU23s1L33HNPvvGNb1S7fW3JkiWpqKjIRhttVG1NqVdeeSXt27fPs88+m1122eVTj7to0aJsttlm+eUvf5lvfetb5fE333wze+65Z3r06JGRI0cut1BibXLINRNquoUNzl2n71XTLbCe2HOP79Z0CxucByfeWtMtABuQtf07bpL85Cc/yXXXXZd//vOftXr5huG9D6rpFjY4xz90b023AKwBXyQncttpLbNsTan/9N3vfjedOnXKOeec84XXlPpPpVIpCxcuLL//5z//mT333LP81KjaHLwBsOEZMmRIzj///Jx22mm59tprk/z738KLL744w4cPz5w5c9KjR4/84he/yA477JDk//+P/hX53//93xx66KF55ZVX8pOf/CQTJkzIrFmz0rZt23z729/OBRdcsNJb32BDtzZ/x102Zt1UYF3wyvCTa7qFDc5Wxw9b48cUvtUya2JNqX/84x+5884707dv37Rs2TL//Oc/c8UVV6RRo0blhRHffPPN9O7dO1tssUWuvPLKvP322+Xz/ee6VLCuOuz4u2q6hQ3O/w4/pKZbgM9t8uTJGT58eLp06VJtfOjQobn66qszcuTIbLvttrn00kuzzz77ZPr06WnSpEnatWuXmTNnVttn+PDhGTp0aPbff/8kyd/+9rcsXbo0N910U7bZZps899xzOe6447JgwQJPDIeVWFu/4y5j3VRYPavyBdYyTzzxRC644II8+eSTqVevXnbZZZf84Q9/SKNGjZIk/fv3z9SpUzN79uxsttlm6dOnT6644oq0bdt2bU8TPjeXKm2APmtNqYYNG+aRRx7J17/+9WyzzTY57LDD0rhx4zz++ONp1apVkmTcuHF56aWXMmHChGy++eZp06ZN+QUA67P58+fnyCOPzM0335zNNtusPF4qlXLttdfmggsuyCGHHJIdd9wxo0aNygcffJA77rgjSVKnTp3yf+gve9199905/PDDs8kmmyRJ9ttvv9x6663p27dvtt566/Tv3z9nnXVW7rrLlwKwOtbE77jLWDcVVt1nfYE1bNiwTJ48OVVVVdlnn33y/vvvl2ueeOKJ7Lfffunbt2+eeuqpTJ48OSeffHK1u6z23HPP/O///m+mT5+e3/72t3n55Zfz//w//89amx+sCmu+fU7ry5pvFMeab2tfkWu+ufJt7Svyyjdrvq19tXnNt6OOOirNmjXLNddck969e2eXXXbJtddem3/84x/p0KFDnnnmmey6667l+oMOOiibbrppRo0atdyxpkyZku7du+exxx5Lr169VnrOCy+8MGPHjs3TTz9dyJwAVsaab2tfbV7zbf78+enatWuuv/76XHrppeV/Q0ulUtq2bZuBAwfmnHPOSZIsXLgwrVu3zhVXXJETTjghSbLbbrtln332yU9+8pPPfc777rsvBx98cBYuXFgrbxN32+na93lvO/0iOZEr3wAA/j9jxozJM888kyFDhiy3bdasWUmS1q1bVxtv3bp1edsnjRgxIp07d/7U4O3ll1/Oddddl+9///ur0TkA1LyTTjop/fr1S58+faqNz5gxI7NmzUrfvn3LYw0aNMgee+yRxx9/PEkye/bsPPnkk2nVqlV69eqV1q1bZ4899sijjz660vO9++67uf3229OrV69aGbxRe1jzDQAgyeuvv57TTjst48aNS8OGDVdaV1FRUe19qVRabixJPvzww9xxxx350Y9+tNJjvfnmm9lvv/1y6KGH5thjj1315mEt+vauu9d0Cxuc0c+uPHyAdcWyL7AmT5683LZP+wLr1VdfTZL84x//SJIMGjQoV155ZXbZZZf86le/yt57753nnnsuHTt2LO93zjnnZNiwYfnggw+y22675f777y9qWrBGCN8KMvgPj9V0Cxuc8/f/ak23AMB6bMqUKZk9e3a6detWHluyZEkefvjhDBs2rLx4+6xZs6qtcTp79uzl/mMiSX7zm9/kgw8+yHe+850Vnu/NN9/MnnvumZ49e2b48OFreDYAsPasiS+wli5dmiQ54YQT8t3v/ntJkV133TV/+tOfcsstt1S7Kv2HP/xhjjnmmLz66qu5+OKL853vfCf333//Cr8Mg3WB8A0AIMnee++dadOmVRv77ne/m06dOuWcc87J1ltvnaqqqowfP7685tuiRYsyceLEXHHFFcsdb8SIEenfv39atmy53LZ//vOf2XPPPdOtW7fceuut1RaSBoD1zZr4AmvZ+Pbbb1/t2J07d85rr71WbaxFixZp0aJFtt1223Tu3Dnt2rXLpEmT0rNnz0LmB6tL+AYAkKRJkybZcccdq401btw4zZs3L48PHDgwgwcPTseOHdOxY8cMHjw4G2+8cY444ohq+7300kt5+OGH8/vf/36587z55pvp3bt3tthii1x55ZV5++23y9uqqqoKmBkAFGtNfIG11VZbpW3btuWgbpkXX3wx+++//0rPvewZkgsXLlyTU4I1SvgGAPA5nX322fnwww9z4oknZs6cOenRo0fGjRuXJk2aVKu75ZZb8qUvfanawtLLjBs3Li+99FJeeumlbL755tW2eQg9AOujNfEFVkVFRX74wx/moosuys4775xddtklo0aNyt/+9rf85je/SZI89dRTeeqpp7L77rtns802yz/+8Y/8+Mc/TocOHVz1xjpN+AYAsBIPPfRQtfcVFRUZNGhQBg0a9Kn7DR48OIMHD17htqOPPjpHH330mmkQANYTn+cLrIEDB+ajjz7K6aefnnfffTc777xzxo8fnw4dOiRJGjVqlLvuuisXXXRRFixYkDZt2mS//fbLmDFj0qBBg5qaGnwm4RsAAACwRq3qF1jnnntuzj333BVu22mnnTJhwoQ11CGsPcI3AGCdss02O9R0Cxucl156vqZbAACotYRvAAAAUAtMOubrNd3CBme3Ecs/XAk+yXPtAQAAAKAgwjcAAAAAKMg6E74NGTIkFRUVGThwYHmsVCpl0KBBadu2bRo1apTevXvn+eerr0mycOHCnHLKKWnRokUaN26c/v3754033qhWM2fOnAwYMCCVlZWprKzMgAED8t57762FWQEAAACwIVsnwrfJkydn+PDh6dKlS7XxoUOH5uqrr86wYcMyefLkVFVVZZ999sn7779frhk4cGDuvvvujBkzJo8++mjmz5+fAw44IEuWLCnXHHHEEZk6dWrGjh2bsWPHZurUqRkwYMBamx8AAAAAG6YaD9/mz5+fI488MjfffHM222yz8nipVMq1116bCy64IIccckh23HHHjBo1Kh988EHuuOOOJMncuXMzYsSIXHXVVenTp0923XXXjB49OtOmTcsDDzyQJHnhhRcyduzY/PKXv0zPnj3Ts2fP3Hzzzbn//vszffr0GpkzAAAAABuGGg/fTjrppPTr1y99+vSpNj5jxozMmjUrffv2LY81aNAge+yxRx5//PEkyZQpU7J48eJqNW3bts2OO+5YrnniiSdSWVmZHj16lGt22223VFZWlmtWZOHChZk3b161FwAAAAB8EXVr8uRjxozJM888k8mTJy+3bdasWUmS1q1bVxtv3bp1Xn311XJN/fr1q10xt6xm2f6zZs1Kq1atljt+q1atyjUrMmTIkFx88cVfbEIAAAAA8B9q7Mq3119/PaeddlpGjx6dhg0brrSuoqKi2vtSqbTc2Cd9smZF9Z91nPPOOy9z584tv15//fVPPScAAAAAfFKNhW9TpkzJ7Nmz061bt9StWzd169bNxIkT8/Of/zx169YtX/H2yavTZs+eXd5WVVWVRYsWZc6cOZ9a89Zbby13/rfffnu5q+r+U4MGDdK0adNqLwAAAAD4ImosfNt7770zbdq0TJ06tfzq3r17jjzyyEydOjVbb711qqqqMn78+PI+ixYtysSJE9OrV68kSbdu3VKvXr1qNTNnzsxzzz1XrunZs2fmzp2bp556qlzz5JNPZu7cueUaAAAAAChCja351qRJk+y4447Vxho3bpzmzZuXxwcOHJjBgwenY8eO6dixYwYPHpyNN944RxxxRJKksrIyxxxzTM4888w0b948zZo1y1lnnZWddtqp/ACHzp07Z7/99stxxx2Xm266KUly/PHH54ADDsh22223FmcMAAAAwIamRh+48FnOPvvsfPjhhznxxBMzZ86c9OjRI+PGjUuTJk3KNddcc03q1q2bww47LB9++GH23nvvjBw5MnXq1CnX3H777Tn11FPLT0Xt379/hg0bttbnAwAAAMCGZZ0K3x566KFq7ysqKjJo0KAMGjRopfs0bNgw1113Xa677rqV1jRr1iyjR49eQ10CAAAAwOdTY2u+AQAAAEBtJ3wDAAAAgIII3wAAAACgIMI3AABqnRtuuCFdunRJ06ZN07Rp0/Ts2TN/+MMfytsrKipW+PrpT39arnn55ZfzjW98Iy1btkzTpk1z2GGH5a233qp2nq222mq5Y5x77rlrbZ4AwLpP+AYAQK2z+eab5/LLL8/TTz+dp59+OnvttVcOOuigPP/880mSmTNnVnvdcsstqaioyH//938nSRYsWJC+ffumoqIiEyZMyGOPPZZFixblwAMPzNKlS6ud65JLLql2rAsvvHCtzxcAWHetU087BQCANeHAAw+s9v6yyy7LDTfckEmTJmWHHXZIVVVVte333ntv9txzz2y99dZJksceeyyvvPJKnn322TRt2jRJcuutt6ZZs2aZMGFC+vTpU963SZMmyx0PAGAZV74BAFCrLVmyJGPGjMmCBQvSs2fP5ba/9dZb+b//+78cc8wx5bGFCxemoqIiDRo0KI81bNgwG220UR599NFq+19xxRVp3rx5dtlll1x22WVZtGhRcZMBANY7rnwDAKBWmjZtWnr27JmPPvoom2yySe6+++5sv/32y9WNGjUqTZo0ySGHHFIe22233dK4ceOcc845GTx4cEqlUs4555wsXbo0M2fOLNeddtpp6dq1azbbbLM89dRTOe+88zJjxoz88pe/XCtzBADWfa58AwCgVtpuu+0yderUTJo0KT/4wQ9y1FFH5a9//etydbfcckuOPPLINGzYsDzWsmXL/PrXv87vfve7bLLJJqmsrMzcuXPTtWvX1KlTp1x3+umnZ4899kiXLl1y7LHH5sYbb8yIESPyr3/9a63MEQBY97nyDQCAWql+/frZZpttkiTdu3fP5MmT87Of/Sw33XRTueaRRx7J9OnTc+eddy63f9++ffPyyy/nnXfeSd26dbPpppumqqoq7du3X+k5d9tttyTJSy+9lObNm6/hGQEA6yPhGwAAG4RSqZSFCxdWGxsxYkS6deuWnXfeeaX7tWjRIkkyYcKEzJ49O/37919p7bPPPpskadOmzRroGACoDYRvAADUOueff37233//tGvXLu+//37GjBmThx56KGPHji3XzJs3L7/+9a9z1VVXrfAYt956azp37pyWLVvmiSeeyGmnnZbTTz892223XZLkiSeeyKRJk7LnnnumsrIykydPzumnn57+/ftniy22WCvzBADWfcI3AABqnbfeeisDBgzIzJkzU1lZmS5dumTs2LHZZ599yjVjxoxJqVTKt771rRUeY/r06TnvvPPy7rvvZquttsoFF1yQ008/vby9QYMGufPOO3PxxRdn4cKF2XLLLXPcccfl7LPPLnx+AMD6Q/gGAECtM2LEiM+sOf7443P88cevdPvll1+eyy+/fKXbu3btmkmTJq1SfwDAhsPTTgEAAACgIMI3AAAAACiI204BACjUTu071HQLG5xpM16u6RYAgP+PK98AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAAChIjYZvN9xwQ7p06ZKmTZumadOm6dmzZ/7whz+Ut5dKpQwaNCht27ZNo0aN0rt37zz//PPVjrFw4cKccsopadGiRRo3bpz+/fvnjTfeqFYzZ86cDBgwIJWVlamsrMyAAQPy3nvvrY0pAgAAALABq9HwbfPNN8/ll1+ep59+Ok8//XT22muvHHTQQeWAbejQobn66qszbNiwTJ48OVVVVdlnn33y/vvvl48xcODA3H333RkzZkweffTRzJ8/PwcccECWLFlSrjniiCMyderUjB07NmPHjs3UqVMzYMCAtT5fAAAAADYsdWvy5AceeGC195dddlluuOGGTJo0Kdtvv32uvfbaXHDBBTnkkEOSJKNGjUrr1q1zxx135IQTTsjcuXMzYsSI3HbbbenTp0+SZPTo0WnXrl0eeOCB7LvvvnnhhRcyduzYTJo0KT169EiS3HzzzenZs2emT5+e7bbbbu1OGgAAAIANxjqz5tuSJUsyZsyYLFiwID179syMGTMya9as9O3bt1zToEGD7LHHHnn88ceTJFOmTMnixYur1bRt2zY77rhjueaJJ55IZWVlOXhLkt122y2VlZXlmhVZuHBh5s2bV+0FAAAAAF9EjYdv06ZNyyabbJIGDRrk+9//fu6+++5sv/32mTVrVpKkdevW1epbt25d3jZr1qzUr18/m2222afWtGrVarnztmrVqlyzIkOGDCmvEVdZWZl27dqt1jwBAAAA2PDUePi23XbbZerUqZk0aVJ+8IMf5Kijjspf//rX8vaKiopq9aVSabmxT/pkzYrqP+s45513XubOnVt+vf766593SgAAAACQZB0I3+rXr59tttkm3bt3z5AhQ7LzzjvnZz/7WaqqqpJkuavTZs+eXb4arqqqKosWLcqcOXM+teatt95a7rxvv/32clfV/acGDRqUn8K67AUAAAAAX0SNh2+fVCqVsnDhwrRv3z5VVVUZP358eduiRYsyceLE9OrVK0nSrVu31KtXr1rNzJkz89xzz5Vrevbsmblz5+app54q1zz55JOZO3duuQYAAAAAilCjTzs9//zzs//++6ddu3Z5//33M2bMmDz00EMZO3ZsKioqMnDgwAwePDgdO3ZMx44dM3jw4Gy88cY54ogjkiSVlZU55phjcuaZZ6Z58+Zp1qxZzjrrrOy0007lp5927tw5++23X4477rjcdNNNSZLjjz8+BxxwgCedAgAAAFCoGg3f3nrrrQwYMCAzZ85MZWVlunTpkrFjx2afffZJkpx99tn58MMPc+KJJ2bOnDnp0aNHxo0blyZNmpSPcc0116Ru3bo57LDD8uGHH2bvvffOyJEjU6dOnXLN7bffnlNPPbX8VNT+/ftn2LBha3eyAAAAAGxwajR8GzFixKdur6ioyKBBgzJo0KCV1jRs2DDXXXddrrvuupXWNGvWLKNHj17VNgEAAABglaxza74BAAAAQG0hfAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAggjfAAAAAKAgwjcAAAAAKIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCCrFL7ttddeee+995YbnzdvXvbaa6/V7QkAAAAAaoVVCt8eeuihLFq0aLnxjz76KI888shqNwUAAAAAtUHdL1L8l7/8pfznv/71r5k1a1b5/ZIlSzJ27Nh86UtfWnPdAQAAAMB67AuFb7vssksqKipSUVGxwttLGzVqlOuuu26NNQcAAAAA67MvFL7NmDEjpVIpW2+9dZ566qm0bNmyvK1+/fpp1apV6tSps8abBAAAAID10RcK37bccsskydKlSwtpBgAAAABqky8Uvv2nF198MQ899FBmz569XBj34x//eLUbAwAAAID13SqFbzfffHN+8IMfpEWLFqmqqkpFRUV5W0VFhfANAAAAALKK4dull16ayy67LOecc86a7gcAAAAAao2NVmWnOXPm5NBDD13TvQAAAABArbJK4duhhx6acePGreleAAAAAKBWWaXbTrfZZpv86Ec/yqRJk7LTTjulXr161bafeuqpa6Q5AAAAAFifrVL4Nnz48GyyySaZOHFiJk6cWG1bRUWF8A0AAAAAsorh24wZM9Z0HwAAAABQ66zSmm8AAAAAwGdbpSvfvve9733q9ltuuWWVmgEAAACA2mSVwrc5c+ZUe7948eI899xzee+997LXXnutkcYAAAAAYH23SuHb3XffvdzY0qVLc+KJJ2brrbde7aYAAAAAoDZYY2u+bbTRRjn99NNzzTXXrKlDAgAAAMB6bY0+cOHll1/Oxx9/vCYPCQAAAADrrVW67fSMM86o9r5UKmXmzJn5v//7vxx11FFrpDEAAAAAWN+tUvj27LPPVnu/0UYbpWXLlrnqqqs+80moAAAAALChWKXw7cEHH1zTfQAAAABArbNK4dsyb7/9dqZPn56Kiopsu+22admy5ZrqCwAAAADWe6v0wIUFCxbke9/7Xtq0aZOvfe1r+a//+q+0bds2xxxzTD744IM13SMAAAAArJdWKXw744wzMnHixPzud7/Le++9l/feey/33ntvJk6cmDPPPHNN9wgAAAAA66VVuu30t7/9bX7zm9+kd+/e5bGvf/3radSoUQ477LDccMMNa6o/AAAAAFhvrdKVbx988EFat2693HirVq3cdgoAAAAA/59VCt969uyZiy66KB999FF57MMPP8zFF1+cnj17rrHmAAAAAGB9tkq3nV577bXZf//9s/nmm2fnnXdORUVFpk6dmgYNGmTcuHFrukcAAAAAWC+tUvi200475e9//3tGjx6dv/3tbymVSvnmN7+ZI488Mo0aNVrTPQIAAADAemmVwrchQ4akdevWOe6446qN33LLLXn77bdzzjnnrJHmAAAAAGB9tkprvt10003p1KnTcuM77LBDbrzxxtVuCgAAAABqg1UK32bNmpU2bdosN96yZcvMnDlztZsCAAAAgNpglcK3du3a5bHHHltu/LHHHkvbtm1XuykAAAAAqA1Wac23Y489NgMHDszixYuz1157JUn+9Kc/5eyzz86ZZ565RhsEAAAAgPXVKoVvZ599dt59992ceOKJWbRoUZKkYcOGOeecc3Leeeet0QYBAAAAYH21SuFbRUVFrrjiivzoRz/KCy+8kEaNGqVjx45p0KDBmu4PAAAAANZbqxS+LbPJJpvky1/+8prqBQAAAABqlVV64AIAAAAA8NmEbwAAAABQEOEbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAAAAURPgGAAAAAAURvgEAAABAQYRvAAAAAFAQ4RsAAAAAFET4BgAAAAAFEb4BAAAAQEGEbwAAAABQEOEbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAA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KIjwDQAAAAAKInwDAAAAgIII3wAAAACgIMI3AAAAACiI8A0AAAAACiJ8AwAAAICCCN8AAAAAoCDCNwAAAAAoiPANAAAAAAoifAMAAACAgtRo+Pbwww/nwAMPTNu2bVNRUZF77rmn2vZSqZRBgwalbdu2adSoUXr37p3nn3++Ws3ChQtzyimnpEWLFmncuHH69++fN954o1rNnDlzMmDAgFRWVqaysjIDBgzIe++9V/DsAAAAANjQ1Wj4tmDBguy8884ZNmzYCrcPHTo0V199dYYNG5bJkyenqqoq++yzT95///1yzcCBA3P33XdnzJgxefTRRzN//vwccMABWbJkSbnmiCOOyNSpUzN27NiMHTs2U6dOzYABAwqfHwAAAAAbtro1efL9998/+++//wq3lUqlXHvttbngggtyyCGHJElGjRqV1q1b54477sgJJ5yQuXPnZsSIEbntttvSp0+fJMno0aPTrl27PPDAA9l3333zwgsvZOzYsZk0aVJ69OiRJLn55pvTs2fPTJ8+Pdttt93amSwAAAAAG5x1ds23GTNmZNasWenbt295rEGDBtljjz3y+OOPJ0mmTJmSxYsXV6tp27Ztdtxxx3LNE088kcrKynLwliS77bZbKisryzUrsnDhwsybN6/aCwAAAAC+iHU2fJs1a1aSpHXr1tXGW7duXd42a9as1K9fP5ttttmn1rRq1Wq547dq1apcsyJDhgwprxFXWVmZdu3ardZ8AAAAANjwrLPh2zIVFRXV3pdKpeXGPumTNSuq/6zjnHfeeZk7d2759frrr3/BzgEAAADY0K2z4VtVVVWSLHd12uzZs8tXw1VVVWXRokWZM2fOp9a89dZbyx3/7bffXu6quv/UoEGDNG3atNoLAAAAAL6IdTZ8a9++faqqqjJ+/Pjy2KJFizJx4sT06tUrSdKtW7fUq1evWs3MmTPz3HPPlWt69uyZuXPn5qmnnirXPPnkk5k7d265BgAAAACKUKNPO50/f35eeuml8vsZM2Zk6tSpadasWbbYYosMHDgwgwcPTseOHdOxY8cMHjw4G2+8cY444ogkSWVlZY455piceeaZad68eZo1a5azzjorO+20U/npp507d85+++2X4447LjfddFOS5Pjjj88BBxzgSacAAAAAFKpGw7enn346e+65Z/n9GWeckSQ56qijMnLkyJx99tn5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u2TKlCk13RarYKuttlru72dFRUVOOumkmm6NVfDxxx/nwgsvTPv27dOoUaNsvfXWueSSS7J06dKabo3V8P7772fgwIHZcsst06hRo/Tq1SuTJ0+u6bZqnPCNJMmdd96ZgQMH5oILLsizzz6b//qv/8r++++f1157raZbYxUsWLAgO++8c4YNG1bTrbAGTJw4MSeddFImTZqU8ePH5+OPP07fvn2zYMGCmm6NVbD55pvn8ssvz9NPP52nn346e+21Vw466KA8//zzNd0aq2ny5MkZPnx4unTpUtOtsJp22GGHzJw5s/yaNm1aTbfEKpozZ06++tWvpl69evnDH/6Qv/71r7nqqquy6aab1nRrrILJkydX+7s5fvz4JMmhhx5aw52xKq644orceOONGTZsWF544YUMHTo0P/3pT3PdddfVdGushmOPPTbjx4/PbbfdlmnTpqVv377p06dP/vnPf9Z0azWqolQqlWq6CWpejx490rVr19xwww3lsc6dO+fggw/OkCFDarAzVldFRUXuvvvuHHzwwTXdCmvI22+/nVatWmXixIn52te+VtPtsAY0a9YsP/3pT3PMMcfUdCusovnz56dr1665/vrrc+mll2aXXXbJtddeW9NtsQoGDRqUe+65J1OnTq3pVlgDzj333Dz22GPu6KilBg4cmPvvvz9///vfU1FRUdPt8AUdcMABad26dUaMGFEe++///u9svPHGue2222qwM1bVhx9+mCZNmuTee+9Nv379yuO77LJLDjjggFx66aU12F3NcuUbWbRoUaZMmZK+fftWG+/bt28ef/zxGuoKWJm5c+cm+Xdgw/ptyZIlGTNmTBYsWJCePXvWdDushpNOOin9+vVLnz59aroV1oC///3vadu2bdq3b59vfvOb+cc//lHTLbGK7rvvvnTv3j2HHnpoWrVqlV133TU333xzTbfFGrBo0aKMHj063/ve9wRv66ndd989f/rTn/Liiy8mSf785z/n0Ucfzde//vUa7oxV9fHHH2fJkiVp2LBhtfFGjRrl0UcfraGu1g11a7oBat4777yTJUuWpHXr1tXGW7dunVmzZtVQV8CKlEqlnHHGGdl9992z44471nQ7rKJp06alZ8+e+eijj7LJJpvk7rvvzvbbb1/TbbGKxowZk2eeecZ6JrVEjx498qtf/Srbbrtt3nrrrVx66aXp1atXnn/++TRv3rym2+ML+sc//pEbbrghZ5xxRs4///w89dRTOfXUU9OgQYN85zvfqen2WA333HNP3nvvvRx99NE13Qqr6JxzzsncuXPTqVOn1KlTJ0uWLMlll12Wb33rWzXdGquoSZMm6dmzZ37yk5+kc+fOad26df7nf/4nTz75ZDp27FjT7dUo4Rtln/zGqFQq+RYJ1jEnn3xy/vKXv2zw3xyt77bbbrtMnTo17733Xn7729/mqKOOysSJEwVw66HXX389p512WsaNG7fct7ysn/bff//yn3faaaf07NkzHTp0yKhRo3LGGWfUYGesiqVLl6Z79+4ZPHhwkmTXXXfN888/nxtuuEH4tp4bMWJE9t9//7Rt27amW2EV3XnnnRk9enTuuOOO7LDDDpk6dWoGDhyYtm3b5qijjqrp9lhFt912W773ve/lS1/6UurUqZOuXbvmiCOOyDPPPFPTrdUo4Rtp0aJF6tSps9xVbrNnz17uajig5pxyyim577778vDDD2fzzTev6XZYDfXr188222yTJOnevXsmT56cn/3sZ7nppptquDO+qClTpmT27Nnp1q1beWzJkiV5+OGHM2zYsCxcuDB16tSpwQ5ZXY0bN85OO+2Uv//97zXdCqugTZs2y32x0blz5/z2t7+toY5YE1599dU88MADueuuu2q6FVbDD3/4w5x77rn55je/meTfX3i8+uqrGTJkiPBtPdahQ4dMnDgxCxYsyLx589KmTZscfvjhad++fU23VqOs+Ubq16+fbt26lZ8WtMz48ePTq1evGuoKWKZUKuXkk0/OXXfdlQkTJmzw/3DVRqVSKQsXLqzpNlgFe++9d6ZNm5apU6eWX927d8+RRx6ZqVOnCt5qgYULF+aFF15ImzZtaroVVsFXv/rVTJ8+vdrYiy++mC233LKGOmJNuPXWW9OqVatqC7qz/vnggw+y0UbVI4k6depk6dKlNdQRa1Ljxo3Tpk2bzJkzJ3/84x9z0EEH1XRLNcqVbyRJzjjjjAwYMCDdu3dPz549M3z48Lz22mv5/ve/X9OtsQrmz5+fl156qfx+xowZmTp1apo1a5YtttiiBjtjVZx00km54447cu+996ZJkyblq1QrKyvTqFGjGu6OL+r888/P/vvvn3bt2uX999/PmDFj8tBDD2Xs2LE13RqroEmTJsutv9i4ceM0b97cuozrqbPOOisHHnhgtthii8yePTuXXnpp5s2b5yqM9dTpp5+eXr16ZfDgwTnssMPy1FNPZfjw4Rk+fHhNt8YqWrp0aW699dYcddRRqVvXf86uzw488MBcdtll2WKLLbLDDjvk2WefzdVXX53vfe97Nd0aq+GPf/xjSqVStttuu7z00kv54Q9/mO222y7f/e53a7q1GuX/rUiSHH744fnXv/6VSy65JDNnzsyOO+6Y3//+974VXE89/fTT2XPPPcvvl61Rc9RRR2XkyJE11BWr6oYbbkiS9O7du9r4rbfeapHh9dBbb72VAQMGZObMmamsrEyXLl0yduzY7LPPPjXdGpDkjTfeyLe+9a288847admyZXbbbbdMmjTJ70TrqS9/+cu5++67c9555+WSSy5J+/btc+211+bII4+s6dZYRQ888EBee+01AU0tcN111+VHP/pRTjzxxMyePTtt27bNCSeckB//+Mc13RqrYe7cuTnvvPPyxhtvpFmzZvnv//7vXHbZZalXr15Nt1ajKkqlUqmmmwAAAACA2siabwAAAABQEOEbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAAAAURPgGAAAAAAURvgEAAABAQYRvAAAbmN69e2fgwIGfq/ahhx5KRUVF3nvvvdU651ZbbZVrr712tY4BALA+Er4BAAAAQEGEbwAAAABQEOEbAMAGbPTo0enevXuaNGmSqqqqHHHEEZk9e/ZydY899lh23nnnNGzYMD169Mi0adOqbX/88cfzta99LY0aNUq7du1y6qmnZsGCBWtrGgAA6yzhGwDABmzRokX5yU9+kj//+c+55557MmPGjBx99NHL1f3whz/MlVdemcmTJ6dVq1bp379/Fi9enCSZNm1a9t133xxyyCH5y1/+kjvvvDOPPvpoTj755LU8GwCAdU/dmm4AAICa873vfa/856233jo///nP85WvfCXz58/PJptsUt520UUXZZ999kmSjBo1KptvvnnuvvvuHHbYYfnpT3+aI444ovwQh44dO+bnP/959thjj9xwww1p2LDhWp0TAMC6xJVvAAAbsGeffTYHHXRQttxyyzRp0iS9e/dOkrz22mvV6nr27Fn+c7NmzbLddtvlhRdeSJJMmTIlI0eOzCabbFJ+7bvvvlm6dGlmzJix1uYCALAucuUbAMAGasGCBenbt2/69u2b0aNHp2XLlnnttdey7777ZtGiRZ+5f0VFRZJk6dKlOeGEE3LqqacuV7PFFlus8b4BANYnwjcAgA3U3/72t7zzzju5/PLL065duyTJ008/vcLaSZMmlYO0OXPm5MUXX0ynTp2SJF27ds3zzz+fbbbZZu00DgCwHnHbKQDABmqLLbZI/fr1c9111+Uf//hH7rvvvvzkJz9ZYe0ll1ySP/3pT3nuuedy9NFHp0WLFjn44IOTJOecc06eeOKJnHTSSZk6dWr+/ve/57777sspp5yyFmcDALBuEr4BAGygWrZsmZEjR+bXv/51tt9++1x++eW58sorV1h7+eWX57TTTku3bt0yc+bM3Hfffalfv36SpEuXLpk4cWL+/ve/57/+67+y66675kc/+lHatGmzNqcDALBOqiiVSqWabgIAAAAAaiNXvgEAAABAQYRvAAAAAFAQ4RsAAAAAFET4BgAAAAAFEb4BAAAAQEGEbwAAAABQEOEbAAAAABRE+AYAAAAABRG+AQAAAEBBhG8AAAAAUBDhGwAAAAAU5P8FkPnad3On3ewAAAAASUVORK5CYII=",
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
   "execution_count": 15,
   "id": "c6abbc56-b339-4642-823b-5fbef119f3a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 15,
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
   "execution_count": 16,
   "id": "203bbe15-75ec-4202-871a-dcc16e778cfc",
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
    "missing_values = test.isnull().any(axis=1)\n",
    "count_missing_values = missing_values.sum()\n",
    "count_missing_values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "882b7a06-220f-4aa2-9caa-6f5b338084f4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((42000, 784), (28000, 784))"
      ]
     },
     "execution_count": 17,
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
   "execution_count": 18,
   "id": "8616be13-b6c4-4868-913c-46448c356726",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((42000, 28, 28, 1), (28000, 28, 28, 1))"
      ]
     },
     "execution_count": 18,
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
   "execution_count": 19,
   "id": "3df5db8a-e6dc-4b85-8464-16a7f4530c76",
   "metadata": {},
   "outputs": [],
   "source": [
    "#pip install tensorflow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "db861f4a-e6ed-4562-8bc9-8c89acdbe886",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-30 02:42:28.375351: I external/local_xla/xla/tsl/cuda/cudart_stub.cc:32] Could not find cuda drivers on your machine, GPU will not be used.\n",
      "2024-10-30 02:42:28.379757: I external/local_xla/xla/tsl/cuda/cudart_stub.cc:32] Could not find cuda drivers on your machine, GPU will not be used.\n",
      "2024-10-30 02:42:28.391590: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered\n",
      "2024-10-30 02:42:28.408563: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered\n",
      "2024-10-30 02:42:28.413262: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered\n",
      "2024-10-30 02:42:28.426123: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\n",
      "To enable the following instructions: AVX2 AVX512F FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\n",
      "2024-10-30 02:42:30.024313: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT\n"
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
   "execution_count": 21,
   "id": "1659d280-f0e7-4911-9303-2a581a1b78c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((37800, 28, 28, 1), (4200, 28, 28, 1), (37800, 10), (4200, 10))"
      ]
     },
     "execution_count": 21,
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
   "execution_count": 22,
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
   "execution_count": 23,
   "id": "4cd21efe-c5f0-4dd6-ab27-18e1e46d1188",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix , classification_report\n",
    "from tensorflow.keras.models import Sequential\n",
    "from tensorflow.keras.layers import Dropout, Dense, Flatten, Conv2D, MaxPool2D\n",
    "from tensorflow.keras.optimizers import Adam # Adaptive Moment Estimation\n",
    "from tensorflow.keras.preprocessing.image import ImageDataGenerator"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a96803e-60bc-4f9f-9cb9-0d3a168aae32",
   "metadata": {},
   "source": [
    "#### CNN is used for image classification and object detection \n",
    "\n",
    "After having convolution layer we use ReLU to break up linearity. Increase nonlinearity. Because images are non linear.\n",
    "\n",
    "#### Padding\n",
    "As we keep applying conv layers, the size of the volume will decrease faster than we would like. In the early layers of our network, we want to preserve as much information about the original input volume so that we can extract those low level features.\n",
    "input size and output size are same\n",
    "\n",
    "\n",
    "#### Max Pooling\n",
    "It makes down-sampling or sub-sampling (Reduces the number of parameters)\n",
    "It makes the detection of features invariant to scale or orientation changes.\n",
    "It reduce the amount of parameters and computation in the network, and hence to also control overfitting\n",
    "\n",
    "\n",
    "#### Flattening \n",
    "\n",
    "\n",
    "Full Connection\n",
    "Neurons in a fully connected layer have connections to all activations in the previous layer\n",
    "Artificial Neural Netwo\n",
    "\n",
    "Implementing with Keras¶\n",
    "\n",
    "Create Model\n",
    "conv => max pool => dropout => conv => max pool => dropout => fully connected (2 layer)\n",
    "Dropout: Dropout is a technique where randomly selected neurons are ignored during trails"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
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
    "model.add(Conv2D(filters = 16, kernel_size=(3,3), padding = 'Same', activation = 'relu'))\n",
    "model.add(MaxPool2D(pool_size=(2,2), strides = (2,2)))\n",
    "model.add(Dropout(0.25))\n",
    "\n",
    "model.add(Flatten())\n",
    "model.add(Dense(256, activation = 'relu'))\n",
    "model.add(Dropout(0.5))\n",
    "model.add(Dense(10, activation = 'softmax'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "18f2961b-b1e4-4586-bf82-0ea0fe14ab60",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the optimizer \n",
    "\n",
    "optimizer = Adam(learning_rate = 0.001, beta_1 = 0.9, beta_2 = 0.999)\n",
    "model.compile(optimizer=optimizer, loss = 'categorical_crossentropy', metrics = ['accuracy'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4d69bd95-1a0b-4066-b8ef-daad421f74c6",
   "metadata": {},
   "source": [
    "Epochs and Batch Size Say you have a dataset of 10 examples (or samples). You have a batch size of 2, and you've specified you want the algorithm to run for 3 epochs. Therefore, in each epoch, you have 5 batches (10/2 = 5). Each batch gets passed through the algorithm, therefore you have 5 iterations per epoch. reference: \n",
    "\n",
    "https://stackoverflow.com/questions/4752626/epoch-vs-iteration-when-training-neural-networks\n",
    "\n",
    "\n",
    "Data Augmentation To avoid overfitting problem, we need to expand artificially our handwritten digit dataset Alter the training data with small transformations to reproduce the variations of digit. For example, the number is not centered The scale is not the same (some who write with big/small numbers) The image is rotated."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "b5825f28-0647-410c-a39f-d2d6a5869377",
   "metadata": {},
   "outputs": [],
   "source": [
    "epoch = 10\n",
    "batch_size = 250\n",
    "\n",
    "datagen = ImageDataGenerator(featurewise_center = False, \n",
    "                            samplewise_center = False,\n",
    "                            featurewise_std_normalization = False, \n",
    "                            zca_whitening = False, \n",
    "                            rotation_range = 5,\n",
    "                            zoom_range = 0.1, \n",
    "                            width_shift_range = 0.1, \n",
    "                            height_shift_range = 0.1, \n",
    "                            horizontal_flip = False, \n",
    "                            vertical_flip = False)\n",
    "datagen.fit(X_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5dfc6f99-3d82-42a4-80f5-de3c79a494f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/10\n",
      "\u001b[1m151/151\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m19s\u001b[0m 116ms/step - accuracy: 0.4721 - loss: 1.5542 - val_accuracy: 0.9376 - val_loss: 0.2185\n",
      "Epoch 2/10\n",
      "\u001b[1m  1/151\u001b[0m \u001b[37m━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[1m12s\u001b[0m 85ms/step - accuracy: 0.8360 - loss: 0.4974"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-30 02:42:51.853767: I tensorflow/core/framework/local_rendezvous.cc:404] Local rendezvous is aborting with status: OUT_OF_RANGE: End of sequence\n",
      "\t [[{{node IteratorGetNext}}]]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m151/151\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 5ms/step - accuracy: 0.8360 - loss: 0.4974 - val_accuracy: 0.9371 - val_loss: 0.2199\n",
      "Epoch 3/10\n",
      "\u001b[1m151/151\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m23s\u001b[0m 149ms/step - accuracy: 0.8458 - loss: 0.4765 - val_accuracy: 0.9621 - val_loss: 0.1340\n",
      "Epoch 4/10\n",
      "\u001b[1m  1/151\u001b[0m \u001b[37m━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[1m12s\u001b[0m 83ms/step - accuracy: 0.8720 - loss: 0.3862"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-30 02:43:15.804417: I tensorflow/core/framework/local_rendezvous.cc:404] Local rendezvous is aborting with status: OUT_OF_RANGE: End of sequence\n",
      "\t [[{{node IteratorGetNext}}]]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m151/151\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 4ms/step - accuracy: 0.8720 - loss: 0.3862 - val_accuracy: 0.9617 - val_loss: 0.1359\n",
      "Epoch 5/10\n",
      "\u001b[1m151/151\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m20s\u001b[0m 126ms/step - accuracy: 0.8996 - loss: 0.3293 - val_accuracy: 0.9669 - val_loss: 0.1113\n",
      "Epoch 6/10\n",
      "\u001b[1m151/151\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 4ms/step - accuracy: 0.9000 - loss: 0.3403 - val_accuracy: 0.9695 - val_loss: 0.1066\n",
      "Epoch 7/10\n",
      "\u001b[1m151/151\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m16s\u001b[0m 100ms/step - accuracy: 0.9108 - loss: 0.2803 - val_accuracy: 0.9738 - val_loss: 0.0893\n",
      "Epoch 8/10\n",
      "\u001b[1m  1/151\u001b[0m \u001b[37m━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[1m8s\u001b[0m 59ms/step - accuracy: 0.9440 - loss: 0.1934"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-30 02:43:52.654657: I tensorflow/core/framework/local_rendezvous.cc:404] Local rendezvous is aborting with status: OUT_OF_RANGE: End of sequence\n",
      "\t [[{{node IteratorGetNext}}]]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m151/151\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 4ms/step - accuracy: 0.9440 - loss: 0.1934 - val_accuracy: 0.9733 - val_loss: 0.0888\n",
      "Epoch 9/10\n",
      "\u001b[1m151/151\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m21s\u001b[0m 134ms/step - accuracy: 0.9230 - loss: 0.2470 - val_accuracy: 0.9762 - val_loss: 0.0813\n",
      "Epoch 10/10\n",
      "\u001b[1m151/151\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 5ms/step - accuracy: 0.9280 - loss: 0.2552 - val_accuracy: 0.9755 - val_loss: 0.0820\n"
     ]
    }
   ],
   "source": [
    "history = model.fit(datagen.flow(X_train, y_train, \n",
    "                                 batch_size = batch_size), \n",
    "                                 epochs = epoch, \n",
    "                                 validation_data = (X_val, y_val), \n",
    "                                 steps_per_epoch = X_train.shape[0]//batch_size)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e417abd-580c-480f-86ce-6bb2cbc74207",
   "metadata": {},
   "source": [
    "When evaluating a machine learning model, especially a Convolutional Neural Network (CNN) for image classification, there are several key aspects to infer from the validation, training, and error metrics. Here's a breakdown of what to look for and how to interpret the results:\n",
    "\n",
    "### 1. **Training Loss and Accuracy**\n",
    "\n",
    "- **Training Loss**: This measures how well the model is performing on the training data. A decreasing training loss indicates that the model is learning from the training data and improving over time. If the training loss is very high, it suggests that the model is not learning effectively or that the learning rate might be too high.\n",
    "\n",
    "- **Training Accuracy**: This shows the proportion of correctly classified samples in the training set. Increasing training accuracy indicates that the model is getting better at classifying the training samples. A high training accuracy typically means that the model is learning well from the training data.\n",
    "\n",
    "### 2. **Validation Loss and Accuracy**\n",
    "\n",
    "- **Validation Loss**: This measures how well the model performs on unseen validation data. A decreasing validation loss indicates that the model is generalizing well to new, unseen data. If the validation loss starts to increase while the training loss continues to decrease, this is a sign of overfitting.\n",
    "\n",
    "- **Validation Accuracy**: This shows the proportion of correctly classified samples in the validation set. Increasing validation accuracy indicates that the model is generalizing well to unseen data. If the validation accuracy is much lower than the training accuracy, it suggests overfitting."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "8e3e67d8-a103-4172-bdbb-693b3814338c",
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
    "# Plot the training and validation accuracy and loss scores\n",
    "\n",
    "plt.plot(history.history['accuracy'])\n",
    "plt.plot(history.history['val_accuracy'])\n",
    "plt.title(\"Model Accuracy\")\n",
    "plt.xlabel(\"Epochs\")\n",
    "plt.ylabel(\"Accuracy\")\n",
    "plt.legend(['Train','Validation'], loc = 'upper left')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "67a2b022-e14c-48ec-b9a8-ddc0441f6a7b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjcAAAHFCAYAAAAOmtghAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAABVHUlEQVR4nO3deVxU5f4H8M+ZGRgYVgHZF0E0QHNFDdQUNVPLm2lXs3LJNk0t89e9Zd666c287VamZqVmq9l+yxbcFzT3UkFlUVAB2WSHgZk5vz8GRkZgBBw4s3zer9d5wTxzzpnvgDofn+c55xFEURRBREREZCNkUhdAREREZE4MN0RERGRTGG6IiIjIpjDcEBERkU1huCEiIiKbwnBDRERENoXhhoiIiGwKww0RERHZFIYbIiIisikMN0TUrA0bNkAQBAiCgJ07dzZ6XhRFREZGQhAEDB8+3KyvLQgCXnzxxVYfd/78eQiCgA0bNrRov9dff71tBRKRxWK4IaLrcnNzw0cffdSofdeuXUhPT4ebm5sEVRERNY3hhoiua8qUKfjmm29QWlpq1P7RRx8hLi4OoaGhElVGRNQYww0RXdfUqVMBAF988YWhraSkBN988w1mzZrV5DFFRUV4/PHHERQUBEdHR0RERGDx4sVQq9VG+5WWluKRRx6Bt7c3XF1dMWbMGJw9e7bJc6ampuK+++6Dr68vlEoloqOj8d5775npXTYtKysLDzzwgNFrvvHGG9DpdEb7rV69Gr1794arqyvc3NwQFRWF5557zvB8ZWUlnn76aYSHh8PJyQleXl6IjY01+pkSkXkopC6AiCyfu7s77rnnHqxbtw6PPfYYAH3QkclkmDJlClasWGG0f3V1NRISEpCeno4lS5agV69e2LNnD5YvX47jx4/j559/BqCfszNhwgQkJSXhhRdewIABA7Bv3z6MHTu2UQ3JycmIj49HaGgo3njjDfj7++O3337DE088gYKCAvz73/82+/vOz89HfHw8ampq8J///AddunTBTz/9hKeffhrp6elYtWoVAODLL7/E448/jvnz5+P111+HTCZDWloakpOTDedauHAhPvnkE7z00kvo27cvKioqcPLkSRQWFpq9biK7JxIRNWP9+vUiAPHQoUPijh07RADiyZMnRVEUxQEDBogzZ84URVEUe/ToIQ4bNsxw3Jo1a0QA4ldffWV0vldeeUUEIP7++++iKIriL7/8IgIQ3377baP9li1bJgIQ//3vfxvabr/9djE4OFgsKSkx2nfevHmik5OTWFRUJIqiKJ47d04EIK5fv97ke6vf77XXXmt2n2effVYEIP7xxx9G7XPmzBEFQRDPnDljqMHT09Pk6/Xs2VOcMGGCyX2IyDw4LEVELTJs2DB07doV69atw4kTJ3Do0KFmh6S2b98OFxcX3HPPPUbtM2fOBABs27YNALBjxw4AwP3332+033333Wf0uLq6Gtu2bcPdd98NlUoFjUZj2MaNG4fq6mocOHDAHG+z0fuIiYnBwIEDG70PURSxfft2AMDAgQNRXFyMqVOn4ocffkBBQUGjcw0cOBC//PILnn32WezcuRNVVVVmr5eI9BhuiKhFBEHAgw8+iE8//RRr1qxB9+7dMXTo0Cb3LSwshL+/PwRBMGr39fWFQqEwDMUUFhZCoVDA29vbaD9/f/9G59NoNHj33Xfh4OBgtI0bNw4AmgwUN6qwsBABAQGN2gMDAw3PA8C0adOwbt06ZGZmYtKkSfD19cWgQYOQmJhoOOadd97BM888g++//x4JCQnw8vLChAkTkJqaava6iewdww0RtdjMmTNRUFCANWvW4MEHH2x2P29vb1y+fBmiKBq15+XlQaPRwMfHx7CfRqNpNO8kNzfX6HGnTp0gl8sxc+ZMHDp0qMmtPuSYk7e3N3Jychq1Z2dnA4DhfQDAgw8+iKSkJJSUlODnn3+GKIq48847kZmZCQBwcXHBkiVLcPr0aeTm5mL16tU4cOAAxo8fb/a6iewdww0RtVhQUBD+8Y9/YPz48ZgxY0az+40cORLl5eX4/vvvjdo3btxoeB4AEhISAACfffaZ0X6ff/650WOVSoWEhAQcO3YMvXr1QmxsbKPt2t4fcxg5ciSSk5Nx9OjRRu9DEARD/Q25uLhg7NixWLx4MWpqanDq1KlG+/j5+WHmzJmYOnUqzpw5g8rKSrPXTmTPeLUUEbXKf//73+vuM336dLz33nuYMWMGzp8/j5tvvhl79+7Fyy+/jHHjxmHUqFEAgNGjR+PWW2/FP//5T1RUVCA2Nhb79u3DJ5980uicb7/9NoYMGYKhQ4dizpw56NKlC8rKypCWlob//e9/hvkvrXXixAl8/fXXjdoHDBiAp556Chs3bsQdd9yBpUuXIiwsDD///DNWrVqFOXPmoHv37gCARx55BM7Ozhg8eDACAgKQm5uL5cuXw8PDAwMGDAAADBo0CHfeeSd69eqFTp06ISUlBZ988gni4uKgUqnaVDsRNUPiCc1EZMEaXi1lyrVXS4miKBYWFoqzZ88WAwICRIVCIYaFhYmLFi0Sq6urjfYrLi4WZ82aJXp6eooqlUq87bbbxNOnTze6WkoU9Vc4zZo1SwwKChIdHBzEzp07i/Hx8eJLL71ktA9acbVUc1v98ZmZmeJ9990nent7iw4ODuJNN90kvvbaa6JWqzWc6+OPPxYTEhJEPz8/0dHRUQwMDBQnT54s/vXXX4Z9nn32WTE2Nlbs1KmTqFQqxYiICPGpp54SCwoKTNZJRK0niOI1g+JEREREVoxzboiIiMimMNwQERGRTWG4ISIiIpvCcENEREQ2heGGiIiIbArDDREREdkUu7uJn06nQ3Z2Ntzc3Bqte0NERESWSRRFlJWVITAwEDKZ6b4Zuws32dnZCAkJkboMIiIiaoMLFy4gODjY5D52F27c3NwA6H847u7uEldDRERELVFaWoqQkBDD57gpdhdu6oei3N3dGW6IiIisTEumlHBCMREREdkUhhsiIiKyKQw3REREZFPsbs5NS2m1WtTW1kpdBpmBg4MD5HK51GUQEVEHYbi5hiiKyM3NRXFxsdSlkBl5enrC39+f9zYiIrIDDDfXqA82vr6+UKlU/DC0cqIoorKyEnl5eQCAgIAAiSsiIqL2xnDTgFarNQQbb29vqcshM3F2dgYA5OXlwdfXl0NUREQ2jhOKG6ifY6NSqSSuhMyt/nfKeVRERLaP4aYJHIqyPfydEhHZD4YbIiIisikMN9Ss4cOHY8GCBVKXQURE1CqcUGwDrjfkMmPGDGzYsKHV5/3222/h4ODQxqqIiIikwXBjRlqdDjUaHZwdO/bHmpOTY/h+06ZNeOGFF3DmzBlDW/3VQvVqa2tbFFq8vLzMVyQREVEH4bCUmVTVaJCcXYZzBZUQRbFDX9vf39+weXh4QBAEw+Pq6mp4enriq6++wvDhw+Hk5IRPP/0UhYWFmDp1KoKDg6FSqXDzzTfjiy++MDrvtcNSXbp0wcsvv4xZs2bBzc0NoaGhWLt2bYe+VyIiouthuLkOURRRWaO57qYVRag1WpSra3GlsqZFx1xvM2dIeuaZZ/DEE08gJSUFt99+O6qrq9G/f3/89NNPOHnyJB599FFMmzYNf/zxh8nzvPHGG4iNjcWxY8fw+OOPY86cOTh9+rTZ6iQiIrpRHJa6jqpaLWJe+E2S105eejtUZhriWrBgASZOnGjU9vTTTxu+nz9/Pn799Vds3rwZgwYNavY848aNw+OPPw5AH5jeeust7Ny5E1FRUWapk4iI6EYx3NiJ2NhYo8darRb//e9/sWnTJly6dAlqtRpqtRouLi4mz9OrVy/D9/XDX/VLGxAREVkChpvrcHaQI3np7S3at7JGg4z8CsgFAVEBbjd84zhnB/MtE3BtaHnjjTfw1ltvYcWKFbj55pvh4uKCBQsWoKamxuR5rp2ILAgCdDqd2eokIiK6UQw31yEIQouHhpwd5LhcqoZWJ7bqOCns2bMHd911Fx544AEAgE6nQ2pqKqKjoyWujIiI6MZwQrEZCYIAl7pAU67WSFyNaZGRkUhMTERSUhJSUlLw2GOPITc3V+qyiIiIbhjDjZm5OtWFm2rLDjfPP/88+vXrh9tvvx3Dhw+Hv78/JkyYIHVZREREN0wQO/qmLBIrLS2Fh4cHSkpK4O7ubvRcdXU1zp07h/DwcDg5ObXp/NW1Wpy9XAaZICAm0B0yLthoEczxuyUiIumY+vy+FntuzEypkEEhk0Eniqis0UpdDhERkd1huDEzQRDgqtQPTVVY+LwbIiIiW8Rw0w5cnfSXcFv6vBsiIiJbxHDTDlzqem4qa7TQ6uxqShMREZHkGG7agaNcBke5DCL061IRERFRx2G4aQeCIBh6byz9fjdERES2huGmnVjL/W6IiIhsDcNNO6m/YqqqVguNlmsvERERdRSGm3biIJdBqdBfNVXB+90QERF1GEnDze7duzF+/HgEBgZCEAR8//331z1m165d6N+/P5ycnBAREYE1a9a0f6FtZE33uxk+fDgWLFhgeNylSxesWLHC5DEt/Z1dj7nOQ0REBEgcbioqKtC7d2+sXLmyRfufO3cO48aNw9ChQ3Hs2DE899xzeOKJJ/DNN9+0c6Vt01H3uxk/fjxGjRrV5HP79++HIAg4evRoq8556NAhPProo+Yoz+DFF19Enz59GrXn5ORg7NixZn0tIiKyXwopX3zs2LGt+lBbs2YNQkNDDT0K0dHROHz4MF5//XVMmjSpnapsu/oVwqs1WtRqdXCQt0+WfOihhzBx4kRkZmYiLCzM6Ll169ahT58+6NevX6vO2blzZ3OWaJK/v3+HvRYREdk+q5pzs3//fowePdqo7fbbb8fhw4dRW1srUVXNU8hlcHaom3fTjkNTd955J3x9fbFhwwaj9srKSmzatAkTJkzA1KlTERwcDJVKhZtvvhlffPGFyXNeOyyVmpqKW2+9FU5OToiJiUFiYmKjY5555hl0794dKpUKEREReP755w2/lw0bNmDJkiX4888/IQgCBEEw1HvtsNSJEycwYsQIODs7w9vbG48++ijKy8sNz8+cORMTJkzA66+/joCAAHh7e2Pu3LkW+WeAiIg6nqQ9N62Vm5sLPz8/ozY/Pz9oNBoUFBQgICCg0TFqtRpqtdrwuLS0tHUvKopAbWWb6gUAN5ka1bU1qCjXwFPh3LqDHVRAC1YVVygUmD59OjZs2IAXXngBQt0xmzdvRk1NDR5++GF88cUXeOaZZ+Du7o6ff/4Z06ZNQ0REBAYNGnTd8+t0OkycOBE+Pj44cOAASktLjebnGN6rmxs2bNiAwMBAnDhxAo888gjc3Nzwz3/+E1OmTMHJkyfx66+/YuvWrQAADw+PRueorKzEmDFjcMstt+DQoUPIy8vDww8/jHnz5hmFtx07diAgIAA7duxAWloapkyZgj59+uCRRx657vshIiLbZlXhBoDhg7ueKIpNttdbvnw5lixZ0vYXrK0EXg5s8+H+dVubPJcNOLq0aNdZs2bhtddew86dO5GQkABAPyQ1ceJEBAUF4emnnzbsO3/+fPz666/YvHlzi8LN1q1bkZKSgvPnzyM4OBgA8PLLLzcaUvzXv/5l+L5Lly74v//7P2zatAn//Oc/4ezsDFdXVygUCpPDUJ999hmqqqqwceNGuLjo3/vKlSsxfvx4vPLKK4Zw26lTJ6xcuRJyuRxRUVG44447sG3bNoYbIiKyrmEpf39/5ObmGrXl5eVBoVDA29u7yWMWLVqEkpISw3bhwoWOKLXDRUVFIT4+HuvWrQMApKenY8+ePZg1axa0Wi2WLVuGXr16wdvbG66urvj999+RlZXVonOnpKQgNDTUEGwAIC4urtF+X3/9NYYMGQJ/f3+4urri+eefb/FrNHyt3r17G4INAAwePBg6nQ5nzpwxtPXo0QNyudzwOCAgAHl5ea16LSIisk1W1XMTFxeH//3vf0Ztv//+O2JjY+Hg4NDkMUqlEkqlsu0v6qDS96DcgPT8ClTWaBDk6QwvF8fWvXYrPPTQQ5g3bx7ee+89rF+/HmFhYRg5ciRee+01vPXWW1ixYgVuvvlmuLi4YMGCBaipqWnReet7xxq6tqfswIEDuPfee7FkyRLcfvvt8PDwwJdffok33nijVe9BFMVme+Eatl/7+xYEATodb5ZIREQSh5vy8nKkpaUZHp87dw7Hjx+Hl5cXQkNDsWjRIly6dAkbN24EAMyePRsrV67EwoUL8cgjj2D//v346KOPrjs59oYIQouHhprj4ipHRVk1ykVHeDm2LrC0xuTJk/Hkk0/i888/x8cff4xHHnkEgiBgz549uOuuu/DAAw8A0M+hSU1NRXR0dIvOGxMTg6ysLGRnZyMwUD9Et3//fqN99u3bh7CwMCxevNjQlpmZabSPo6MjtFrTNzSMiYnBxx9/jIqKCkPvzb59+yCTydC9e/cW1UtERPZN0mGpw4cPo2/fvujbty8AYOHChejbty9eeOEFAPr7nzQc1ggPD8eWLVuwc+dO9OnTB//5z3/wzjvvWORl4A25Kuvud6PWNNkLYrbXcXXFlClT8NxzzyE7OxszZ84EAERGRiIxMRFJSUlISUnBY4891mh4z5RRo0bhpptuwvTp0/Hnn39iz549RiGm/jWysrLw5ZdfIj09He+88w6+++47o326dOliCLAFBQVGE73r3X///XBycsKMGTNw8uRJ7NixA/Pnz8e0adMaTSYnIiJqiqThZvjw4RBFsdFWf1XMhg0bsHPnTqNjhg0bhqNHj0KtVuPcuXOYPXt2xxfeSipHBWSCAI1WB7WmfYdOHnroIVy5cgWjRo1CaGgoAOD5559Hv379cPvtt2P48OHw9/fHhAkTWnxOmUyG7777Dmq1GgMHDsTDDz+MZcuWGe1z11134amnnsK8efPQp08fJCUl4fnnnzfaZ9KkSRgzZgwSEhLQuXPnJnvcVCoVfvvtNxQVFWHAgAG45557MHLkyBbf6JGIiEgQ27MrwQKVlpbCw8MDJSUlcHd3N3quuroa586dQ3h4OJycnMz6uhn55ShXaxDo6Qwf1xuYA0Rt0p6/WyIian+mPr+vZVVXS1kza1pnioiIyJox3HQQl7pw097zboiIiOwdw00HUTnKIRcEaHUiqmtNXzFEREREbcdw00EEQTDqvSEiIqL2wXDThPYaNroabthz09E4FEhEZD8Ybhqov+ttZWXbF8o0peGkYh0/bDtU/e+0uTtZExGR7bCq5Rfam1wuh6enp2GNIpVK1exSAG0iipDpNNDqdCguq4DKkT/+9iaKIiorK5GXlwdPT0+j9aiIiMg28dP1GvUrVrfXIowlFTWorNGi+ooC7k7sRegonp6eJlcjJyIi28Fwcw1BEBAQEABfX1/U1taa/fwnjl/C2ztS0TvYA29O6Wv281NjDg4O7LEhIrIjDDfNkMvl7fKBGNvVD5e+P438s8UQZQ5wduSHLhERkTlxQnEHC/dxQYCHE2q0OhzJvCJ1OURERDaH4aaDCYKAuK7eAICk9AKJqyEiIrI9DDcSiO/qAwBISi+UuBIiIiLbw3Ajgfi6npu/LhajtNr8k5aJiIjsGcONBAI9nRHu4wKdCBzMKJK6HCIiIpvCcCORq/NuODRFRERkTgw3EonnpGIiIqJ2wXAjkbgIfbg5nVuGgnK1xNUQERHZDoYbiXi7KhHl7wYAOJDBoSkiIiJzYbiREC8JJyIiMj+GGwnVz7vZz3BDRERkNgw3EhoY4QWZAJwrqEB2cZXU5RAREdkEhhsJuTs5oFewJwAOTREREZkLw43EeEk4ERGReTHcSKx+UvH+9EKIoihxNURERNaP4UZi/cM6wVEuQ05JNc4VVEhdDhERkdVjuJGYs6Mc/cI8AXDeDRERkTkw3FiAhkNTREREdGMYbiyA4X43GYXQ6TjvhoiI6EYw3FiAXsGeUDnKUVRRg9O5ZVKXQ0REZNUYbiyAo0KGgeFeAHhJOBER0Y1iuLEQXIqBiIjIPBhuLET9pOI/zhVBo9VJXA0REZH1YrixENEB7vBwdkC5WoO/LpVIXQ4REZHVYrixEHKZgLgIDk0RERHdKIYbCxIfyXWmiIiIbhTDjQWpn1R8+PwVVNdqJa6GiIjIOjHcWJCunV3h66aEWqPD0awrUpdDRERklRhuLIggCLwknIiI6AYx3FiY+kvCuYgmERFR2zDcWJi4up6bPy8Uo1ytkbgaIiIi68NwY2FCvFQI8XKGRifi0LkiqcshIiKyOgw3FmiwYWiKl4QTERG1FsONBaofmuK8GyIiotZjuLFA9eEmOacUVypqJK6GiIjIujDcWCBfNyd083WFKAIHMth7Q0RE1BoMNxZqcCQvCSciImoLhhsLdXXeDScVExERtQbDjYW6JdwbggCk51fgcmm11OUQERFZDYYbC+WhckDPQA8A7L0hIiJqDYYbC1a/zlRSGufdEBERtRTDjQWLbzCpWBRFiashIiKyDgw3FmxAl05QyARcKq7ChaIqqcshIiKyCgw3FkzlqEDfUE8AnHdDRETUUgw3Fi6ubp2pfbzfDRERUYsw3Fi4wXWTivenF3DeDRERUQsw3Fi4PqGecHKQoaC8Bql55VKXQ0REZPEkDzerVq1CeHg4nJyc0L9/f+zZs8fk/p999hl69+4NlUqFgIAAPPjggygstN0hG6VCjgFdvAAASWmcd0NERHQ9koabTZs2YcGCBVi8eDGOHTuGoUOHYuzYscjKympy/71792L69Ol46KGHcOrUKWzevBmHDh3Cww8/3MGVd6z6pRg474aIiOj6JA03b775Jh566CE8/PDDiI6OxooVKxASEoLVq1c3uf+BAwfQpUsXPPHEEwgPD8eQIUPw2GOP4fDhwx1ceccaXDep+EBGIbQ6zrshIiIyRbJwU1NTgyNHjmD06NFG7aNHj0ZSUlKTx8THx+PixYvYsmULRFHE5cuX8fXXX+OOO+5o9nXUajVKS0uNNmvTI9Adbk4KlFVrcCq7ROpyiIiILJpk4aagoABarRZ+fn5G7X5+fsjNzW3ymPj4eHz22WeYMmUKHB0d4e/vD09PT7z77rvNvs7y5cvh4eFh2EJCQsz6PjqCQi7DoPD6VcI5NEVERGSK5BOKBUEweiyKYqO2esnJyXjiiSfwwgsv4MiRI/j1119x7tw5zJ49u9nzL1q0CCUlJYbtwoULZq2/o9SvM7WPk4qJiIhMUkj1wj4+PpDL5Y16afLy8hr15tRbvnw5Bg8ejH/84x8AgF69esHFxQVDhw7FSy+9hICAgEbHKJVKKJVK87+BDja4bp2pQ+eLUKPRwVEheS4lIiKySJJ9Qjo6OqJ///5ITEw0ak9MTER8fHyTx1RWVkImMy5ZLpcDgM3f4K67nyu8XRxRXavD8QvFUpdDRERksST97//ChQvx4YcfYt26dUhJScFTTz2FrKwswzDTokWLMH36dMP+48ePx7fffovVq1cjIyMD+/btwxNPPIGBAwciMDBQqrfRIQRBMFwSznWmiIiImifZsBQATJkyBYWFhVi6dClycnLQs2dPbNmyBWFhYQCAnJwco3vezJw5E2VlZVi5ciX+7//+D56enhgxYgReeeUVqd5Ch4rv6oOf/spBUlohFoySuhoiIiLLJIi2Pp5zjdLSUnh4eKCkpATu7u5Sl9MqmYUVGPbaTjjIBfz579FQOUqaTYmIiDpMaz6/OSvVioR6qRDk6YxarYjD569IXQ4REZFFYrixIsbzbni/GyIioqYw3FiZeE4qJiIiMonhxsrE160zdfJSCUoqayWuhoiIyPIw3FgZfw8nRHR2gU4E/jjHoSkiIqJrMdxYoXjOuyEiImoWw40Vqh+a4rwbIiKixhhurFBchL7n5uzlcuSXqSWuhoiIyLIw3FihTi6OiAnQ38BofwaHpoiIiBpiuLFS9fNu9nNoioiIyAjDjZWKj9SHm31p7LkhIiJqiOHGSg0M94ZcJiCrqBIXiiqlLoeIiMhiMNxYKVelAr2DPQBw3g0REVFDDDdWrP6S8P283w0REZEBw40Vq59UvC+tAKIoSlwNERGRZWC4sWL9wjrBUSFDXpka6fkVUpdDRERkERhurJiTgxyxYZ0A8JJwIiKiegw3Vo7rTBERERljuLFycfWTijMKodNx3g0RERHDjZXrHewBV6UCxZW1SM4plbocIiIiyTHcWDmFXIaB4V4AeEk4ERERwHBjE67Ou+GkYiIiIoYbGxBXF24OnitCrVYncTVERETSYrixAdH+7uikckBFjRZ/XSyWuhwiIiJJMdzYAJlMMPTeJHGVcCIisnMMNzai/pJw3u+GiIjsHcONjaifVHwk6wqqa7USV0NERCQdhhsbEeHjAn93J9RodDiSeUXqcoiIiCTDcGMjBEHgJeFERERguLEpcVxnioiIiOHGlsRH6icV/3WxBGXVtRJXQ0REJA2GGxsS5OmMLt4qaHUiDp4rkrocIiIiSTDc2BheEk5ERPaO4cbGxHPeDRER2TmGGxtTP6k4JacUheVqiashIiLqeAw3NsbHVYkofzcAwIEMzrshIiL7w3Bjg+J4vxsiIrJjDDc2KL5uUvF+zrshIiI7xHBjgwaGe0EmABkFFcgpqZK6HCIiog7FcGODPJwdcHOQBwAgKY29N0REZF8YbmxU/d2KeUk4ERHZG4YbG1V/v5v96QUQRVHiaoiIiDoOw42Nig3zgoNcQHZJNc4XVkpdDhERUYdhuLFRzo5y9A3tBICXhBMRkX1huLFhg7nOFBER2SGGGxsWH6mfd3MgvRA6HefdEBGRfWC4sWG9gz3h7CBHYUUNzlwuk7ocIiKiDsFwY8McFTIMCPcCwKEpIiKyHww3Nm5wg0vCiYiI7AHDjY2rX2fqj4wiaLQ6iashIiJqfww3Ni4m0B3uTgqUqTU4calE6nKIiIjaHcONjZPLBNwSoR+a4rwbIiKyBww3dmBw3TpT+xluiIjIDjDc2IH6daYOnS+CWqOVuBoiIqL2xXBjByJ9XeHjqoRao8PRzGKpyyEiImpXDDd2QBAEo1XCiYiIbBnDjZ0YHMlJxUREZB8kDzerVq1CeHg4nJyc0L9/f+zZs8fk/mq1GosXL0ZYWBiUSiW6du2KdevWdVC11qv+fjfHLxSjQq2RuBoiIqL2o5DyxTdt2oQFCxZg1apVGDx4MN5//32MHTsWycnJCA0NbfKYyZMn4/Lly/joo48QGRmJvLw8aDT8sL6eEC8Vgjs54+KVKhw8X4SEm3ylLomIiKhdCKIotnq56AsXLkAQBAQHBwMADh48iM8//xwxMTF49NFHW3yeQYMGoV+/fli9erWhLTo6GhMmTMDy5csb7f/rr7/i3nvvRUZGBry8vFpbNgCgtLQUHh4eKCkpgbu7e5vOYa3++fWf+OrwRTx6awSeGxctdTlEREQt1prP7zYNS913333YsWMHACA3Nxe33XYbDh48iOeeew5Lly5t0Tlqampw5MgRjB492qh99OjRSEpKavKYH3/8EbGxsXj11VcRFBSE7t274+mnn0ZVVVWzr6NWq1FaWmq02av6+90kcVIxERHZsDaFm5MnT2LgwIEAgK+++go9e/ZEUlISPv/8c2zYsKFF5ygoKIBWq4Wfn59Ru5+fH3Jzc5s8JiMjA3v37sXJkyfx3XffYcWKFfj6668xd+7cZl9n+fLl8PDwMGwhISEte5M2KK7uTsWnsktRXFkjcTVERETto03hpra2FkqlEgCwdetW/O1vfwMAREVFIScnp1XnEgTB6LEoio3a6ul0OgiCgM8++wwDBw7EuHHj8Oabb2LDhg3N9t4sWrQIJSUlhu3ChQutqs+W+Lo7IdLXFaIIHMjgVVNERGSb2hRuevTogTVr1mDPnj1ITEzEmDFjAADZ2dnw9vZu0Tl8fHwgl8sb9dLk5eU16s2pFxAQgKCgIHh4eBjaoqOjIYoiLl682OQxSqUS7u7uRps9q7/fDS8JJyIiW9WmcPPKK6/g/fffx/DhwzF16lT07t0bgH5OTP1w1fU4Ojqif//+SExMNGpPTExEfHx8k8cMHjwY2dnZKC8vN7SdPXsWMpnMMLmZTKu/JJzhhoiIbFWbrpYCAK1Wi9LSUnTq1MnQdv78eahUKvj6tuwy402bNmHatGlYs2YN4uLisHbtWnzwwQc4deoUwsLCsGjRIly6dAkbN24EAJSXlyM6Ohq33HILlixZgoKCAjz88MMYNmwYPvjggxa9pj1fLQUAxZU16PufRIgicPC5kfB1d5K6JCIioutq96ulqqqqoFarDcEmMzMTK1aswJkzZ1ocbABgypQpWLFiBZYuXYo+ffpg9+7d2LJlC8LCwgAAOTk5yMrKMuzv6uqKxMREFBcXIzY2Fvfffz/Gjx+Pd955py1vwy55qhzRI1D/h4K9N0REZIva1HMzevRoTJw4EbNnz0ZxcTGioqLg4OCAgoICvPnmm5gzZ0571GoW9t5zAwAvb0nB2t0ZmBwbjFfv6S11OURERNfV7j03R48exdChQwEAX3/9Nfz8/JCZmYmNGzeyF8UKcFIxERHZsjaFm8rKSri5uQEAfv/9d0ycOBEymQy33HILMjMzzVogmd+ALl5QyARcvFKFC0WVUpdDRERkVm0KN5GRkfj+++9x4cIF/Pbbb4a7DOfl5dntUI81cVEq0CfEEwCwL413KyYiItvSpnDzwgsv4Omnn0aXLl0wcOBAxMXFAdD34vTt29esBVL74NAUERHZqjaFm3vuuQdZWVk4fPgwfvvtN0P7yJEj8dZbb5mtOGo/8ZFX73fTxrsBEBERWSRFWw/09/eHv78/Ll68CEEQEBQU1OIb+JH0+oZ6QqmQoaBcjbS8cnTzc5O6JCIiIrNoU8+NTqfD0qVL4eHhgbCwMISGhsLT0xP/+c9/oNPpzF0jtQOlQo4BXbwAcN4NERHZljaFm8WLF2PlypX473//i2PHjuHo0aN4+eWX8e677+L55583d43UTuI474aIiGxQm4alPv74Y3z44YeG1cABoHfv3ggKCsLjjz+OZcuWma1Aaj+DI33w2m9ncCCjEFqdCLms6dXYiYiIrEmbem6KiooQFRXVqD0qKgpFRUU3XBR1jJ6B7nBTKlBarUFydqnU5RAREZlFm8JN7969sXLlykbtK1euRK9evW64KOoYCrkMgyLq5t2kc94NERHZhjYNS7366qu44447sHXrVsTFxUEQBCQlJeHChQvYsmWLuWukdhTX1QdbU/KQlF6I2cO6Sl0OERHRDWtTz82wYcNw9uxZ3H333SguLkZRUREmTpyIU6dOYf369eaukdrR4Ej9pOJD54pQo+GVbkREZP3atCp4c/7880/069cPWq3WXKc0O64KbkynEzFg2VYUVtRg8+w4w+XhRERElqTdVwUn2yGTCbil7pJw3u+GiIhsAcMNcZ0pIiKyKQw3hMFd9etMHcu6gqoayx1SJCIiaolWXS01ceJEk88XFxffSC0kkTBvFQI9nJBdUo3DmUUY2q2z1CURERG1WavCjYeHx3Wfnz59+g0VRB1PEATEdfXBN0cvYl9aIcMNERFZtVaFG17mbbviu3rjm6MXsZ838yMiIivHOTcEAIivu9/NiUslKKmqlbgaIiKitmO4IQBAgIczInxcoBOBg+e4PhgREVkvhhsyiOP9boiIyAYw3JBBfN0l4ft5vxsiIrJiDDdkUN9zc+ZyGfLL1BJXQ0RE1DYMN2Tg5eKI6AD9eh0HMth7Q0RE1onhhoxcXYqB826IiMg6MdyQkfpwszetANW1XIqBiIisD8MNGRkY7gVHuQwXiqow9NUd+GB3BirUGqnLIiIiajGGGzLi5uSAd+/riyBPZ+SXqbFsSwqGvLId725L5c39iIjIKgiiKIpSF9GRSktL4eHhgZKSEri7u0tdjsWq0ejw/fFLWLUjDecLKwEAbkoFpseHYdbgcHi7KiWukIiI7ElrPr8ZbsgkrU7ET39l470daTh7uRwA4Owgx/2DQvHorRHwdXeSuEIiIrIHDDcmMNy0jU4nIjHlMlZuT8OJSyUAAEeFDFNiQ/DYsAgEd1JJXCEREdkyhhsTGG5ujCiK2HU2Hyu3p+Fw5hUAgEIm4O6+QZgzvCsiOrtKXCEREdkihhsTGG7MQxRF/HGuCCu3p2Fv3VpUMgG4o1cg5iZ0RZQ/f7ZERGQ+DDcmMNyY37GsK3hvRxq2puQZ2m6L8cO8hEj0DvGUrjAiIrIZDDcmMNy0n1PZJVi1Ix1bTuag/k/Vrd07Y15CJAaGe0lbHBERWTWGGxMYbtpfWl45Vu1Mww/Hs6HV6f94DQz3wvwRkRgS6QNBECSukIiIrA3DjQkMNx0nq7ASa3an4+vDF1Gj1QEAeod4Yn5CJEZG+zLkEBFRizHcmMBw0/FySqqwdncGvjiYhepafciJ8nfDvBGRGNszAHIZQw4REZnGcGMCw410CsrV+GjvOWxMOo+KGv2inBGdXfD48Ejc1ScQDnKuBkJERE1juDGB4UZ6xZU12JB0Huv3nTesVxXcyRmzh3XF32ODoVTIJa6QiIgsDcONCQw3lqNcrcGnBzLx4Z4MFJTXAAD83JV49NauuG9gKJwdGXKIiEiP4cYEhhvLU1WjxZeHsvD+rgzkllYDALxdHPHQ0HBMuyUMbk4OEldIRERSY7gxgeHGcqk1Wnx79BJW7UzDhaIqAIC7kwIzB4fjwfgu6OTiKHGFREQkFYYbExhuLJ9Gq8P//srGyu1pSM+vAACoHOWYdksYHhoaDl83rkRORGRvGG5MYLixHjqdiF9P5eLd7WlIySkFACgVMtw7IASPDeuKQE9niSskIqKOwnBjAsON9RFFEdtP5+Hd7Wk4fqEYAOAgFzCpXzDmDO+KMG8XaQskIqJ2x3BjAsON9RJFEUnphVi5PQ37MwoB6Fci/1vvQMxNiEQ3PzeJKyQiovbCcGMCw41tOHy+CCt3pGHnmXwAgCAAY3r4Y25CJHoGeUhcHRERmRvDjQkMN7blxMUSrNyRit9OXTa0JdzUGfNGdEP/sE4SVkZERObEcGMCw41tOpNbhlU70/C/P7NRtxA54iK88diwCMR39YGjgks7EBFZM4YbExhubNv5ggqs3pmOb45ehKYu5agc5YiL8MbQbj64tXtnhPu4cEVyIiIrw3BjAsONfbhUXIW1u9Lx84kcw9IO9YI7OePW7p1xa7fOiI/0hjvvgExEZPEYbkxguLEvOp2IlNxS7D5bgN1n83E4swi12qt/5OUyAX1DPPVhp3tn3BzkAbmMvTpERJaG4cYEhhv7VqHW4EBGIfak6sNORkGF0fOeKgcMifTBrd30Ycffg3dDJiKyBAw3JjDcUEMXiiqxOzUfu8/mIymtEGVqjdHz3f1cDUFnYLgXnBy4UjkRkRQYbkxguKHm1Gp1+PNCMXafzceu1AL8dbEYDf92KBUyDAz3wrC6Iaxuvq6cmExE1EGsKtysWrUKr732GnJyctCjRw+sWLECQ4cOve5x+/btw7Bhw9CzZ08cP368xa/HcEMtdaWiBnvTCrAnNR+7zxYgt7Ta6PkADyfDFViDu/pw1XIionZkNeFm06ZNmDZtGlatWoXBgwfj/fffx4cffojk5GSEhoY2e1xJSQn69euHyMhIXL58meGG2p0oikjNK9f36pzNx8FzRVBrdIbnBQHoFeyJYXVhp0+IJxRy3luHiMhcrCbcDBo0CP369cPq1asNbdHR0ZgwYQKWL1/e7HH33nsvunXrBrlcju+//57hhjpcda0WB88VYffZfOxOzcfZy+VGz7s5KTC4qw+GdtdPTg7xUklUKRGRbWjN57eig2pqpKamBkeOHMGzzz5r1D569GgkJSU1e9z69euRnp6OTz/9FC+99NJ1X0etVkOtVhsel5aWtr1oojpODnLD5eMAkFNShT1nC7A7NR970wpQXFmLX0/l4tdTuQCACB+Xuv19MCjcGy5Kyf7qERHZPMn+hS0oKIBWq4Wfn59Ru5+fH3Jzc5s8JjU1Fc8++yz27NkDhaJlpS9fvhxLliy54XqJTAnwcMbkASGYPCAEWp2IE5dK9L06Z/Nx7EIxMgoqkFFQgQ1J5+EgFxAb5mUIOzEB7pyYTERkRpL/9/Haf9RFUWzyH3qtVov77rsPS5YsQffu3Vt8/kWLFmHhwoWGx6WlpQgJCWl7wUTXIZcJ6BPiiT4hnnhiZDeUVtciKa3QcMn5xStV2J9RiP0ZhXjlV8DHVYlb6+bqDOnmAx9XpdRvgYjIqkkWbnx8fCCXyxv10uTl5TXqzQGAsrIyHD58GMeOHcO8efMAADqdDqIoQqFQ4Pfff8eIESMaHadUKqFU8sOCpOPu5IAxPf0xpqc/RFHEuYIK7D6bjz2pBdifUYiCcjW+PXYJ3x67BADoEehuWB6if1gnLvpJRNRKkk8o7t+/P1atWmVoi4mJwV133dVoQrFOp0NycrJR26pVq7B9+3Z8/fXXCA8Ph4uLy3VfkxOKyZKoNVocybxiWB4iOcd4Tlj9op8JUb6Y2C8IKkfJO1uJiCRhFROKAWDhwoWYNm0aYmNjERcXh7Vr1yIrKwuzZ88GoB9SunTpEjZu3AiZTIaePXsaHe/r6wsnJ6dG7UTWQqmQI76rD+K7+uDZsVHIL1Njb5r+vjp7UvNRUF6DbafzsO10HlZsPYvHbu2KB24Jg7Mj75RMRNQcScPNlClTUFhYiKVLlyInJwc9e/bEli1bEBYWBgDIyclBVlaWlCUSdajObkrc3TcYd/cNhk4nIjmnFLtT8/HFwSxcKKrCsi0peH93OmYP64r7BzHkEBE1RfI7FHc0DkuRNarV6vDt0Yt4d3saLl6pAqCfiDx7WAQeuCWMa14Rkc2zmpv4SYHhhqxZrVaHb47oQ86lYn3I6eymrOvJCWXIISKbxXBjAsMN2YIazdWenIYhZ86wrriPIYeIbBDDjQkMN2RLajQ6fHP0IlY2CDm+bkrMGd4VUwcy5BCR7WC4MYHhhmxRjUaHr49cxHs7jEPO48O74l6GHCKyAQw3JjDckC2r0eiw+cgFvLc9Ddkl1QAAP3clHh8eiSkDQhhyiMhqMdyYwHBD9kCt0WLz4YtYteNqyPF3d8LjCV0xOZYhh4isD8ONCQw3ZE/UGi2+qgs5OdeEnCkDQqBUMOQQkXVguDGB4YbskVqjxVeHLuC9HenILdWHnAAPJzw+vCsmM+QQkRVguDGB4YbsWbMhJyESk2ODGXKIyGIx3JjAcEMEVNdq8dXhC3hvRxoul6oBAIGGkBPClciJyOIw3JjAcEN0VXWtFpsOXcCqnVdDTpCnMx5P6Iq/92fIISLLwXBjAsMNUWPVtVp8eTALq3amI6/sasiZmxCJe/oHM+QQkeQYbkxguCFqXnWtFl8czMLqa0LOvBGRmNTPfkNOhVqD07llSM4uQXJOKfLL1LizVyDG9w6EXCZIXR6RXWC4MYHhhuj6qmu1+PyPLKzelY78upAT3MkZ8xIiMal/MBzkthty8sqqkZxdiuScUpzKLkVKdinOFVagqX8pu/m6YsGo7hjb0x8yhhyidsVwYwLDDVHLVddq8dkf+p6cgvKrIWf+iEhM7GfdIUenE3G+sAKn6oJMcrY+zNS/z2v5uinRI9AdMYHukAsCPt6fiZKqWgBAlL8bnrqtO0bH+EEQGHKI2gPDjQkMN0StV1WjxecHjUNOiJcz5id0w939giw+5FTXanEmt6yuN6YEydmlOJ1bhsoabaN9BQGI8HFBTKCHPswEuCM6wB2d3ZRG+5VW12Ld3nP4aM85lKk1AICbgzyw8LbuGH5TZ4YcIjNjuDGB4Yao7apqtPjsj0ys2ZVhsSGnqKKmblipxNAbk55fDl0T/9I5OcgQ5a/vjYkJcEePQHfc5O8GlaOixa9XXFmDD/ecw/p951BRF5b6hnpi4W3dMSTShyGHyEwYbkxguCG6cVdDTjoKymsAAKFeKswbEYmJfYOg6ICQI4oiLhRVITmnRD+0VDe8VL/MxLW8XBwNPTExgfog08XbxWy1FlXU4P1d6fh4/3lU1+oAAAO7eGHh6O64JcLbLK9BZM8YbkxguCEyn8oaDT47kIU1u9JRWKEPOWHeKsxLiMTdZgw5NRodzl4uM8yNSc7RT/StHw66VhdvlaE3Rh9kPODrpuyQXpS8smqs2ZmBT//IRI1GH3Liu3rj/0Z3R/8wr3Z/fSJbxXBjAsMNkflV1mjw6YFMvL8rwyjkzB/RDRP6BLYq5JRU1SKl7kql+iCTlleGWm3jf6oc5TJ093etG1LyQEygO6L83eDm5GC299ZWuSXVeG9HGr48lGWofVj3znjqtu7oE+IpbXFEVojhxgSGG6L2U1mjwSf7M/H+7gwU1YWcLnUh565rQo4oisguqbvsum6OzKnsUly8UtXkud2dFIYAExPgjh5B7uja2dUi5vmYcqm4Ciu3p2Lz4YvQ1E38GRXti6du644egR4SV0dkPRhuTGC4IWp/FWoNPjmQibUNQk64jwvuGxiKy6XV+uGlnFIUV9Y2eXyQp7NhXkz90FKQp7NVT87NKqzE29tS8d2xi4bJzWN6+OOp27rjJn83aYsjsgIMNyYw3BB1nKZCTkMKmYBIX1fj+TEBHvBQST+s1F4y8svx9rZU/PhnNkRRf+n5nb0C8eTIboj0dZW6PCKLxXBjAsMNUcerUGuwcX8mDmQUoou3yjC8FOnrCicHudTlSeLs5TKs2HoWW07kAgBkAjChTxCeGNkNXXxcJK6OyPIw3JjAcENEliQ5uxRvbT2LxOTLAAC5TMA9/YIxb0QkQrxUEldHZDkYbkxguCEiS3TiYgneTDyDHWfyAQAOcgGTY0Mwb0QkAjycJa6OSHoMNyYw3BCRJTuSeQVvJZ7F3rQCAPrL3e8bFIrHh3eFr7uTxNURSYfhxgSGGyKyBn9kFOLNxLP441wRAP1SEdNuCcPsYV3h7aq8ztFEtofhxgSGGyKyFqIoIim9EG/8fgZHs4oBACpHOWbEd8GjQyPQycVR2gKJOhDDjQkMN0RkbURRxK6z+Xgz8Sz+ulgCAHBVKjBrSDgeGhIOD2fbvXSeqB7DjQkMN0RkrURRxNaUPLyZeBYpOaUA9HdufmRoBB4cEg5XZctXMyeyNgw3JjDcEJG10+lE/HYqF29tPYuzl8sBAJ1UDnhsWFdMjwuDypEhh2wPw40JDDdEZCu0OhE//ZWNt7emIqOgAgDg4+qI2cO64oFbwuz2BolkmxhuTGC4ISJbo9Hq8MPxbLy9LRVZRZUAAF83JeYmROLegSFQKhhyyPox3JjAcENEtqpWq8M3Ry7i3e1puFSsX1090MMJ80Z0wz39g+GosOwV1IlMYbgxgeGGiGxdjUaHTYcv4L3tacgtrQYABHdyxhMju2Fi3yAo5Aw5ZH0YbkxguCEie1Fdq8UXB7Pw3o50FJSrAQDhPi54cmQ3jO8dCLlMkLhCopZjuDGB4YaI7E1VjRafHDiPNbsyUFRRAwCI9HXFglHdMK5nAGQMOWQFGG5MYLghIntVodZgQ9J5rN2dgZKqWgBAdz9XzB/RDeNuDmBPDlk0hhsTGG6IyN6VVtdi/d7z+HBvBsqqNQD0PTnzR0Tizl4criLLxHBjAsMNEZFeSVUtPk46j4/2njP05ET4uGBuQiTu6hPIicdkURhuTGC4ISIyVlZdi437M/HBngwUV+pDTqiXCvMSInF3vyA4MORQM9QaLXJLqnGpuArZxdXILq5CdnEVHBUyLL2rp1lfi+HGBIYbIqKmlas1+KQu5NRPPA7u5Iy5CZGY1I/3ybE3oiiioLwG2cVVyCmpwqUG4SW7WP+4/iq8a3m7OOLI87eZtR6GGxMYboiITKus0eCzA1l4f3c6Csr1ISfQwwlzEiIxOTaYdzy2EZU1GqPeluziKmSXVBt9X6PRXfc8zg5yBHo6IdDTGYEezvqvnk64p38wBMF887cYbkxguCEiapmqGv19ctbsSkdemf5/6P7uTpgzvCumDAjh2lUWTKsTkV+mrhsuMu5tySnRf3+lbgjSFEEA/NycDOElyNMZAR51QabusafKwawhpjkMNyYw3BARtU51rRabDl3A6p3phjse+7op8diwrrhvYCicHRlyOlppda1+uKi4+poAo398ubQaGt31P97dlApDT0vDwFIfYPw9nCxmzhXDjQkMN0REbaPWaLH58EWs3pluWLvKx9URj94agQduCYPKUSFxhbahVqtDbv3wUEnVNUNH+u/L1JrrnkchE+Dv4VQ3VGQcXgI9nRHg6QR3J4cOeEfmwXBjAsMNEdGNqdHo8M3Ri3hvRxouXtGHHC8XRzwyNALT4sLgqmTIaY20vHJsTbmMnWfycL6gEpfLqtGST+ZOKgdDYAlsMFRUH2A6uylt6p5FDDcmMNwQEZlHrVaH745dwns70pBZWAkA8FQ54JGhEZgeFwY3K+oV6EgarQ5Hs4qxNeUytiZfRkZBRaN9HOUyo96WxgHGye56yhhuTGC4ISIyL41Whx+OZ2PljjScq/ugdndS4KEhEZg5uAs8nBlyKtQa7EnNx+/Jl7HjdJ7RZF4HuYC4rj64LdoXvYI9EejpDG8XR675dQ2GGxMYboiI2odWJ+Knv7LxzrZUpOfrQ46bUoEHB3fBrCHh8FQ5Slxhx7pcWo2tKZeRmHwZSWmFqNFevazaU+WAETf5YlSMH4Z282EvVwsw3JjAcENE1L60OhFbTuTg3e2pOHu5HADgqlRgRnwYHhoSAS8X2ww5oijidG4ZEpMvY2vKZfx1scTo+TBvFW6L9sOoGD/EhnXi8hatxHBjAsMNEVHH0OlE/HYqF29vS8Xp3DIAgMpRjmlxYXhkaAR8XJUSV3jjarU6HDxXhMRkfQ9N/VVkgP4eMX1DPDEqxg+3Rfsh0te1Q+4HY6sYbkxot3Cj0wFVVwBRC4g6/aar/14LiGITbfX76Zpoa+OxugbPNTpXw/10TbQ12M+7K9DnAUBhm//DIqKOo9OJSEy5jHe2peJUdikA/V1tH7glFI/cGgFfNyeJK2ydkqpa7DyTh60pedh5Js+wsjoAODnIMCSyM26L8UVClK/VvTdLxnBjQruFm7Jc4I2bzHc+S+AdCYx5Beg2SupKiMgGiKKI7afz8Pa2VMOQjVIhw32DQjF7WFf4uVtuELhQVKm/uinlMv7IKDK6QZ6PqyNGRumHm4ZE+vCmhu2E4caEdgs35XnA69303wuyBptc/1Um1/dRNmqrfyw00VZ3DllT55IZb42OE5o5V/1rNXWuuudEETjxFVCRr38/N40Dbl8GeEWY7+dFRHZLFEXsPJuPt7em4viFYgCAo0KGeweEYM7wrgjwcJa2QOh7m05cKjFMCK4fVqvXzdcVo2L8MCraD31DPHllUwdguDGh3cKNKOo3QdBv1q66BNj1KvDHGkCnAeSOQPx8YMhCQOkqdXVEZANEUcTetAK8vTUVhzOvANDf3+XvscGYM7wrgjupOrSe6lot9qcXIjHlMralXMbl0qsrXssEYEAXL9xWF2i6+Lh0aG1kZeFm1apVeO2115CTk4MePXpgxYoVGDp0aJP7fvvtt1i9ejWOHz8OtVqNHj164MUXX8Ttt9/e4tfjhOJWyj8D/PIMkLFD/9gtEBj9H6DnJNsIcUQkOVEUsT+9EG9vS8Uf54oA6JcOuKd/MOYmRCLEq/1CTlFFDbafzsPW5MvYnZqPyhqt4TkXRzmG3dQZo6L9kHCTLzrZ6FVe1sJqws2mTZswbdo0rFq1CoMHD8b777+PDz/8EMnJyQgNDW20/4IFCxAYGIiEhAR4enpi/fr1eP311/HHH3+gb9++LXpNhps2EEXgzBbg10VAcaa+LTQeGPsKENBL2tqIyKYcyCjEO9tSkZReCACQywRM7BuEuQmRZustycgvNww3Hcm8gobrS/q7O2FUjC9GRfshrqs3lArOn7EUVhNuBg0ahH79+mH16tWGtujoaEyYMAHLly9v0Tl69OiBKVOm4IUXXmjR/gw3N6C2Gkh6F9jzBqCp0s/T6f8gMOJfgMpL6uqIyIYcOl+Ed7alYk9qAQD9sNCEPkGYOyISXTu3bmhcqxNxLOsKEusCTUa+8XIHMQHuGBXjh9ExfugR6M7LtS1Uaz6/JVuYoqamBkeOHMGzzz5r1D569GgkJSW16Bw6nQ5lZWXw8mr+g1WtVkOtvjpuWlpa2raCCXBwAob9A+gzFfj9eeDUt8Dhj4CT3+gDTv8HAbl9rXVCRO1jQBcvfPLQIBzNuoJ3t6Vix5l8fHvsEr4/fgnjewdiXkIkuvm5NXt8ZY0Ge1ILsDX5MrafzkNhRY3hOQe5gFsivDGq7oZ6QZ7ST2Am85Lsk6igoABarRZ+fn5G7X5+fsjNzW3ROd544w1UVFRg8uTJze6zfPlyLFmy5IZqpWt4BAN/Xw8MeAjY8k8g7xSw5WngyAb9UFWXIVJXSEQ2ol9oJ6x/cCD+uliMd7alYmtKHn44no0f/8zGuJsDMH9EJKL89f+LzyutxrbTeUhMvoy9aQWo0Vxd7sDdSYGEKP1w07CbOsOdyx3YNMmGpbKzsxEUFISkpCTExcUZ2pctW4ZPPvkEp0+fNnn8F198gYcffhg//PADRo1q/j4sTfXchISEcFjKXLQa4Mh6YPtLQHWxvq3nJOC2pfoQRERkRicvleDd7an47dRlQ9vIKF8UVNTgz7rLyuuFeDnjtmh/jIrxxYAuXnDgcgdWzSqGpXx8fCCXyxv10uTl5TXqzbnWpk2b8NBDD2Hz5s0mgw0AKJVKKJXWf4tviyVXAAMfAXpMBHa8BBxerx+mOvMLMHQhEDdfP5xFRGQGPYM88P60WCRnl2LljlRsOZGLbafzDM/3DvHE6LrLtbv7cbkDeyX5hOL+/ftj1apVhraYmBjcddddzU4o/uKLLzBr1ix88cUXmDBhQqtfkxOK21nOn/pLx7P26x97hgFjlutvBMh/ZIjIzM7kluHHPy8huJMKI6N84WvBdzmmG2M1V0vVXwq+Zs0axMXFYe3atfjggw9w6tQphIWFYdGiRbh06RI2btwIQB9spk+fjrfffhsTJ040nMfZ2RkeHh4tek2Gmw4givrem9//BZTl6Nu6jgTG/Bfo3F3a2oiIyCq15vNb0gHIKVOmYMWKFVi6dCn69OmD3bt3Y8uWLQgLCwMA5OTkICsry7D/+++/D41Gg7lz5yIgIMCwPfnkk1K9BWqKIAA33wPMO6y/o7HcEUjfBqyOA35bDFTzijUiImo/kt+huKOx50YChen6UHP2F/1jF19g1ItA76n6dbOIiIiuw2p6bshOeHcF7vsSuP9r/UrjFXnAD48DH90GXDoidXVERGRjGG6o43S7DZizX3+ZuKMrcOkw8MEI4Ie5+lXViYiIzIDhhjqWwhEY/CQw/4h+WAoAjn0KvNsf2P8eoK2Vtj4iIrJ6DDckDTd/4O41wEOJQEAfQF0K/PYcsHowkL5d6uqIiMiKMdyQtEIGAo/sAP72LqDyAQrOAJ/cDXx5P3DlvNTVERGRFWK4IenJZEC/6fqhqkFzAEEOnP4JWDkQ2L4MqKmUukIiIrIiDDdkOZw9gbH/BebsA8JvBbRqYPerwMoBwMlv9TcHJCIiug6GG7I8vtHA9B+ByZ8AHqFA6UXg6weBj8cDl09JXR0REVk4hhuyTIIAxPwNmPsHMHwRoHACzu8B1gwBtvwDqCySukIiIrJQDDdk2RxVwPBngXmHgJi7AFEHHFyrv3T88DpAp5W6QiIisjAMN2QdPEOByRv1w1Wdo4GqIuCnp4C1w4GsA1JXR0REFoThhqxLxDBg9l5g7KuAkweQ+xew7nbgm0eA0mypqyMiIgvAcEPWR64ABj0GzD8K9JsBQABOfAW8GwvseRPQqKWukIiIJMRwQ9bLxQf42zvAozuA4IFAbQWwbQmw6hbg7G9SV0dERBIRRNG+bh7SmiXTyYqIIvDXV0DiC0B5rr6t22jg1n8ADipApwFELaDT1X3V6Ccj17cZntde/Wr0vcTHyx0Bn276y+R9o/Xzjtz89VeVERHZgdZ8fjPckG1RlwG7XwP2rwJ0Nr4Ip5OHPuT4Rhl/dfVl6CEim8NwYwLDjZ0oSNP34lw4oF/OQSav+yoDZIpr2hp+r6j7XlbXrmhin4b7yq45rrX7XlOPTHH1tRvuqy4D8s8A+SlA3mmgKF1/WXxTnDs1Dj2+MfphPCIiK8VwYwLDDdmE2mqgMFUfdOoDT34KUHQOQDN/pVU+dUNaUQ2CTzSg8urQ0omI2oLhxgSGG7JptVVAwdnGoedKJpoNPS6+jYe2fKP0PUBERBaiNZ/fig6qiYg6goMzENBbvzVUU3E19OQlA/mn9d+XZAEVecC5PODcbuNjXP0bTGCOqvt6k36uDxGRBWO4IbIHji5AYF/91pC6vMFcnpSroaf0ov6qs/JcIGOH8THuQQ3CToPQo3TruPdDRGQCh6WIqLHqUuMJzPXhpyyn+WM8Qq7O5/GN0X/f+SZ9sCIiukGcc2MCww3RDagqruvdSTH+Wn65+WM8w6728nhH6sOOwglQKPXDaApl3eO6NkWDNjk7l4lIj+HGBIYbonZQWdR06KnIv7HzCnJ9yHFoGH6crglDTQWllu7XRKAyBCsH3i+IyIJwQjERdSyVFxAWr98aqigwDjzFmfrL2DVV+jXANNVXv9ZW6782vPmiqNUvq1Fb0bHvB9Dfb6i5oOSgAtwDAY/gui0E8AzRf88J10SSY7ghovbj4gOED9VvLaXTNgg+1cYBSKPWX+5uFIxMBKVmz1N/rmvatQ0WXRV1QG2lfmsNpbtx6DH6Ggy4BXC4jaid8W8YEVkWmRxwVOm3jqbT6QOOyaCkBmrKgJJLQMnFuu2C/mtVEaAu1V9un5fc9GsI8mt6ferDT4MA5MQhc6IbwXBDRFRPJgNkzvp5OW2hLgdKL10NO/Vb8QV9W+kl/SKpJXWPm+PkYRx2rg1Abv76EEhETWK4ISIyF6Wr/vL3zjc1/bxOC5Tn1YWeLOMAZOj9uQJUl+i3yyebPo9MAbgFXp3n01QAUrq23/sksnAMN0REHUUmB9wD9FvIgKb3UTcc8rrQ+Gtpdl3vT5Z+a46T59WgYxSC6gKQq5++p4rIBjHcEBFZEqVb3Y0Qo5p+XqfV31eo5CJQfG3vT12PUHUJUF2s3y6faPo8Moe6yc31l7wL13xFE20CIDTX3ppz1D13vXNcd5+65wWZ/go2R1d9j5Wjq/7neL3HcodW/nLIWjDcEBFZE1ndhGT3QCBkYNP7VJfWzf2p6+0pvmYOUOkl/SX3pnp+7IFcaSL8uAKObi1/7OjKnjALwnBDRGRrnNz1m29008/rtEBZrn45DW0tABEQRdNfgQZtaNkxJr+i8eO2nksU9Zfs15TrJ3XXlNV9LW/wtUy/1ZQD2hr9y2nVQKUaqCw0z8/dweU6YagFPUoyeeP3ZvR+ddc8r2v659GqYxo+jzYcU//7bNCmcAJ6TDDPz7UNGG6IiOyNTA54BOk3e6SpuRp4mg1EzQQko8d1+4k6/XkNN5w0sRyJvXD1Z7ghIiLqMApHQOGlv7P2jRJF/Y0lmww/13vcRIgSdVfnEV07x8jo+2uflzW/b5PPN3U8WnH+hs+j8fPOZvjZ3gCGGyIiorYShKs3nXT1lboaqsPZT0RERGRTGG6IiIjIpjDcEBERkU1huCEiIiKbwnBDRERENoXhhoiIiGwKww0RERHZFIYbIiIisikMN0RERGRTGG6IiIjIpjDcEBERkU1huCEiIiKbwnBDRERENoXhhoiIiGyKQuoCOpooigCA0tJSiSshIiKilqr/3K7/HDfF7sJNWVkZACAkJETiSoiIiKi1ysrK4OHhYXIfQWxJBLIhOp0O2dnZcHNzgyAIZj13aWkpQkJCcOHCBbi7u5v13NR6/H1YFv4+LA9/J5aFvw/TRFFEWVkZAgMDIZOZnlVjdz03MpkMwcHB7foa7u7u/INpQfj7sCz8fVge/k4sC38fzbtej009TigmIiIim8JwQ0RERDaF4caMlEol/v3vf0OpVEpdCoG/D0vD34fl4e/EsvD3YT52N6GYiIiIbBt7boiIiMimMNwQERGRTWG4ISIiIpvCcENEREQ2heHGTFatWoXw8HA4OTmhf//+2LNnj9Ql2a3ly5djwIABcHNzg6+vLyZMmIAzZ85IXRbVWb58OQRBwIIFC6QuxW5dunQJDzzwALy9vaFSqdCnTx8cOXJE6rLskkajwb/+9S+Eh4fD2dkZERERWLp0KXQ6ndSlWTWGGzPYtGkTFixYgMWLF+PYsWMYOnQoxo4di6ysLKlLs0u7du3C3LlzceDAASQmJkKj0WD06NGoqKiQujS7d+jQIaxduxa9evWSuhS7deXKFQwePBgODg745ZdfkJycjDfeeAOenp5Sl2aXXnnlFaxZswYrV65ESkoKXn31Vbz22mt49913pS7NqvFScDMYNGgQ+vXrh9WrVxvaoqOjMWHCBCxfvlzCyggA8vPz4evri127duHWW2+Vuhy7VV5ejn79+mHVqlV46aWX0KdPH6xYsULqsuzOs88+i3379rF32ULceeed8PPzw0cffWRomzRpElQqFT755BMJK7Nu7Lm5QTU1NThy5AhGjx5t1D569GgkJSVJVBU1VFJSAgDw8vKSuBL7NnfuXNxxxx0YNWqU1KXYtR9//BGxsbH4+9//Dl9fX/Tt2xcffPCB1GXZrSFDhmDbtm04e/YsAODPP//E3r17MW7cOIkrs252t3CmuRUUFECr1cLPz8+o3c/PD7m5uRJVRfVEUcTChQsxZMgQ9OzZU+py7NaXX36Jo0eP4tChQ1KXYvcyMjKwevVqLFy4EM899xwOHjyIJ554AkqlEtOnT5e6PLvzzDPPoKSkBFFRUZDL5dBqtVi2bBmmTp0qdWlWjeHGTARBMHosimKjNup48+bNw19//YW9e/dKXYrdunDhAp588kn8/vvvcHJykrocu6fT6RAbG4uXX34ZANC3b1+cOnUKq1evZriRwKZNm/Dpp5/i888/R48ePXD8+HEsWLAAgYGBmDFjhtTlWS2Gmxvk4+MDuVzeqJcmLy+vUW8Odaz58+fjxx9/xO7duxEcHCx1OXbryJEjyMvLQ//+/Q1tWq0Wu3fvxsqVK6FWqyGXyyWs0L4EBAQgJibGqC06OhrffPONRBXZt3/84x949tlnce+99wIAbr75ZmRmZmL58uUMNzeAc25ukKOjI/r374/ExESj9sTERMTHx0tUlX0TRRHz5s3Dt99+i+3btyM8PFzqkuzayJEjceLECRw/ftywxcbG4v7778fx48cZbDrY4MGDG90a4ezZswgLC5OoIvtWWVkJmcz4o1gul/NS8BvEnhszWLhwIaZNm4bY2FjExcVh7dq1yMrKwuzZs6UuzS7NnTsXn3/+OX744Qe4ubkZetU8PDzg7OwscXX2x83NrdF8JxcXF3h7e3MelASeeuopxMfH4+WXX8bkyZNx8OBBrF27FmvXrpW6NLs0fvx4LFu2DKGhoejRoweOHTuGN998E7NmzZK6NOsmklm89957YlhYmOjo6Cj269dP3LVrl9Ql2S0ATW7r16+XujSqM2zYMPHJJ5+Uugy79b///U/s2bOnqFQqxaioKHHt2rVSl2S3SktLxSeffFIMDQ0VnZycxIiICHHx4sWiWq2WujSrxvvcEBERkU3hnBsiIiKyKQw3REREZFMYboiIiMimMNwQERGRTWG4ISIiIpvCcENEREQ2heGGiIiIbArDDRHZJUEQ8P3330tdBhG1A4YbIupwM2fOhCAIjbYxY8ZIXRoR2QCuLUVEkhgzZgzWr19v1KZUKiWqhohsCXtuiEgSSqUS/v7+RlunTp0A6IeMVq9ejbFjx8LZ2Rnh4eHYvHmz0fEnTpzAiBEj4OzsDG9vbzz66KMoLy832mfdunXo0aMHlEolAgICMG/ePKPnCwoKcPfdd0OlUqFbt2748ccfDc9duXIF999/Pzp37gxnZ2d069atURgjIsvEcENEFun555/HpEmT8Oeff+KBBx7A1KlTkZKSAgCorKzEmDFj0KlTJxw6dAibN2/G1q1bjcLL6tWrMXfuXDz66KM4ceIEfvzxR0RGRhq9xpIlSzB58mT89ddfGDduHO6//34UFRUZXj85ORm//PILUlJSsHr1avj4+HTcD4CI2k7qlTuJyP7MmDFDlMvloouLi9G2dOlSURT1K7vPnj3b6JhBgwaJc+bMEUVRFNeuXSt26tRJLC8vNzz/888/izKZTMzNzRVFURQDAwPFxYsXN1sDAPFf//qX4XF5ebkoCIL4yy+/iKIoiuPHjxcffPBB87xhIupQnHNDRJJISEjA6tWrjdq8vLwM38fFxRk9FxcXh+PHjwMAUlJS0Lt3b7i4uBieHzx4MHQ6Hc6cOQNBEJCdnY2RI0earKFXr16G711cXODm5oa8vDwAwJw5czBp0iQcPXoUo0ePxoQJExAfH9+m90pEHYvhhogk4eLi0miY6HoEQQAAiKJo+L6pfZydnVt0PgcHh0bH6nQ6AMDYsWORmZmJn3/+GVu3bsXIkSMxd+5cvP76662qmYg6HufcEJFFOnDgQKPHUVFRAICYmBgcP34cFRUVhuf37dsHmUyG7t27w83NDV26dMG2bdtuqIbOnTtj5syZ+PTTT7FixQqsXbv2hs5HRB2DPTdEJAm1Wo3c3FyjNoVCYZi0u3nzZsTGxmLIkCH47LPPcPDgQXz00UcAgPvvvx///ve/MWPGDLz44ovIz8/H/PnzMW3aNPj5+QEAXnzxRcyePRu+vr4YO3YsysrKsG/fPsyfP79F9b3wwgvo378/evToAbVajZ9++gnR0dFm/AkQUXthuCEiSfz6668ICAgwarvppptw+vRpAPormb788ks8/vjj8Pf3x2effYaYmBgAgEqlwm+//YYnn3wSAwYMgEqlwqRJk/Dmm28azjVjxgxUV1fjrbfewtNPPw0fHx/cc889La7P0dERixYtwvnz5+Hs7IyhQ4fiyy+/NMM7J6L2JoiiKEpdBBFRQ4Ig4LvvvsOECROkLoWIrBDn3BAREZFNYbghIiIim8I5N0RkcThaTkQ3gj03REREZFMYboiIiMimMNwQERGRTWG4ISIiIpvCcENEREQ2heGGiIiIbArDDREREdkUhhsiIiKyKQw3REREZFP+HxcKdAkv9sU/AAAAAElFTkSuQmCC",
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
    "plt.plot(history.history['loss'])\n",
    "plt.plot(history.history['val_loss'])\n",
    "plt.title(\"Model Loss\")\n",
    "plt.xlabel(\"Epochs\")\n",
    "plt.ylabel(\"Loss\")\n",
    "plt.legend(['Train','Validation'], loc = 'upper left')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d52b7475-37b5-4227-be9b-33ce5752fd63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m875/875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m4s\u001b[0m 4ms/step\n",
      "[[1.3022795e-06 3.2154421e-08 9.9956912e-01 ... 3.0990063e-06\n",
      "  9.1785631e-07 6.5940062e-09]\n",
      " [9.9743360e-01 1.5769320e-09 2.6193052e-04 ... 3.5026014e-06\n",
      "  1.7450214e-04 7.3298259e-04]\n",
      " [5.3708383e-04 1.2365617e-03 3.1831358e-02 ... 3.6268965e-03\n",
      "  1.1400817e-01 8.3568078e-01]\n",
      " ...\n",
      " [9.6196585e-11 9.2993711e-09 5.3834594e-07 ... 3.3930752e-07\n",
      "  5.8776777e-07 2.9991881e-07]\n",
      " [1.3017122e-06 1.7426686e-05 3.4301257e-07 ... 2.8709287e-03\n",
      "  5.6520486e-05 9.9645215e-01]\n",
      " [8.2022228e-07 1.9730791e-08 9.9997860e-01 ... 1.3577294e-07\n",
      "  4.7105336e-06 7.7861460e-09]]\n"
     ]
    }
   ],
   "source": [
    "# Testing data \n",
    "predict = model.predict(test)\n",
    "print(predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "aba24062-5c31-4aba-949b-3ac35538b028",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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uPzCabZL9XhhXllZWavr6d+/vySptLS0TX1K529seO655/Tzn/9c48eP1zXXXKMuXbpo1qxZPjc0LFiwQD169NDLL7+sF154QV27dtW4ceP061//2nuDycaNG7V48WK9+OKL+sUvfqGePXtq+vTpWrp0aYufEZ0XIQTrhgwZ4v3L61K+eXRwQXR0tPr06aOtW7e2WBMRESFJ3qCpqKjQtdde613e0NBw2WsUF65Lffrpp62Ou5To6GhJ0u9//3slJiZectw3e7xYS/MuNmHCBIWGhmrTpk168MEH29Tryy+/rPvuu09LlizxmX/y5En16tXL+zokJEQ5OTnKycnR6dOntW3bNj355JOaNGmSysvLFR4erujoaK1cuVIrV67UsWPH9Oabb+qJJ55QZWXlJf+80DlxOg5Ba8qUKTp16pQaGxs1cuTIZtOFC+lpaWmSpPXr1/vU/9u//ZsaGhpaXcfAgQM1YMAAvfTSS6qtrb3kOLfbLUnNboGeNGmSQkJC9Mknn7TY44XwHTRokOLi4vTKK6/IGOOtP3r0qHbt2nXZbeHxeDRr1iwVFBRc8o66Tz75RB999NEl38Plcnk/xwWbN29u9YvDvXr10p133qk5c+boiy++aPGIrX///po7d64mTpyoDz744LKfBZ0LR0IIWnfffbfWr1+v22+/Xf/wD/+gUaNGKTQ0VJ9++ql27NihqVOnavr06RoyZIh+8pOfaOXKlQoNDdVtt92mP//5z3r22WebneJryXPPPafMzEylpKTo4YcfVv/+/XXs2DEVFBR4g23YsGGSpN/85jfKzs5WaGioBg0apOuuu06//OUvtXDhQh05ckSTJ0/WNddco88++0zvvfeeevTooaefflpdunTRr371K82aNUvTp0/X7Nmzdfr0aeXm5l7x6asVK1boyJEjmjFjhgoKCjR9+nTFxsbq5MmTKiwsVH5+vl599dVL3qY9ZcoUrVmzRoMHD9bw4cO1d+9eLVu2rNmpyMzMTO93u/r27aujR49q5cqVSkxMVHJysqqqqjRhwgTdc889Gjx4sCIiIlRSUqKtW7cqKyvrij4LOhHbd0ag87pwd1xJSUmr47Kzs02PHj1aXFZfX2+effZZM2LECNO9e3fTs2dPM3jwYPPAAw+Yw4cPe8fV1taaRx55xMTExJju3bublJQUs3v3bpOYmHjZu+OM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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAaEAAAGxCAYAAADLfglZAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAleUlEQVR4nO3de3RUZZ7u8afIpQhQiUIulUiIWUy4tCAeRS4ZLoGRaFykgciIbbcmLKF1BHow2oyIc0i3DnFQGJxG8Yy2AVoQenpovA4xHkjQBbQRUWnb1igBYkNMEyWJEXN9zx8caiwTLjtW8eby/ay117L23r/av9psediXestljDECAMCCXrYbAAD0XIQQAMAaQggAYA0hBACwhhACAFhDCAEArCGEAADWEEIAAGsIIQCANYQQrFm/fr1cLpdvCg0N1cCBAzV37lz95S9/uSg9XH755crJyfG9Li4ulsvlUnFxsaP32bNnj/Ly8nTy5MmA9idJOTk5uvzyyy9o3dbWVv3mN7/Rddddp+joaIWFhSk2NlbTp0/XSy+9pNbWVknS4cOH5XK5tH79+oD3CzhBCMG6goIC7d27V0VFRZo/f76ef/55TZw4UfX19Re9l6uvvlp79+7V1Vdf7ahuz549+sUvfhGUELpQ33zzjW688UZlZ2crNjZW69at086dO/XUU08pISFBf//3f6+XXnrJWn9Ae0JtNwCMGDFCo0ePliRNmTJFLS0teuihh7R9+3b9+Mc/brfm66+/Vp8+fQLeS2RkpMaNGxfw970YcnNzVVhYqA0bNuj222/3W5aVlaWf//znOnXqlKXugPZxJoRO50wIHDlyRNLpy1H9+vXTwYMHlZ6eLo/Ho7/7u7+TJDU2Nurhhx/WsGHD5Ha7FRMTo7lz5+qvf/2r33s2NTVpyZIl8nq96tOnjyZMmKC33nqrzbbPdjnuD3/4gzIzMzVgwAD17t1bgwcP1uLFiyVJeXl5+vnPfy5JSk5O9l1e/PZ7bN26VePHj1ffvn3Vr18/XX/99Tpw4ECb7a9fv15Dhw6V2+3W8OHDtXHjxgvaZ5WVlXrmmWd0/fXXtwmgM1JSUnTllVee9T0++eQTzZ07VykpKerTp48uu+wyZWZm6uDBg37rtba26uGHH9bQoUMVERGhSy65RFdeeaUef/xx3zp//etf9dOf/lSJiYm+P5e//du/1euvv35Bnwc9B2dC6HQ++eQTSVJMTIxvXmNjo374wx/qzjvv1P3336/m5ma1trZqxowZeuONN7RkyRKlpqbqyJEjWr58udLS0vT2228rIiJCkjR//nxt3LhR9913n6ZNm6Y//vGPysrKUl1d3Xn7KSwsVGZmpoYPH67Vq1dr0KBBOnz4sF577TVJ0rx58/TFF1/oV7/6lbZt26b4+HhJ0g9+8ANJ0ooVK/Tggw9q7ty5evDBB9XY2KhHH31UEydO1FtvveVbb/369Zo7d65mzJihVatWqaamRnl5eWpoaFCvXuf+9+KuXbvU1NSkmTNnOtvZ33Ls2DENGDBAjzzyiGJiYvTFF19ow4YNGjt2rA4cOKChQ4dKklauXKm8vDw9+OCDmjRpkpqamvTnP//Z71LkbbfdpnfeeUf/8i//oiFDhujkyZN65513VF1d3eH+0E0ZwJKCggIjyezbt880NTWZuro68/LLL5uYmBjj8XhMZWWlMcaY7OxsI8k8++yzfvXPP/+8kWT+67/+y29+aWmpkWSefPJJY4wxH374oZFk7rnnHr/1Nm3aZCSZ7Oxs37xdu3YZSWbXrl2+eYMHDzaDBw82p06dOutnefTRR40kU15e7jf/6NGjJjQ01CxatMhvfl1dnfF6vebmm282xhjT0tJiEhISzNVXX21aW1t96x0+fNiEhYWZpKSks27bGGMeeeQRI8ns2LHjnOudUV5ebiSZgoKCs67T3NxsGhsbTUpKit++mz59urnqqqvO+f79+vUzixcvvqBe0LNxOQ7WjRs3TmFhYfJ4PJo+fbq8Xq/++7//W3FxcX7r3XTTTX6vX375ZV1yySXKzMxUc3Ozb7rqqqvk9Xp9l8N27dolSW3uL918880KDT33xYCPP/5Yn376qe644w717t3b8WcrLCxUc3Ozbr/9dr8ee/furcmTJ/t6/Oijj3Ts2DHdeuutcrlcvvqkpCSlpqY63m5HNDc3a8WKFfrBD36g8PBwhYaGKjw8XGVlZfrwww99640ZM0bvvfee7r77bhUWFqq2trbNe40ZM0br16/Xww8/rH379qmpqemifAZ0PVyOg3UbN27U8OHDFRoaqri4ON/lrG/r06ePIiMj/eZ9/vnnOnnypMLDw9t93xMnTkiS7xKQ1+v1Wx4aGqoBAwacs7cz95YGDhx4YR/mOz7//HNJ0rXXXtvu8jOX2c7W45l5hw8fPud2Bg0aJEkqLy/vUJ/S6QcbnnjiCf3TP/2TJk+erEsvvVS9evXSvHnz/B5oWLp0qfr27avnnntOTz31lEJCQjRp0iT967/+q+8Bk61bt+rhhx/WM888o3/+539Wv379NGvWLK1cubLdz4ieixCCdcOHD/f95XU23z47OCM6OloDBgzQjh072q3xeDyS5AuayspKXXbZZb7lzc3N571Hcea+1GeffXbO9c4mOjpakvS73/1OSUlJZ13v2z1+V3vzvmvKlCkKCwvT9u3bddddd3Wo1+eee0633367VqxY4Tf/xIkTuuSSS3yvQ0NDlZubq9zcXJ08eVKvv/66HnjgAV1//fWqqKhQnz59FB0drTVr1mjNmjU6evSoXnzxRd1///2qqqo6658XeiYux6HLmj59uqqrq9XS0qLRo0e3mc7cSE9LS5Mkbdq0ya/+t7/9rZqbm8+5jSFDhmjw4MF69tln1dDQcNb13G63JLV5BPr6669XaGioPv3003Z7PBO+Q4cOVXx8vJ5//nkZY3z1R44c0Z49e867L7xer+bNm6fCwsKzPlH36aef6v333z/re7hcLt/nOOOVV1455xeHL7nkEs2ePVsLFizQF1980e4Z26BBg7Rw4UJNmzZN77zzznk/C3oWzoTQZd1yyy3atGmTbrzxRv3jP/6jxowZo7CwMH322WfatWuXZsyYoVmzZmn48OH6yU9+ojVr1igsLEzXXXed/vjHP+qxxx5rc4mvPU888YQyMzM1btw43XPPPRo0aJCOHj2qwsJCX7CNHDlSkvT4448rOztbYWFhGjp0qC6//HL98pe/1LJly3To0CHdcMMNuvTSS/X555/rrbfeUt++ffWLX/xCvXr10kMPPaR58+Zp1qxZmj9/vk6ePKm8vLwLvny1evVqHTp0SDk5OSosLNSsWbMUFxenEydOqKioSAUFBdqyZctZH9OePn261q9fr2HDhunKK6/U/v379eijj7a5FJmZmen7bldMTIyOHDmiNWvWKCkpSSkpKaqpqdGUKVN06623atiwYfJ4PCotLdWOHTuUlZV1QZ8FPYjtJyPQc515Oq60tPSc62VnZ5u+ffu2u6ypqck89thjZtSoUaZ3796mX79+ZtiwYebOO+80ZWVlvvUaGhrMvffea2JjY03v3r3NuHHjzN69e01S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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAaEAAAGxCAYAAADLfglZAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAlOklEQVR4nO3de3RU9b338c9AkuE2CUIuk0iIOZxwqVxcCAIp95ZoXKRAtMXa1sASCgqsg1GpiOcQqyUUhQdXUTzVGuAISJ8eixcsMT4Q0ANoRKzUYz0gCcRCjETJxIiTC7/nDx7mYUy47JjwyyTv11p7LWbv33f2dzZ78eE3s2ePyxhjBACABR1sNwAAaL8IIQCANYQQAMAaQggAYA0hBACwhhACAFhDCAEArCGEAADWEEIAAGsIIVizbt06uVyuwBIWFqZevXpp5syZ+sc//nFFerjmmms0Y8aMwOPCwkK5XC4VFhY6ep49e/YoJydHp06datb+JGnGjBm65pprLmvsmTNn9B//8R/64Q9/qOjoaIWHhys2NlaTJ0/WK6+8ojNnzkiSSkpK5HK5tG7dumbvF3CCEIJ1eXl52rt3rwoKCjR79mxt3rxZY8aMUXV19RXvZejQodq7d6+GDh3qqG7Pnj16+OGHWySELtc333yjm2++WVlZWYqNjdXatWu1Y8cOPf3000pISNCPf/xjvfLKK9b6AxoTZrsBYODAgRo2bJgkacKECaqvr9cjjzyirVu36mc/+1mjNV9//bW6dOnS7L1ERkZq5MiRzf68V0J2drby8/O1fv163XHHHUHbMjMzdf/99+v06dOWugMax0wIrc65EDh69Kiks29HdevWTQcPHlRaWpo8Ho9+8IMfSJJqamr06KOPqn///nK73YqJidHMmTP1+eefBz1nbW2tFi1aJK/Xqy5dumj06NF65513Guz7Qm/Hvf3228rIyFDPnj3VqVMn9enTRwsXLpQk5eTk6P7775ckJScnB95ePP85tmzZolGjRqlr167q1q2bbrzxRh04cKDB/tetW6d+/frJ7XZrwIAB2rBhw2Uds7KyMj377LO68cYbGwTQOSkpKRo8ePAFn+Pw4cOaOXOmUlJS1KVLF1199dXKyMjQwYMHg8adOXNGjz76qPr166fOnTure/fuGjx4sJ544onAmM8//1y//OUvlZiYGPh7+f73v6833njjsl4P2g9mQmh1Dh8+LEmKiYkJrKupqdGPfvQjzZkzRw888IDq6up05swZTZkyRW+++aYWLVqk1NRUHT16VEuXLtX48eP17rvvqnPnzpKk2bNna8OGDbrvvvs0adIk/e1vf1NmZqaqqqou2U9+fr4yMjI0YMAArVq1Sr1791ZJSYlef/11SdKsWbP0xRdf6He/+51efPFFxcfHS5K+973vSZKWLVumhx56SDNnztRDDz2kmpoaPfbYYxozZozeeeedwLh169Zp5syZmjJlilauXKnKykrl5OTI7/erQ4eL/39x586dqq2t1dSpU50d7PMcP35cPXv21PLlyxUTE6MvvvhC69ev14gRI3TgwAH169dPkrRixQrl5OTooYce0tixY1VbW6u///3vQW9F/uIXv9B7772n3/zmN+rbt69OnTql9957TxUVFU3uD22UASzJy8szksy+fftMbW2tqaqqMq+++qqJiYkxHo/HlJWVGWOMycrKMpLMc889F1S/efNmI8n853/+Z9D6oqIiI8k89dRTxhhjPvroIyPJ3HPPPUHjNm7caCSZrKyswLqdO3caSWbnzp2BdX369DF9+vQxp0+fvuBreeyxx4wkU1xcHLT+2LFjJiwszCxYsCBofVVVlfF6veYnP/mJMcaY+vp6k5CQYIYOHWrOnDkTGFdSUmLCw8NNUlLSBfdtjDHLly83ksz27dsvOu6c4uJiI8nk5eVdcExdXZ2pqakxKSkpQcdu8uTJ5rrrrrvo83fr1s0sXLjwsnpB+8bbcbBu5MiRCg8Pl8fj0eTJk+X1evWXv/xFcXFxQeNuueWWoMevvvqqunfvroyMDNXV1QWW6667Tl6vN/B22M6dOyWpwedLP/nJTxQWdvE3A/7nf/5Hn3zyie6880516tTJ8WvLz89XXV2d7rjjjqAeO3XqpHHjxgV6/Pjjj3X8+HHdfvvtcrlcgfqkpCSlpqY63m9T1NXVadmyZfre976niIgIhYWFKSIiQocOHdJHH30UGHfDDTfor3/9q+6++27l5+fL5/M1eK4bbrhB69at06OPPqp9+/aptrb2irwGhB7ejoN1GzZs0IABAxQWFqa4uLjA21nn69KliyIjI4PWffbZZzp16pQiIiIafd6TJ09KUuAtIK/XG7Q9LCxMPXv2vGhv5z5b6tWr1+W9mG/57LPPJEnDhw9vdPu5t9ku1OO5dSUlJRfdT+/evSVJxcXFTepTOnthw5NPPqlf/epXGjdunK666ip16NBBs2bNCrqgYfHixeratauef/55Pf300+rYsaPGjh2r3/72t4ELTLZs2aJHH31Uzz77rP71X/9V3bp107Rp07RixYpGXyPaL0II1g0YMCDwj9eFnD87OCc6Olo9e/bU9u3bG63xeDySFAiasrIyXX311YHtdXV1l/yM4tznUp9++ulFx11IdHS0JOlPf/qTkpKSLjju/B6/rbF13zZhwgSFh4dr69atmjt3bpN6ff7553XHHXdo2bJlQetPnjyp7t27Bx6HhYUpOztb2dnZOnXqlN544w09+OCDuvHGG1VaWqouXbooOjpaq1ev1urVq3Xs2DG9/PLLeuCBB1ReXn7Bvy+0T7wdh5A1efJkVVRUqL6+XsOGDWuwnPsgffz48ZKkjRs3BtX/8Y9/VF1d3UX30bdvX/Xp00fPPfec/H7/Bce53W5JanAJ9I033qiwsDB98sknjfZ4Lnz79eun+Ph4bd68WcaYQP3Ro0e1Z8+eSx4Lr9erWbNmKT8//4JX1H3yySf64IMPLvgcLpcr8DrO2bZt20W/ONy9e3fdeuutmjdvnr744otGZ2y9e/fW/PnzNWnSJL333nuXfC1oX5gJIWTddttt2rhxo26++Wb9y7/8i2644QaFh4fr008/1c6dOzVlyhRNmzZNAwYM0M9//nOtXr1a4eHh+uEPf6i//e1vevzxxxu8xdeYJ598UhkZGRo5cqTuuece9e7dW8eOHVN+fn4g2AYNGiRJeuKJJ5SVlaXw8HD169dP11xzjX79619ryZIlOnLkiG666SZdddVV+uyzz/TOO++oa9euevjhh9WhQwc98sgjmjVrlqZNm6bZs2fr1KlTysnJuey3r1atWqUjR45oxowZys/P17Rp0xQXF6eTJ0+qoKBAeXl5euGFFy54mfbkyZO1bt069e/fX4MHD9b+/fv12GOPNXgrMiMjI/DdrpiYGB09elSrV69WUlKSUlJSVFlZqQkTJuj2229X//795fF4VFRUpO3btyszM/OyXgvaEdtXRqD9Ond1XFFR0UXHZWVlma5duza6rba21jz++ONmyJAhplOnTqZbt26mf//+Zs6cOebQoUOBcX6/39x7770mNjbWdOrUyYwcOdLs3bvXJCUlXfLq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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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oqOj1alT01d9brgjoU6dOqlv375NjgkNDe3QO1k9tsMlbIdL2A6XsB0usb0drnYEVI8bEwAA1hBCAABr2lQIud1uLV26VG6323YrVrEdLmE7XMJ2uITtcElb2w433I0JAICOo00dCQEA2hdCCABgDSEEALCGEAIAWEMIAQCsaVMh9MILLyguLk5du3bVHXfcoXfeecd2S9dVVlaWXC6X3+TxeGy31er27t2r1NRURUdHy+VyaevWrX7LjTHKyspSdHS0goKClJiYqE8++cROs63oatshIyOjwf4xevRoO822kuzsbI0cOVIhISGKiIjQvffeq6NHj/qN6Qj7w7Vsh7ayP7SZENq8ebMWLFigJUuW6NChQxo3bpxSUlJ06tQp261dV7fccovOnDnjmw4fPmy7pVZXVVWl4cOHa9WqVY0uX758uVauXKlVq1apsLBQHo9HkyZN8j0Mt7242naQpMmTJ/vtH9u3t68HAe/Zs0dz587VgQMHlJ+fr9raWiUnJ6uqqso3piPsD9eyHaQ2sj+YNuLOO+80jzzyiN+8wYMHm0WLFlnq6PpbunSpGT58uO02rJJkXnvtNd/ruro64/F4zDPPPOOb9+2335qwsDDz4osvWujw+rh8OxhjTHp6upk6daqVfmwpKyszksyePXuMMR13f7h8OxjTdvaHNnEkVF1drYMHDyo5OdlvfnJysvbt22epKzuKiooUHR2tuLg4Pfjggzp+/LjtlqwqLi5WaWmp377hdrs1YcKEDrdvSFJBQYEiIiI0cOBAzZkzR2VlZbZbalXl5eWSpJ49e0rquPvD5duhXlvYH9pECJ09e1YXL15UZGSk3/zIyEiVlpZa6ur6GzVqlNavX6+8vDy99NJLKi0tVUJCgs6dO2e7NWvq//w7+r4hSSkpKdqwYYN27dqlFStWqLCwUBMnTpTX67XdWqswxigzM1Njx47V0KFDJXXM/aGx7SC1nf3hhvsph6Zc/vtCxpgG89qzlJQU338PGzZMY8aM0YABA7Ru3TplZmZa7My+jr5vSNL06dN9/z106FCNGDFCsbGx2rZtm9LS0ix21jrmzZunjz76SO+++26DZR1pf7jSdmgr+0ObOBIKDw9X586dG/xLpqysrMG/eDqSbt26adiwYSoqKrLdijX1dweybzQUFRWl2NjYdrl/zJ8/X2+88YZ2797t9/tjHW1/uNJ2aMyNuj+0iRDq0qWL7rjjDuXn5/vNz8/PV0JCgqWu7PN6vTpy5IiioqJst2JNXFycPB6P375RXV2tPXv2dOh9Q5LOnTunkpKSdrV/GGM0b948bdmyRbt27VJcXJzf8o6yP1xtOzTmht0fLN4U4cirr75qAgMDzW9/+1vz5z//2SxYsMB069bNnDhxwnZr183jjz9uCgoKzPHjx82BAwfMlClTTEhISLvfBpWVlebQoUPm0KFDRpJZuXKlOXTokDl58qQxxphnnnnGhIWFmS1btpjDhw+bH/7whyYqKspUVFRY7rxlNbUdKisrzeOPP2727dtniouLze7du82YMWNMnz592tV2+OlPf2rCwsJMQUGBOXPmjG/65ptvfGM6wv5wte3QlvaHNhNCxhjz/PPPm9jYWNOlSxdz++23+92O2BFMnz7dREVFmcDAQBMdHW3S0tLMJ598YrutVrd7924jqcGUnp5ujLl0W+7SpUuNx+MxbrfbjB8/3hw+fNhu062gqe3wzTffmOTkZNO7d28TGBho+vXrZ9LT082pU6dst92iGvv8kkxubq5vTEfYH662HdrS/sDvCQEArGkT14QAAO0TIQQAsIYQAgBYQwgBAKwhhAAA1hBCAABrCCEAgDWEEADAGkIIAGANIQQAsIYQAgBY8/8AFPBvCQn/scYAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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O812oR7PzSsuLm5yPf3795ckFRUVNatP6eyNDc8884z+4z/+Q+PHj9fll1+uLl26aObMmUE3NMyfP189e/bUSy+9pOeee05du3bVuHHj9Jvf/CZwg8mGDRv05JNP6oUXXtAvf/lL9erVS1OnTtXixYsb/YzovAghWDdkyJDAX14Xcv7RwTkRERHq06ePtmzZ0miNx+ORpEDQlJaWqm/fvoHltbW1F71Gce661GeffdbkuAuJiIiQJP3pT39SfHz8Bced3+O3NTbv2yZMmKDQ0FBt2rRJ999/f7N6femll3TPPfdo0aJFQfNPnDihyy67LPA6JCREmZmZyszM1KlTp7R161b94he/0KRJk1RSUqIePXooIiJCy5cv1/Lly3X06FG99tprevTRR1VWVnbBPy90TpyOQ7s1efJklZeXq66uTiNHjmwwnbuQnpycLElau3ZtUP0f//hH1dbWNrmOgQMHasCAAXrxxRdVVVV1wXFut1uSGtwCPWnSJIWEhOjTTz9ttMdz4Tto0CDFxMTo5ZdfljEmUH/kyBHt2rXrotvC5/Np5syZys3NveAddZ9++qk++uijC76Hy+UKfI5zNm/e3OQXhy+77DLdfvvtmj17tr788stGj9j69++vOXPmaOLEifrggw8u+lnQuXAkhHbrzjvv1Nq1a3XLLbfo3//933X99dcrNDRUn332mbZv364pU6Zo6tSpGjJkiP71X/9Vy5cvV2hoqG666SZ9/PHHevrppxuc4mvMM888o7S0NI0ePVo///nP1b9/fx09elS5ubmBYBs2bJgk6be//a0yMjIUGhqqQYMG6YorrtATTzyhBQsW6PDhw7r55pt1+eWX6/PPP9d7772nnj176vHHH1eXLl30q1/9SjNnztTUqVM1a9YsnTp1SllZWd/59NWyZct0+PBhTZ8+Xbm5uZo6daqio6N14sQJ5eXlKScnR+vXr7/gbdqTJ0/WqlWrNHjwYA0fPlx79+7VkiVLGpyKTEtLC3y3KzIyUkeOHNHy5csVHx+vxMREVVRUaMKECZo2bZoGDx4sj8ejgoICbdmyRenp6d/ps6ATsX1nBDqvc3fHFRQUNDkuIyPD9OzZs9FlNTU15umnnzYjRoww3bt3N7169TKDBw829913nyksLAyMq6qqMg8++KCJiooy3bt3N6NHjza7d+828fHxF707zhhj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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot the predictions \n",
    "\n",
    "for i in range(5):\n",
    "    plt.imshow(test[i])\n",
    "    plt.title(\"Predicted Class\")\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "f3c7f219-33ac-4d61-89dc-b67830e9ce71",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 0, 9, ..., 3, 9, 2])"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Evaluation Metrics \n",
    "\n",
    "predict_labels = np.argmax(predict, axis = 1)\n",
    "predict_labels"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "f783d803-4203-4acc-98ed-90082775a750",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m132/132\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 5ms/step\n"
     ]
    }
   ],
   "source": [
    "val_predict = model.predict(X_val)\n",
    "val_predict_labels = np.argmax(val_predict, axis = 1)\n",
    "y_val_labels = np.argmax(y_val, axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "8668f1e5-4464-4129-b99e-fc4f1a657c55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[408   0   0   0   1   0   1   0   1   0]\n",
      " [  0 473   1   7   1   0   0   0   3   0]\n",
      " [  1   0 395   2   0   0   0   0   4   1]\n",
      " [  1   0   0 409   0   2   0   1   4   1]\n",
      " [  0   2   0   0 441   1   1   1   1  14]\n",
      " [  0   0   0   3   0 362   1   0   3   3]\n",
      " [  4   0   0   0   0   0 404   0   5   0]\n",
      " [  0   0   1   0   0   0   0 440   1   4]\n",
      " [  0   0   1   1   2   4   1   0 370   3]\n",
      " [  1   0   0   5   3   1   0   2   2 395]]\n"
     ]
    }
   ],
   "source": [
    "cm = confusion_matrix(y_val_labels, val_predict_labels)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "791d2424-3500-4730-93a0-21aed445425c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.98      0.99      0.99       411\n",
      "           1       1.00      0.98      0.99       485\n",
      "           2       0.99      0.98      0.99       403\n",
      "           3       0.96      0.98      0.97       418\n",
      "           4       0.98      0.96      0.97       461\n",
      "           5       0.98      0.97      0.98       372\n",
      "           6       0.99      0.98      0.98       413\n",
      "           7       0.99      0.99      0.99       446\n",
      "           8       0.94      0.97      0.95       382\n",
      "           9       0.94      0.97      0.95       409\n",
      "\n",
      "    accuracy                           0.98      4200\n",
      "   macro avg       0.98      0.98      0.98      4200\n",
      "weighted avg       0.98      0.98      0.98      4200\n",
      "\n"
     ]
    }
   ],
   "source": [
    "classreport = classification_report(y_val_labels, val_predict_labels)\n",
    "print(classreport)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47268656-8b4c-4220-ae6d-4d35c416173f",
   "metadata": {},
   "source": [
    "\n",
    "### 3. **Overfitting and Underfitting**\n",
    "\n",
    "- **Overfitting**: This occurs when the model performs well on the training data but poorly on the validation data. It typically happens when the model is too complex or trained for too many epochs. Signs include:\n",
    "  - Training accuracy is high, but validation accuracy is low or stagnating.\n",
    "  - Training loss decreases, but validation loss starts to increase.\n",
    "\n",
    "- **Underfitting**: This occurs when the model performs poorly on both the training and validation data. This often happens when the model is too simple or not trained enough. Signs include:\n",
    "  - Both training and validation accuracy are low.\n",
    "  - Training and validation loss are high and don't improve over time.\n",
    "\n",
    "### 4. **Confusion Matrix**\n",
    "\n",
    "- **Confusion Matrix**: This provides a detailed view of how well the model is performing across different classes. It shows:\n",
    "  - **True Positives (TP)**: Correctly classified samples for each class.\n",
    "  - **False Positives (FP)**: Samples incorrectly classified as a given class.\n",
    "  - **False Negatives (FN)**: Samples that belong to a given class but were classified incorrectly.\n",
    "  - **True Negatives (TN)**: Samples correctly classified as not belonging to a given class.\n",
    "\n",
    "From the confusion matrix, you can infer:\n",
    "  - **Class Imbalance**: If certain classes have high false positives or false negatives, it may indicate class imbalance.\n",
    "  - **Model Performance**: Which classes the model is performing well on and which it is struggling with.\n",
    "  - **Error Types**: Patterns of errors, such as confusion between similar classes.\n",
    "\n",
    "### Interpreting Specific Cases\n",
    "\n",
    "1. **Training and Validation Loss Curves**:\n",
    "   - If both curves decrease and stabilize, your model is likely well-trained.\n",
    "   - If training loss decreases while validation loss increases, overfitting might be occurring.\n",
    "   - If both curves are high, your model might be underfitting.\n",
    "\n",
    "2. **Training and Validation Accuracy Curves**:\n",
    "   - If both accuracy curves are increasing and eventually plateau, your model is likely learning effectively.\n",
    "   - If training accuracy is high but validation accuracy is low or decreasing, it indicates overfitting.\n",
    "   - If both accuracies are low, consider increasing model complexity or training more epochs.\n",
    "\n",
    "3. **Confusion Matrix**:\n",
    "   - Look for high counts in diagonal entries (true positives), which indicates good performance.\n",
    "   - Analyze off-diagonal entries to understand which classes are confused with each other.\n",
    "\n",
    "### Example Interpretation\n",
    "\n",
    "- **Training Loss**: Decreases from 0.6 to 0.1.\n",
    "- **Validation Loss**: Decreases from 0.7 to 0.2 but starts to increase after 8 epochs.\n",
    "\n",
    "**Inference**:\n",
    "- The model is learning well from the training data, but it begins to overfit after a certain point, as indicated by the increasing validation loss after 8 epochs.\n",
    "- **Action**: You might consider stopping training earlier (early stopping), using regularization techniques, or tuning hyperparameters to improve generalization.\n",
    "\n",
    "By analyzing these metrics, you can make informed decisions about how to adjust your model, data, and training process to achieve better performance."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6016acf7-5fad-4370-8dd3-599f02a8dcbc",
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
