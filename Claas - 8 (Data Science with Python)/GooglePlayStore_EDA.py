{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4cd53474-cfa4-411d-a6c8-184f9fa4d008",
   "metadata": {},
   "source": [
    "### Exploratory Data Analysis \n",
    "\n",
    "1. Import the necessary libraries\n",
    "2. read the files (CSv or Excel)\n",
    "3. Data inspection\n",
    "4. check for null values in the rows\n",
    "5. Data handling and cleaning \n",
    "6. describe function\n",
    "7. check for inconsistencies in your data (missing vales, NAN, incorrect spellings in the rows)\n",
    "8. Impute these inconsistencies (missing data or NAN values , replace it with mean, median or mode statistics)\n",
    "9. Visualize the data , check for outliers in each columns\n",
    "10. Inferences in for the data (on your understanding of the data set) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0076a376-fafc-4903-a365-2621fedbcc71",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing necessary library \n",
    "import numpy as np, pandas as pd\n",
    "import seaborn as sns, matplotlib.pyplot as plt\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "157b501f-b0f5-4aa9-89c9-f8620f2f3a6b",
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
       "      <th>App</th>\n",
       "      <th>Category</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Reviews</th>\n",
       "      <th>Size</th>\n",
       "      <th>Installs</th>\n",
       "      <th>Type</th>\n",
       "      <th>Price</th>\n",
       "      <th>Content Rating</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Last Updated</th>\n",
       "      <th>Current Ver</th>\n",
       "      <th>Android Ver</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Photo Editor &amp; Candy Camera &amp; Grid &amp; ScrapBook</td>\n",
       "      <td>ART_AND_DESIGN</td>\n",
       "      <td>4.1</td>\n",
       "      <td>159</td>\n",
       "      <td>19000.0</td>\n",
       "      <td>10,000+</td>\n",
       "      <td>Free</td>\n",
       "      <td>0</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Art &amp; Design</td>\n",
       "      <td>January 7, 2018</td>\n",
       "      <td>1.0.0</td>\n",
       "      <td>4.0.3 and up</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Coloring book moana</td>\n",
       "      <td>ART_AND_DESIGN</td>\n",
       "      <td>3.9</td>\n",
       "      <td>967</td>\n",
       "      <td>14000.0</td>\n",
       "      <td>500,000+</td>\n",
       "      <td>Free</td>\n",
       "      <td>0</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Art &amp; Design;Pretend Play</td>\n",
       "      <td>January 15, 2018</td>\n",
       "      <td>2.0.0</td>\n",
       "      <td>4.0.3 and up</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>U Launcher Lite – FREE Live Cool Themes, Hide ...</td>\n",
       "      <td>ART_AND_DESIGN</td>\n",
       "      <td>4.7</td>\n",
       "      <td>87510</td>\n",
       "      <td>8700.0</td>\n",
       "      <td>5,000,000+</td>\n",
       "      <td>Free</td>\n",
       "      <td>0</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Art &amp; Design</td>\n",
       "      <td>August 1, 2018</td>\n",
       "      <td>1.2.4</td>\n",
       "      <td>4.0.3 and up</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Sketch - Draw &amp; Paint</td>\n",
       "      <td>ART_AND_DESIGN</td>\n",
       "      <td>4.5</td>\n",
       "      <td>215644</td>\n",
       "      <td>25000.0</td>\n",
       "      <td>50,000,000+</td>\n",
       "      <td>Free</td>\n",
       "      <td>0</td>\n",
       "      <td>Teen</td>\n",
       "      <td>Art &amp; Design</td>\n",
       "      <td>June 8, 2018</td>\n",
       "      <td>Varies with device</td>\n",
       "      <td>4.2 and up</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Pixel Draw - Number Art Coloring Book</td>\n",
       "      <td>ART_AND_DESIGN</td>\n",
       "      <td>4.3</td>\n",
       "      <td>967</td>\n",
       "      <td>2800.0</td>\n",
       "      <td>100,000+</td>\n",
       "      <td>Free</td>\n",
       "      <td>0</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Art &amp; Design;Creativity</td>\n",
       "      <td>June 20, 2018</td>\n",
       "      <td>1.1</td>\n",
       "      <td>4.4 and up</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                 App        Category  Rating  \\\n",
       "0     Photo Editor & Candy Camera & Grid & ScrapBook  ART_AND_DESIGN     4.1   \n",
       "1                                Coloring book moana  ART_AND_DESIGN     3.9   \n",
       "2  U Launcher Lite – FREE Live Cool Themes, Hide ...  ART_AND_DESIGN     4.7   \n",
       "3                              Sketch - Draw & Paint  ART_AND_DESIGN     4.5   \n",
       "4              Pixel Draw - Number Art Coloring Book  ART_AND_DESIGN     4.3   \n",
       "\n",
       "  Reviews     Size     Installs  Type Price Content Rating  \\\n",
       "0     159  19000.0      10,000+  Free     0       Everyone   \n",
       "1     967  14000.0     500,000+  Free     0       Everyone   \n",
       "2   87510   8700.0   5,000,000+  Free     0       Everyone   \n",
       "3  215644  25000.0  50,000,000+  Free     0           Teen   \n",
       "4     967   2800.0     100,000+  Free     0       Everyone   \n",
       "\n",
       "                      Genres      Last Updated         Current Ver  \\\n",
       "0               Art & Design   January 7, 2018               1.0.0   \n",
       "1  Art & Design;Pretend Play  January 15, 2018               2.0.0   \n",
       "2               Art & Design    August 1, 2018               1.2.4   \n",
       "3               Art & Design      June 8, 2018  Varies with device   \n",
       "4    Art & Design;Creativity     June 20, 2018                 1.1   \n",
       "\n",
       "    Android Ver  \n",
       "0  4.0.3 and up  \n",
       "1  4.0.3 and up  \n",
       "2  4.0.3 and up  \n",
       "3    4.2 and up  \n",
       "4    4.4 and up  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reading the csv file\n",
    "data = pd.read_csv(\"googleplaystore_v2.csv\")\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d39d9d56-16ae-410e-b598-61ef7ff6fd34",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10841, 13)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# data inspection \n",
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4db9c574-1adc-4b78-bd11-02071c727a78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "App                  0\n",
       "Category             0\n",
       "Rating            1474\n",
       "Reviews              0\n",
       "Size                 0\n",
       "Installs             0\n",
       "Type                 1\n",
       "Price                0\n",
       "Content Rating       1\n",
       "Genres               0\n",
       "Last Updated         0\n",
       "Current Ver          8\n",
       "Android Ver          3\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# checking the rows for null values \n",
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a719e73-d1ed-4502-8c42-e495e819fa88",
   "metadata": {},
   "source": [
    "# Data handling and cleaning \n",
    "For missing values we can do the following \n",
    "\n",
    "1. dropping them\n",
    "2. imputing them with statistical values\n",
    "3. keep them as zeroes\n",
    "\n",
    "Incorrect data \n",
    "1. Clean them with correct values \n",
    "2. clean and convert the entire columns "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "88b58387-abc0-4d7c-9cd5-c5dbbb840f8c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 10841 entries, 0 to 10840\n",
      "Data columns (total 13 columns):\n",
      " #   Column          Non-Null Count  Dtype  \n",
      "---  ------          --------------  -----  \n",
      " 0   App             10841 non-null  object \n",
      " 1   Category        10841 non-null  object \n",
      " 2   Rating          9367 non-null   float64\n",
      " 3   Reviews         10841 non-null  object \n",
      " 4   Size            10841 non-null  float64\n",
      " 5   Installs        10841 non-null  object \n",
      " 6   Type            10840 non-null  object \n",
      " 7   Price           10841 non-null  object \n",
      " 8   Content Rating  10840 non-null  object \n",
      " 9   Genres          10841 non-null  object \n",
      " 10  Last Updated    10841 non-null  object \n",
      " 11  Current Ver     10833 non-null  object \n",
      " 12  Android Ver     10838 non-null  object \n",
      "dtypes: float64(2), object(11)\n",
      "memory usage: 1.1+ MB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f63952d3-eddb-48d1-ba8d-a9d41150bdf9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(9367, 13)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Since Rating column has lot of missing values i will delete those rows \n",
    "data = data[-data.Rating.isnull()]\n",
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "efb77a48-740a-4820-9fbb-a6de9014abce",
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
       "      <th>App</th>\n",
       "      <th>Category</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Reviews</th>\n",
       "      <th>Size</th>\n",
       "      <th>Installs</th>\n",
       "      <th>Type</th>\n",
       "      <th>Price</th>\n",
       "      <th>Content Rating</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Last Updated</th>\n",
       "      <th>Current Ver</th>\n",
       "      <th>Android Ver</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4453</th>\n",
       "      <td>[substratum] Vacuum: P</td>\n",
       "      <td>PERSONALIZATION</td>\n",
       "      <td>4.4</td>\n",
       "      <td>230</td>\n",
       "      <td>11000.000000</td>\n",
       "      <td>1,000+</td>\n",
       "      <td>Paid</td>\n",
       "      <td>$1.49</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Personalization</td>\n",
       "      <td>July 20, 2018</td>\n",
       "      <td>4.4</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4490</th>\n",
       "      <td>Pi Dark [substratum]</td>\n",
       "      <td>PERSONALIZATION</td>\n",
       "      <td>4.5</td>\n",
       "      <td>189</td>\n",
       "      <td>2100.000000</td>\n",
       "      <td>10,000+</td>\n",
       "      <td>Free</td>\n",
       "      <td>0</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Personalization</td>\n",
       "      <td>March 27, 2018</td>\n",
       "      <td>1.1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10472</th>\n",
       "      <td>Life Made WI-Fi Touchscreen Photo Frame</td>\n",
       "      <td>1.9</td>\n",
       "      <td>19.0</td>\n",
       "      <td>3.0M</td>\n",
       "      <td>21516.529524</td>\n",
       "      <td>Free</td>\n",
       "      <td>0</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>NaN</td>\n",
       "      <td>February 11, 2018</td>\n",
       "      <td>1.0.19</td>\n",
       "      <td>4.0 and up</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                           App         Category  Rating  \\\n",
       "4453                    [substratum] Vacuum: P  PERSONALIZATION     4.4   \n",
       "4490                      Pi Dark [substratum]  PERSONALIZATION     4.5   \n",
       "10472  Life Made WI-Fi Touchscreen Photo Frame              1.9    19.0   \n",
       "\n",
       "      Reviews          Size Installs  Type     Price Content Rating  \\\n",
       "4453      230  11000.000000   1,000+  Paid     $1.49       Everyone   \n",
       "4490      189   2100.000000  10,000+  Free         0       Everyone   \n",
       "10472    3.0M  21516.529524     Free     0  Everyone            NaN   \n",
       "\n",
       "                  Genres    Last Updated Current Ver Android Ver  \n",
       "4453     Personalization   July 20, 2018         4.4         NaN  \n",
       "4490     Personalization  March 27, 2018         1.1         NaN  \n",
       "10472  February 11, 2018          1.0.19  4.0 and up         NaN  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# fetching the 3 null rows in the \"Android Ver\" column\n",
    "data[data['Android Ver'].isnull()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5442497c-b7ff-4e93-a106-8646b3401f20",
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
       "      <th>App</th>\n",
       "      <th>Category</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Reviews</th>\n",
       "      <th>Size</th>\n",
       "      <th>Installs</th>\n",
       "      <th>Type</th>\n",
       "      <th>Price</th>\n",
       "      <th>Content Rating</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Last Updated</th>\n",
       "      <th>Current Ver</th>\n",
       "      <th>Android Ver</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>10472</th>\n",
       "      <td>Life Made WI-Fi Touchscreen Photo Frame</td>\n",
       "      <td>1.9</td>\n",
       "      <td>19.0</td>\n",
       "      <td>3.0M</td>\n",
       "      <td>21516.529524</td>\n",
       "      <td>Free</td>\n",
       "      <td>0</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>NaN</td>\n",
       "      <td>February 11, 2018</td>\n",
       "      <td>1.0.19</td>\n",
       "      <td>4.0 and up</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                           App Category  Rating Reviews  \\\n",
       "10472  Life Made WI-Fi Touchscreen Photo Frame      1.9    19.0    3.0M   \n",
       "\n",
       "               Size Installs Type     Price Content Rating             Genres  \\\n",
       "10472  21516.529524     Free    0  Everyone            NaN  February 11, 2018   \n",
       "\n",
       "      Last Updated Current Ver Android Ver  \n",
       "10472       1.0.19  4.0 and up         NaN  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 10472 row is having shifted values so will drop this row \n",
    "data.loc[10472,:]\n",
    "data[(data['Android Ver'].isnull() & (data.Category == '1.9'))]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ec17c133-a5a0-40b4-b542-85f23f88f12d",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = data[-(data['Android Ver'].isnull() & (data.Category == '1.9'))]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "5d8f3cee-5853-4e2b-82bb-f3af186460c7",
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
       "      <th>App</th>\n",
       "      <th>Category</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Reviews</th>\n",
       "      <th>Size</th>\n",
       "      <th>Installs</th>\n",
       "      <th>Type</th>\n",
       "      <th>Price</th>\n",
       "      <th>Content Rating</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Last Updated</th>\n",
       "      <th>Current Ver</th>\n",
       "      <th>Android Ver</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4453</th>\n",
       "      <td>[substratum] Vacuum: P</td>\n",
       "      <td>PERSONALIZATION</td>\n",
       "      <td>4.4</td>\n",
       "      <td>230</td>\n",
       "      <td>11000.0</td>\n",
       "      <td>1,000+</td>\n",
       "      <td>Paid</td>\n",
       "      <td>$1.49</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Personalization</td>\n",
       "      <td>July 20, 2018</td>\n",
       "      <td>4.4</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4490</th>\n",
       "      <td>Pi Dark [substratum]</td>\n",
       "      <td>PERSONALIZATION</td>\n",
       "      <td>4.5</td>\n",
       "      <td>189</td>\n",
       "      <td>2100.0</td>\n",
       "      <td>10,000+</td>\n",
       "      <td>Free</td>\n",
       "      <td>0</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Personalization</td>\n",
       "      <td>March 27, 2018</td>\n",
       "      <td>1.1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         App         Category  Rating Reviews     Size  \\\n",
       "4453  [substratum] Vacuum: P  PERSONALIZATION     4.4     230  11000.0   \n",
       "4490    Pi Dark [substratum]  PERSONALIZATION     4.5     189   2100.0   \n",
       "\n",
       "     Installs  Type  Price Content Rating           Genres    Last Updated  \\\n",
       "4453   1,000+  Paid  $1.49       Everyone  Personalization   July 20, 2018   \n",
       "4490  10,000+  Free      0       Everyone  Personalization  March 27, 2018   \n",
       "\n",
       "     Current Ver Android Ver  \n",
       "4453         4.4         NaN  \n",
       "4490         1.1         NaN  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Cross checking if its dropped \n",
    "data[data['Android Ver'].isnull()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "1a8e9ebb-6be8-4ce9-af25-0ae3a9458529",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.1 and up            2059\n",
       "Varies with device    1319\n",
       "4.0.3 and up          1240\n",
       "4.0 and up            1131\n",
       "4.4 and up             875\n",
       "2.3 and up             582\n",
       "5.0 and up             535\n",
       "4.2 and up             338\n",
       "2.3.3 and up           240\n",
       "3.0 and up             211\n",
       "2.2 and up             208\n",
       "4.3 and up             207\n",
       "2.1 and up             113\n",
       "1.6 and up              87\n",
       "6.0 and up              48\n",
       "7.0 and up              41\n",
       "3.2 and up              31\n",
       "2.0 and up              27\n",
       "5.1 and up              18\n",
       "1.5 and up              16\n",
       "3.1 and up               8\n",
       "2.0.1 and up             7\n",
       "4.4W and up              6\n",
       "8.0 and up               5\n",
       "7.1 and up               3\n",
       "4.0.3 - 7.1.1            2\n",
       "5.0 - 8.0                2\n",
       "1.0 and up               2\n",
       "7.0 - 7.1.1              1\n",
       "4.1 - 7.1.1              1\n",
       "5.0 - 6.0                1\n",
       "Name: Android Ver, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"Android Ver\"].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "99d312db-7e4c-4723-bf8e-3852712a9b09",
   "metadata": {},
   "source": [
    "# Imputing the missing values using statistical techinique \n",
    " For numerical columns we can use mean and median statistics \n",
    " \n",
    " For categorical columns we use mode statistics "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "56a3ee18-9023-4c11-8322-aa111d127299",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"Android Ver\"] = data[\"Android Ver\"].fillna(data[\"Android Ver\"].mode()[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "dfc4aa44-abe8-4b49-ab48-863b1655ad07",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "App               0\n",
       "Category          0\n",
       "Rating            0\n",
       "Reviews           0\n",
       "Size              0\n",
       "Installs          0\n",
       "Type              0\n",
       "Price             0\n",
       "Content Rating    0\n",
       "Genres            0\n",
       "Last Updated      0\n",
       "Current Ver       4\n",
       "Android Ver       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "de5651b6-de87-4b70-88e3-58b523bc5636",
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
       "      <th>App</th>\n",
       "      <th>Category</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Reviews</th>\n",
       "      <th>Size</th>\n",
       "      <th>Installs</th>\n",
       "      <th>Type</th>\n",
       "      <th>Price</th>\n",
       "      <th>Content Rating</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Last Updated</th>\n",
       "      <th>Current Ver</th>\n",
       "      <th>Android Ver</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Learn To Draw Kawaii Characters</td>\n",
       "      <td>ART_AND_DESIGN</td>\n",
       "      <td>3.2</td>\n",
       "      <td>55</td>\n",
       "      <td>2700.0</td>\n",
       "      <td>5,000+</td>\n",
       "      <td>Free</td>\n",
       "      <td>0</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Art &amp; Design</td>\n",
       "      <td>June 6, 2018</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.2 and up</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1553</th>\n",
       "      <td>Market Update Helper</td>\n",
       "      <td>LIBRARIES_AND_DEMO</td>\n",
       "      <td>4.1</td>\n",
       "      <td>20145</td>\n",
       "      <td>11.0</td>\n",
       "      <td>1,000,000+</td>\n",
       "      <td>Free</td>\n",
       "      <td>0</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Libraries &amp; Demo</td>\n",
       "      <td>February 12, 2013</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.5 and up</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6322</th>\n",
       "      <td>Virtual DJ Sound Mixer</td>\n",
       "      <td>TOOLS</td>\n",
       "      <td>4.2</td>\n",
       "      <td>4010</td>\n",
       "      <td>8700.0</td>\n",
       "      <td>500,000+</td>\n",
       "      <td>Free</td>\n",
       "      <td>0</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Tools</td>\n",
       "      <td>May 10, 2017</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0 and up</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7333</th>\n",
       "      <td>Dots puzzle</td>\n",
       "      <td>FAMILY</td>\n",
       "      <td>4.0</td>\n",
       "      <td>179</td>\n",
       "      <td>14000.0</td>\n",
       "      <td>50,000+</td>\n",
       "      <td>Paid</td>\n",
       "      <td>$0.99</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Puzzle</td>\n",
       "      <td>April 18, 2018</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0 and up</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                  App            Category  Rating Reviews  \\\n",
       "15    Learn To Draw Kawaii Characters      ART_AND_DESIGN     3.2      55   \n",
       "1553             Market Update Helper  LIBRARIES_AND_DEMO     4.1   20145   \n",
       "6322           Virtual DJ Sound Mixer               TOOLS     4.2    4010   \n",
       "7333                      Dots puzzle              FAMILY     4.0     179   \n",
       "\n",
       "         Size    Installs  Type  Price Content Rating            Genres  \\\n",
       "15     2700.0      5,000+  Free      0       Everyone      Art & Design   \n",
       "1553     11.0  1,000,000+  Free      0       Everyone  Libraries & Demo   \n",
       "6322   8700.0    500,000+  Free      0       Everyone             Tools   \n",
       "7333  14000.0     50,000+  Paid  $0.99       Everyone            Puzzle   \n",
       "\n",
       "           Last Updated Current Ver Android Ver  \n",
       "15         June 6, 2018         NaN  4.2 and up  \n",
       "1553  February 12, 2013         NaN  1.5 and up  \n",
       "6322       May 10, 2017         NaN  4.0 and up  \n",
       "7333     April 18, 2018         NaN  4.0 and up  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data[\"Current Ver\"].isnull()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "62a288b3-7426-4e3f-96d2-c5cb1f376186",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Varies with device    1415\n",
       "1.0                    458\n",
       "1.1                    195\n",
       "1.2                    126\n",
       "1.3                    120\n",
       "                      ... \n",
       "2.9.10                   1\n",
       "3.18.5                   1\n",
       "1.3.A.2.9                1\n",
       "9.9.1.1910               1\n",
       "0.3.4                    1\n",
       "Name: Current Ver, Length: 2638, dtype: int64"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"Current Ver\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "fe82d428-1418-48a1-860e-c1b2c63a1233",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"Current Ver\"] = data[\"Current Ver\"].fillna(data[\"Current Ver\"].mode()[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d9c67207-2045-494b-a073-bf65a68954e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "App               0\n",
       "Category          0\n",
       "Rating            0\n",
       "Reviews           0\n",
       "Size              0\n",
       "Installs          0\n",
       "Type              0\n",
       "Price             0\n",
       "Content Rating    0\n",
       "Genres            0\n",
       "Last Updated      0\n",
       "Current Ver       0\n",
       "Android Ver       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "8fe5be88-5a26-4057-96d2-84e7beef0f5e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "App                object\n",
       "Category           object\n",
       "Rating            float64\n",
       "Reviews            object\n",
       "Size              float64\n",
       "Installs           object\n",
       "Type               object\n",
       "Price              object\n",
       "Content Rating     object\n",
       "Genres             object\n",
       "Last Updated       object\n",
       "Current Ver        object\n",
       "Android Ver        object\n",
       "dtype: object"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Handling incorrect data types\n",
    "data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "f77a2ddf-6aae-419e-8487-fe1f834f24c7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0          8719\n",
       "$2.99       114\n",
       "$0.99       107\n",
       "$4.99        70\n",
       "$1.99        59\n",
       "           ... \n",
       "$1.29         1\n",
       "$299.99       1\n",
       "$379.99       1\n",
       "$37.99        1\n",
       "$1.20         1\n",
       "Name: Price, Length: 73, dtype: int64"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.Price.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "ec319d47-fd76-477f-9daa-95b68b014500",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "App                object\n",
       "Category           object\n",
       "Rating            float64\n",
       "Reviews            object\n",
       "Size              float64\n",
       "Installs           object\n",
       "Type               object\n",
       "Price             float64\n",
       "Content Rating     object\n",
       "Genres             object\n",
       "Last Updated       object\n",
       "Current Ver        object\n",
       "Android Ver        object\n",
       "dtype: object"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.Price = data.Price.apply(lambda x: 0 if x == '0' else float(x[1:]))\n",
    "data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "0a82526b-56f0-4eda-94fa-5d0ac5aaa21b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2         83\n",
       "3         78\n",
       "4         74\n",
       "5         74\n",
       "1         67\n",
       "          ..\n",
       "49657      1\n",
       "41420      1\n",
       "7146       1\n",
       "44706      1\n",
       "398307     1\n",
       "Name: Reviews, Length: 5992, dtype: int64"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.Reviews.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "3792eb93-a42e-4575-ae03-cab5dd6723f9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "App                object\n",
       "Category           object\n",
       "Rating            float64\n",
       "Reviews             int32\n",
       "Size              float64\n",
       "Installs           object\n",
       "Type               object\n",
       "Price             float64\n",
       "Content Rating     object\n",
       "Genres             object\n",
       "Last Updated       object\n",
       "Current Ver        object\n",
       "Android Ver        object\n",
       "dtype: object"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.Reviews = data.Reviews.astype(\"int32\")\n",
    "data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "8bd9e4db-cc17-498a-b331-7c1891bec1f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    9.366000e+03\n",
       "mean     5.140498e+05\n",
       "std      3.144042e+06\n",
       "min      1.000000e+00\n",
       "25%      1.862500e+02\n",
       "50%      5.930500e+03\n",
       "75%      8.153275e+04\n",
       "max      7.815831e+07\n",
       "Name: Reviews, dtype: float64"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.Reviews.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "3a1061ed-7846-4d8b-aa4d-d9bd700181e2",
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
       "      <th>Rating</th>\n",
       "      <th>Reviews</th>\n",
       "      <th>Size</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>9366.000000</td>\n",
       "      <td>9.366000e+03</td>\n",
       "      <td>9366.000000</td>\n",
       "      <td>9366.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.191757</td>\n",
       "      <td>5.140498e+05</td>\n",
       "      <td>22705.733753</td>\n",
       "      <td>0.960928</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.515219</td>\n",
       "      <td>3.144042e+06</td>\n",
       "      <td>21305.040123</td>\n",
       "      <td>15.816585</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000e+00</td>\n",
       "      <td>8.500000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.862500e+02</td>\n",
       "      <td>6600.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.300000</td>\n",
       "      <td>5.930500e+03</td>\n",
       "      <td>21000.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>4.500000</td>\n",
       "      <td>8.153275e+04</td>\n",
       "      <td>27000.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>5.000000</td>\n",
       "      <td>7.815831e+07</td>\n",
       "      <td>100000.000000</td>\n",
       "      <td>400.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Rating       Reviews           Size        Price\n",
       "count  9366.000000  9.366000e+03    9366.000000  9366.000000\n",
       "mean      4.191757  5.140498e+05   22705.733753     0.960928\n",
       "std       0.515219  3.144042e+06   21305.040123    15.816585\n",
       "min       1.000000  1.000000e+00       8.500000     0.000000\n",
       "25%       4.000000  1.862500e+02    6600.000000     0.000000\n",
       "50%       4.300000  5.930500e+03   21000.000000     0.000000\n",
       "75%       4.500000  8.153275e+04   27000.000000     0.000000\n",
       "max       5.000000  7.815831e+07  100000.000000   400.000000"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "3784b79e-c52f-46d3-8bbb-e2c94ff401df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1,000,000+        1577\n",
       "10,000,000+       1252\n",
       "100,000+          1150\n",
       "10,000+           1010\n",
       "5,000,000+         752\n",
       "1,000+             713\n",
       "500,000+           538\n",
       "50,000+            467\n",
       "5,000+             432\n",
       "100,000,000+       409\n",
       "100+               309\n",
       "50,000,000+        289\n",
       "500+               201\n",
       "500,000,000+        72\n",
       "10+                 69\n",
       "1,000,000,000+      58\n",
       "50+                 56\n",
       "5+                   9\n",
       "1+                   3\n",
       "Name: Installs, dtype: int64"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.Installs.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "8fd56fd7-a597-4200-af70-a51d57630b1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# clean function \n",
    "def clean_installs(val):\n",
    "    return int(val.replace(\",\", \"\").replace(\"+\",\"\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "07693e78-5b75-430d-85a4-70ad031b8621",
   "metadata": {},
   "outputs": [],
   "source": [
    "type(clean_installs(\"3,000+\"))\n",
    "data.Installs = data.Installs.apply(clean_installs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "de3481e0-0576-421e-bae3-47fb9e771f82",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000000       1577\n",
       "10000000      1252\n",
       "100000        1150\n",
       "10000         1010\n",
       "5000000        752\n",
       "1000           713\n",
       "500000         538\n",
       "50000          467\n",
       "5000           432\n",
       "100000000      409\n",
       "100            309\n",
       "50000000       289\n",
       "500            201\n",
       "500000000       72\n",
       "10              69\n",
       "1000000000      58\n",
       "50              56\n",
       "5                9\n",
       "1                3\n",
       "Name: Installs, dtype: int64"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.Installs.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "abcf9509-55b4-4c6c-9baf-9705cf7a71c7",
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
       "      <th>Rating</th>\n",
       "      <th>Reviews</th>\n",
       "      <th>Size</th>\n",
       "      <th>Installs</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>9366.000000</td>\n",
       "      <td>9.366000e+03</td>\n",
       "      <td>9366.000000</td>\n",
       "      <td>9.366000e+03</td>\n",
       "      <td>9366.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.191757</td>\n",
       "      <td>5.140498e+05</td>\n",
       "      <td>22705.733753</td>\n",
       "      <td>1.789744e+07</td>\n",
       "      <td>0.960928</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.515219</td>\n",
       "      <td>3.144042e+06</td>\n",
       "      <td>21305.040123</td>\n",
       "      <td>9.123822e+07</td>\n",
       "      <td>15.816585</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000e+00</td>\n",
       "      <td>8.500000</td>\n",
       "      <td>1.000000e+00</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.862500e+02</td>\n",
       "      <td>6600.000000</td>\n",
       "      <td>1.000000e+04</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.300000</td>\n",
       "      <td>5.930500e+03</td>\n",
       "      <td>21000.000000</td>\n",
       "      <td>5.000000e+05</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>4.500000</td>\n",
       "      <td>8.153275e+04</td>\n",
       "      <td>27000.000000</td>\n",
       "      <td>5.000000e+06</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>5.000000</td>\n",
       "      <td>7.815831e+07</td>\n",
       "      <td>100000.000000</td>\n",
       "      <td>1.000000e+09</td>\n",
       "      <td>400.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Rating       Reviews           Size      Installs        Price\n",
       "count  9366.000000  9.366000e+03    9366.000000  9.366000e+03  9366.000000\n",
       "mean      4.191757  5.140498e+05   22705.733753  1.789744e+07     0.960928\n",
       "std       0.515219  3.144042e+06   21305.040123  9.123822e+07    15.816585\n",
       "min       1.000000  1.000000e+00       8.500000  1.000000e+00     0.000000\n",
       "25%       4.000000  1.862500e+02    6600.000000  1.000000e+04     0.000000\n",
       "50%       4.300000  5.930500e+03   21000.000000  5.000000e+05     0.000000\n",
       "75%       4.500000  8.153275e+04   27000.000000  5.000000e+06     0.000000\n",
       "max       5.000000  7.815831e+07  100000.000000  1.000000e+09   400.000000"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "d36a1c5c-3fe8-477d-87ff-b2ab92546c39",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "App                object\n",
       "Category           object\n",
       "Rating            float64\n",
       "Reviews             int32\n",
       "Size              float64\n",
       "Installs            int64\n",
       "Type               object\n",
       "Price             float64\n",
       "Content Rating     object\n",
       "Genres             object\n",
       "Last Updated       object\n",
       "Current Ver        object\n",
       "Android Ver        object\n",
       "dtype: object"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "57a3961a-37d4-433e-9908-200316f454fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Free    8719\n",
       "Paid     647\n",
       "Name: Type, dtype: int64"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.Type.value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a2383f64-802e-4ce6-930d-ab0ea79db193",
   "metadata": {},
   "source": [
    "# Lets do some sanity check \n",
    "1. Ratings should have values 1 to 5\n",
    "2. Reviews should be less than or equal to Installs\n",
    "3. If Type column shows Free apps then should show 0 and paid should have some value in the Price column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "fcc50057-2a91-44df-b241-8d4fdb4f9268",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0, 13)"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[(data.Type == \"Free\") & (data.Price > 0)].shape\n",
    "\n",
    "# Here its showing 0 which means data points are sitting correctly "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "115c34b1-45e6-41e0-8135-54d3ac84404c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7, 13)"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.Reviews > data.Installs].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "d5d21005-3610-4180-afe7-2d5c86277bc5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    9366.000000\n",
       "mean        4.191757\n",
       "std         0.515219\n",
       "min         1.000000\n",
       "25%         4.000000\n",
       "50%         4.300000\n",
       "75%         4.500000\n",
       "max         5.000000\n",
       "Name: Rating, dtype: float64"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.Rating.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "3ade531e-387f-448f-9c09-06fcf2f804ca",
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
       "      <th>App</th>\n",
       "      <th>Category</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Reviews</th>\n",
       "      <th>Size</th>\n",
       "      <th>Installs</th>\n",
       "      <th>Type</th>\n",
       "      <th>Price</th>\n",
       "      <th>Content Rating</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Last Updated</th>\n",
       "      <th>Current Ver</th>\n",
       "      <th>Android Ver</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2454</th>\n",
       "      <td>KBA-EZ Health Guide</td>\n",
       "      <td>MEDICAL</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4</td>\n",
       "      <td>25000.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>Free</td>\n",
       "      <td>0.00</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Medical</td>\n",
       "      <td>August 2, 2018</td>\n",
       "      <td>1.0.72</td>\n",
       "      <td>4.0.3 and up</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4663</th>\n",
       "      <td>Alarmy (Sleep If U Can) - Pro</td>\n",
       "      <td>LIFESTYLE</td>\n",
       "      <td>4.8</td>\n",
       "      <td>10249</td>\n",
       "      <td>21516.529524</td>\n",
       "      <td>10000</td>\n",
       "      <td>Paid</td>\n",
       "      <td>2.49</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Lifestyle</td>\n",
       "      <td>July 30, 2018</td>\n",
       "      <td>Varies with device</td>\n",
       "      <td>Varies with device</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5917</th>\n",
       "      <td>Ra Ga Ba</td>\n",
       "      <td>GAME</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2</td>\n",
       "      <td>20000.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>Paid</td>\n",
       "      <td>1.49</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Arcade</td>\n",
       "      <td>February 8, 2017</td>\n",
       "      <td>1.0.4</td>\n",
       "      <td>2.3 and up</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6700</th>\n",
       "      <td>Brick Breaker BR</td>\n",
       "      <td>GAME</td>\n",
       "      <td>5.0</td>\n",
       "      <td>7</td>\n",
       "      <td>19000.000000</td>\n",
       "      <td>5</td>\n",
       "      <td>Free</td>\n",
       "      <td>0.00</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Arcade</td>\n",
       "      <td>July 23, 2018</td>\n",
       "      <td>1.0</td>\n",
       "      <td>4.1 and up</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7402</th>\n",
       "      <td>Trovami se ci riesci</td>\n",
       "      <td>GAME</td>\n",
       "      <td>5.0</td>\n",
       "      <td>11</td>\n",
       "      <td>6100.000000</td>\n",
       "      <td>10</td>\n",
       "      <td>Free</td>\n",
       "      <td>0.00</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Arcade</td>\n",
       "      <td>March 11, 2017</td>\n",
       "      <td>0.1</td>\n",
       "      <td>2.3 and up</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8591</th>\n",
       "      <td>DN Blog</td>\n",
       "      <td>SOCIAL</td>\n",
       "      <td>5.0</td>\n",
       "      <td>20</td>\n",
       "      <td>4200.000000</td>\n",
       "      <td>10</td>\n",
       "      <td>Free</td>\n",
       "      <td>0.00</td>\n",
       "      <td>Teen</td>\n",
       "      <td>Social</td>\n",
       "      <td>July 23, 2018</td>\n",
       "      <td>1.0</td>\n",
       "      <td>4.0 and up</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10697</th>\n",
       "      <td>Mu.F.O.</td>\n",
       "      <td>GAME</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2</td>\n",
       "      <td>16000.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>Paid</td>\n",
       "      <td>0.99</td>\n",
       "      <td>Everyone</td>\n",
       "      <td>Arcade</td>\n",
       "      <td>March 3, 2017</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.3 and up</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                 App   Category  Rating  Reviews  \\\n",
       "2454             KBA-EZ Health Guide    MEDICAL     5.0        4   \n",
       "4663   Alarmy (Sleep If U Can) - Pro  LIFESTYLE     4.8    10249   \n",
       "5917                        Ra Ga Ba       GAME     5.0        2   \n",
       "6700                Brick Breaker BR       GAME     5.0        7   \n",
       "7402            Trovami se ci riesci       GAME     5.0       11   \n",
       "8591                         DN Blog     SOCIAL     5.0       20   \n",
       "10697                        Mu.F.O.       GAME     5.0        2   \n",
       "\n",
       "               Size  Installs  Type  Price Content Rating     Genres  \\\n",
       "2454   25000.000000         1  Free   0.00       Everyone    Medical   \n",
       "4663   21516.529524     10000  Paid   2.49       Everyone  Lifestyle   \n",
       "5917   20000.000000         1  Paid   1.49       Everyone     Arcade   \n",
       "6700   19000.000000         5  Free   0.00       Everyone     Arcade   \n",
       "7402    6100.000000        10  Free   0.00       Everyone     Arcade   \n",
       "8591    4200.000000        10  Free   0.00           Teen     Social   \n",
       "10697  16000.000000         1  Paid   0.99       Everyone     Arcade   \n",
       "\n",
       "           Last Updated         Current Ver         Android Ver  \n",
       "2454     August 2, 2018              1.0.72        4.0.3 and up  \n",
       "4663      July 30, 2018  Varies with device  Varies with device  \n",
       "5917   February 8, 2017               1.0.4          2.3 and up  \n",
       "6700      July 23, 2018                 1.0          4.1 and up  \n",
       "7402     March 11, 2017                 0.1          2.3 and up  \n",
       "8591      July 23, 2018                 1.0          4.0 and up  \n",
       "10697     March 3, 2017                 1.0          2.3 and up  "
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data[\"Reviews\"] > data[\"Installs\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "e4a885d1-26a1-4f88-a634-5e995c6abfb1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(9359, 13)"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "condition = data[\"Reviews\"] > data[\"Installs\"]\n",
    "data = data.drop(data[condition].index)\n",
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "2cad0670-d26f-490f-9eb0-66e0779f5728",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0, 13)"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data[\"Reviews\"] > data[\"Installs\"]].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a237c4c-2c4a-48e4-9a7a-05a9032a7357",
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
