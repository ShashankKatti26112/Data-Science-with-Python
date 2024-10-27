{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ff28a8ea-85f9-4e22-b7b7-9691fdfeded5",
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
       "      <th>Poster_Link</th>\n",
       "      <th>Series_Title</th>\n",
       "      <th>Released_Year</th>\n",
       "      <th>Certificate</th>\n",
       "      <th>Runtime</th>\n",
       "      <th>Genre</th>\n",
       "      <th>IMDB_Rating</th>\n",
       "      <th>Overview</th>\n",
       "      <th>Meta_score</th>\n",
       "      <th>Director</th>\n",
       "      <th>Star1</th>\n",
       "      <th>Star2</th>\n",
       "      <th>Star3</th>\n",
       "      <th>Star4</th>\n",
       "      <th>No_of_Votes</th>\n",
       "      <th>Gross</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>https://m.media-amazon.com/images/M/MV5BMDFkYT...</td>\n",
       "      <td>The Shawshank Redemption</td>\n",
       "      <td>1994</td>\n",
       "      <td>A</td>\n",
       "      <td>142 min</td>\n",
       "      <td>Drama</td>\n",
       "      <td>9.3</td>\n",
       "      <td>Two imprisoned men bond over a number of years...</td>\n",
       "      <td>80.0</td>\n",
       "      <td>Frank Darabont</td>\n",
       "      <td>Tim Robbins</td>\n",
       "      <td>Morgan Freeman</td>\n",
       "      <td>Bob Gunton</td>\n",
       "      <td>William Sadler</td>\n",
       "      <td>2343110</td>\n",
       "      <td>28,341,469</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>https://m.media-amazon.com/images/M/MV5BM2MyNj...</td>\n",
       "      <td>The Godfather</td>\n",
       "      <td>1972</td>\n",
       "      <td>A</td>\n",
       "      <td>175 min</td>\n",
       "      <td>Crime, Drama</td>\n",
       "      <td>9.2</td>\n",
       "      <td>An organized crime dynasty's aging patriarch t...</td>\n",
       "      <td>100.0</td>\n",
       "      <td>Francis Ford Coppola</td>\n",
       "      <td>Marlon Brando</td>\n",
       "      <td>Al Pacino</td>\n",
       "      <td>James Caan</td>\n",
       "      <td>Diane Keaton</td>\n",
       "      <td>1620367</td>\n",
       "      <td>134,966,411</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>https://m.media-amazon.com/images/M/MV5BMTMxNT...</td>\n",
       "      <td>The Dark Knight</td>\n",
       "      <td>2008</td>\n",
       "      <td>UA</td>\n",
       "      <td>152 min</td>\n",
       "      <td>Action, Crime, Drama</td>\n",
       "      <td>9.0</td>\n",
       "      <td>When the menace known as the Joker wreaks havo...</td>\n",
       "      <td>84.0</td>\n",
       "      <td>Christopher Nolan</td>\n",
       "      <td>Christian Bale</td>\n",
       "      <td>Heath Ledger</td>\n",
       "      <td>Aaron Eckhart</td>\n",
       "      <td>Michael Caine</td>\n",
       "      <td>2303232</td>\n",
       "      <td>534,858,444</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                         Poster_Link  \\\n",
       "0  https://m.media-amazon.com/images/M/MV5BMDFkYT...   \n",
       "1  https://m.media-amazon.com/images/M/MV5BM2MyNj...   \n",
       "2  https://m.media-amazon.com/images/M/MV5BMTMxNT...   \n",
       "\n",
       "               Series_Title Released_Year Certificate  Runtime  \\\n",
       "0  The Shawshank Redemption          1994           A  142 min   \n",
       "1             The Godfather          1972           A  175 min   \n",
       "2           The Dark Knight          2008          UA  152 min   \n",
       "\n",
       "                  Genre  IMDB_Rating  \\\n",
       "0                 Drama          9.3   \n",
       "1          Crime, Drama          9.2   \n",
       "2  Action, Crime, Drama          9.0   \n",
       "\n",
       "                                            Overview  Meta_score  \\\n",
       "0  Two imprisoned men bond over a number of years...        80.0   \n",
       "1  An organized crime dynasty's aging patriarch t...       100.0   \n",
       "2  When the menace known as the Joker wreaks havo...        84.0   \n",
       "\n",
       "               Director           Star1           Star2          Star3  \\\n",
       "0        Frank Darabont     Tim Robbins  Morgan Freeman     Bob Gunton   \n",
       "1  Francis Ford Coppola   Marlon Brando       Al Pacino     James Caan   \n",
       "2     Christopher Nolan  Christian Bale    Heath Ledger  Aaron Eckhart   \n",
       "\n",
       "            Star4  No_of_Votes        Gross  \n",
       "0  William Sadler      2343110   28,341,469  \n",
       "1    Diane Keaton      1620367  134,966,411  \n",
       "2   Michael Caine      2303232  534,858,444  "
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "imdb_data = pd.read_csv(\"imdb_top_1000.csv\")\n",
    "imdb_data.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "89ea5c8f-a815-47d0-b7eb-cf80478f1edf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Poster_Link        0\n",
       "Series_Title       0\n",
       "Released_Year      0\n",
       "Certificate      101\n",
       "Runtime            0\n",
       "Genre              0\n",
       "IMDB_Rating        0\n",
       "Overview           0\n",
       "Meta_score       157\n",
       "Director           0\n",
       "Star1              0\n",
       "Star2              0\n",
       "Star3              0\n",
       "Star4              0\n",
       "No_of_Votes        0\n",
       "Gross            169\n",
       "dtype: int64"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "imdb_data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "12cb81e7-0f3d-4d17-b4cd-300d2d3c3530",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1000, 16)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "imdb_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f919422f-101c-4116-bf99-e783ff7665f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1000 entries, 0 to 999\n",
      "Data columns (total 16 columns):\n",
      " #   Column         Non-Null Count  Dtype  \n",
      "---  ------         --------------  -----  \n",
      " 0   Poster_Link    1000 non-null   object \n",
      " 1   Series_Title   1000 non-null   object \n",
      " 2   Released_Year  1000 non-null   object \n",
      " 3   Certificate    899 non-null    object \n",
      " 4   Runtime        1000 non-null   object \n",
      " 5   Genre          1000 non-null   object \n",
      " 6   IMDB_Rating    1000 non-null   float64\n",
      " 7   Overview       1000 non-null   object \n",
      " 8   Meta_score     843 non-null    float64\n",
      " 9   Director       1000 non-null   object \n",
      " 10  Star1          1000 non-null   object \n",
      " 11  Star2          1000 non-null   object \n",
      " 12  Star3          1000 non-null   object \n",
      " 13  Star4          1000 non-null   object \n",
      " 14  No_of_Votes    1000 non-null   int64  \n",
      " 15  Gross          831 non-null    object \n",
      "dtypes: float64(2), int64(1), object(13)\n",
      "memory usage: 125.1+ KB\n"
     ]
    }
   ],
   "source": [
    "imdb_data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e7b2a9cb-9072-47bb-bba7-4911918cf6c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3b82bcd2-2b59-45c0-9ac9-ec466290633e",
   "metadata": {},
   "outputs": [],
   "source": [
    "features = ['IMDB_Rating']\n",
    "X = imdb_data[features]\n",
    "y = imdb_data['Genre']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "95044bc6-444c-463a-b6b3-80ffc8fdf969",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y , test_size = 0.2, random_state = 42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "137ecf3b-4106-49d4-a644-cef8e0098493",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7.7    157\n",
       "7.8    151\n",
       "8.0    141\n",
       "8.1    127\n",
       "7.6    123\n",
       "7.9    106\n",
       "8.2     67\n",
       "8.3     44\n",
       "8.4     31\n",
       "8.5     20\n",
       "8.6     15\n",
       "8.7      5\n",
       "8.8      5\n",
       "8.9      3\n",
       "9.0      3\n",
       "9.2      1\n",
       "9.3      1\n",
       "Name: IMDB_Rating, dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "imdb_data.IMDB_Rating.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "87a8e87c-5734-4409-bf4d-58649b1b60e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "scaler = StandardScaler()\n",
    "X_train_scaled = scaler.fit_transform(X_train)\n",
    "X_test_scaled = scaler.transform(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "aa72094e-d148-4eb2-9ee8-62f9f705a4e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>KNeighborsClassifier(n_neighbors=550)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">KNeighborsClassifier</label><div class=\"sk-toggleable__content\"><pre>KNeighborsClassifier(n_neighbors=550)</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "KNeighborsClassifier(n_neighbors=550)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "k = 550\n",
    "knn_classifier = KNeighborsClassifier(n_neighbors = k)\n",
    "knn_classifier.fit(X_train_scaled, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "72b557e4-e61a-49bd-a0c1-578463f2a657",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/joblib/externals/loky/backend/context.py:110: UserWarning: Could not find the number of physical cores for the following reason:\n",
      "found 0 physical cores < 1\n",
      "Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.\n",
      "  warnings.warn(\n",
      "  File \"/opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/joblib/externals/loky/backend/context.py\", line 217, in _count_physical_cores\n",
      "    raise ValueError(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array(['Drama', 'Drama', 'Drama', 'Drama', 'Drama', 'Drama', 'Drama',\n",
       "       'Drama', 'Drama', 'Drama'], dtype=object)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred = knn_classifier.predict(X_test_scaled)\n",
    "y_pred[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ed43442b-a0bf-4386-8816-c7badff60a36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.075\n"
     ]
    }
   ],
   "source": [
    "accuarcy = accuracy_score(y_test, y_pred)\n",
    "print(accuarcy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4f1b5df8-7cf8-4753-8d4b-9257631a21af",
   "metadata": {},
   "outputs": [],
   "source": [
    "# new movie \n",
    "new_movie_rating = 4\n",
    "new_movie = pd.DataFrame({'IMDB_Rating':[new_movie_rating]})\n",
    "new_movie_scaled = scaler.transform(new_movie)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ef1108d9-81a9-432d-ad73-a40d861e0075",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Drama']\n"
     ]
    }
   ],
   "source": [
    "predicted_genre = knn_classifier.predict(new_movie_scaled)\n",
    "print(predicted_genre)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "197b93e4-fbbd-40b3-a5d1-5149a17877d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.impute import KNNImputer\n",
    "imputer = KNNImputer(n_neighbors = 200)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "446c350d-8891-4fa2-8b30-20e79d577df4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4,360,000      5\n",
       "25,000,000     2\n",
       "5,450,000      2\n",
       "5,321,508      2\n",
       "9,600,000      2\n",
       "              ..\n",
       "106,662        1\n",
       "10,950         1\n",
       "4,018,695      1\n",
       "141,319,928    1\n",
       "30,500,000     1\n",
       "Name: Gross, Length: 823, dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "imdb_data.Gross.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "07c49bdf-2f98-45ea-af21-84df6fd79038",
   "metadata": {},
   "outputs": [],
   "source": [
    "imdb_data['Gross'] = imdb_data['Gross'].str.replace(',','')\n",
    "imdb_data['Gross'] = pd.to_numeric(imdb_data['Gross'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c65f7a58-dadc-4b7f-8fb4-c096a1017904",
   "metadata": {},
   "outputs": [],
   "source": [
    "imdb_data_imputed = pd.DataFrame(imputer.fit_transform(imdb_data[['Gross']]), columns=['Gross_Imputed'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "b0470533-9e14-4981-9793-aeaff94d16c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "imdb_data_imputed['Gross'] = imdb_data['Gross']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1d499bda-d578-46bb-ab04-2ac38e079cf9",
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
       "      <th>Gross_Imputed</th>\n",
       "      <th>Gross</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>28341469.0</td>\n",
       "      <td>28341469.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>134966411.0</td>\n",
       "      <td>134966411.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>534858444.0</td>\n",
       "      <td>534858444.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>57300000.0</td>\n",
       "      <td>57300000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4360000.0</td>\n",
       "      <td>4360000.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Gross_Imputed        Gross\n",
       "0     28341469.0   28341469.0\n",
       "1    134966411.0  134966411.0\n",
       "2    534858444.0  534858444.0\n",
       "3     57300000.0   57300000.0\n",
       "4      4360000.0    4360000.0"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "imdb_data_imputed.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "87af5d89-95db-40f3-a76f-4b2c6eded682",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Gross_Imputed      0\n",
       "Gross            169\n",
       "dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "imdb_data_imputed.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46f1ef0b-ef6a-494c-a6b2-7c88b3ee2f86",
   "metadata": {},
   "source": [
    "## You can use KNeighborsRegressor (from sklearn.neighbors) instead of using the KNNImputer for imputing missing values. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "5d15f07f-05d0-44c3-9146-2f0d1916ab26",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsRegressor\n",
    "imdb_data = pd.DataFrame(imdb_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "96b5d1a7-cf75-4bf9-bf93-372ba40e3a77",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Separate rows with missing values and complete rows\n",
    "missing_mask = imdb_data['Gross'].isnull()\n",
    "\n",
    "# Step 1: Training the KNN Regressor on the complete data (where 'Gross' is not missing)\n",
    "X_train = imdb_data.loc[~missing_mask, ['IMDB_Rating']]  # Use 'Rating' as a feature to predict 'Gross'\n",
    "y_train = imdb_data.loc[~missing_mask, 'Gross']     # 'Gross' is the target\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "a1228ba3-8d79-4f61-897d-64756749b73d",
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
       "      <th>Poster_Link</th>\n",
       "      <th>Series_Title</th>\n",
       "      <th>Released_Year</th>\n",
       "      <th>Certificate</th>\n",
       "      <th>Runtime</th>\n",
       "      <th>Genre</th>\n",
       "      <th>IMDB_Rating</th>\n",
       "      <th>Overview</th>\n",
       "      <th>Meta_score</th>\n",
       "      <th>Director</th>\n",
       "      <th>Star1</th>\n",
       "      <th>Star2</th>\n",
       "      <th>Star3</th>\n",
       "      <th>Star4</th>\n",
       "      <th>No_of_Votes</th>\n",
       "      <th>Gross</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>https://m.media-amazon.com/images/M/MV5BMDFkYT...</td>\n",
       "      <td>The Shawshank Redemption</td>\n",
       "      <td>1994</td>\n",
       "      <td>A</td>\n",
       "      <td>142 min</td>\n",
       "      <td>Drama</td>\n",
       "      <td>9.3</td>\n",
       "      <td>Two imprisoned men bond over a number of years...</td>\n",
       "      <td>80.0</td>\n",
       "      <td>Frank Darabont</td>\n",
       "      <td>Tim Robbins</td>\n",
       "      <td>Morgan Freeman</td>\n",
       "      <td>Bob Gunton</td>\n",
       "      <td>William Sadler</td>\n",
       "      <td>2343110</td>\n",
       "      <td>28341469.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>https://m.media-amazon.com/images/M/MV5BM2MyNj...</td>\n",
       "      <td>The Godfather</td>\n",
       "      <td>1972</td>\n",
       "      <td>A</td>\n",
       "      <td>175 min</td>\n",
       "      <td>Crime, Drama</td>\n",
       "      <td>9.2</td>\n",
       "      <td>An organized crime dynasty's aging patriarch t...</td>\n",
       "      <td>100.0</td>\n",
       "      <td>Francis Ford Coppola</td>\n",
       "      <td>Marlon Brando</td>\n",
       "      <td>Al Pacino</td>\n",
       "      <td>James Caan</td>\n",
       "      <td>Diane Keaton</td>\n",
       "      <td>1620367</td>\n",
       "      <td>134966411.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>https://m.media-amazon.com/images/M/MV5BMTMxNT...</td>\n",
       "      <td>The Dark Knight</td>\n",
       "      <td>2008</td>\n",
       "      <td>UA</td>\n",
       "      <td>152 min</td>\n",
       "      <td>Action, Crime, Drama</td>\n",
       "      <td>9.0</td>\n",
       "      <td>When the menace known as the Joker wreaks havo...</td>\n",
       "      <td>84.0</td>\n",
       "      <td>Christopher Nolan</td>\n",
       "      <td>Christian Bale</td>\n",
       "      <td>Heath Ledger</td>\n",
       "      <td>Aaron Eckhart</td>\n",
       "      <td>Michael Caine</td>\n",
       "      <td>2303232</td>\n",
       "      <td>534858444.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>https://m.media-amazon.com/images/M/MV5BMWMwMG...</td>\n",
       "      <td>The Godfather: Part II</td>\n",
       "      <td>1974</td>\n",
       "      <td>A</td>\n",
       "      <td>202 min</td>\n",
       "      <td>Crime, Drama</td>\n",
       "      <td>9.0</td>\n",
       "      <td>The early life and career of Vito Corleone in ...</td>\n",
       "      <td>90.0</td>\n",
       "      <td>Francis Ford Coppola</td>\n",
       "      <td>Al Pacino</td>\n",
       "      <td>Robert De Niro</td>\n",
       "      <td>Robert Duvall</td>\n",
       "      <td>Diane Keaton</td>\n",
       "      <td>1129952</td>\n",
       "      <td>57300000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>https://m.media-amazon.com/images/M/MV5BMWU4N2...</td>\n",
       "      <td>12 Angry Men</td>\n",
       "      <td>1957</td>\n",
       "      <td>U</td>\n",
       "      <td>96 min</td>\n",
       "      <td>Crime, Drama</td>\n",
       "      <td>9.0</td>\n",
       "      <td>A jury holdout attempts to prevent a miscarria...</td>\n",
       "      <td>96.0</td>\n",
       "      <td>Sidney Lumet</td>\n",
       "      <td>Henry Fonda</td>\n",
       "      <td>Lee J. Cobb</td>\n",
       "      <td>Martin Balsam</td>\n",
       "      <td>John Fiedler</td>\n",
       "      <td>689845</td>\n",
       "      <td>4360000.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                         Poster_Link  \\\n",
       "0  https://m.media-amazon.com/images/M/MV5BMDFkYT...   \n",
       "1  https://m.media-amazon.com/images/M/MV5BM2MyNj...   \n",
       "2  https://m.media-amazon.com/images/M/MV5BMTMxNT...   \n",
       "3  https://m.media-amazon.com/images/M/MV5BMWMwMG...   \n",
       "4  https://m.media-amazon.com/images/M/MV5BMWU4N2...   \n",
       "\n",
       "               Series_Title Released_Year Certificate  Runtime  \\\n",
       "0  The Shawshank Redemption          1994           A  142 min   \n",
       "1             The Godfather          1972           A  175 min   \n",
       "2           The Dark Knight          2008          UA  152 min   \n",
       "3    The Godfather: Part II          1974           A  202 min   \n",
       "4              12 Angry Men          1957           U   96 min   \n",
       "\n",
       "                  Genre  IMDB_Rating  \\\n",
       "0                 Drama          9.3   \n",
       "1          Crime, Drama          9.2   \n",
       "2  Action, Crime, Drama          9.0   \n",
       "3          Crime, Drama          9.0   \n",
       "4          Crime, Drama          9.0   \n",
       "\n",
       "                                            Overview  Meta_score  \\\n",
       "0  Two imprisoned men bond over a number of years...        80.0   \n",
       "1  An organized crime dynasty's aging patriarch t...       100.0   \n",
       "2  When the menace known as the Joker wreaks havo...        84.0   \n",
       "3  The early life and career of Vito Corleone in ...        90.0   \n",
       "4  A jury holdout attempts to prevent a miscarria...        96.0   \n",
       "\n",
       "               Director           Star1           Star2          Star3  \\\n",
       "0        Frank Darabont     Tim Robbins  Morgan Freeman     Bob Gunton   \n",
       "1  Francis Ford Coppola   Marlon Brando       Al Pacino     James Caan   \n",
       "2     Christopher Nolan  Christian Bale    Heath Ledger  Aaron Eckhart   \n",
       "3  Francis Ford Coppola       Al Pacino  Robert De Niro  Robert Duvall   \n",
       "4          Sidney Lumet     Henry Fonda     Lee J. Cobb  Martin Balsam   \n",
       "\n",
       "            Star4  No_of_Votes        Gross  \n",
       "0  William Sadler      2343110   28341469.0  \n",
       "1    Diane Keaton      1620367  134966411.0  \n",
       "2   Michael Caine      2303232  534858444.0  \n",
       "3    Diane Keaton      1129952   57300000.0  \n",
       "4    John Fiedler       689845    4360000.0  "
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Step 2: Fit KNN Regressor\n",
    "knn_regressor = KNeighborsRegressor(n_neighbors=2)  # You can tune the number of neighbors\n",
    "knn_regressor.fit(X_train, y_train)\n",
    "\n",
    "# Step 3: Predict missing 'Gross' value using the trained model\n",
    "X_test = imdb_data.loc[missing_mask, ['IMDB_Rating']]  # The 'Rating' for the row with missing 'Gross'\n",
    "predicted_gross = knn_regressor.predict(X_test)\n",
    "\n",
    "# Step 4: Fill in the missing value\n",
    "imdb_data.loc[missing_mask, 'Gross'] = predicted_gross\n",
    "\n",
    "imdb_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "da4aa97a-0023-4241-adee-5a7c084dba00",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "267289695.5    29\n",
       "2500538.5      28\n",
       "4842488.0      28\n",
       "18076173.0     21\n",
       "151534373.0    17\n",
       "               ..\n",
       "106662.0        1\n",
       "10950.0         1\n",
       "4018695.0       1\n",
       "141319928.0     1\n",
       "30500000.0      1\n",
       "Name: Gross, Length: 834, dtype: int64"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "imdb_data.Gross.value_counts()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "85bdd457-2e88-4a42-a64f-ef8d9eff99e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "imdb_data.Gross.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f204966d-945b-4691-b2f9-cde43aefb15e",
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
