{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "57d613c1-93bf-4548-8406-0b0ca9cc917e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns, matplotlib.pyplot as plt\n",
    "import pandas as pd, numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "591b4349-8747-4b90-b47c-0670fbd7ff32",
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
       "      <th>url</th>\n",
       "      <th>address</th>\n",
       "      <th>name</th>\n",
       "      <th>online_order</th>\n",
       "      <th>book_table</th>\n",
       "      <th>rate</th>\n",
       "      <th>votes</th>\n",
       "      <th>phone</th>\n",
       "      <th>location</th>\n",
       "      <th>rest_type</th>\n",
       "      <th>dish_liked</th>\n",
       "      <th>cuisines</th>\n",
       "      <th>approx_cost(for two people)</th>\n",
       "      <th>reviews_list</th>\n",
       "      <th>menu_item</th>\n",
       "      <th>listed_in(type)</th>\n",
       "      <th>listed_in(city)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>\n",
       "      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>\n",
       "      <td>Jalsa</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>4.1/5</td>\n",
       "      <td>775</td>\n",
       "      <td>080 42297555\\r\\n+91 9743772233</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>\n",
       "      <td>North Indian, Mughlai, Chinese</td>\n",
       "      <td>800</td>\n",
       "      <td>[('Rated 4.0', 'RATED\\n  A beautiful place to ...</td>\n",
       "      <td>[]</td>\n",
       "      <td>Buffet</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>https://www.zomato.com/bangalore/spice-elephan...</td>\n",
       "      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>\n",
       "      <td>Spice Elephant</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>4.1/5</td>\n",
       "      <td>787</td>\n",
       "      <td>080 41714161</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>\n",
       "      <td>Chinese, North Indian, Thai</td>\n",
       "      <td>800</td>\n",
       "      <td>[('Rated 4.0', 'RATED\\n  Had been here for din...</td>\n",
       "      <td>[]</td>\n",
       "      <td>Buffet</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>\n",
       "      <td>1112, Next to KIMS Medical College, 17th Cross...</td>\n",
       "      <td>San Churro Cafe</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>3.8/5</td>\n",
       "      <td>918</td>\n",
       "      <td>+91 9663487993</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Cafe, Casual Dining</td>\n",
       "      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>\n",
       "      <td>Cafe, Mexican, Italian</td>\n",
       "      <td>800</td>\n",
       "      <td>[('Rated 3.0', \"RATED\\n  Ambience is not that ...</td>\n",
       "      <td>[]</td>\n",
       "      <td>Buffet</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>\n",
       "      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>\n",
       "      <td>Addhuri Udupi Bhojana</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>3.7/5</td>\n",
       "      <td>88</td>\n",
       "      <td>+91 9620009302</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Quick Bites</td>\n",
       "      <td>Masala Dosa</td>\n",
       "      <td>South Indian, North Indian</td>\n",
       "      <td>300</td>\n",
       "      <td>[('Rated 4.0', \"RATED\\n  Great food and proper...</td>\n",
       "      <td>[]</td>\n",
       "      <td>Buffet</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>https://www.zomato.com/bangalore/grand-village...</td>\n",
       "      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>\n",
       "      <td>Grand Village</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>3.8/5</td>\n",
       "      <td>166</td>\n",
       "      <td>+91 8026612447\\r\\n+91 9901210005</td>\n",
       "      <td>Basavanagudi</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>Panipuri, Gol Gappe</td>\n",
       "      <td>North Indian, Rajasthani</td>\n",
       "      <td>600</td>\n",
       "      <td>[('Rated 4.0', 'RATED\\n  Very good restaurant ...</td>\n",
       "      <td>[]</td>\n",
       "      <td>Buffet</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                 url  \\\n",
       "0  https://www.zomato.com/bangalore/jalsa-banasha...   \n",
       "1  https://www.zomato.com/bangalore/spice-elephan...   \n",
       "2  https://www.zomato.com/SanchurroBangalore?cont...   \n",
       "3  https://www.zomato.com/bangalore/addhuri-udupi...   \n",
       "4  https://www.zomato.com/bangalore/grand-village...   \n",
       "\n",
       "                                             address                   name  \\\n",
       "0  942, 21st Main Road, 2nd Stage, Banashankari, ...                  Jalsa   \n",
       "1  2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...         Spice Elephant   \n",
       "2  1112, Next to KIMS Medical College, 17th Cross...        San Churro Cafe   \n",
       "3  1st Floor, Annakuteera, 3rd Stage, Banashankar...  Addhuri Udupi Bhojana   \n",
       "4  10, 3rd Floor, Lakshmi Associates, Gandhi Baza...          Grand Village   \n",
       "\n",
       "  online_order book_table   rate  votes                             phone  \\\n",
       "0          Yes        Yes  4.1/5    775    080 42297555\\r\\n+91 9743772233   \n",
       "1          Yes         No  4.1/5    787                      080 41714161   \n",
       "2          Yes         No  3.8/5    918                    +91 9663487993   \n",
       "3           No         No  3.7/5     88                    +91 9620009302   \n",
       "4           No         No  3.8/5    166  +91 8026612447\\r\\n+91 9901210005   \n",
       "\n",
       "       location            rest_type  \\\n",
       "0  Banashankari        Casual Dining   \n",
       "1  Banashankari        Casual Dining   \n",
       "2  Banashankari  Cafe, Casual Dining   \n",
       "3  Banashankari          Quick Bites   \n",
       "4  Basavanagudi        Casual Dining   \n",
       "\n",
       "                                          dish_liked  \\\n",
       "0  Pasta, Lunch Buffet, Masala Papad, Paneer Laja...   \n",
       "1  Momos, Lunch Buffet, Chocolate Nirvana, Thai G...   \n",
       "2  Churros, Cannelloni, Minestrone Soup, Hot Choc...   \n",
       "3                                        Masala Dosa   \n",
       "4                                Panipuri, Gol Gappe   \n",
       "\n",
       "                         cuisines approx_cost(for two people)  \\\n",
       "0  North Indian, Mughlai, Chinese                         800   \n",
       "1     Chinese, North Indian, Thai                         800   \n",
       "2          Cafe, Mexican, Italian                         800   \n",
       "3      South Indian, North Indian                         300   \n",
       "4        North Indian, Rajasthani                         600   \n",
       "\n",
       "                                        reviews_list menu_item  \\\n",
       "0  [('Rated 4.0', 'RATED\\n  A beautiful place to ...        []   \n",
       "1  [('Rated 4.0', 'RATED\\n  Had been here for din...        []   \n",
       "2  [('Rated 3.0', \"RATED\\n  Ambience is not that ...        []   \n",
       "3  [('Rated 4.0', \"RATED\\n  Great food and proper...        []   \n",
       "4  [('Rated 4.0', 'RATED\\n  Very good restaurant ...        []   \n",
       "\n",
       "  listed_in(type) listed_in(city)  \n",
       "0          Buffet    Banashankari  \n",
       "1          Buffet    Banashankari  \n",
       "2          Buffet    Banashankari  \n",
       "3          Buffet    Banashankari  \n",
       "4          Buffet    Banashankari  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato = pd.read_csv('data.csv', on_bad_lines='skip', encoding='utf-8', skiprows=[4271])\n",
    "zomato.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "614b7e27-15f6-4c52-969d-b11fecc9b1de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 4270 entries, 0 to 4269\n",
      "Data columns (total 17 columns):\n",
      " #   Column                       Non-Null Count  Dtype \n",
      "---  ------                       --------------  ----- \n",
      " 0   url                          4270 non-null   object\n",
      " 1   address                      4270 non-null   object\n",
      " 2   name                         4270 non-null   object\n",
      " 3   online_order                 4270 non-null   object\n",
      " 4   book_table                   4270 non-null   object\n",
      " 5   rate                         3736 non-null   object\n",
      " 6   votes                        4270 non-null   int64 \n",
      " 7   phone                        4207 non-null   object\n",
      " 8   location                     4269 non-null   object\n",
      " 9   rest_type                    4252 non-null   object\n",
      " 10  dish_liked                   1806 non-null   object\n",
      " 11  cuisines                     4265 non-null   object\n",
      " 12  approx_cost(for two people)  4263 non-null   object\n",
      " 13  reviews_list                 4270 non-null   object\n",
      " 14  menu_item                    4270 non-null   object\n",
      " 15  listed_in(type)              4270 non-null   object\n",
      " 16  listed_in(city)              4270 non-null   object\n",
      "dtypes: int64(1), object(16)\n",
      "memory usage: 567.2+ KB\n"
     ]
    }
   ],
   "source": [
    "zomato.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "fe28a620-7e88-4b1b-93ef-5354b5ea8dfd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "url                               0\n",
       "address                           0\n",
       "name                              0\n",
       "online_order                      0\n",
       "book_table                        0\n",
       "rate                            534\n",
       "votes                             0\n",
       "phone                            63\n",
       "location                          1\n",
       "rest_type                        18\n",
       "dish_liked                     2464\n",
       "cuisines                          5\n",
       "approx_cost(for two people)       7\n",
       "reviews_list                      0\n",
       "menu_item                         0\n",
       "listed_in(type)                   0\n",
       "listed_in(city)                   0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b3214bfd-e409-4ac1-90a1-b62a7352f6c4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4270, 17)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6484c0c0-2489-4b03-8e1a-d4b73664c5f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "zomato.dropna(how = 'any', inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "363832c4-4442-43d5-a67d-731f4f6adafc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1782, 17)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3c847f21-d81b-4f7a-a5d6-6f437819a2c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "url                            0\n",
       "address                        0\n",
       "name                           0\n",
       "online_order                   0\n",
       "book_table                     0\n",
       "rate                           0\n",
       "votes                          0\n",
       "phone                          0\n",
       "location                       0\n",
       "rest_type                      0\n",
       "dish_liked                     0\n",
       "cuisines                       0\n",
       "approx_cost(for two people)    0\n",
       "reviews_list                   0\n",
       "menu_item                      0\n",
       "listed_in(type)                0\n",
       "listed_in(city)                0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f2be32fa-ff6f-467a-83a5-dc58915abf28",
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
       "      <th>name</th>\n",
       "      <th>online_order</th>\n",
       "      <th>book_table</th>\n",
       "      <th>rate</th>\n",
       "      <th>votes</th>\n",
       "      <th>location</th>\n",
       "      <th>rest_type</th>\n",
       "      <th>cuisines</th>\n",
       "      <th>approx_cost(for two people)</th>\n",
       "      <th>listed_in(city)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jalsa</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>4.1/5</td>\n",
       "      <td>775</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>North Indian, Mughlai, Chinese</td>\n",
       "      <td>800</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Spice Elephant</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>4.1/5</td>\n",
       "      <td>787</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>Chinese, North Indian, Thai</td>\n",
       "      <td>800</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>San Churro Cafe</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>3.8/5</td>\n",
       "      <td>918</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Cafe, Casual Dining</td>\n",
       "      <td>Cafe, Mexican, Italian</td>\n",
       "      <td>800</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Addhuri Udupi Bhojana</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>3.7/5</td>\n",
       "      <td>88</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Quick Bites</td>\n",
       "      <td>South Indian, North Indian</td>\n",
       "      <td>300</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Grand Village</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>3.8/5</td>\n",
       "      <td>166</td>\n",
       "      <td>Basavanagudi</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>North Indian, Rajasthani</td>\n",
       "      <td>600</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    name online_order book_table   rate  votes      location  \\\n",
       "0                  Jalsa          Yes        Yes  4.1/5    775  Banashankari   \n",
       "1         Spice Elephant          Yes         No  4.1/5    787  Banashankari   \n",
       "2        San Churro Cafe          Yes         No  3.8/5    918  Banashankari   \n",
       "3  Addhuri Udupi Bhojana           No         No  3.7/5     88  Banashankari   \n",
       "4          Grand Village           No         No  3.8/5    166  Basavanagudi   \n",
       "\n",
       "             rest_type                        cuisines  \\\n",
       "0        Casual Dining  North Indian, Mughlai, Chinese   \n",
       "1        Casual Dining     Chinese, North Indian, Thai   \n",
       "2  Cafe, Casual Dining          Cafe, Mexican, Italian   \n",
       "3          Quick Bites      South Indian, North Indian   \n",
       "4        Casual Dining        North Indian, Rajasthani   \n",
       "\n",
       "  approx_cost(for two people) listed_in(city)  \n",
       "0                         800    Banashankari  \n",
       "1                         800    Banashankari  \n",
       "2                         800    Banashankari  \n",
       "3                         300    Banashankari  \n",
       "4                         600    Banashankari  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato = zomato.drop(['url','address','phone','dish_liked','reviews_list','menu_item','listed_in(type)'], axis = 1)\n",
    "zomato.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b6539a42-bf7f-4f81-905b-038ac0e236b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "512"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# check for duplicates \n",
    "\n",
    "zomato.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1c3a165b-28e8-41c3-8bad-b98367294ab3",
   "metadata": {},
   "outputs": [],
   "source": [
    "zomato.drop_duplicates(inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d170cf93-9b79-4b04-a393-2155867bac71",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1270, 10)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "36a20830-25b9-444f-8d38-151255cf70d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "zomato = zomato.rename(columns = {'approx_cost(for two people)':'cost','listed_in(city)':'city'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "fb60175b-f022-499e-96d6-849c848003b6",
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
       "      <th>name</th>\n",
       "      <th>online_order</th>\n",
       "      <th>book_table</th>\n",
       "      <th>rate</th>\n",
       "      <th>votes</th>\n",
       "      <th>location</th>\n",
       "      <th>rest_type</th>\n",
       "      <th>cuisines</th>\n",
       "      <th>cost</th>\n",
       "      <th>city</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jalsa</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>4.1/5</td>\n",
       "      <td>775</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>North Indian, Mughlai, Chinese</td>\n",
       "      <td>800</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Spice Elephant</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>4.1/5</td>\n",
       "      <td>787</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>Chinese, North Indian, Thai</td>\n",
       "      <td>800</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>San Churro Cafe</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>3.8/5</td>\n",
       "      <td>918</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Cafe, Casual Dining</td>\n",
       "      <td>Cafe, Mexican, Italian</td>\n",
       "      <td>800</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Addhuri Udupi Bhojana</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>3.7/5</td>\n",
       "      <td>88</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Quick Bites</td>\n",
       "      <td>South Indian, North Indian</td>\n",
       "      <td>300</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Grand Village</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>3.8/5</td>\n",
       "      <td>166</td>\n",
       "      <td>Basavanagudi</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>North Indian, Rajasthani</td>\n",
       "      <td>600</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    name online_order book_table   rate  votes      location  \\\n",
       "0                  Jalsa          Yes        Yes  4.1/5    775  Banashankari   \n",
       "1         Spice Elephant          Yes         No  4.1/5    787  Banashankari   \n",
       "2        San Churro Cafe          Yes         No  3.8/5    918  Banashankari   \n",
       "3  Addhuri Udupi Bhojana           No         No  3.7/5     88  Banashankari   \n",
       "4          Grand Village           No         No  3.8/5    166  Basavanagudi   \n",
       "\n",
       "             rest_type                        cuisines cost          city  \n",
       "0        Casual Dining  North Indian, Mughlai, Chinese  800  Banashankari  \n",
       "1        Casual Dining     Chinese, North Indian, Thai  800  Banashankari  \n",
       "2  Cafe, Casual Dining          Cafe, Mexican, Italian  800  Banashankari  \n",
       "3          Quick Bites      South Indian, North Indian  300  Banashankari  \n",
       "4        Casual Dining        North Indian, Rajasthani  600  Banashankari  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "27c26c10-d534-4ee4-b2e4-d48f18f635e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "400      183\n",
       "600      125\n",
       "500      125\n",
       "300      114\n",
       "800      103\n",
       "200       62\n",
       "700       54\n",
       "250       54\n",
       "450       49\n",
       "750       47\n",
       "1,000     43\n",
       "650       41\n",
       "150       39\n",
       "1,200     34\n",
       "550       30\n",
       "350       29\n",
       "100       27\n",
       "900       22\n",
       "1,500     20\n",
       "1,300     13\n",
       "1,100     12\n",
       "850        9\n",
       "1,600      7\n",
       "1,400      6\n",
       "950        5\n",
       "1,700      4\n",
       "1,800      4\n",
       "1,350      2\n",
       "2,000      2\n",
       "230        1\n",
       "2,200      1\n",
       "1,900      1\n",
       "180        1\n",
       "330        1\n",
       "Name: cost, dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.cost.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5f281245-9a9e-4dad-9b02-93e657388dd1",
   "metadata": {},
   "outputs": [],
   "source": [
    "zomato['cost'] = zomato['cost'].astype(str)\n",
    "zomato['cost'] = zomato['cost'].apply(lambda x :x.replace(',',''))\n",
    "zomato['cost'] = zomato['cost'].astype(float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7abdaee2-be80-48f7-bbc0-33f8adb2a469",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.cost.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "5e00ca06-e468-41e8-a2f7-6af71335510a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['4.1/5', '3.8/5', '3.7/5', '4.6/5', '4.0/5', '4.2/5', '3.9/5',\n",
       "       '3.0/5', '3.6/5', '2.8/5', '4.4/5', '3.1/5', '4.3/5', '2.6/5',\n",
       "       '3.3/5', '3.5/5', '3.8 /5', '3.2/5', '4.5/5', '2.5/5', '2.9/5',\n",
       "       '3.4/5', '2.7/5', '4.7/5', 'NEW', '2.4/5', '2.2/5', '2.3/5',\n",
       "       '4.8/5', '3.9 /5', '4.2 /5', '4.0 /5', '4.1 /5', '2.9 /5',\n",
       "       '2.7 /5', '2.5 /5', '2.6 /5', '4.5 /5', '4.3 /5', '3.7 /5',\n",
       "       '4.4 /5', '4.9/5'], dtype=object)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato['rate'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d36ddc3e-ec66-423c-a54c-fc607eb005e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.9/5     188\n",
       "3.8/5     178\n",
       "4.0/5     148\n",
       "4.1/5     141\n",
       "3.7/5     105\n",
       "4.2/5      90\n",
       "3.6/5      56\n",
       "4.3/5      48\n",
       "4.4/5      36\n",
       "3.5/5      29\n",
       "3.0/5      28\n",
       "2.9/5      25\n",
       "3.2/5      23\n",
       "2.7/5      14\n",
       "3.4/5      14\n",
       "3.3/5      14\n",
       "2.8/5      14\n",
       "2.6/5      12\n",
       "4.5/5      12\n",
       "3.1/5      12\n",
       "4.1 /5     12\n",
       "4.2 /5      8\n",
       "4.6/5       8\n",
       "NEW         7\n",
       "4.0 /5      7\n",
       "2.4/5       5\n",
       "2.5/5       5\n",
       "4.7/5       5\n",
       "2.3/5       4\n",
       "3.8 /5      4\n",
       "3.9 /5      4\n",
       "4.3 /5      3\n",
       "4.8/5       2\n",
       "2.9 /5      1\n",
       "2.7 /5      1\n",
       "2.5 /5      1\n",
       "2.6 /5      1\n",
       "4.5 /5      1\n",
       "2.2/5       1\n",
       "3.7 /5      1\n",
       "4.4 /5      1\n",
       "4.9/5       1\n",
       "Name: rate, dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.rate.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "2f2b6cc4-113e-40ca-a012-b1fbd558525d",
   "metadata": {},
   "outputs": [],
   "source": [
    "zomato = zomato.loc[zomato.rate != 'NEW']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "4a635c8e-2ab4-47f9-bb78-fd2cf4bc4e50",
   "metadata": {},
   "outputs": [],
   "source": [
    "remove_slash = lambda x:x.replace('/5','')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "4794f645-6df6-445d-b99d-1ebeabd804c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "zomato.rate  = zomato.rate.apply(remove_slash).str.strip().astype('float')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "cd9c3135-502d-4700-9584-0d00f527d617",
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
       "      <th>name</th>\n",
       "      <th>online_order</th>\n",
       "      <th>book_table</th>\n",
       "      <th>rate</th>\n",
       "      <th>votes</th>\n",
       "      <th>location</th>\n",
       "      <th>rest_type</th>\n",
       "      <th>cuisines</th>\n",
       "      <th>cost</th>\n",
       "      <th>city</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jalsa</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>4.1</td>\n",
       "      <td>775</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>North Indian, Mughlai, Chinese</td>\n",
       "      <td>800.0</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Spice Elephant</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>4.1</td>\n",
       "      <td>787</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>Chinese, North Indian, Thai</td>\n",
       "      <td>800.0</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>San Churro Cafe</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>3.8</td>\n",
       "      <td>918</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Cafe, Casual Dining</td>\n",
       "      <td>Cafe, Mexican, Italian</td>\n",
       "      <td>800.0</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Addhuri Udupi Bhojana</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>3.7</td>\n",
       "      <td>88</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Quick Bites</td>\n",
       "      <td>South Indian, North Indian</td>\n",
       "      <td>300.0</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Grand Village</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>3.8</td>\n",
       "      <td>166</td>\n",
       "      <td>Basavanagudi</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>North Indian, Rajasthani</td>\n",
       "      <td>600.0</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    name online_order book_table  rate  votes      location  \\\n",
       "0                  Jalsa          Yes        Yes   4.1    775  Banashankari   \n",
       "1         Spice Elephant          Yes         No   4.1    787  Banashankari   \n",
       "2        San Churro Cafe          Yes         No   3.8    918  Banashankari   \n",
       "3  Addhuri Udupi Bhojana           No         No   3.7     88  Banashankari   \n",
       "4          Grand Village           No         No   3.8    166  Basavanagudi   \n",
       "\n",
       "             rest_type                        cuisines   cost          city  \n",
       "0        Casual Dining  North Indian, Mughlai, Chinese  800.0  Banashankari  \n",
       "1        Casual Dining     Chinese, North Indian, Thai  800.0  Banashankari  \n",
       "2  Cafe, Casual Dining          Cafe, Mexican, Italian  800.0  Banashankari  \n",
       "3          Quick Bites      South Indian, North Indian  300.0  Banashankari  \n",
       "4        Casual Dining        North Indian, Rajasthani  600.0  Banashankari  "
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "5257e4fe-fd4a-42c5-a650-6cb0bf655304",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Yes    1005\n",
       "No      258\n",
       "Name: online_order, dtype: int64"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.online_order.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "ed7f6b5a-a388-40d3-8108-b7b86b25e392",
   "metadata": {},
   "outputs": [],
   "source": [
    "zomato.online_order.replace(('Yes','No'), (1,0), inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "6edadc12-0434-4193-8ab6-e22373a1aa63",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1    1005\n",
       "0     258\n",
       "Name: online_order, dtype: int64"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.online_order.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "b579ebfd-07e9-465d-b68d-9e1bcd94baf5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     1056\n",
       "Yes     207\n",
       "Name: book_table, dtype: int64"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.book_table.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "45b2c614-6a99-4431-bace-0a5e0664d2f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "zomato.book_table.replace(('Yes','No'), (1,0), inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "30b3441c-6f62-417c-956c-967e283dbd19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1056\n",
       "1     207\n",
       "Name: book_table, dtype: int64"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.book_table.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "c1e1d229-0b8d-4a53-a692-866483a37e84",
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
       "      <th>name</th>\n",
       "      <th>online_order</th>\n",
       "      <th>book_table</th>\n",
       "      <th>rate</th>\n",
       "      <th>votes</th>\n",
       "      <th>location</th>\n",
       "      <th>rest_type</th>\n",
       "      <th>cuisines</th>\n",
       "      <th>cost</th>\n",
       "      <th>city</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jalsa</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4.1</td>\n",
       "      <td>775</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>North Indian, Mughlai, Chinese</td>\n",
       "      <td>800.0</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Spice Elephant</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4.1</td>\n",
       "      <td>787</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>Chinese, North Indian, Thai</td>\n",
       "      <td>800.0</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>San Churro Cafe</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3.8</td>\n",
       "      <td>918</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Cafe, Casual Dining</td>\n",
       "      <td>Cafe, Mexican, Italian</td>\n",
       "      <td>800.0</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Addhuri Udupi Bhojana</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3.7</td>\n",
       "      <td>88</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Quick Bites</td>\n",
       "      <td>South Indian, North Indian</td>\n",
       "      <td>300.0</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Grand Village</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3.8</td>\n",
       "      <td>166</td>\n",
       "      <td>Basavanagudi</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>North Indian, Rajasthani</td>\n",
       "      <td>600.0</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    name  online_order  book_table  rate  votes      location  \\\n",
       "0                  Jalsa             1           1   4.1    775  Banashankari   \n",
       "1         Spice Elephant             1           0   4.1    787  Banashankari   \n",
       "2        San Churro Cafe             1           0   3.8    918  Banashankari   \n",
       "3  Addhuri Udupi Bhojana             0           0   3.7     88  Banashankari   \n",
       "4          Grand Village             0           0   3.8    166  Basavanagudi   \n",
       "\n",
       "             rest_type                        cuisines   cost          city  \n",
       "0        Casual Dining  North Indian, Mughlai, Chinese  800.0  Banashankari  \n",
       "1        Casual Dining     Chinese, North Indian, Thai  800.0  Banashankari  \n",
       "2  Cafe, Casual Dining          Cafe, Mexican, Italian  800.0  Banashankari  \n",
       "3          Quick Bites      South Indian, North Indian  300.0  Banashankari  \n",
       "4        Casual Dining        North Indian, Rajasthani  600.0  Banashankari  "
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "d29c2360-1e29-404c-9342-3b2c045b53db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Banashankari', 'Bannerghatta Road', 'Basavanagudi', 'Bellandur'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zomato.city.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "d582e8f0-637c-4691-8e56-4f4b5fd2946a",
   "metadata": {},
   "outputs": [],
   "source": [
    "zomato1 = zomato[['online_order','book_table','rate','votes','cost']]\n",
    "corr = zomato1.corr(method = 'kendall')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "0d3e83b0-7a7d-4db1-9a04-b3a8815e8190",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 1500x800 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (15,8))\n",
    "sns.heatmap(corr, annot = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "f2ea5b56-60b2-4b37-857a-b81995e732fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "X = zomato1.drop(['cost'], axis = 1)\n",
    "y = zomato1['cost']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "c035a0ee-4b17-4e8a-9b14-0b5296de68b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((1010, 4), (253, 4), (1010,), (253,))"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)\n",
    "X_train.shape, X_test.shape, y_train.shape, y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "02ed3e17-f2cf-4838-931e-8e157d0e84bc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "reg = LinearRegression()\n",
    "reg.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "bccd59f5-2f60-4405-8188-e1b4ce853e48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 492.59352764, 1041.02515609,  464.25906727,  428.40310357,\n",
       "        480.02195083, 1113.97866557,  454.5465854 ,  458.29936619,\n",
       "       1079.71302373,  471.14487333])"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred = reg.predict(X_test)\n",
    "y_pred[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "3c20e1aa-9009-4382-8471-472de552a3d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.44503765283086094"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import r2_score\n",
    "r2_score(y_test, y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "fcfd4056-6fd4-4390-a9fc-a94b4c899f12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-2 {color: black;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>DecisionTreeRegressor(min_samples_leaf=0.0001)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">DecisionTreeRegressor</label><div class=\"sk-toggleable__content\"><pre>DecisionTreeRegressor(min_samples_leaf=0.0001)</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "DecisionTreeRegressor(min_samples_leaf=0.0001)"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.tree import DecisionTreeRegressor\n",
    "dt = DecisionTreeRegressor(min_samples_leaf = 0.0001)\n",
    "dt.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "e56e199b-034f-4016-96de-06e1d890dbde",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 400.,  800.,  600., 1500.,  300., 1200.,  750.,  600.,  800.,\n",
       "        750.])"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_predit = dt.predict(X_test)\n",
    "y_predit[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "198ee624-379f-4f35-8870-616a79b20388",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.22074361227896666"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r2_score(y_test,y_predit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "426709d6-cea3-43f1-b682-70063d18ae38",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestRegressor\n",
    "rf = RandomForestRegressor(n_estimators = 500, random_state = 300, min_samples_leaf = 0.001)\n",
    "rf.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "7720711e-2393-4319-910a-8680c84ef871",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 484.19519841,  939.82293651,  575.0147619 ,  507.98746032,\n",
       "        485.74130952, 1151.94849206,  545.54107143,  574.3420671 ,\n",
       "        986.7784127 ,  621.04396465])"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_predited = rf.predict(X_test)\n",
    "y_predited[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "4666d81b-51f1-4b41-a881-3dde39a5bdbd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.49938015287202986"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r2_score(y_test,y_predited)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "ae51b65b-7e44-4b36-acb2-9abf23f9b37b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-4 {color: black;}#sk-container-id-4 pre{padding: 0;}#sk-container-id-4 div.sk-toggleable {background-color: white;}#sk-container-id-4 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-4 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-4 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-4 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-4 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-4 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-4 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-4 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-4 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-4 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-4 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-4 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-4 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-4 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-4 div.sk-item {position: relative;z-index: 1;}#sk-container-id-4 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-4 div.sk-item::before, #sk-container-id-4 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-4 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-4 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-4 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-4 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-4 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-4 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-4 div.sk-label-container {text-align: center;}#sk-container-id-4 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-4 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-4\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>ExtraTreesRegressor()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-4\" type=\"checkbox\" checked><label for=\"sk-estimator-id-4\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">ExtraTreesRegressor</label><div class=\"sk-toggleable__content\"><pre>ExtraTreesRegressor()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "ExtraTreesRegressor()"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import ExtraTreesRegressor\n",
    "et = ExtraTreesRegressor(n_estimators = 100)\n",
    "et.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "442c4766-7014-4ab4-b612-ae94af006d9a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 506. ,  800. ,  620. ,  530.5,  329. , 1200. ,  746.5,  530.5,\n",
       "        960. ,  750. ])"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_predited1 = et.predict(X_test)\n",
    "y_predited1[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "7b233138-aedd-49f0-8d1d-bf741bc28aae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.3506691285210082"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r2_score(y_test,y_predited1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a6140ee-ecd4-4819-938b-07a43f3ba91b",
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
