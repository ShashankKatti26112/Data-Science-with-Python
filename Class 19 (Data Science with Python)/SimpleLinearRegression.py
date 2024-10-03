{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "761d57b1-8cbd-448e-9cb1-6b66902ee9ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['anagrams',\n",
       " 'anscombe',\n",
       " 'attention',\n",
       " 'brain_networks',\n",
       " 'car_crashes',\n",
       " 'diamonds',\n",
       " 'dots',\n",
       " 'dowjones',\n",
       " 'exercise',\n",
       " 'flights',\n",
       " 'fmri',\n",
       " 'geyser',\n",
       " 'glue',\n",
       " 'healthexp',\n",
       " 'iris',\n",
       " 'mpg',\n",
       " 'penguins',\n",
       " 'planets',\n",
       " 'seaice',\n",
       " 'taxis',\n",
       " 'tips',\n",
       " 'titanic',\n",
       " 'anagrams',\n",
       " 'anagrams',\n",
       " 'anscombe',\n",
       " 'anscombe',\n",
       " 'attention',\n",
       " 'attention',\n",
       " 'brain_networks',\n",
       " 'brain_networks',\n",
       " 'car_crashes',\n",
       " 'car_crashes',\n",
       " 'diamonds',\n",
       " 'diamonds',\n",
       " 'dots',\n",
       " 'dots',\n",
       " 'dowjones',\n",
       " 'dowjones',\n",
       " 'exercise',\n",
       " 'exercise',\n",
       " 'flights',\n",
       " 'flights',\n",
       " 'fmri',\n",
       " 'fmri',\n",
       " 'geyser',\n",
       " 'geyser',\n",
       " 'glue',\n",
       " 'glue',\n",
       " 'healthexp',\n",
       " 'healthexp',\n",
       " 'iris',\n",
       " 'iris',\n",
       " 'mpg',\n",
       " 'mpg',\n",
       " 'penguins',\n",
       " 'penguins',\n",
       " 'planets',\n",
       " 'planets',\n",
       " 'seaice',\n",
       " 'seaice',\n",
       " 'taxis',\n",
       " 'taxis',\n",
       " 'tips',\n",
       " 'tips',\n",
       " 'titanic',\n",
       " 'titanic',\n",
       " 'anagrams',\n",
       " 'anscombe',\n",
       " 'attention',\n",
       " 'brain_networks',\n",
       " 'car_crashes',\n",
       " 'diamonds',\n",
       " 'dots',\n",
       " 'dowjones',\n",
       " 'exercise',\n",
       " 'flights',\n",
       " 'fmri',\n",
       " 'geyser',\n",
       " 'glue',\n",
       " 'healthexp',\n",
       " 'iris',\n",
       " 'mpg',\n",
       " 'penguins',\n",
       " 'planets',\n",
       " 'seaice',\n",
       " 'taxis',\n",
       " 'tips',\n",
       " 'titanic']"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Different types of data sets available in Seaborn library\n",
    "\n",
    "import seaborn as sns\n",
    "sns.get_dataset_names()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d7207fa6-d81f-4a3c-8dcd-a6c6fba51d5a",
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
       "      <th>total_bill</th>\n",
       "      <th>tip</th>\n",
       "      <th>sex</th>\n",
       "      <th>smoker</th>\n",
       "      <th>day</th>\n",
       "      <th>time</th>\n",
       "      <th>size</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>16.99</td>\n",
       "      <td>1.01</td>\n",
       "      <td>Female</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10.34</td>\n",
       "      <td>1.66</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>21.01</td>\n",
       "      <td>3.50</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>23.68</td>\n",
       "      <td>3.31</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>24.59</td>\n",
       "      <td>3.61</td>\n",
       "      <td>Female</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   total_bill   tip     sex smoker  day    time  size\n",
       "0       16.99  1.01  Female     No  Sun  Dinner     2\n",
       "1       10.34  1.66    Male     No  Sun  Dinner     3\n",
       "2       21.01  3.50    Male     No  Sun  Dinner     3\n",
       "3       23.68  3.31    Male     No  Sun  Dinner     2\n",
       "4       24.59  3.61  Female     No  Sun  Dinner     4"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tips = sns.load_dataset('tips')\n",
    "tips.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0cda12b2-f54c-485e-937a-c6bd18def4a6",
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
       "      <th>pickup</th>\n",
       "      <th>dropoff</th>\n",
       "      <th>passengers</th>\n",
       "      <th>distance</th>\n",
       "      <th>fare</th>\n",
       "      <th>tip</th>\n",
       "      <th>tolls</th>\n",
       "      <th>total</th>\n",
       "      <th>color</th>\n",
       "      <th>payment</th>\n",
       "      <th>pickup_zone</th>\n",
       "      <th>dropoff_zone</th>\n",
       "      <th>pickup_borough</th>\n",
       "      <th>dropoff_borough</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2019-03-23 20:21:09</td>\n",
       "      <td>2019-03-23 20:27:24</td>\n",
       "      <td>1</td>\n",
       "      <td>1.60</td>\n",
       "      <td>7.0</td>\n",
       "      <td>2.15</td>\n",
       "      <td>0.0</td>\n",
       "      <td>12.95</td>\n",
       "      <td>yellow</td>\n",
       "      <td>credit card</td>\n",
       "      <td>Lenox Hill West</td>\n",
       "      <td>UN/Turtle Bay South</td>\n",
       "      <td>Manhattan</td>\n",
       "      <td>Manhattan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2019-03-04 16:11:55</td>\n",
       "      <td>2019-03-04 16:19:00</td>\n",
       "      <td>1</td>\n",
       "      <td>0.79</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>9.30</td>\n",
       "      <td>yellow</td>\n",
       "      <td>cash</td>\n",
       "      <td>Upper West Side South</td>\n",
       "      <td>Upper West Side South</td>\n",
       "      <td>Manhattan</td>\n",
       "      <td>Manhattan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2019-03-27 17:53:01</td>\n",
       "      <td>2019-03-27 18:00:25</td>\n",
       "      <td>1</td>\n",
       "      <td>1.37</td>\n",
       "      <td>7.5</td>\n",
       "      <td>2.36</td>\n",
       "      <td>0.0</td>\n",
       "      <td>14.16</td>\n",
       "      <td>yellow</td>\n",
       "      <td>credit card</td>\n",
       "      <td>Alphabet City</td>\n",
       "      <td>West Village</td>\n",
       "      <td>Manhattan</td>\n",
       "      <td>Manhattan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2019-03-10 01:23:59</td>\n",
       "      <td>2019-03-10 01:49:51</td>\n",
       "      <td>1</td>\n",
       "      <td>7.70</td>\n",
       "      <td>27.0</td>\n",
       "      <td>6.15</td>\n",
       "      <td>0.0</td>\n",
       "      <td>36.95</td>\n",
       "      <td>yellow</td>\n",
       "      <td>credit card</td>\n",
       "      <td>Hudson Sq</td>\n",
       "      <td>Yorkville West</td>\n",
       "      <td>Manhattan</td>\n",
       "      <td>Manhattan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2019-03-30 13:27:42</td>\n",
       "      <td>2019-03-30 13:37:14</td>\n",
       "      <td>3</td>\n",
       "      <td>2.16</td>\n",
       "      <td>9.0</td>\n",
       "      <td>1.10</td>\n",
       "      <td>0.0</td>\n",
       "      <td>13.40</td>\n",
       "      <td>yellow</td>\n",
       "      <td>credit card</td>\n",
       "      <td>Midtown East</td>\n",
       "      <td>Yorkville West</td>\n",
       "      <td>Manhattan</td>\n",
       "      <td>Manhattan</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               pickup             dropoff  passengers  distance  fare   tip  \\\n",
       "0 2019-03-23 20:21:09 2019-03-23 20:27:24           1      1.60   7.0  2.15   \n",
       "1 2019-03-04 16:11:55 2019-03-04 16:19:00           1      0.79   5.0  0.00   \n",
       "2 2019-03-27 17:53:01 2019-03-27 18:00:25           1      1.37   7.5  2.36   \n",
       "3 2019-03-10 01:23:59 2019-03-10 01:49:51           1      7.70  27.0  6.15   \n",
       "4 2019-03-30 13:27:42 2019-03-30 13:37:14           3      2.16   9.0  1.10   \n",
       "\n",
       "   tolls  total   color      payment            pickup_zone  \\\n",
       "0    0.0  12.95  yellow  credit card        Lenox Hill West   \n",
       "1    0.0   9.30  yellow         cash  Upper West Side South   \n",
       "2    0.0  14.16  yellow  credit card          Alphabet City   \n",
       "3    0.0  36.95  yellow  credit card              Hudson Sq   \n",
       "4    0.0  13.40  yellow  credit card           Midtown East   \n",
       "\n",
       "            dropoff_zone pickup_borough dropoff_borough  \n",
       "0    UN/Turtle Bay South      Manhattan       Manhattan  \n",
       "1  Upper West Side South      Manhattan       Manhattan  \n",
       "2           West Village      Manhattan       Manhattan  \n",
       "3         Yorkville West      Manhattan       Manhattan  \n",
       "4         Yorkville West      Manhattan       Manhattan  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "taxis = sns.load_dataset('taxis')\n",
    "taxis.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b800c62b-55af-4617-aaf4-5457cc76c8ff",
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
       "      <th>sepal_length</th>\n",
       "      <th>sepal_width</th>\n",
       "      <th>petal_length</th>\n",
       "      <th>petal_width</th>\n",
       "      <th>species</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   sepal_length  sepal_width  petal_length  petal_width species\n",
       "0           5.1          3.5           1.4          0.2  setosa\n",
       "1           4.9          3.0           1.4          0.2  setosa\n",
       "2           4.7          3.2           1.3          0.2  setosa\n",
       "3           4.6          3.1           1.5          0.2  setosa\n",
       "4           5.0          3.6           1.4          0.2  setosa"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = sns.load_dataset('iris')\n",
    "a.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2d43acd5-bf8d-4da0-8552-1f3c9493d092",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Simple Linear Regression Model\n",
    "# Y = mX + c This is the straight line formula \n",
    "#Y is the response variable \n",
    "# X is the predictor , here its TV column \n",
    "# C is the intercept \n",
    "# m is the co-effiecient for X\n",
    "\n",
    "# Y(Sales) = C + m * TV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e9eb7e0d-9f26-4b3d-a82f-9971cc86eb25",
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
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>230.1</td>\n",
       "      <td>37.8</td>\n",
       "      <td>69.2</td>\n",
       "      <td>22.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>44.5</td>\n",
       "      <td>39.3</td>\n",
       "      <td>45.1</td>\n",
       "      <td>10.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>17.2</td>\n",
       "      <td>45.9</td>\n",
       "      <td>69.3</td>\n",
       "      <td>12.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>151.5</td>\n",
       "      <td>41.3</td>\n",
       "      <td>58.5</td>\n",
       "      <td>16.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>180.8</td>\n",
       "      <td>10.8</td>\n",
       "      <td>58.4</td>\n",
       "      <td>17.9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      TV  Radio  Newspaper  Sales\n",
       "0  230.1   37.8       69.2   22.1\n",
       "1   44.5   39.3       45.1   10.4\n",
       "2   17.2   45.9       69.3   12.0\n",
       "3  151.5   41.3       58.5   16.5\n",
       "4  180.8   10.8       58.4   17.9"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np, pandas as pd\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "advertising = pd.read_csv(\"advertising.csv\")\n",
    "advertising.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "00e9b044-0dc5-4b6d-b123-395b91a25d9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 200 entries, 0 to 199\n",
      "Data columns (total 4 columns):\n",
      " #   Column     Non-Null Count  Dtype  \n",
      "---  ------     --------------  -----  \n",
      " 0   TV         200 non-null    float64\n",
      " 1   Radio      200 non-null    float64\n",
      " 2   Newspaper  200 non-null    float64\n",
      " 3   Sales      200 non-null    float64\n",
      "dtypes: float64(4)\n",
      "memory usage: 6.4 KB\n"
     ]
    }
   ],
   "source": [
    "advertising.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1998ea46-b062-443d-a890-9104b3c77407",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "TV           0\n",
       "Radio        0\n",
       "Newspaper    0\n",
       "Sales        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "advertising.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0910c968-3fe8-43ff-abbf-7f3815989e31",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(200, 4)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "advertising.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "62e25575-3261-4c69-a006-60823e86bb3f",
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
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>200.000000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>200.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>147.042500</td>\n",
       "      <td>23.264000</td>\n",
       "      <td>30.554000</td>\n",
       "      <td>15.130500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>85.854236</td>\n",
       "      <td>14.846809</td>\n",
       "      <td>21.778621</td>\n",
       "      <td>5.283892</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.700000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.300000</td>\n",
       "      <td>1.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>74.375000</td>\n",
       "      <td>9.975000</td>\n",
       "      <td>12.750000</td>\n",
       "      <td>11.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>149.750000</td>\n",
       "      <td>22.900000</td>\n",
       "      <td>25.750000</td>\n",
       "      <td>16.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>218.825000</td>\n",
       "      <td>36.525000</td>\n",
       "      <td>45.100000</td>\n",
       "      <td>19.050000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>296.400000</td>\n",
       "      <td>49.600000</td>\n",
       "      <td>114.000000</td>\n",
       "      <td>27.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               TV       Radio   Newspaper       Sales\n",
       "count  200.000000  200.000000  200.000000  200.000000\n",
       "mean   147.042500   23.264000   30.554000   15.130500\n",
       "std     85.854236   14.846809   21.778621    5.283892\n",
       "min      0.700000    0.000000    0.300000    1.600000\n",
       "25%     74.375000    9.975000   12.750000   11.000000\n",
       "50%    149.750000   22.900000   25.750000   16.000000\n",
       "75%    218.825000   36.525000   45.100000   19.050000\n",
       "max    296.400000   49.600000  114.000000   27.000000"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "advertising.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "505e602d-cfc3-4675-b422-4d7c9f8effa7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABJ4AAAGOCAYAAADW/cnWAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAACvGElEQVR4nOzdeXxU9b0//le2STIJWUgMhAohMqGKLMaitiSAQt21qFxvpe0tEG5vWwW13FvXolgVtIvfXtzuba8g/d0WbUVxqV1cKhK4tQWjLG4EI6CAMSEzIZlkJsv5/YFnmOWcM2fOnH1ez8fDx0My2+csn/fncz5rliAIAoiIiIiIiIiIiHSWbXUCiIiIiIiIiIjIndjwREREREREREREhmDDExERERERERERGYINT0REREREREREZAg2PBERERERERERkSHY8ERERERERERERIZgwxMRERERERERERmCDU9ERERERERERGQI1zc8CYKA7u5uCIJgdVKIiEhHjO9ERO7E+E5E5C6ub3g6duwYSktLcezYMauTQkREOmJ8JyJyJ8Z3IiJ3cX3DExERERERERERWYMNT0REREREREREZAg2PBERERERERERkSHY8ERERERERERERIZgwxMRERERERERERmCDU9ERERERERERGQINjwREREREREREZEh2PBERERERERERESGYMMTEREREREREREZgg1PRERERERERERkiFyrE0BEROYIBMPo6Amju38AJYV5qCzyoNTrsTpZRERkAywjyCl4rxI5DxueiIgywCF/H27euBNb9nZE/jarrhL3zZ+KMWWFFqaMiIisxjKCnIL3KpEzcaodEZHLBYLhhEoaALy+twO3bNyJQDBsUcqIiMhqLCPIKXivEjkXG56IiFyuoyecUEkTvb63Ax09rKgREWUqlhHkFLxXiZyLDU9ERC7X3T+g+PqxJK8TEZF7sYwgp+C9SuRcbHgiInK5koI8xddHJHmdiIjci2UEOQXvVSLnYsMTEZHLVRZ7MKuuUvK1WXWVqCzmTjBERJmKZQQ5Be9VIudiwxMRkcuVej24b/7UhMrarLpK3D9/KrcgJiLKYCwjyCl4rxI5V5YgCILViTBSd3c3SktLEQgEUFJSYnVyiIgsEwiG0dETxrH+AYwoyENlscfRlTTGdyIi/dipjGB8JyV2uleJSJ1cqxNA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vVgOEpHbMc4RERmHDU8qdPcPKL5+LMnrRERETsZykIjcjnGOiMg4bHhSoaQgT/H1EUleJyIicjKWg0TkdoxzRETGYcOTCpXFHsyqq5R8bVZdJSqLudMFERG5F8tBInI7xjkiIuOw4UmFUq8H982fmlAYzaqrxP3zp3KLVSIicjWWg0TkdoxzRETGyRIEQbA6EUbq7u5GaWkpAoEASkpK0vquQDCMjp4wjvUPYERBHiqLPSyEiIgsomd8J3VYDhKRGayM74xzRET6y7U6AU5S6mXBQ0REmYvlIBG5HeMcEZH+ONWOiIiIiIiIiIgMwYYnIiIiIiIiIiIyBBueiIiIiIiIiIjIEGx4IiIiIiIiIiIiQ7DhiYiIiIiIiIiIDMGGJyIiIiIiIiIiMgQbnoiIiIiIiIiIyBBseCIiIiIiIiIiIkOw4YmIiIiIiIiIiAzBhiciIiIiIiIiIjJErtUJsLtAMIyOnjC6+wdQUpiHyiIPSr0eq5NFRERERAZg3Y+S4T1CRJQaNjwpOOTvw80bd2LL3o7I32bVVeK++VMxpqzQwpQRERERkd5Y96NkeI8QEaWOU+1kBILhhEIFAF7f24FbNu5EIBi2KGVEREREpDfW/SgZ3iNERNqw4UlGR084oVARvb63Ax09LFiIiIiI3IJ1P0qG9wgRkTZseJLR3T+g+PqxJK8TERERkXOw7kfJ8B4hItKGDU8ySgryFF8fkeR1IiIiInIO1v0oGd4jRETasOFJRmWxB7PqKiVfm1VXicpi7lxBRERE5Bas+1EyvEeIiLRhw5OMUq8H982fmlC4zKqrxP3zp3LLVCIiIiIXYd2PkuE9QkSkTZYgCILViTBSd3c3SktLEQgEUFJSkvLnA8EwOnrCONY/gBEFeags9rBQISKygXTjOxGRFNb9rGf3+M57hIgoNblWJ8DuSr0sSIiIiIgyBet+lAzvESKi1HCqHRERERERERERGYINT0REREREREREZAg2PBERERERERERkSHY8ERERERERERERIZgwxMRERERERERERmCDU9ERERERERERGQINjwREREREREREZEh2PBERERERERERESGyLU6AUYTBAEA0N3dbXFKiIgomREjRiArK0vVexnfiYicg/GdiMid1MR31zc8HTt2DAAwduxYi1NCRETJBAIBlJSUqHov4zsRkXMwvhMRuZOa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L7448v9TpkzBV77yFUyYMAHr16+PLGzslmMVaTkeJxzz17/+9cj/T548GdOnT0dNTQ3+8Ic/4KqrrpL9nB2PbenSpdi5cyeam5sTXnP69ZM7Nqdfvy9+8Yt466234Pf7sXHjRixcuBCbN2+OvO606+a2uKeXTDsvescipzEiXzvNwYMHccMNN+Avf/kLCgoKZN+XCefCDXVGu6cvHW6OV5mSD4eHhzF9+nSsWrUKAFBfX489e/bg0Ucfxbe//e3I+5x+nE8++ST+93//F7/97W9x+umn46233sKNN96IMWPGYOHChZH3Of04pTitPmwWTrWTUFlZiZycnIRWx/b29oQWTCcqKirClClTsHfv3shOJW45VjXHM3r0aITDYXR1dcm+xymqq6tRU1ODvXv3AnDOsS1btgzPPfcc/vrXv+Lkk0+O/N0N10/u2KQ47fp5PB74fD5Mnz4dq1evxrRp0/Cf//mfjrtubo/xWrmtPFAjnVjkFunka7fYsWMH2tvb8aUvfQm5ubnIzc3F5s2bsWbNGuTm5kaONxPORTwn1RndHtvdHq8yJR9WV1dj0qRJMX877bTTcODAAQDuuZ4//OEPccstt+Caa67BlClT8C//8i/4wQ9+gNWrVwNwz3FGc1p92GxseJLg8XjwpS99CS+99FLM31966SXMmDHDolTpJxQK4d1330V1dTVqa2sxevTomGMNh8PYvHmzI49VzfF86UtfQl5eXsx7Dh8+jN27dzvumDs7O3Hw4EFUV1cDsP+xCYKApUuX4umnn8arr76K2tramNedfP2SHZsUp12/eIIgIBQKOe66uT3Ga+W28kCJHrHIrVLJ124xd+5c7Nq1C2+99Vbkv+nTp+Ob3/wm3nrrLZxyyikZcy7iOanO6NbYninxKlPyYUNDA95///2Yv33wwQeoqakB4J7rGQwGkZ0d29SQk5OD4eFhAO45zmhOqw+bzvDlyx1K3I71scceE9555x3hxhtvFIqKioSPPvrI6qSl7N///d+F1157Tfjwww+Fv/3tb8Jll10mjBgxInIs9913n1BaWio8/fTTwq5du4QFCxbYeivLY8eOCS0tLUJLS4sAQHjggQeElpaWyFa5ao7ne9/7nnDyyScLL7/8svDmm28Kc+bMscU2lkrHduzYMeHf//3fhW3btgltbW3CX//6V+ErX/mK8IUvfMERxyYIgvD9739fKC0tFV577bWYrZqDwWDkPU69fsmOzenX79ZbbxVef/11oa2tTdi5c6dw2223CdnZ2cJf/vIXQRCcd93cFONToUf8dAO9YpHT6ZGv3Sp6Ny1ByJxz4fQ6oxtjeybHKzfmw7///e9Cbm6ucO+99wp79+4VfvOb3wher1f43//938h73HCcCxcuFL7whS8IL7zwgtDW1iY8/fTTQmVlpXDTTTdF3uPE43Tzc6jR2PCk4OGHHxZqamoEj8cjnHnmmTHbojvJ17/+daG6ulrIy8sTxowZI1x11VXCnj17Iq8PDw8Ld955pzB69GghPz9fmDVrlrBr1y4LU6zsr3/9qwAg4b+FCxcKgqDuePr6+oSlS5cKI0eOFAoLC4XLLrtMOHDggAVHE0vp2ILBoHDBBRcIJ510kpCXlyeMGzdOWLhwYUK67XpsgiBIHhsAYd26dZH3OPX6JTs2p1+/pqamSDw86aSThLlz50YeTgXBmdfNLTE+FXrETzfQKxY5nR752q3iH3gz5Vy4oc7ottieyfHKrfnw+eefFyZPnizk5+cLp556qvDLX/4y5nU3HGd3d7dwww03COPGjRMKCgqEU045Rbj99tuFUCgUeY8Tj9PNz6FGyxIEQdB/HBUREREREREREWU6rvFERERERERERESGYMMTEREREREREREZgg1PRERERERERERkCDY8ERERERERERGRIdjwREREREREREREhmDDExERERERERERGYINT0REREREREREZAg2PBERERHZ1KJFi3DFFVdE/n3uuefixhtvtCw9RERERKliwxORzWRlZSn+d/HFFyMvLw//+7//K/n57373u5g6darJqSYiymyLFi2KxOnc3FyMGzcO3//+99HV1aXr7zz99NO4++67df1OIiK3EWPyfffdF/P3TZs2ISsry6JUEWUuNjwR2czhw4cj//3iF79ASUlJzN+eeOIJXHrppVi3bl3CZ/v6+vDEE09gyZIlFqSciCizXXTRRTh8+DA++ugj/M///A+ef/55XHvttbr+xsiRIzFixAhdv5OIyI0KCgpw//33694B4DYDAwNWJ4EyABueiGxm9OjRkf9KS0uRlZWV8LclS5bgr3/9Kz766KOYzz711FPo7+/Ht771LWsST0SUwfLz8zF69GicfPLJuOCCC/D1r38df/nLXwAAQ0ND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",
      "text/plain": [
       "<Figure size 1200x400 with 3 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt, seaborn as sns\n",
    "sns.pairplot(advertising, x_vars = ['TV','Radio','Newspaper'], y_vars = ['Sales'],kind = 'scatter',size = 4 )\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "af811b88-ddc3-43f5-9527-42642d279938",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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fIiri0o9A6mpqXB2dgaQPz/gzVLCNm3a4MwZ5VvzEhERUdmlUjLg4uKCBw8eAADc3Nywa9cuAPk9BqampuqKjYiISCMkEi21beWBSlF6e3vjypX8h174+/vL5g5MnToVX3zxhVoDJCIiKn0SNW5ln0pzBqZOnSr7d8eOHRETE4OIiAi4urqiUaNGhexJREREZU2xegYuXryIP/6QX26xefNmtG/fHr6+vvjpp5+UHkBERERU3ohtNUGxkoE5c+bg6tWrstfXrl2Dj48PunTpAn9/fxw4cABBQUFqD5KIiKg0MRkoRFRUFDp37ix7vWPHDjRv3hy//PILpk6dimXLlskmExIREVH5UKw5A2lpabCxsZG9Pn36NLp3//cRox988AHi4+PVFx0REZFGlI9VAOpSrNba2NggNjYWAJCdnY3Lly+jZcuWsvefP38OXV1d9UZIRERUyiQSidq28qBYyUD37t0xc+ZMhIWFwd/fH5UrV0bbtm1l71+9ehWurq5qD5KIiKh0cWnhO33zzTf4+OOP0b59exgZGWHTpk3Q09OTvb9+/Xp069ZN7UESERFRySlWMmBlZYWwsDCkp6fDyMgI2tracu/v3r0bRkZGag2QiIiotJWXVQDqotJNh0xMTAosNzc3f69giIiIygZOICQiIiIRUalngIiIqCLjMAEREZHIlZclgerCYQIiIiKRY88AERGREnH1DDAZICIiUiARWce5uFpLREREStgzQEREpITDBERERKImttUETAaIiIiUiCsZ4JwBIiIikWPPABERkQKxrSZgMkBERKSEwwREREQkIuwZICIiUsAHFREREYmc2JYWcpiAiIhI5NgzQEREpERc35WZDBARESkQ25wBcaU+REREpIQ9A0RERErE1TPAZICIiEiB2FYTMBkgIiJSIq5RdHG1loiIiJSwZ4CIiEiB2FYTSARBEDQdREWQlZWFoKAg+Pv7Q19fX9PhiB6vR9nBa1F28FrQuzAZUJOMjAyYmJggPT0dxsbGmg5H9Hg9yg5ei7KD14LehXMGiIiIRI7JABERkcgxGSAiIhI5JgNqoq+vj4CAAE7KKSN4PcoOXouyg9eC3oUTCImIiESOPQNEREQix2SAiIhI5JgMEBERiRyTASIiIpFjMkCi4OXlhb59+8ped+jQAVOmTNFYPESasHHjRpiammo6DCqDmAwU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",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(advertising.corr(),cmap = \"YlGnBu\", annot = True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "230c5cfc-9237-42f6-b958-7510594996e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = advertising['TV']\n",
    "y = advertising['Sales']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "cb8f3bd7-b41e-482d-9f57-6ed4ae292209",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "import statsmodels.api as sm "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "85ba40c0-c4a5-46cd-aaa5-0b6555cd4ba8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#pip install scikit-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "a4e640af-e9dd-4f03-81bd-cb908c374c51",
   "metadata": {},
   "outputs": [],
   "source": [
    "#pip install statsmodels"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "02b05f53-71aa-4d8d-ac00-e7fd38bbd9ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.2, train_size = 0.8, random_state= 42)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "d59c3877-77d7-42a7-ac29-178782389e98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "79     116.0\n",
       "197    177.0\n",
       "38      43.1\n",
       "24      62.3\n",
       "122    224.0\n",
       "Name: TV, dtype: float64"
      ]
     },
     "execution_count": 59,
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
   "execution_count": 61,
   "id": "adafa306-5de0-440a-849d-35049d9c370a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "79     11.0\n",
       "197    14.8\n",
       "38     10.1\n",
       "24      9.7\n",
       "122    16.6\n",
       "Name: Sales, dtype: float64"
      ]
     },
     "execution_count": 61,
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
   "execution_count": 63,
   "id": "ae651d82-7ece-46c4-8a75-d260f74c9ed5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((160,), (160,), (40,), (40,))"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.shape, y_train.shape, X_test.shape, y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "7499f098-fccc-40ea-bbfb-9b742b56fe8a",
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
       "      <th>const</th>\n",
       "      <th>TV</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>79</th>\n",
       "      <td>1.0</td>\n",
       "      <td>116.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>197</th>\n",
       "      <td>1.0</td>\n",
       "      <td>177.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>1.0</td>\n",
       "      <td>43.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>1.0</td>\n",
       "      <td>62.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122</th>\n",
       "      <td>1.0</td>\n",
       "      <td>224.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>106</th>\n",
       "      <td>1.0</td>\n",
       "      <td>25.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>1.0</td>\n",
       "      <td>204.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>92</th>\n",
       "      <td>1.0</td>\n",
       "      <td>217.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>179</th>\n",
       "      <td>1.0</td>\n",
       "      <td>165.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>102</th>\n",
       "      <td>1.0</td>\n",
       "      <td>280.2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>160 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     const     TV\n",
       "79     1.0  116.0\n",
       "197    1.0  177.0\n",
       "38     1.0   43.1\n",
       "24     1.0   62.3\n",
       "122    1.0  224.0\n",
       "..     ...    ...\n",
       "106    1.0   25.0\n",
       "14     1.0  204.1\n",
       "92     1.0  217.7\n",
       "179    1.0  165.6\n",
       "102    1.0  280.2\n",
       "\n",
       "[160 rows x 2 columns]"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train_sm = sm.add_constant(X_train)\n",
    "X_train_sm # C term is added , where it touches the y-axis at 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "4c33447c-6479-4b75-a898-512d89b8fc31",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "const    7.007108\n",
       "TV       0.055483\n",
       "dtype: float64"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# For linear reg you will Ordinary Least Squares Method \n",
    "\n",
    "lr = sm.OLS(y_train, X_train_sm).fit()\n",
    "lr.params # you have got the m's or the co-effcients"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "deee1508-b300-4b68-b4e8-0023855bf0a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                            OLS Regression Results                            \n",
      "==============================================================================\n",
      "Dep. Variable:                  Sales   R-squared:                       0.813\n",
      "Model:                            OLS   Adj. R-squared:                  0.812\n",
      "Method:                 Least Squares   F-statistic:                     689.1\n",
      "Date:                Tue, 01 Oct 2024   Prob (F-statistic):           1.71e-59\n",
      "Time:                        03:44:39   Log-Likelihood:                -355.76\n",
      "No. Observations:                 160   AIC:                             715.5\n",
      "Df Residuals:                     158   BIC:                             721.7\n",
      "Df Model:                           1                                         \n",
      "Covariance Type:            nonrobust                                         \n",
      "==============================================================================\n",
      "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
      "------------------------------------------------------------------------------\n",
      "const          7.0071      0.364     19.274      0.000       6.289       7.725\n",
      "TV             0.0555      0.002     26.251      0.000       0.051       0.060\n",
      "==============================================================================\n",
      "Omnibus:                        0.631   Durbin-Watson:                   2.262\n",
      "Prob(Omnibus):                  0.730   Jarque-Bera (JB):                0.767\n",
      "Skew:                          -0.110   Prob(JB):                        0.681\n",
      "Kurtosis:                       2.742   Cond. No.                         352.\n",
      "==============================================================================\n",
      "\n",
      "Notes:\n",
      "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n"
     ]
    }
   ],
   "source": [
    "print(lr.summary())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5472b3fd-d00f-4826-8298-ed611ea9d3be",
   "metadata": {},
   "source": [
    "####  Looking at some key statistics from the summary\n",
    "The values we are concerned with are -\n",
    "1. The coefficients and significance (p-values)\n",
    "2. R-squared\n",
    "3. F statistic and its significance\n",
    "\n",
    "##### 1. The coefficient for TV is 0.0555, with a very low p value\n",
    "The coefficient is statistically significant. So the association is not purely by chance.\n",
    "\n",
    "##### 2. R - squared is 0.813\n",
    "Meaning that 81.3% of the variance in `Sales` is explained by `TV`\n",
    "\n",
    "This is a decent R-squared value.\n",
    "\n",
    "###### 3. F statistic has a very low p value (practically low)\n",
    "Meaning that the model fit is statistically significant, and the explained variance isn't purely by chance.\n",
    "\n",
    "\n",
    "---\n",
    "The fit is significant. Let's visualize how well the model fit the data.\n",
    "\n",
    "From the parameters that we get, our linear regression equation becomes:\n",
    "\n",
    "Sales = 7.0071 + 0.0555 * TV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "2c0ac0cc-6cb5-4fa8-9406-4eb38ed97813",
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
    "# Sales = 7.0071 + 0.0555 * TV\n",
    "\n",
    "plt.scatter(X_train, y_train)\n",
    "plt.plot(X_train,7.0071 + 0.0555 * X_train,'r')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9df14cb8-1fd3-47ba-8955-8da373db4f41",
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