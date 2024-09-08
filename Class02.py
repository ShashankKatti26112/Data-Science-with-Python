{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4c628d60-0ef8-4436-bc04-0a6613b5c179",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to NUCOT's DataScience Class\n"
     ]
    }
   ],
   "source": [
    "print(\"Welcome to NUCOT's DataScience Class\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3f32ac80-6246-4905-85a1-ae2b4950a172",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = -5\n",
    "y = -10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "aa4babb9-7943-430a-ba30-bb413a00bfdf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Comprehension operators\n",
    "x == y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b9c9f00d-d022-40b4-9a6a-02039a05c3fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x != y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4aae44f9-5689-41b7-a317-1c06305e40c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x > y "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4825426c-cf6f-47b3-b8dc-4cccaa8aeb8e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x < y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "83ed01e4-77b7-4a87-9302-cf4789a0c8fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x >= y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7c4080fc-918d-4b1d-a226-9460e2b2a377",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x <= y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8db6a5e9-5f20-4f2a-9f0b-13acaeddb3ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "# conditional operators\n",
    "print(x < 10 and y > 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "97c3a849-3f03-4b90-be34-be35997b410c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(x < 10 or y > 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5667c0c7-393a-4e89-8078-11f2a1da5196",
   "metadata": {},
   "outputs": [],
   "source": [
    "# String literals \n",
    "name = 'Alice'\n",
    "age = 21"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "223ad1ec-056c-4bb4-aa52-978dd5cdba76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is Alice and I am 21 years old\n"
     ]
    }
   ],
   "source": [
    "message = f\"My name is {name} and I am {age} years old\"\n",
    "print(message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "7244b46f-8246-4873-8889-80c0dfb5e9ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Swapping of numbers \n",
    "\n",
    "x = 5 \n",
    "y = 10 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1521d2fe-7c9e-4a1b-864d-f4e0faf87aa3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Before Swapping\n",
      "x = 5\n",
      "y = 10\n",
      "After Swapping\n",
      "x = 10\n",
      "y = 5\n"
     ]
    }
   ],
   "source": [
    "print(\"Before Swapping\")\n",
    "print(\"x =\", x)\n",
    "print(\"y =\", y)\n",
    "\n",
    "print(\"After Swapping\")\n",
    "temp = x\n",
    "x = y\n",
    "y = temp\n",
    "print(\"x =\", x)\n",
    "print(\"y =\", y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "02c62b8d-8e11-4999-b6b8-d54b9bb8a781",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Before Swapping\n",
      "a = 5\n",
      "b = 6\n",
      "After Swapping\n",
      "a = 6\n",
      "b = 5\n"
     ]
    }
   ],
   "source": [
    "a = 5\n",
    "b = 6\n",
    "print(\"Before Swapping\")\n",
    "print(\"a =\", a)\n",
    "print(\"b =\", b)\n",
    "\n",
    "a,b = b,a\n",
    "\n",
    "print(\"After Swapping\")\n",
    "print(\"a =\", a)\n",
    "print(\"b =\", b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4048fcd9-72e2-4693-90ac-fc49646f3e90",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "BEFORE SWAPPING a = 6 b = 5\n",
      "AFTER SWAPPING a = 5 b = 6\n"
     ]
    }
   ],
   "source": [
    "# Formatted string literals\n",
    "print(f\"BEFORE SWAPPING a = {a} b = {b}\") \n",
    "print(f\"AFTER SWAPPING a = {b} b = {a}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c172892c-27eb-4116-b983-b1d1c1d7eb9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Agumented operators\n",
    "x = x + 5\n",
    "x += 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9ed69e59-3556-4c34-996e-8d8a923be5a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x raised to y =  25\n"
     ]
    }
   ],
   "source": [
    "# Lambda functions\n",
    "\n",
    "x = 5\n",
    "y = 2\n",
    "raise_to_power = lambda x,y : x ** y\n",
    "print(\"x raised to y = \", raise_to_power(x,y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "793ae1cb-0b7c-4a1b-8ec0-8194b5e74c05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n"
     ]
    }
   ],
   "source": [
    "x = 5\n",
    "y = 2\n",
    "a = x**y\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "2d160868-0773-4a97-84fd-d1fe8d5f8ad9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[169, 900, 1600, 2500]\n"
     ]
    }
   ],
   "source": [
    "# Map functions \n",
    "\n",
    "nums = [13,30,40,50]\n",
    "square_all = list(map(lambda nums : nums ** 2, nums))\n",
    "print(square_all)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "149fb3cc-b75b-4588-9317-5dc67b3bc0eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[100, 900, 2025, 6400, 10000, 62500, 3996001]\n"
     ]
    }
   ],
   "source": [
    "var = [10,30,45,80,100,250,1999]\n",
    "ans = list(map(lambda var: var**2, var))\n",
    "print(ans)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c0f19582-c7ab-442d-820e-e67dddc59d05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[32.0, 50.0, 68.0, 86.0]\n"
     ]
    }
   ],
   "source": [
    "deegre_temps = [0,10,20,30]\n",
    "farenhit_temp = list(map(lambda x: (x * 9/5) + 32, deegre_temps))\n",
    "print(farenhit_temp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "3dcf1bc4-be05-44e8-ab1a-2a9b2ec32604",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 20, 30, 40, 50, 48]\n"
     ]
    }
   ],
   "source": [
    "# filter function\n",
    "# syntax : filter(function, iteration)\n",
    "\n",
    "num = [10, 20, 30 , 40, 50 , 99, 48, 87]\n",
    "even = list(filter(lambda x : x % 2 == 0, num))\n",
    "print(even)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "109b241c-2097-40f7-94d8-d5b4e089c9df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7537185976320\n"
     ]
    }
   ],
   "source": [
    "# reduce function \n",
    "\n",
    "from functools import reduce\n",
    "numbers = [1,2,3,4,5,6,8,99,34,56,78,89]\n",
    "product = reduce(lambda x,y : x*y, numbers)\n",
    "print(product)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "371ac8f0-c6d9-40f0-b621-3d7a269df1a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-7537185976320\n"
     ]
    }
   ],
   "source": [
    "numbers = [1,2,3,4,5,-6,-8,99,34,56,-78,89]\n",
    "product = reduce(lambda x,y : x*y, numbers)\n",
    "print(product)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "7f0c0850-4a03-4bce-a6c6-c61785e6a0a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello World'"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Concatenation \n",
    "\n",
    "str1 = \"Hello\"\n",
    "str2 = \"World\"\n",
    "res = str1 +\" \"+str2\n",
    "res"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "3c5b14d5-1a72-44d5-a0b5-7d51cf76599a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python for Data Science\n"
     ]
    }
   ],
   "source": [
    "a = \"Python for\"\n",
    "b = \"Data Science\"\n",
    "text = a+ \" \"+b\n",
    "print(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a4b3e612-cd5d-4cca-988b-0d63bb1c8ffd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yth\n"
     ]
    }
   ],
   "source": [
    "# slicing \n",
    "\n",
    "# Python = 012345\n",
    "text = \"Python Language\"\n",
    "print(text[1:4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "cc546b3b-0f5c-409c-bd18-fe6b70a53d0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "# trying to search for \"is\" in the text\n",
    "text = \"Python is awesome\"\n",
    "print(text.find('is'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "7526666a-3319-4054-8604-32565bd1d314",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python is great\n"
     ]
    }
   ],
   "source": [
    "# replace function \n",
    "\n",
    "new_text = text.replace(\"awesome\", \"great\")\n",
    "print(new_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d6f50142-12af-4532-87bd-91ec69f47b9a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Python', 'is', 'fun']\n"
     ]
    }
   ],
   "source": [
    "# Breaking a string of substrings \n",
    "\n",
    "text = \"Python is fun\"\n",
    "words = text.split()\n",
    "print(words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "5fab42f8-61b8-419d-986b-c369d8176578",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Python ', ' fun']\n"
     ]
    }
   ],
   "source": [
    "\n",
    "text = \"Python is fun\"\n",
    "words = text.split('is')\n",
    "print(words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "bbf727a2-b302-409f-82cf-b9f9576ea816",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter value for m 5\n",
      "Enter value for n 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.81839487 0.05212173 0.16798653]\n",
      " [0.02409657 0.88624696 0.5724023 ]\n",
      " [0.56863129 0.9738209  0.00183716]\n",
      " [0.53220684 0.94230291 0.77353329]\n",
      " [0.30018593 0.01184925 0.17403108]]\n"
     ]
    }
   ],
   "source": [
    "# numpy is numerical python\n",
    "import numpy as np \n",
    "m = int(input(\"Enter value for m\"))\n",
    "n = int(input(\"Enter value for n\"))\n",
    "matrix = np.random.rand(m,n)\n",
    "print(matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "bc594512-405f-4ee3-b8ee-f2412b8cb214",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1\n",
       "1    2\n",
       "2    3\n",
       "3    4\n",
       "4    5\n",
       "dtype: int64"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "data = [1,2,3,4,5]\n",
    "series = pd.Series(data)\n",
    "series"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "14e404df-93d1-47c8-b771-4c0baa53d903",
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
       "      <th>Name</th>\n",
       "      <th>City</th>\n",
       "      <th>Degree</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>John</td>\n",
       "      <td>California</td>\n",
       "      <td>MS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Sahana</td>\n",
       "      <td>New York</td>\n",
       "      <td>MCA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Syeda</td>\n",
       "      <td>London</td>\n",
       "      <td>MBA</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Name        City Degree\n",
       "0    John  California     MS\n",
       "1  Sahana    New York    MCA\n",
       "2   Syeda      London    MBA"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = {'Name': [\"John\", \"Sahana\", \"Syeda\"], 'City': [\"California\", \"New York\", \"London\"], \"Degree\": ['MS', 'MCA', 'MBA']}\n",
    "df = pd.DataFrame(data)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "fdf01e05-5d85-4979-b020-f8e9577e35aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 1., 1.],\n",
       "       [1., 1., 1.],\n",
       "       [1., 1., 1.]])"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1 = np.zeros((3,3))\n",
    "arr2 = np.ones((3,3))\n",
    "result = arr1 + arr2\n",
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "72019f2f-4706-4c91-b3f9-dad0aeb0f790",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9.0"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total = np.sum(arr2)\n",
    "total"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "c41ab6ce-e5e4-40d5-88ad-7bae658dc53b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3,  7,  8,  9],\n",
       "       [ 4,  5,  6, 10, 11, 12]])"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1 = np.array([[1,2,3],[4,5,6]])\n",
    "arr2 = np.array([[7,8,9],[10,11,12]])\n",
    "hstack = np.hstack((arr1,arr2))\n",
    "hstack"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "0bbeea5f-86d4-4aee-9278-d97545135202",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3]\n",
      " [ 4  5  6]\n",
      " [ 7  8  9]\n",
      " [10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "vstack = np.vstack((arr1,arr2))\n",
    "print(vstack)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "f5236c03-28da-4bf7-901f-78d76cbf96a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Students  Subject  Score\n",
      "0     John     Math     85\n",
      "1    Alice     Math     90\n",
      "2      Bob     Math     88\n",
      "3     John  Science     78\n",
      "4    Alice  Science     66\n",
      "5      Bob  Science     35\n"
     ]
    }
   ],
   "source": [
    "# groupby functions\n",
    "data = {'Students': ['John', 'Alice', 'Bob', 'John','Alice','Bob'], 'Subject':['Math','Math','Math','Science','Science','Science'], 'Score': [85,90,88,78,66,35]}\n",
    "data = pd.DataFrame(data)\n",
    "print(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "f2fae99c-4d01-4660-ae5b-2ecb02a6a753",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Students\n",
       "Alice    156\n",
       "Bob      123\n",
       "John     163\n",
       "Name: Score, dtype: int64"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "group = data.groupby(\"Students\")['Score'].sum()\n",
    "group"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "79a356ef-6253-45cd-8937-76fce2b73639",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Students\n",
       "Alice    78.0\n",
       "Bob      61.5\n",
       "John     81.5\n",
       "Name: Score, dtype: float64"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "group = data.groupby(\"Students\")['Score'].mean()\n",
    "group"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "6ddc6536-b31d-4627-94bf-d2c6fb5fd6c4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Subject\n",
       "Math       263\n",
       "Science    179\n",
       "Name: Score, dtype: int64"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "group = data.groupby(\"Subject\")['Score'].sum()\n",
    "group"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "eac0711e-bc36-4ff3-b918-c0067deb36df",
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
       "      <th>Date</th>\n",
       "      <th>Product</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2022-01-01</td>\n",
       "      <td>A</td>\n",
       "      <td>100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022-01-02</td>\n",
       "      <td>B</td>\n",
       "      <td>150</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022-01-01</td>\n",
       "      <td>A</td>\n",
       "      <td>200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2022-01-02</td>\n",
       "      <td>B</td>\n",
       "      <td>120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2022-01-01</td>\n",
       "      <td>A</td>\n",
       "      <td>180</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date Product  Sales\n",
       "0  2022-01-01       A    100\n",
       "1  2022-01-02       B    150\n",
       "2  2022-01-01       A    200\n",
       "3  2022-01-02       B    120\n",
       "4  2022-01-01       A    180"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = {'Date': ['2022-01-01','2022-01-02','2022-01-01','2022-01-02','2022-01-01'], 'Product':['A','B','A','B','A'], 'Sales':[100,150,200,120,180]}\n",
    "data = pd.DataFrame(data)\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "a28364f9-f6c0-4602-bb20-ecd88c9af471",
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
       "      <th>Product</th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2022-01-01</th>\n",
       "      <td>480.0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-01-02</th>\n",
       "      <td>NaN</td>\n",
       "      <td>270.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Product         A      B\n",
       "Date                    \n",
       "2022-01-01  480.0    NaN\n",
       "2022-01-02    NaN  270.0"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pivottable = data.pivot_table(index = 'Date', columns = 'Product', values = 'Sales', aggfunc = 'sum')\n",
    "pivottable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68ace7d8-f051-4ff1-b7f8-309b7c8f92c9",
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
