{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Simple Linear Regression\n",
    "\n",
    "In this notebook, we'll build a linear regression model to predict `Sales` using an appropriate predictor variable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Reading and Understanding the Data\n",
    "\n",
    "Let's start with the following steps:\n",
    "\n",
    "1. Importing data using the pandas library\n",
    "2. Understanding the structure of the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Supress Warnings\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the numpy and pandas package\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
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
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Read the given CSV file, and view some sample records\n",
    "\n",
    "advertising = pd.read_csv(\"advertising.csv\")\n",
    "advertising.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's inspect the various aspects of our dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(200, 4)"
      ]
     },
     "execution_count": 7,
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
   "execution_count": 8,
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
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "advertising.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: Visualising the Data\n",
    "\n",
    "Let's now visualise our data using seaborn. We'll first make a pairplot of all the variables present to visualise which variables are most correlated to `Sales`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt \n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABJ4AAAGOCAYAAADW/cnWAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAACu8ElEQVR4nOzdeXxU9b0//le2STLZSQyECiEyoYosxqJWEhax7va6cL0t7b0Fwr23rYJa7q1rqVgVsL3124vbvW0F6e9WtBXFpXZxqcjS2oJBFjeCEaKAMSGZkEwyk+X8/ohnmOWcM2dmzpnzOWdez8fDx0My2zkz57w/7/M+nyVDkiQJREREREREREREBsu0egOIiIiIiIiIiMiZWHgiIiIiIiIiIiJTsPBERERERERERESmYOGJiIiIiIiIiIhMwcITERERERERERGZgoUnIiIiIiIiIiIyBQtPRERERERERERkChaeiIiIiIiIiIjIFI4vPEmShO7ubkiSZPWmEBGRgRjfiYicifGdiMhZHF94OnHiBEpKSnDixAmrN4WIiAzE+E5E5EyM70REzuL4whMREREREREREVmDhSciIiIiIiIiIjIFC09ERERERERERGQKFp6IiIiIiIiIiMgULDwREREREREREZEpWHgiIiIiIiIiIiJTsPBERERERERERESmYOGJiIiIiIiIiIhMwcITERERERERERGZgoUnIiIiIiIiIiIyRbbVG0BERKnh9QXQ3hNAd/8AivNzUFHgQonbZfVmEZmCxzsRERGRGDkRC09ERGngSFcfbt20B1sPtAf/Nru2AmvmT8PY0nwLt4zIeDzeiYiIiMTJiTjUjojI4by+QFSDAwBvHGjHbZv2wOsLWLRlRMbj8U5EREQkVk7EwhMRkcO19wSiGhzZGwfa0d7DC3FyDh7vRERERGLlRCw8ERE5XHf/gObjJ2I8TmQnPN6JiIiIxMqJWHgiInK44rwczceLYjxOZCc83omIiIjEyolYeCIicriKQhdm11YoPja7tgIVhVzpi5yDxzsRERGRWDkRC09ERA5X4nZhzfxpUQ3P7NoK3D9/GpeYJ0fh8U5EREQkVk6UIUmSlLJPs0B3dzdKSkrg9XpRXFxs9eYQEVnG6wugvSeAE/0DKMrLQUWhy9YX4YzvpMVpxztROmF8JyIyjgg5UXZKP42IiCxT4uaF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5CRs14goFVh40qGi0IXZtRWKj82urUBFIVd8ICJKB2wPiIjISdiuEVEqsPCkQ4nbhTXzp0UF5dm1Fbh//jQuNUpElCbYHhARkZOwXSOiVMiQJEmyeiPM1N3djZKSEni9XhQXFyf1Xl5fAO09AZzoH0BRXg4qCl0MxkREFjEyvseL7QERkXmsjO/piu0aEZkp2+oNsJMSNwMwERGxPSAiImdhu0ZEZuJQOyIiIiIiIiIiMgULT0REREREREREZAoWnoiIiIiIiIiIyBQsPBERERERERERkSlYeCIiIiIiIiIiIlOw8ERERERERERERKZg4YmIiIiIiIiIiEzBwhMREREREREREZmChSciIiIiIiIiIjIFC09ERERERERERGSKbKs3QHReXwDtPQF09w+gOD8HFQUulLhdVm8WEREJju0HERERkTiYm1mHhScNR7r6cOumPdh6oD34t9m1FVgzfxrGluZbuGVERCQyth9ERERE4mBuZi0OtVPh9QWiDkwAeONAO27btAdeX8CiLSMiIpGx/SAiIiISB3Mz67HwpKK9JxB1YMreONCO9h4enEREFI3tBxEREZE4mJtZj4UnFd39A5qPn4jxOBERpSe2H0RERETiYG5mPRaeVBTn5Wg+XhTjcSIiSk9sP4iIiIjEwdzMeiw8qagodGF2bYXiY7NrK1BRyNnviYgoGtsPIiIiInEwN7MeC08qStwurJk/LeoAnV1bgfvnT+Oyi0REpIjtBxEREZE4mJtZL0OSJMnqjTBTd3c3SkpK4PV6UVxcHPfrvb4A2nsCONE/gKK8HFQUunhgEhEJINn4bja2H0REiRE9vhORPTE3s0621RsguhI3D0YiIoof2w8iIiIicTA3sw6H2hERERERERERkSlYeCIiIiIiIiIiIlOw8ERERERERERERKZg4YmIiIiIiIiIiEzBwhMREREREREREZmChSciIiIiIiIiIjIFC09ERERERERERGQKFp6IiIiIiIiIiMgU2VZvgNkkSQIAdHd3W7wlREQUS1FRETIyMnQ9l/GdiMg+GN+JiJxJT3x3fOHpxIkTAIBx48ZZvCVERBSL1+tFcXGxrucyvhMR2QfjOxGRM+mJ7xmSfEvBoYaHh3HkyJG47rKE6u7uxrhx49Da2qq7sbQTJ++fk/cN4P7ZnZP3L5l9iydWM77rw/10Fu6ns6TL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7dmzR7rjjjukzMxM6U9/+pMkSfb63ZwU32VGnVt2FLoyjSQ5Yz//9re/SdnZ2dJ9990nHThwQPr1r38tud1u6f/+7/+Cz3HCfi5cuFD6whe+IL344otSS0uL9Mwzz0gVFRXSLbfcEnyOHffTyXmKHTgxxuthxHHnBOncHoYyIm9zMifmDrFYXRNg4UnDww8/LFVXV0sul0s6++yzw5ZFt5Ovfe1rUlVVlZSTkyONHTtWuvbaa6X9+/cHHx8eHpbuuusuacyYMVJubq40e/Zsae/evRZusbY///nPEoCo/xYuXChJkr796evrk5YuXSqNGjVKys/Pl6688krp8OHDFuxNOK198/l80sUXXyydcsopUk5OjjR+/Hhp4cKFUdst6r5JkqS4bwCk9evXB59j198v1r7Z/fdrbGwMxsNTTjlFuvDCC4PJiyTZ73dzSnyXGXVu2VFk8uiU/XzhhRekKVOmSLm5udLpp58u/fznPw973An72d3dLd10003S+PHjpby8POm0006T7rzzTsnv9wefY8f9dHKeYhdOi/F6GHHcOUE6t4ehjMjbnMypuYMWq2sCGZIkScb0nSIiIiIiIiIiIjqJczwREREREREREZEpWHgiIiIiIiIiIiJTsPBERERERERERESmYOGJiIiIiIiIiIhMwcITERERERERERGZgoUnIiIiIiIiIiIyBQtPRERERERERERkChaeiIiIiIiIiFJo0aJFuPrqq4P/njt3Lm6++WbLtofITCw8EQkmIyND87/LLrsMOTk5+L//+z/F13/729/GtGnTUrzVRET2s2jRImRkZGDNmjVhf9+8eTMyMjIs2ioiIhKJ3FZkZGQgOzsb48ePx3e/+110dnYa+jnPPPMM7rnnHkPfk0gULDwRCebo0aPB/372s5+huLg47G9PPvkkrrjiCqxfvz7qtX19fXjyySexZMkSC7aciMh+8vLycP/99xt+AeE0AwMDVm8CEZFlLr30Uhw9ehQfffQRfvnLX+KFF17A9ddfb+hnjBo1CkVFRYa+J5EoWHgiEsyYMWOC/5WUlCAjIyPqb0uWLMGf//xnfPTRR2Gvffrpp9Hf349//ud/tmbjiYhs5itf+QrGjBmD1atXqz5nx44dmD17NvLz8zFu3DjceOON6O3tBQA8+OCDmDp1avC5cm+phx9+OPi3Sy65BLfffjsA4O2338YFF1yAoqIiFBcX40tf+hJ27twJAHj88cdRWlqKzZs3Y9KkScjLy8NFF12E1tbW4HsdPHgQV111FUaPHo3CwkKcc845eOWVV8K2d8KECbjnnnvwjW98A4WFhRg7diwefPDBsOd4vV78+7//OyorK1FcXIx58+bh7bffDj6+cuVKnHXWWVi3bh1OO+005ObmQpKkeL9eIiJHyM3NxZgxY3Dqqafi4osvxte+9jX86U9/AgAMDQ1hyZIlqKmpQX5+Pr74xS/iv//7v8NePzQ0hOXLl6O0tBTl5eW45ZZbomJq5FC7zs5OfOtb30JZWRncbjcuu+wyHDhwwPR9JTIDC09ENnT55ZdjzJgxePzxx8P+vm7dOlx99dUoLy+3ZsOIiGwmKysLq1atwoMPPoiPP/446vG9e/fikksuwbXXXos9e/bgqaeewrZt27B06VIAIxcK+/fvR3t7OwBgy5YtqKiowJYtWwAAg4OD2LFjB+bMmQMA+OY3v4lTTz0Vf//737Fr1y7cdtttyMnJCX6ez+fDfffdhw0bNmD79u3o7u7G17/+9eDjPT09uPzyy/HKK6+gqakJl1xyCb761a/i8OHDYdv9k5/8BNOmTcNbb72F22+/Hd/73vfw8ssvAwAkScIVV1yBY8eO4aWXXsKuXbtw9tln48ILL8Tx48eD79Hc3Izf/OY32LRpE3bv3m3At01EZH8ffvgh/vCHPwRj9/DwME499VT85je/wTvvvIMf/vCHuOOOO/Cb3/wm+Jqf/vSnWLduHR577DFs27YNx48fx7PPPqv5OYsWLcLOnTvx/PPP4y9/+QskScLll1/OHqhkTxIRCWv9+vVSSUmJ4mO33nqrVF1dLQ0PD0uSJEkffvihlJGRIf3xj39M4RYSEdnXwoULpauuukqSJEn68pe/LDU2NkqSJEnPPvusJKdI//Iv/yL9+7//e9jrtm7dKmVmZkp9fX3S8PCwVFFRIT399NOSJEnSWWedJa1evVqqrKyUJEmSduzYIWVnZ0snTpyQJEmSioqKpMcff1xxe9avXy8BkP76178G//buu+9KAKQ333xTdT8mT54sPfjgg8F/V1dXS5deemnYc772ta9Jl112mSRJkvTqq69KxcXFUn9/f9hzJk6cKP3v//6vJEmSdNddd0k5OTlSW1ub6ucSEaWDhQsXSllZWVJBQYGUl5cnAZAASA888IDqa66//npp/vz5wX9XVVVJa9asCf57YGBAOvXUU4NtkCRJ0pw5c6SbbrpJkiRJ+uCDDyQA0vbt24OPt7e3S/n5+dJvfvMb43aOKEXY44nIppYsWYJDhw7htddeAzDS2+nUU0/FV77yFYu3jIjIfu6//35s2LAB77zzTtjfd+3ahccffxyFhYXB/y655BIMDw+jpaUFGRkZmD17Nl5//XV0dXVh//79+M53voOhoSG8++67eP3113H22WejsLAQALB8+XL867/+K77yla9gzZo1OHjwYNjnZWdnY8aMGcF/n3766SgtLcW7774LAOjt7cUtt9yCyZMno7S0FIWFhXjvvfeiejydf/75Uf+W32PXrl3o6elBeXl52H61tLSEbU91dTVOOeWUJL9ZIiL7u+CCC7B79268+eabWLZsGS655BIsW7Ys+Pj//M//YMaMGTjllFNQWFiIX/ziF8G47PV6cfTo0bC4HBnrI7377rvIzs7GeeedF/xbeXk5vvjFLwZjOZGdsPBEZFO1tbWYNWsW1q9fj+HhYWzYsAGLFy9GZiZPayKieM2ePRuXXHIJ7rjjjrC/Dw8P49vf/jZ2794d/O/tt9/GgQMHMHHiRAAjw+1ef/11bN26FdOnT0dpaSlmz56NLVu24PXXX8fcuXOD77dy5Urs378fV1xxBV577TVMnjw5ariF0op68t++//3vY9OmTbjvvvuwdetW7N69G1OnTkUgEIi5j/J7DA8Po6qqKmyfdu/ejffffx/f//73g88vKCjQ9+URETlcQUEBPB4Ppk2bhrVr18Lv9+Puu+8GAPzmN7/B9773PTQ2NuJPf/oTdu/ejcWLF+uKy2oklTn1JEniqqtkS9lWbwARJW7JkiX47ne/i6uuugoff/wxFi9ebPUmERHZ1po1a3DWWWdh0qRJwb+dffbZ2L9/Pzwej+rr5s6di5tuuglPP/10sMg0Z84cvPLKK9ixYwduuummsOdPmjQJkyZNwve+9z0sWLAA69evxzXXXANgZE6onTt34txzzwUAvP/+++jq6sLpp58OANi6dSsWLVoUfH5PT0/UQhMA8Ne//jXq3/J7nH322Th27Biys7MxYcIE/V8QEREBAO666y5cdtll+O53v4utW7di5syZYavchfYeLSkpQVVVFf76179i9uzZAEZivTy/npLJkydjcHAQb775JmbOnAkA6OjowAcffIAzzjjDxD0jMge7RhDZ2HXXXYecnBx8+9vfxoUXXsgLCCKiJEydOhXf/OY3w1aAu/XWW/GXv/wFN9xwA3bv3o0DBw7g+eefDxtiMWXKFJSXl+PXv/51sPA0d+5cbN68GX19fWhoaAAA9PX1YenSpXj99ddx6NAhbN++HX//+9/DLiJycnKwbNkyvPnmm3jrrbewePFifPnLXw4WojweD5555plgz6tvfOMbGB4ejtqX7du348c//jE++OADPPzww/jtb38bLIB95Stfwfnnn4+rr74af/zjH/HRRx9hx44d+MEPfhBcYY+IiNTNnTsXZ555JlatWgWPx4OdO3fij3/8Iz744AOsWLECf//738Oef9NNN2HNmjV49tln8d57/397d6/SSBuGAfi2VFCxErGxMaUwWMgIsQ2CErHQIBIkYGM1aGFllVo8AAstPYL0gq2F3YKNJxD0DLKFEBA+PxbW2cXlutr54Zkp3uJ+n4f3R05OTvL29vbp+5eXl9Nut3N8fJyHh4c8PT3l8PAwi4uLabfbNX8dfD3BE3xjU1NT6XQ6eX19Ta/X+9vlAHx7/X7/w4jDyspK7u/v8/z8nGazmaIocnFxkYWFhfE9ExMT41Prms3m+LnZ2dkURZGZmZkk7yfoDYfDdLvdNBqN7O3tZXNzczyukbyv6+fn5zk4OEhZlpmcnMzd3d34+tXVVebm5rK+vp7t7e20Wq3/3DE/OzvL4+NjiqJIv9/P5eVlWq3WuN7BYJCNjY30er00Go10Op28vLxkfn7+C/8mwL/r9PQ019fX2dnZye7ubvb397O2tpbhcPih+yl5X5O73W6Ojo5SlmWmp6fHnaufubm5yerqara2tlKWZUajUQaDwYeTUOG7mBh9NkAKAMAfc3t7m6qq/ncX/FcsLS2lqqpUVfUldQEA/A4dTwAAAADUQvAEAAAAQC2M2gEAAABQCx1PAAAAANRC8AQAAABALQRPAAAAANRC8AQAAABALQRPAAAAANRC8AQAAABALQRPAAAAANRC8AQAAABALQRPAAAAANTiJ5mHsDqKNjpNAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1200x400 with 3 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(advertising, x_vars=['TV', 'Newspaper', 'Radio'], y_vars='Sales',size=4, aspect=1, kind='scatter')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
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
    "sns.heatmap(advertising.corr(), cmap=\"YlGnBu\", annot = True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As is visible from the pairplot and the heatmap, the variable `TV` seems to be most correlated with `Sales`. So let's go ahead and perform simple linear regression using `TV` as our feature variable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## Step 3: Performing Simple Linear Regression\n",
    "\n",
    "Equation of linear regression<br>\n",
    "$y = c + m_1x_1 + m_2x_2 + ... + m_nx_n$\n",
    "\n",
    "-  $y$ is the response\n",
    "-  $c$ is the intercept\n",
    "-  $m_1$ is the coefficient for the first feature\n",
    "-  $m_n$ is the coefficient for the nth feature<br>\n",
    "\n",
    "In our case:\n",
    "\n",
    "$y = c + m_1 \\times TV$\n",
    "\n",
    "The $m$ values are called the model **coefficients** or **model parameters**.\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Generic Steps in model building using `statsmodels`\n",
    "\n",
    "We first assign the feature variable, `TV`, in this case, to the variable `X` and the response variable, `Sales`, to the variable `y`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = advertising['TV']\n",
    "y = advertising['Sales']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Train-Test Split\n",
    "\n",
    "You now need to split our variable into training and testing sets. You'll perform this by importing `train_test_split` from the `sklearn.model_selection` library. It is usually a good practice to keep 70% of the data in your train dataset and the rest 30% in your test dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "74     213.4\n",
       "3      151.5\n",
       "185    205.0\n",
       "26     142.9\n",
       "90     134.3\n",
       "Name: TV, dtype: float64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Let's now take a look at the train dataset\n",
    "\n",
    "X_train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "74     17.0\n",
       "3      16.5\n",
       "185    22.6\n",
       "26     15.0\n",
       "90     14.0\n",
       "Name: Sales, dtype: float64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Building a Linear Model\n",
    "\n",
    "You first need to import the `statsmodel.api` library using which you'll perform the linear regression."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "import statsmodels.api as sm"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "By default, the `statsmodels` library fits a line on the dataset which passes through the origin. But in order to have an intercept, you need to manually use the `add_constant` attribute of `statsmodels`. And once you've added the constant to your `X_train` dataset, you can go ahead and fit a regression line using the `OLS` (Ordinary Least Squares) attribute of `statsmodels` as shown below"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add a constant to get an intercept\n",
    "X_train_sm = sm.add_constant(X_train)\n",
    "\n",
    "# Fit the resgression line using 'OLS'\n",
    "lr = sm.OLS(y_train, X_train_sm).fit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "const    6.948683\n",
       "TV       0.054546\n",
       "dtype: float64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print the parameters, i.e. the intercept and the slope of the regression line fitted\n",
    "lr.params"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                            OLS Regression Results                            \n",
      "==============================================================================\n",
      "Dep. Variable:                  Sales   R-squared:                       0.816\n",
      "Model:                            OLS   Adj. R-squared:                  0.814\n",
      "Method:                 Least Squares   F-statistic:                     611.2\n",
      "Date:                Wed, 02 Oct 2024   Prob (F-statistic):           1.52e-52\n",
      "Time:                        04:00:26   Log-Likelihood:                -321.12\n",
      "No. Observations:                 140   AIC:                             646.2\n",
      "Df Residuals:                     138   BIC:                             652.1\n",
      "Df Model:                           1                                         \n",
      "Covariance Type:            nonrobust                                         \n",
      "==============================================================================\n",
      "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
      "------------------------------------------------------------------------------\n",
      "const          6.9487      0.385     18.068      0.000       6.188       7.709\n",
      "TV             0.0545      0.002     24.722      0.000       0.050       0.059\n",
      "==============================================================================\n",
      "Omnibus:                        0.027   Durbin-Watson:                   2.196\n",
      "Prob(Omnibus):                  0.987   Jarque-Bera (JB):                0.150\n",
      "Skew:                          -0.006   Prob(JB):                        0.928\n",
      "Kurtosis:                       2.840   Cond. No.                         328.\n",
      "==============================================================================\n",
      "\n",
      "Notes:\n",
      "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n"
     ]
    }
   ],
   "source": [
    "# Performing a summary operation lists out all the different parameters of the regression line fitted\n",
    "print(lr.summary())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "####  Looking at some key statistics from the summary"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The values we are concerned with are - \n",
    "1. The coefficients and significance (p-values)\n",
    "2. R-squared\n",
    "3. F statistic and its significance"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### 1. The coefficient for TV is 0.054, with a very low p value\n",
    "The coefficient is statistically significant. So the association is not purely by chance. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### 2. R - squared is 0.816\n",
    "Meaning that 81.6% of the variance in `Sales` is explained by `TV`\n",
    "\n",
    "This is a decent R-squared value."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### 3. F statistic has a very low p value (practically low)\n",
    "Meaning that the model fit is statistically significant, and the explained variance isn't purely by chance."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "The fit is significant. Let's visualize how well the model fit the data.\n",
    "\n",
    "From the parameters that we get, our linear regression equation becomes:\n",
    "\n",
    "$ Sales = 6.948 + 0.054 \\times TV $"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "scrolled": true
   },
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
    "plt.scatter(X_train, y_train)\n",
    "plt.plot(X_train, 6.948 + 0.054*X_train, 'r')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Residual analysis \n",
    "To validate assumptions of the model, and hence the reliability for inference"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Distribution of the error terms\n",
    "We need to check if the error terms are also normally distributed (which is infact, one of the major assumptions of linear regression), let us plot the histogram of the error terms and see what it looks like."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_train_pred = lr.predict(X_train_sm)\n",
    "res = (y_train - y_train_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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9p7GYG9vj3fffRcSiQQXL14UuxyidosBiIhalY2NDZ5//nnodDrMmzcPJSUlhn3Xr1/HP//5TwDA//3f/7VpXa+++iqsrKywcOFC/PDDD7X25+XlYe3atSgrK2vTuu71xRdf4NKlS7W2//zzzxAEodXGRxGZA94CIzJTDa347uvri5UrVxrtvVatWoXTp08jMjISnTt3xogRIwwTIZaXl+OVV17BX/7yF6O9X2N07doVX375JZ599lmMHz8e3bt3R1BQEARBQHJyMq5cuQKNRoOpU6fCysqqTWurtmfPHkyfPh2BgYF44IEHYGVlhaSkJJw+fRoymQzvvvuuKHURdQQMQERm6vPPP693X58+fYwagOzs7HD8+HF8+OGH2LVrF/bv3w+5XI4BAwZg7ty5ePrpp432Xk3x+OOP48KFC/jwww8RGRmJn376CUqlEl5eXnjmmWfwxBNP1HoqrS0tWrQInTp1wqlTp3Dy5EmUlJTA29sbTz/9NBYvXox+/fqJVhtRe8fV4ImIiMjscAwQERERmR0GICIiIjI7DEBERERkdhiAiIiIyOwwABEREZHZYQAiIiIis8MARERERGaHAYiIiIjMDgMQERERmR0GICIiIjI7DEBERERkdhiAiIiIyOwwABEREZHZYQAiIiIis8MARERERGaHAYiIiIjMDgMQERERmR0GICIiIjI7DEBERERkdhiAiIiIyOwwABEREZHZYQAiIiIis8MARERERGaHAYiIiIjMDgMQERERmR0GICIiIjI7DEBERERkdhiAiIiIyOwwABEREZHZsRC7AFOk0+mQkZEBOzs7SCQSscshIiKiRhAEAUVFRfDy8oJU2nAfDwNQHTIyMuDj4yN2GURERNQMqamp6NSpU4NtGIDqYGdnB0D/Adrb24tcDRERETWGWq2Gj4+P4ed4QxiA6lB928ve3p4BiIiIqJ1pzPAVDoImIiIis8MARERERGaHAYiIiIjMDgMQERERmR0GICIiIjI7DEBERERkdhiAiIiIyOwwABEREZHZYQAiIiIis8MARERERGaHAYiIiIjMDgMQERERmR0GICIiIjI7DEBERERkdhiAiIiIyOxYiF0AEZGx7DiTInYJ9zV1sK/YJRAR2ANEREREZogBiIiIiMwOAxARERGZHQYgIiIiMjsMQERERGR2GICIiIjI7DAAERERkdlh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dlxUuKl6ezvAQipBdlEF0gvKxC6HyGwwABFRi8RnqgEAPT3tua5VM1jJZQj2VgEAzifni1wNkflgACKiZtPqBFzLKgIABHly5ffmCvFzBABcSC2ApkoncjVE5oEBiIiaLTWvFGWVWlhZyuDrzLW/mivAxQaO1paoqNLhSmah2OUQmQUGICJqtuu39b0/Xd1tIeXtr2aTSiTof7cXiLfBiNoGAxARNVt1AOrmbidyJe1ff19HSAAk3ClBfolG7HKIOjwGICJqlqLySmQUlgNgADIGR2s5Al1tAQAxKewFImptDEBE1CzXbxcDALwdrGCr4JRixlA9GPq35HzoBC6QStSaGICIqFl4+8v4enrZQ2kpRUFZJZJzS8Uuh6hDYwAioibT6gTcyNYHoO7utiJX03FYyqTo5aWfEygulbfBiFoTAxARNVlafinKK3WwspShkxMffzemvj4OAICL6YWo0nJOIKLWwgBERE12M1s//qeLGx9/N7YAFxvYKy1QXqnDtbu3GYnI+BiAiKjJbt65G4BcefvL2KQSCfp0cgAAxKUWiFoLUUfGAERETVJRqUVqnn6AbqAbA1Br6OvrAAC4mlWEMo1W3GKIOigGICJqksTcEugEwMlGDicbudjldEge9kq42Smg1Qm4nMGlMYhaAwMQETWJYfwPb3+1GolEgn53B0PH8jYYUatgACKiJqkOQLz91bp63w1ASTklKCyrFLcYog6IAYiIGk1dXonsogpIAAS62IhdTofmaC2Hv7MNBAAX2AtEZHQMQETUaLfu9v54OVjBmstftLrqOYH4NBiR8TEAEVGjJdwpAQAEurL3py084K2CTCpBlrocWXcXniUi42AAIqJGS8jR9wB15gDoNmEll6H73bXW2AtEZFwMQETUKPmlGuSXVkIqAfycufxFW+lz9zbY7+kFELhCPJHRMAARUaMk3r395e1gBYWFTORqzEcPDzvILaQoKK1ESh5XiCcyFtED0Nq1axEQEAClUomQkBCcPHmy3raZmZmYOnUqunfvDqlUigULFtRqs3HjRoSHh8PR0RGOjo4YNWoUzp4924pXQGQeEnL0AYi3v9qWpUyKXp72AIALaZwUkchYRA1Au3btwoIFC7B8+XLExsYiPDwcY8aMQUpKSp3tKyoq4OrqiuXLl6NPnz51tjl27BiefvppHD16FNHR0fD19UVERATS09Nb81KIOrzEu+N/Avj4e5vrfXdtsIvphdDqeBuMyBhEDUCrV6/GrFmzMHv2bAQFBWHNmjXw8fHBunXr6mzv7++P//znP5g+fTpUKlWdbb766ivMnTsXffv2RY8ePbBx40bodDr88ssv9dZRUVEBtVpd40VEf8gv4fgfMXVxs4W1XIaSiirDQHQiahnRApBGo0FMTAwiIiJqbI+IiEBUVJTR3qe0tBSVlZVwcnKqt82qVaugUqkMLx8fH6O9P1FHUH37q5OjNcf/iEAmlSDYW/+PvgupvA1GZAyiBaCcnBxotVq4u7vX2O7u7o6srCyjvc/SpUvh7e2NUaNG1dtm2bJlKCwsNLxSU1ON9v5EHQFvf4mvz93bYJczClGp1YlbDFEHIPpUrhKJpMavBUGota253n//fXz99dc4duwYlEplve0UCgUUCoVR3pOoI0q82wPEACQeP2drqKwsUVhWieu3i9DLq+5hAETUOKL1ALm4uEAmk9Xq7cnOzq7VK9QcH3zwAd59910cOnQIvXv3bvH5iMxVVmE58ksrIQHg68TxP2KRSiToXX0bjE+DEbWYaAFILpcjJCQEkZGRNbZHRkYiLCysRef+97//jbfffhs///wzBgwY0KJzEZm788l5AABPlRJKS47/EVP1CvFXM9WoqNSKWwxROyfqLbBFixZh2rRpGDBgAEJDQ7FhwwakpKRgzpw5APRjc9LT07F9+3bDMXFxcQCA4uJi3LlzB3FxcZDL5ejZsycA/W2vN954Azt27IC/v7+hh8nW1ha2tpy/hKipziflAwD8nHn7S2xeKiVcbOXIKdbgSqYa/XwdxS6JqN0SNQBNnjwZubm5WLlyJTIzMxEcHIwDBw7Az88PgH7iwz/PCdSvXz/D/8fExGDHjh3w8/NDUlISAP3EihqNBn/9619rHLdixQq8+eabrXo9RB3RuSR9DxAffxefRCJB704OOHI1GxfSChiAiFpA9EHQc+fOxdy5c+vct23btlrb7rcWTnUQIqKWKyqvRHymfl4s9gCZhj53A9DN7GKUVFTBRiH6X+NE7ZLoS2EQkemKTSmATgAcrS2hsrIUuxwC4GqngJeDEjoBuJTBwdBEzcUARET1On/39pc/e39MSvWcQJwUkaj52HdK1MHsOFP3WnrN8b/fMwHw9pepecBbhZ8uZSEptwQFpRqxyyFql9gDRER1qtLpkJpfCoADoE2Ng7Uc/nd/Ty6msxeIqDkYgIioTpkF5ajUCrCylMHVjjOlm5rqFeIvpBWIWgdRe8UARER1SsrVL3/h52wNqZGWpyHjecBbBakEyCgoR8IdrhBP1FQMQERUp+Rc/e0vDoA2TTYKC3Rx00/uuv9ChsjVELU/DEBEVIsgCDV6gMg0VT8Ntj8u475zpBFRTQxARFRLTrEGpRotLKQSeDtYiV0O1aOnpz0spBIk5JTgcoZa7HKI2hUGICKqJflu708nR2tYyPjXhKlSWMrQw8MOAG+DETUV/2YjolqSDON/ePvL1FU/DfbDhQzodLwNRtRYDEBEVEuyYfwPB0Cbuu4edrBTWCCzsBznk/PFLoeo3WAAIqIaisorkVuigQSArxN7gEydpUyK0cEeAIDv49JFroao/WAAIqIaqh9/d7dXwkouE7kaaozxfbwAAAcuZqJSqxO5GqL2gQGIiGqoXv7Ch70/7UZYoDNcbOXIL63ErzdzxC6HqF1gACKiGlLy9AGIt7/aDwuZFGMf8AQA/BDHp8GIGoMBiIgMtDoB6fllAAAfJ87/055M6Ku/DXbwchbKK7UiV0Nk+hiAiMggq7AcVToBSkspXGy5AGp70t/XEd4OVijRaPFLfLbY5RCZPAYgIjJIqR7/48gFUNsbiUSCcXcHQ++/wKfBiO6HAYiIDFLzOAC6Pat+GuzotTtQl1eKXA2RaWMAIiIDDoBu34I87dDFzRaaKh0OXsoSuxwik8YAREQAgOKKKuSVaADob4FR+yORSAy9QFwbjKhhDEBEBABIu9v742qr4ASI7Vh1ADp1Mwd3iipErobIdDEAERGAewZA8/ZXu+bvYoM+nVTQCfqZoYmobgxARATg3gHQnP+nvRvH22BE98UARETQCQLS7k6AyAHQ7d+4Pl6QSICY5Hyk3e3ZI6KaGICICNnqClRU6SCXSeFurxS7HGohd3slBgc4AQB+uMDbYER1YQAiIsPtr06OVpwAsYOY0NcbAPB9HCdFJKoLAxARcQB0BzQm2AOWMgmuZhXhxu0iscshMjkMQERk6AHi+J+Ow8FajuFdXQFwMDRRXRiAiMxcmUaL7LvzxbAHqGMZ3/ePp8EEQRC5GiLTInoAWrt2LQICAqBUKhESEoKTJ0/W2zYzMxNTp05F9+7dIZVKsWDBgjrb7dmzBz179oRCoUDPnj2xb9++VqqeqP1LK9D3/jjZyGGrsBC5GjKmUUHuUFpKkZxbit/TCsUuh8ikiBqAdu3ahQULFmD58uWIjY1FeHg4xowZg5SUlDrbV1RUwNXVFcuXL0efPn3qbBMdHY3Jkydj2rRpuHDhAqZNm4annnoKZ86cac1LIWq3qtf/8nHk/D8djY3CAqOC3AEA38fxNhjRvSSCiP2igwcPRv/+/bFu3TrDtqCgIEycOBGrVq1q8NgHH3wQffv2xZo1a2psnzx5MtRqNX766SfDtkcffRSOjo74+uuv6zxXRUUFKir+mDJerVbDx8cHhYWFsLe3b8aVEYlnx5m6/wFRn21Ribh+uxiP9fZEWKBLK1VFrWnqYN9690VeuY0Xtp+Hm50C0csehkzKp/yo41Kr1VCpVI36+S1aD5BGo0FMTAwiIiJqbI+IiEBUVFSzzxsdHV3rnKNHj27wnKtWrYJKpTK8fHx8mv3+RO2JIAhIzeMEiB3Z8G4usFdaILuoAmcSc8Uuh8hkNCsAJSYmtviNc3JyoNVq4e7uXmO7u7s7srKymn3erKysJp9z2bJlKCwsNLxSU1Ob/f5E7UlusQZllVpYSCXwUHECxI5IYSHDmGBPAMAPfBqMyKBZAahLly4YOXIkvvzyS5SXl7eoAMmfJl0TBKHWttY+p0KhgL29fY0XkTmonv/H28EKFlLRn4mgVlL9NNiBi1nQVOlErobINDTrb7wLFy6gX79+ePXVV+Hh4YEXX3wRZ8+ebdI5XFxcIJPJavXMZGdn1+rBaQoPDw+jn5OoozIMgObtrw5tSGdnuNopUFhWiRPX74hdDpFJaFYACg4OxurVq5Geno6tW7ciKysLw4YNQ69evbB69WrcuXP/P2ByuRwhISGIjIyssT0yMhJhYWHNKQsAEBoaWuuchw4datE5iTqqVAYgsyCTSvBYb/1tsO+4NAYRgBYOgrawsMCkSZPwzTff4L333sOtW7ewePFidOrUCdOnT0dmZsOL8C1atAibNm3Cli1bEB8fj4ULFyIlJQVz5swBoB+bM3369BrHxMXFIS4uDsXFxbhz5w7i4uJw5coVw/758+fj0KFDeO+993D16lW89957OHz4cL1zBhGZK02VDlmF+lvYHADd8T3erxMA4NCV2ygsrRS5GiLxtSgAnT9/HnPnzoWnpydWr16NxYsX49atWzhy5AjS09MxYcKEBo+fPHky1qxZg5UrV6Jv3744ceIEDhw4AD8/PwD6iQ//PCdQv3790K9fP8TExGDHjh3o168fxo4da9gfFhaGnTt3YuvWrejduze2bduGXbt2YfDgwS25VKIOJ62gFAIAe6UFVFaWYpdDrSzY2x7d3e2gqdJh/+8cDE3UrHmAVq9eja1bt+LatWsYO3YsZs+ejbFjx0J6zyDKmzdvokePHqiqqjJqwW2hKfMIEJmaxs4DdPz6HRy8nIVgL3tMHezXylVRa2poHqB7bTqZgH/+GI8+Pg74ft7QVq6KqO21+jxA69atw9SpU5GSkoLvvvsOjz32WI3wAwC+vr7YvHlzc05PRG2A43/Mz4S+3pBJJbiQWsAV4snsNSsARUZGYsmSJfDw8KixXRAEwy0ruVyOGTNmtLxCIjI6QRAMT4Bx/I/5cLVTYGR3NwDA7pg0kashElezAlBgYCBycnJqbc/Ly0NAQECLiyKi1lVQWoniiipIJYCXA9cAMydPDtAPht4bm44qLecEIvPVrABU37Ch4uJiKJWcTZbI1FVPgOipsoKljBMgmpOR3d3gZCPHnaIKHOecQGTGLJrSeNGiRQD0My3/4x//gLX1H13nWq0WZ86cQd++fY1aIBEZXypvf5ktuYUUE/t6Y8upROyOScPDQZwklsxTkwJQbGwsAH0P0MWLFyGXyw375HI5+vTpg8WLFxu3QiIyOg6ANm9PDuiELacScTj+NvJKNHCykd//IKIOpkkB6OjRowCA5557Dv/5z3/4iDhRO1Sp1SGjgBMgmrMgT3v08rLH5Qw1vo9Lx3NDOXaTzE+zbv5v3bqV4YeoncosKINWEGAjl8HRmhMgmqsnQ/SDofk0GJmrRvcAPf7449i2bRvs7e3x+OOPN9h27969LS6MiFpHSn4ZAP3tL4lEInI1JJbxfb3xzoF4XM5Q41J6IYK9VWKXRNSmGt0DpFKpDH9ZqlSqBl9EZLo4AJoAwMlGjohe+rncdp5r3OzhRB1Jo3uAtm7dWuf/E1H7wgHQVG3qIF/8+HsmvovNwGtjg2Atb9KwUKJ2rVljgMrKylBaWmr4dXJyMtasWYNDhw4ZrTAiMj51WSUKyiohAdCJEyCavdDOzvBztkZxRRX+dyFT7HKI2lSzAtCECROwfft2AEBBQQEGDRqEDz/8EBMmTMC6deuMWiARGU/18hfu9kooLGUiV0Nik0olmDJQv5DqjrO8DUbmpVkB6LfffkN4eDgAYPfu3fDw8EBycjK2b9+Ojz/+2KgFEpHx8PYX/dlfQzrBQipBXGoBrmSoxS6HqM00KwCVlpbCzs4OAHDo0CE8/vjjkEqlGDJkCJKTk41aIBEZDxdApT9ztVMgopd+NmgOhiZz0qwRb126dMF3332HSZMm4eDBg1i4cCEAIDs7m/MDEZmoKp0O6QX6R+AZgDqWHWdaFlzc7fVrOO46l4rOLraQW0gxdbCvMUojMlnN6gH6xz/+gcWLF8Pf3x+DBw9GaGgoAH1vUL9+/YxaIBEZR2ZBOap0AqwsZXCx5dIH9IdAV1s4WluiokqHi+mFYpdD1CaaFYD++te/IiUlBefPn8fPP/9s2P7www/jo48+MlpxRGQ8997+4gSIdC+pRIKB/k4AgHNJeSJXQ9Q2mj3pg4eHBzw8PGpsGzRoUIsLIqLWkcIB0NSAED9HHI6/jZS8UmQVlotdDlGra1YAKikpwb/+9S/88ssvyM7Ohk6nq7E/ISHBKMURkfFwBmhqiJ3SEkGe+gVSz7IXiMxAswLQ7Nmzcfz4cUybNg2enp7sTicycfdOgOjjyAkQqW6D/J1wOUON2JR8lFRUwUbBmaGp42rWt/unn37Cjz/+iKFDhxq7HiJqBZwAkRoj0M0WzjZy5JZosC82Hc8O8RO7JKJW06xB0I6OjnBycjJ2LUTUSjj/DzWGVCLBkM7OAIDt0UkQBEHkiohaT7MC0Ntvv41//OMfNdYDIyLTxQBEjdXf1xGWMgmu3y7GmUSOBaKOq1m3wD788EPcunUL7u7u8Pf3h6WlZY39v/32m1GKI6KWq9LpkMEJEKmRrOQy9PNxxNmkPGyPTjL0CBF1NM0KQBMnTjRyGUTUWqonQLSWy+DMCRCpEYZ0dsbZpDwcvHwbWYXl8FApxS6JyOiaFYBWrFhh7DqIqJUY5v9x5ASI1DgeKiUGBTjhbGIedpxJxqKI7mKXRGR0zRoDBAAFBQXYtGkTli1bhrw8/X3i3377Denp6UYrjohazjD+x5m3v6jxpofqnwDbcTYVmirdfVoTtT/NCkC///47unXrhvfeew8ffPABCgoKAAD79u3DsmXLjFkfEbUQB0BTc4zu5QE3OwVyiivw06VMscshMrpmBaBFixZh5syZuHHjBpTKP+4NjxkzBidOnDBacUTUMoVllSi8OwFiJ06ASE1gKftjRfgvopNFrobI+JoVgM6dO4cXX3yx1nZvb29kZWU16Vxr165FQEAAlEolQkJCcPLkyQbbHz9+HCEhIVAqlejcuTPWr19fq82aNWvQvXt3WFlZwcfHBwsXLkR5Ode2IfNT3fvjoVJCYcEJEKlppg7yhYVUgvPJ+bjEVeKpg2lWAFIqlVCr1bW2X7t2Da6uro0+z65du7BgwQIsX74csbGxCA8Px5gxY5CSklJn+8TERIwdOxbh4eGIjY3Fa6+9hldeeQV79uwxtPnqq6+wdOlSrFixAvHx8di8eTN27drFW3NkllK5ACq1gJu9EmMf8AQAbDmVKHI1RMbVrAA0YcIErFy5EpWVlQAAiUSClJQULF26FE888USjz7N69WrMmjULs2fPRlBQENasWQMfHx+sW7euzvbr16+Hr68v1qxZg6CgIMyePRvPP/88PvjgA0Ob6OhoDB06FFOnToW/vz8iIiLw9NNP4/z58825VKJ2jeN/qKWeHxYAAPjhQgayi9iTTh1HswLQBx98gDt37sDNzQ1lZWUYMWIEunTpAjs7O7zzzjuNOodGo0FMTAwiIiJqbI+IiEBUVFSdx0RHR9dqP3r0aJw/f94QxoYNG4aYmBicPXsWgH5l+gMHDuAvf/lLvbVUVFRArVbXeBG1d5VaHdI5ASK1UF8fB4T4OaJSK+BLjgWiDqRZ8wDZ29vj119/xdGjRxETEwOdTof+/ftj1KhRjT5HTk4OtFot3N3da2x3d3evdxxRVlZWne2rqqqQk5MDT09PTJkyBXfu3MGwYcMgCAKqqqrw0ksvYenSpfXWsmrVKrz11luNrp2oPUjLL4NWJ8BWYQFnG06ASM33/NAAxCTn48szKZg7sguUXFCXOoAmByCdTodt27Zh7969SEpKgkQiQUBAADw8PCAIQpMnWvtz+/udo672924/duwY3nnnHaxduxaDBw/GzZs3MX/+fHh6euKNN96o85zLli3DokWLDL9Wq9Xw8fFp0nUQmZrk3BIAgL8zJ0Cklhndyx3eDlZILyjD93HpmDzQV+ySiFqsSbfABEHA+PHjMXv2bKSnp+OBBx5Ar169kJycjJkzZ2LSpEmNPpeLiwtkMlmt3p7s7OxavTzVPDw86mxvYWEBZ2f9ejVvvPEGpk2bhtmzZ+OBBx7ApEmT8O6772LVqlXQ6eqezEuhUMDe3r7Gi6i9S6oOQC42IldC7Z2FTIoZYfqJEbf8ylXiqWNoUgDatm0bTpw4gV9++QWxsbH4+uuvsXPnTly4cAGHDx/GkSNHsH379kadSy6XIyQkBJGRkTW2R0ZGIiwsrM5jQkNDa7U/dOgQBgwYYFiQtbS0FFJpzcuSyWQQBIF/aMls6AQBybn6AdB+zgxA1HKTB/rCWi7DtdtFOHUzV+xyiFqsSQHo66+/xmuvvYaRI0fW2vfQQw9h6dKl+Oqrrxp9vkWLFmHTpk3YsmUL4uPjsXDhQqSkpGDOnDkA9Lempk+fbmg/Z84cJCcnY9GiRYiPj8eWLVuwefNmLF682NBm3LhxWLduHXbu3InExERERkbijTfewPjx4yGT8b41mYfb6nJUVOmgsJDCw54LWVLLqaws8WRIJwDA5l8TRK6GqOWaNAbo999/x/vvv1/v/jFjxuDjjz9u9PkmT56M3NxcrFy5EpmZmQgODsaBAwfg56fvas3MzKwxJ1BAQAAOHDiAhQsX4tNPP4WXlxc+/vjjGo/ev/7665BIJHj99deRnp4OV1dXjBs3rtFPpxF1BEk5+ttfvk7WkEk5/oeMY+bQAGw/nYyj1+7g1p1iBLrail0SUbNJhCbcF5LL5UhOToanp2ed+zMyMhAQEICKigqjFSgGtVoNlUqFwsJCjgeidmfHmRR8fTYFF9MLMSrIHQ/1cBO7JGqHqpfB+LPZn5/D4fhsPDvEF/+c+EAbV0XUsKb8/G7SLTCtVgsLi/o7jWQyGaqqqppySiIyMkEQajwBRmRM1RMj7o5JQ16JRuRqiJqvSbfABEHAzJkzoVAo6tzf3nt+iDqC/NJKqMurIJNI0MmRAYiMK7SzM4K97XEpXY3t0UlYMKqb2CURNUuTeoBmzJgBNzc3qFSqOl9ubm41Bi0TUdurfvzdy0EJuUWzJnsnqpdEIsHfhgcCALZHJ6O8UityRUTN06QeoK1bt7ZWHURkJNUDoDn/D7WWscEeeN/RCmn5Zdgdk4Znh/iJXRJRk/Gfh0QdTPX8P/6c/4daiYVMill3xwJtOpkArY5zrFH7wwBE1IHkFlfgTrF+LJ4fF0ClVvTUAB+orCyRlFuKyCt1r99IZMoYgIg6kPPJ+QAANzsFrBXNWuuYqFFsFBZ4doj+UfkNJzgxIrU/DEBEHci5xDwAvP1FbWNGmD/kMil+SynA+aQ8scshahIGIKIO5NzdHiB/F97+otbnZqfE4/29AQCfsReI2hkGIKIOolRThcvphQC4ACq1ndnh+sHQh+Nv49adYpGrIWo8BiCiDiIupQBVOgEqK0s4WsvFLofMRBc3O4wKcoMg6J8II2ovGICIOojTd8f/+HH5C2pj1RMj7vktHXeKuCIAtQ8MQEQdRPStHABAoAtX6Ka2NdDfEX19HKCp0mF7dJLY5RA1CgMQUQdQptEiLrUAANDZleN/qG1JJBK8OLwzAOCL08ko1XBRbDJ9DEBEHcD55DxUagV4qpRwsuH4H2p7Eb084OdsjYLSSnxzLlXscojuiwGIqAOIvpULQL9St0QiEbkaMkcyqQSz7y6PsfFkIiq1OpErImoYAxBRBxCdoA9AQwKdRa6EzNmTA3zgbCNHekEZfvw9U+xyiBrEAETUzhVXVOH3NP38P6GdGYBIPEpLGZ4b6g8AWH/8FgSBi6SS6WIAImrnziXlQasT0MnRCj5cAJVENm2IP2zkMlzNKsKxa3fELoeoXgxARO3c6XvG/xCJTWVtiamD9Yukrjt2S+RqiOrHAETUzp26O/9PWBcGIDINs4Z1hqVMgrNJeYhJ5iKpZJoYgIjasbwSDS5nqAEAQ7u4iFwNkZ6HSolJ/fSLpK47xuUxyDQxABG1Y6du5kAQgB4ednCzU4pdDpHB34YHQiLRL5J643aR2OUQ1cIARNSO/XpDf/trGHt/yMR0cbPF6J4eAID1x9kLRKaHAYionRIEAb/evBuAujIAkemZ86B+kdTv49KRUVAmcjVENTEAEbVTiTklSC8og1wmxeAADoAm09PXxwGhnZ1RpROw6WSi2OUQ1cAARNROVff+hPg5wkouE7kaorpV9wLtPJeC/BKNyNUQ/YEBiKidOnmDt7/I9A3v6oKenvYo1WixPTpZ7HKIDBiAiNqhSq3OsABqOAMQmTCJRGLoBdoWlYhSTZXIFRHpMQARtUPnk/JRXFEFZxs5gr1UYpdD1KCxwR7wdbJGfmklvjmXKnY5RAAAC7ELIKKmO3YtGwAworsrpFKJyNVQR7TjTIpRz9fXxwEpeaVYc/gGZFIpZEb63lYvu0HUVKL3AK1duxYBAQFQKpUICQnByZMnG2x//PhxhISEQKlUonPnzli/fn2tNgUFBZg3bx48PT2hVCoRFBSEAwcOtNYlELW5o3cD0MjubiJXQtQ4IX6OsFFYoKCsEr+nFYhdDpG4AWjXrl1YsGABli9fjtjYWISHh2PMmDFISan7Xx6JiYkYO3YswsPDERsbi9deew2vvPIK9uzZY2ij0WjwyCOPICkpCbt378a1a9ewceNGeHt7t9VlEbWqtPxSXL9dDKkEGN7VVexyiBrFUibF0ED9dA0nbtyBIAgiV0TmTtRbYKtXr8asWbMwe/ZsAMCaNWtw8OBBrFu3DqtWrarVfv369fD19cWaNWsAAEFBQTh//jw++OADPPHEEwCALVu2IC8vD1FRUbC0tAQA+Pn5tc0FEbWBo9fuAND/i1plbSlyNUSNNzjAGcev38FtdQWu3S5CDw97sUsiMyZaD5BGo0FMTAwiIiJqbI+IiEBUVFSdx0RHR9dqP3r0aJw/fx6VlZUAgP379yM0NBTz5s2Du7s7goOD8e6770Kr1dZbS0VFBdRqdY0Xkak6dlV/++tB3v6idsZKLsMgfycAwPHrd0SuhsydaAEoJycHWq0W7u7uNba7u7sjKyurzmOysrLqbF9VVYWcHP2cKAkJCdi9eze0Wi0OHDiA119/HR9++CHeeeedemtZtWoVVCqV4eXj49PCqyNqHeWVWpy6pf+uc/wPtUdDu7hAJpUgObcUybklYpdDZkz0QdASSc0nAQRBqLXtfu3v3a7T6eDm5oYNGzYgJCQEU6ZMwfLly7Fu3bp6z7ls2TIUFhYaXqmpfEyTTFN0Qi7KK3XwsFciyNNO7HKImszeyhL9fBwAsBeIxCXaGCAXFxfIZLJavT3Z2dm1enmqeXh41NnewsICzs76wXWenp6wtLSETPbH0gBBQUHIysqCRqOBXC6vdV6FQgGFQtHSSyJqdYcu3wYAjOrp1uA/FIhMWXhXV8Qk5+NqVhFuq8vhbq8UuyQyQ6L1AMnlcoSEhCAyMrLG9sjISISFhdV5TGhoaK32hw4dwoABAwwDnocOHYqbN29Cp9MZ2ly/fh2enp51hh+i9kKrExB5RR+AInp6iFwNUfO52inQ00s/APoEe4FIJKLeAlu0aBE2bdqELVu2ID4+HgsXLkRKSgrmzJkDQH9ravr06Yb2c+bMQXJyMhYtWoT4+Hhs2bIFmzdvxuLFiw1tXnrpJeTm5mL+/Pm4fv06fvzxR7z77ruYN29em18fkTHFpeYjp7gCdkoLDOnM1d+pfauewuFCWgEKSrlIKrU9UR+Dnzx5MnJzc7Fy5UpkZmYiODgYBw4cMDy2npmZWWNOoICAABw4cAALFy7Ep59+Ci8vL3z88ceGR+ABwMfHB4cOHcLChQvRu3dveHt7Y/78+ViyZEmbXx+RMVXf/nqohxvkFqIP3yNqER8na3R2sUFCTgl+vZmDx3p7iV0SmRmJwNmoalGr1VCpVCgsLIS9PeepIPEJgoCRHxxDUm4pPp3aH3/p7VlvW2MvYUDUWm7cLsLWqCRYyiRYMroHrBVN/zc5l8KgezXl5zf/GUnUDtzMLkZSbinkMilGdOfsz9QxdHGzhZdKiUqtgOiEXLHLITPDAETUDvx8Sf/0Y1gXZ9g241/JRKZIIpFgeDd9oI9OyIWmSnefI4iMhwGIqB343++ZAICxD9R/64uoPerlpYKTjRylGi3OJ+eJXQ6ZEQYgIhN3/XYRrt0ugqVMgtG9+Pg7dSwyqQThXV0AAL/eyIFWx2Gp1DYYgIhM3P8uZAAARnRzhcqKi59Sx9Pf1xG2CgsUlFXi97QCscshM8EARGTCBEHAD3dvf43rw8eEqWOylEkRFqif2+r49TvQ8eFkagMMQEQm7HKGGok5JVBYSPFwUN1LxBB1BIMDnKGwkCK7qALXs4rELofMAAMQkQn74Xf97a+Hg9z49Bd1aFZyGQYHOAEAjl2/A05RR62NAYjIRGl1Ar6P1QegcZwll8zA0C4usJBKkJJXisScErHLoQ6OAYjIRJ26mYMsdTkcrC3xUJCb2OUQtTo7pSVC/BwBAMeucZFUal0MQEQm6tuYNADAhD5eUFjIRK6GqG0M7+oKqQS4eacYqXmlYpdDHRgDEJEJKiyrxMHL+tmf/xriI3I1RG3H0UaOvj4OAPRPhBG1FgYgIhP0w4UMaKp06OFhh2BvLshL5mV4N1dIAFzJVCNLXS52OdRBMQARmaDq219/DekEiUQicjVEbcvNToleXvrgf4K9QNRKGICITMzljEJcSC2AhVSCif28xS6HSBQjuusH/l9ILUBeiUbkaqgjYgAiMjFfRCcDAMY84AkXW4XI1RCJw9vBCt3cbSGAY4GodTAAEZmQwtJKfBeXDgCYHuoncjVE4nqwm74X6LeUfBSWVYpcDXU0DEBEJuTbmFSUV+oHPw+4Ox8Kkbnyd7GBv7M1tDoBv95gLxAZFwMQkYnQ6QR8cVp/+2t6qD8HPxMBePDuWKCzSXkoqagSuRrqSBiAiEzEsevZSM4thZ3SAhP7cekLIgDo6mYLLwclKrUCom7lil0OdSAMQEQmYv2xBADA1EG+sJZz4VMiAJBIJIaxQNEJOSiv1IpcEXUUDEBEJuB8Uh7OJuVBLpPi+WEBYpdDZFJ6etnD1VaB8kodohPYC0TGwQBEZALWH78FAHgixBvu9kqRqyEyLVKJBCN7uAIAfr2Rgwr2ApERMAARiexaVhEOx2dDIgH+NjxQ7HKITFLvTg5wsZWjrFLLXiAyCgYgIpF9fOQGAGBMsAcCXGxErobINEklEoy8+0TYrzfZC0Qtx5GWRE2w40yKUc+XXlCGH3/PhEQCvPJwV6Oem6ij6d3JAUeuZiO3RIPTCbmG5TKImoM9QEQiirySBQCY0McLPTy46jtRQ2RSCUb20IeekzdzUFHFXiBqPgYgIpEk5pTg+u1iWEglWPhIN7HLIWoX+nRygLONHKUaLc4k5IldDrVjDEBEItAJAn6+lAkAmDzQB37OHPtD1Bgy6R9jgU7euINSDWeHpuZhACISQWxKAVLzyyC3kGI+x/4QNUkfHwc42chRotHiy7vLxxA1FQMQURsr02jx82X92J+He7jBjfP+EDXJvb1A648noJhrhFEziB6A1q5di4CAACiVSoSEhODkyZMNtj9+/DhCQkKgVCrRuXNnrF+/vt62O3fuhEQiwcSJE41cNVHz/XL1NkoqquBqq0BooLPY5RC1S3199PMC5ZVosOXXRLHLoXZI1AC0a9cuLFiwAMuXL0dsbCzCw8MxZswYpKTU/ahxYmIixo4di/DwcMTGxuK1117DK6+8gj179tRqm5ycjMWLFyM8PLy1L4Oo0dLyS3H67iRuj/XxhIVU9H+DELVLMqkEDwe5AwA2nkhAQalG5IqovRH1b9/Vq1dj1qxZmD17NoKCgrBmzRr4+Phg3bp1dbZfv349fH19sWbNGgQFBWH27Nl4/vnn8cEHH9Rop9Vq8cwzz+Ctt95C586d71tHRUUF1Gp1jReRsVVqddgdkwadAPTupEJXNzuxSyJq1x7wVqGHhx2KKqqw/niC2OVQOyNaANJoNIiJiUFERESN7REREYiKiqrzmOjo6FrtR48ejfPnz6OystKwbeXKlXB1dcWsWbMaVcuqVaugUqkMLx8fnyZeDdH9/RKfjeyiCtgqLDC+t5fY5RC1e1KJBIsjugMAtkUlIruoXOSKqD0RLQDl5ORAq9XC3d29xnZ3d3dkZWXVeUxWVlad7auqqpCTkwMAOHXqFDZv3oyNGzc2upZly5ahsLDQ8EpNTW3i1RA1LDm3BCdv3AEATOzrDWsFJ2EnMoaHg9zQz9cB5ZU6rD16S+xyqB0RfQCCRCKp8WtBEGptu1/76u1FRUV49tlnsXHjRri4uDS6BoVCAXt7+xovImMprqjC12dTIADo5+OAnl78fhEZi0Qiwf+72wv01ZlkpOWXilwRtRei/TPUxcUFMpmsVm9PdnZ2rV6eah4eHnW2t7CwgLOzMy5fvoykpCSMGzfOsF+n0wEALCwscO3aNQQGcrVtajs6QcC351OhLq+Ci60C4/vw1heRsYV1ccHQLs44dTMXH/9yA+//tY/YJVE7IFoPkFwuR0hICCIjI2tsj4yMRFhYWJ3HhIaG1mp/6NAhDBgwAJaWlujRowcuXryIuLg4w2v8+PEYOXIk4uLiOLaH2tzRq9m4kV0MS5kEUwf5QmEpE7skog6peizQ7pg03MwuFrkaag9EvQW2aNEibNq0CVu2bEF8fDwWLlyIlJQUzJkzB4B+bM706dMN7efMmYPk5GQsWrQI8fHx2LJlCzZv3ozFixcDAJRKJYKDg2u8HBwcYGdnh+DgYMjlclGuk8zT72kF+OVqNgBgfB8veKg44SFRa+nn64hHerpDJwDv/XxV7HKoHRB1JObkyZORm5uLlStXIjMzE8HBwThw4AD8/PwAAJmZmTXmBAoICMCBAwewcOFCfPrpp/Dy8sLHH3+MJ554QqxLIKpTal4pdsekAQCGdXFBiJ+TyBURdXxLHu2BI1ezEXnlNk4n5GJIZ040SvWTCNWjiMlArVZDpVKhsLCQA6Kphh1n6p6k8153iiqw4cQtlGi06OFhh2eH+EHawMD+qYN9jVlio2ok6ij+/Ofnje8u4YvTyejdSYXv5g6FVFr/nz3qeJry81v0p8CIOpKCUg22nEpEiUYLLwclJg/waTD8EJFxzR/VFbYKC/yeVogffs8QuxwyYQxAREaiLqvE5l8TUVhWCVdbBWaGBXDQM1Ebc7FV4KUH9U/7vv/zNZRXakWuiEwVAxCRERSUarDxZAJySzRwsLbE88MCYMvJDolE8fzQAHiqlEgvKMO2qCSxyyETxQBE1EJ5JRps+jURuSUaOFpb4oVhnaGyshS7LCKzZSWXGR6L//TITeSVcKFUqo0BiKgFUvNKse6Y/i9YJxs5XgjvDEcbTrdAJLZJ/bzR09MeRRVVWHP4utjlkAliACJqpkvphdh4MkE/4FmlxN/CO8PBmuGHyBRIpRK8/pcgAMCXp5MRn6kWuSIyNQxARE0kCAJ+vZmDr8+moEonoLu7HV4Y3hn2vO1FZFLCurhgTLAHdAKw4vvL4KwvdC8GIKIm0OoE/PB7Bg5czIQAYHCAE54d4geFBZ/2IjJFrz/WE1aWMpxNysP3cXwsnv7AAETUSCUVVfjqTDJOJ+RBAmBMsAfG9/GCjBOtEZksbwcrvPxQFwDAOwfiUVReKXJFZCoYgIgaIVtdjskbonE1qwgWUgmeHuSL8K6ukHCSQyKTNzs8AP7O1rhTVIGPf7khdjlkIhiAiO7jWlYRJn56CpfS1bCRyzA7vDOCvVVil0VEjaSwkGHF+F4AgK2nknDjdpHIFZEpYAAiasCvN3Lw13VRyCgsR2cXG8wZEQhfJ2uxyyKiJhrZ3Q2P9HRHlU7APzggmsAARFSvb86lYubWsyiqqMIgfyfsnRsGZ1uF2GURUTP947GeUFhIEZ2Qi/0XOCDa3DEAEf2JIAj48NA1/H3P76jSCZjQ1wtfzB7EOX6I2jkfJ2v8390B0W/9cIUzRJs5BiCie1RUabFgVxw+OXITAPB/D3XBmsl9+Zg7UQfxt+GB6OFhh7wSDVb+cFnsckhEDEBEdxWWVWL65rP4Pi4DFlIJ3n+iN16N6M4nvYg6ELmFFO890RtSCfBdXAaOXs0WuyQSCQMQEYDb6nJM/iwaZxLzYKuwwNbnBuKpgT5il0VEraCPjwOeHxoAAFi+7yKKK6pErojEwABEZu/WnWI8vjYKV7OK4GqnwDcvhiK8q6vYZRFRK1oU0Q0+TlbIKCzH+z9fFbscEgEDEJm12JR8/HVdFNILyhDgYoO9L4Whp5e92GURUSuzlltg1aTeAIAvTifjfFKeyBVRW2MAIrN14vodTN14BvmllejdSYXdc0Lhwzl+iMzGsK4ueDKkEwQB+Pvu31Gm0YpdErUhC7ELIGotO86k1LsvPlONHWdToNUJ6Opmi0n9vHHw8u02rI6ITMHrf+mJEzfuICGnBO8eiEeQp/F7gKcO9jX6Oanl2ANEZudieiG+OpMMrU5ALy97TAvlau5E5kplbYkPnuwDQH8r7FoWl8kwFwxAZFZiU/Kx82wKdALQu5MKUwb6wkLKPwZE5iy8qytmhvkDAPb+loYSPhVmFvg3P5mN80l52B2TBgFAiK8jnhrgA5mUc/wQEbB0TA90cbNFUUUVvotL51phZoABiMzC+aQ87I1NhwBgcIATJvX3hpQTHBLRXUpLGdZM7gupBLicocZvKQVil0StjAGIOrzYlHzsi00HAIQFOmN8Hy+GHyKqJdhbhVFB7gCA//2ewbXCOjgGIOrQLqQVGG57DQ5wwl8e8OTSFkRUr+HdXOHnbI2KKh2+PpuCKq1O7JKolTAAUYd1Kb0Q355PhQBgoL8jxvXxYvghogZJJRJMHuADK0sZ0gvK8NPlLLFLolbCAEQd0i/xt7HznP5pr/6+jpjQl2N+iKhxHKzleHJAJwBA9K1cXEovFLkiag0MQNThnE7IxUtf/QadAPTppMLjHPBMRE3Uw8Mew7u6AAD2/JaG3OIKkSsiYxM9AK1duxYBAQFQKpUICQnByZMnG2x//PhxhISEQKlUonPnzli/fn2N/Rs3bkR4eDgcHR3h6OiIUaNG4ezZs615CWRCLqUXYvbn56Gp0iHI0x5/DfFh+CGiZnmkpwf8nO6OBzqXgkqOB+pQRA1Au3btwoIFC7B8+XLExsYiPDwcY8aMQUpK3UsYJCYmYuzYsQgPD0dsbCxee+01vPLKK9izZ4+hzbFjx/D000/j6NGjiI6Ohq+vLyIiIpCent5Wl0UiuXWnGNO3nEVxRRVCOztjykDO80NEzSeTSjBlkC+s5TJkFJTjwMVMsUsiI5IIIs72NHjwYPTv3x/r1q0zbAsKCsLEiROxatWqWu2XLFmC/fv3Iz4+3rBtzpw5uHDhAqKjo+t8D61WC0dHR/z3v//F9OnTG1WXWq2GSqVCYWEh7O25Mnh7kFFQhr+ui0JGYTke8FZhxwuD8cOF9vGXlbHXCWpoDTSijqYt/vxcv12EbVFJAIAn+nsjxM+pSefkWmBtpyk/v0XrAdJoNIiJiUFERESN7REREYiKiqrzmOjo6FrtR48ejfPnz6OysrLOY0pLS1FZWQknp/q/sBUVFVCr1TVe1H7kFlfg2c1nkFFYjkBXG2x7biDslJZil0VEHUQ3dzs8HOQGAPguLgMpeaUiV0TGIFoAysnJgVarhbu7e43t7u7uyMqq+7HDrKysOttXVVUhJyenzmOWLl0Kb29vjBo1qt5aVq1aBZVKZXj5+Pg08WpILEXllZix9SwS7pTAS6XEF7MGw9lWIXZZRNTBjOzuhp6e9tDqBHx1Jhnqsrr/0U3th+iDoP88L4sgCA3O1VJX+7q2A8D777+Pr7/+Gnv37oVSqaz3nMuWLUNhYaHhlZqa2pRLIJGUV2ox+/PzuJSuhrONHF/MHgwvByuxyyKiDkgqkeDJkE5ws1OgqLwKX51J5qDodk60AOTi4gKZTFartyc7O7tWL081Dw+POttbWFjA2dm5xvYPPvgA7777Lg4dOoTevXs3WItCoYC9vX2NF5m2Kq0OL++IxZnEPNgpLPD584MQ6GordllE1IEpLGWYNsQPVpYypOaXYX9cBhdNbcdEC0ByuRwhISGIjIyssT0yMhJhYWF1HhMaGlqr/aFDhzBgwABYWv4x5uPf//433n77bfz8888YMGCA8YsnUel0Av6+53ccjr8NhYUUm2YMQLC3SuyyiMgMONsqMGWQDyQAYlLycepWrtglUTOJegts0aJF2LRpE7Zs2YL4+HgsXLgQKSkpmDNnDgD9ral7n9yaM2cOkpOTsWjRIsTHx2PLli3YvHkzFi9ebGjz/vvv4/XXX8eWLVvg7++PrKwsZGVlobi4uM2vj4xPEAS8/eMV7P0tHTKpBGuf6Y/BnZ3vfyARkZF0dbPDmGAPAMBPFzNxOYMzRbdHoj4GD+gnQnz//feRmZmJ4OBgfPTRRxg+fDgAYObMmUhKSsKxY8cM7Y8fP46FCxfi8uXL8PLywpIlSwyBCQD8/f2RnJxc631WrFiBN998s1E18TH4ttfYR7ePXL2Nw/HZAICnBnRCXx/H1iyLiKhOgiDg+wsZOJuYB0uZBLOHdYaPk3WdbfkYfNtpys9v0QOQKWIAanuNCUDRt3Lww+/6uX0e6+2JsECX1i6LiKheWp2AL04n4frtYtgoLPDSiEA42chrtWMAajvtYh4goqb4LTnfEH4e7uHG8ENEopNJJXh6oC88VUqUVFTh8+gklGm0YpdFjcQARCbvYnoh9vyWBgAYGuiMh3q4iVwREZGewlKG6aH+sFda4E5RBb7k4/HtBgMQmbRrWWrsOpcCAcAAP0eMfcCzwXmiiIjamsrKEjPC/KGwkCIxpwS7zqVCq+PoElPHAEQm69adYnx1JgU6AejdSYWJ/bwZfojIJHmqrPDsED9YSCW4kqnGd7HpnCPIxDEAkUlKySvFF9HJqNIJCPKww5MhPpAy/BCRCQt0tcWUgX/MEfTTpSyGIBPGAEQmJ6OgDNuiEqHR6tDF1RZTBvlCJmX4ISLT19NLhcf7dwIA/HozB8ev3xG5IqoPAxCZlOyicmw9lYjySh38nKzx7BA/WMr4NSWi9iPEzxFj706UeOjKbXwelSRuQVQn/mQhk3FbXY7NJxNRotHCy0GJGWH+kFvwK0pE7c+wrq54sLsrAGDF/svYHp0kbkFUC3+6kEnIUpdj08kEFFVUwcNeiefCAqC0lIldFhFRsz0S5I7hXfVzlv3je4YgU8MARKK7kqHGppMJ+p4flRKzhwXARmEhdllERC0ikUgwupcHXhzRGQBDkKnhTxkS1aX0Qjy7+QxKNVp0crTCc2EBsJKz54eIOgaJRIKlj/YAAHx2PAH/+P4yAGB6qL+IVRHAHiAS0fmkPEzdeBoFpZXwcbTC80MZfoio46kOQff2BH169CYfkRcZe4BIFJFXbuPlHb+hokpnmOGZY36IqKOqDkGWUin+e/Qm/n3wGnKLNXj9L0GQcpoPUbAHiNrczrMpePGL86io0uHhHm74YtZghh8i6vAkEgkWj+6ONx7rCQDYcioRr357gWuHiYQBiNqMIAj4+JcbWLr3InQC8NSATvhsWghvexGRWZk1LAAfTe4DC6kE+2LT8bft57mKvAgYgKhNaKp0eG3fRayOvA4AeHlkF7z3RG9YcJJDIjJDk/p1wsbpA6C0lOLotTt46rNoZBaWiV2WWeFPH2p12UXlmLrxNL4+mwqJBHhrfC8sHt2dC5sSkVkb2cMNX80eDCcbOS6mF2L8f08hNiVf7LLMBgMQtaoLqQUY/8kpnE/Oh53SAltmDMSMMH+xyyIiMgkhfk74ft5Q9PCww52iCkzecBr7YtPELsssMABRq9kTk4YnP4tGlrocga42+H7eUIzs4SZ2WUREJsXHyRq7XwrDIz3doanSYeGuC3j3QDwHR7cyBiAyuqLySiz+9gJe/fYCNFU6jApyx3fzhqKzq63YpRERmSRbhQU+ezYEL4/sAgDYcCIBkz+LRmpeqciVdVwMQGRU55PyMPbjk9gdkwapBJj/cFdsmBYCO6Wl2KUREZk0qVT/mPzaZ/rDTmmB31IKMPY/J7H/QobYpXVInAiRjKJSq8PHv9zAp0dvQicA3g5W+GhyXwwKcBK7NCKidmXsA554wFuF+Ttj8VtKAV75OhYnr9/Bm+N7cZ1EI2IPELVYTHIeJvz3FD45og8/j/fzxk8Lwhl+iIiaycfJGt+8GIpXHuoCiQT4NiYNj6w+jsgrt8UurcNglKRmyymuwL9+uordMfonFlRWlvjnxGCM6+MlcmVERO2fhUyKRRHdEdbFBYu/vYC0/DK8sP08HunpjrfG94KXg5XYJbZrDEDUZJVaHb46nYwPI6+jqLwKgH5W5yWP9oCzrULk6oiIOpYhnZ0RuXAE/vPLDWw6mYDIK7dx6mYOFozqiumh/lxKqJkkApejrUWtVkOlUqGwsBD29vZil2MyNFU67I5Jw6dHbyK9QD9jabC3PVZOCEZ/X8cWnXvHmRRjlEhEZHKmDvY12rmuZRVh+b6LOJ+snzDRU6XE/z3UFU8O6ARLzqzfpJ/fDEB1YACqqaJKi2/Pp2HdsVuG4ONqp8D8h7vi6UG+kBlhJWMGICLqqIwZgABApxOwOyYNHx2+jszCcgCAr5M15j/cFRP6epn1EkMMQC3EAKSXnFuCnedS8e35VOQUawAAbnYKzBkRiKmDfY3a7coAREQdlbEDULXySi2+PpuCT4/eQk5xBQD9E7hTB/viqQE+cLUzvyEJDEAtZM4BqLxSiyNXs/H12RScvJFj2O5hr8ScEZ0xZZBxg081BiAi6qhaKwBVK9VUYXt0MjacSEBeif4fq5YyCcY+4Impg3wx0N8JUiP01LcHTfn5zUHQhIJSDY5czcbBy1k4cT0HZZVaAIBEAoR3dcXUQb54OMiN95eJiEyQtdwCc0YEYmaYP378PRNfnE5GXGoBvo/LwPdxGXC3V2B0Lw88GuyBQf5OZn2L7F7sAapDR+8BUpdXIiY5H+cS83AuKQ+/pRRAq/vja+ClUmJSf29MGegLHyfrNqmJPUBE1FG1dg9QXS6mFeKL00n46WIWiiqqDNudbOQI7+qCQQFOGBzghEBXW0gkHad3qF3dAlu7di3+/e9/IzMzE7169cKaNWsQHh5eb/vjx49j0aJFuHz5Mry8vPD3v/8dc+bMqdFmz549eOONN3Dr1i0EBgbinXfewaRJkxpdU0cKQDnFFbiWVYT4TDWuZRXhcoYaV7PU0P3pd72Hhx0ienkgoqc7ennZt/kfCAYgIuqoxAhA1SqqtIi6mYufLmUi8spt5JdW1tjvbCPHAH9HBHnao4eHHXp42MPXybrd3jJrN7fAdu3ahQULFmDt2rUYOnQoPvvsM4wZMwZXrlyBr2/tL0xiYiLGjh2LF154AV9++SVOnTqFuXPnwtXVFU888QQAIDo6GpMnT8bbb7+NSZMmYd++fXjqqafw66+/YvDgwW19ia1GEASoy6qQU1KBnKIK5JZokK0uR3pBGdLyy5CaX4q0/DIU/OnLXs3XyRoD/fX/AhjS2Rm+zm3T00NERG1HYSHDyB5uGNnDDVVaHc4l5eN0Qi7OJubht5R85JZocPDybRy8/McM01aWMvi72MDbwQqdHPUvbwcrONnI4Wgjh6O1HA7Wlu1+WISoPUCDBw9G//79sW7dOsO2oKAgTJw4EatWrarVfsmSJdi/fz/i4+MN2+bMmYMLFy4gOjoaADB58mSo1Wr89NNPhjaPPvooHB0d8fXXXzeqrtbqAcouKsfhK9mo0umgqdKhUiugSqtDpVaHSp2Ayqqa/1+lE1BeqUVxRZX+VV6FkooqFFXo//vnXpy6SCSAn5M1unvYobuHPuH393WEh0pptOsyBvYAEVFHJWYPUEMqqrS4mFaIuNQCXM0qwrWsIly/XYSKKl2jjrdTWsDJRg57pSWs5DJYWd59yWVQWspgLZdBbiGFhVQCC6kUFjIJLGUSyKRSWMokcLNT4tFgD6NeU7voAdJoNIiJicHSpUtrbI+IiEBUVFSdx0RHRyMiIqLGttGjR2Pz5s2orKyEpaUloqOjsXDhwlpt1qxZU28tFRUVqKioMPy6sLAQgP6DNKb4lHws3XnWqOe0VcjgbKuAs40cTjZyeDlYwdtBCS8Ha31qd7SCtfzPv80aqNUao9bRUqUlRWKXQETUKoz9s8SYujlZoJuTC9DHBQCg1QlIzitBWn4ZMgvKkF5Qjoz8UmSpK1BQqkFBqQaF5VUQBKCwArj747JZendSIczXuHcfqj/rxvTtiBaAcnJyoNVq4e7uXmO7u7s7srKy6jwmKyurzvZVVVXIycmBp6dnvW3qOycArFq1Cm+99Vat7T4+Po29HCIiojq9IHYBJioVgGpx65y7qKgIKpWqwTaiPwb/58G2giA0OAC3rvZ/3t7Ucy5btgyLFi0y/Fqn0yEvLw/Ozs4danT8n6nVavj4+CA1NbXdD/ZuDnO/foCfAcDPwNyvH+BnAHScz0AQBBQVFcHL6/6LcosWgFxcXCCTyWr1zGRnZ9fqwanm4eFRZ3sLCws4Ozs32Ka+cwKAQqGAQlFzxkwHB4fGXkq7Z29v366/8C1l7tcP8DMA+BmY+/UD/AyAjvEZ3K/np5poQ7jlcjlCQkIQGRlZY3tkZCTCwsLqPCY0NLRW+0OHDmHAgAGwtLRssE195yQiIiLzI+otsEWLFmHatGkYMGAAQkNDsWHDBqSkpBjm9Vm2bBnS09Oxfft2APonvv773/9i0aJFeOGFFxAdHY3NmzfXeLpr/vz5GD58ON577z1MmDAB33//PQ4fPoxff/1VlGskIiIi0yNqAJo8eTJyc3OxcuVKZGZmIjg4GAcOHICfnx8AIDMzEykpfzweHRAQgAMHDmDhwoX49NNP4eXlhY8//tgwBxAAhIWFYefOnXj99dfxxhtvIDAwELt27epQcwAZi0KhwIoVK2rd/jMX5n79AD8DgJ+BuV8/wM8AMM/PQPSZoImIiIjaWvuexpGIiIioGRiAiIiIyOwwABEREZHZYQAiIiIis8MAZCaOHTsGiURS5+vcuXP1Hjdz5sxa7YcMGdKGlRuXv79/rev583p0fyYIAt588014eXnBysoKDz74IC5fvtxGFRtXUlISZs2ahYCAAFhZWSEwMBArVqyARtPw2nDt+Xuwdu1aBAQEQKlUIiQkBCdPnmyw/fHjxxESEgKlUonOnTtj/fr1bVSp8a1atQoDBw6EnZ0d3NzcMHHiRFy7dq3BY+r7u+Lq1attVLVxvfnmm7WuxcOj4QU4O9J3AKj77z2JRIJ58+bV2b6jfQfqI/pSGNQ2wsLCkJmZWWPbG2+8gcOHD2PAgAENHvvoo49i69athl/L5fJWqbGtrFy5Ei+88MfqPLa2tg22f//997F69Wps27YN3bp1wz//+U888sgjuHbtGuzs7Fq7XKO6evUqdDodPvvsM3Tp0gWXLl3CCy+8gJKSEnzwwQcNHtsevwe7du3CggULsHbtWgwdOhSfffYZxowZgytXrsDXt/YK3YmJiRg7dixeeOEFfPnllzh16hTmzp0LV1fXGtNttBfHjx/HvHnzMHDgQFRVVWH58uWIiIjAlStXYGNj0+Cx165dqzEjsKura2uX22p69eqFw4cPG34tk8nqbdvRvgMAcO7cOWi1WsOvL126hEceeQRPPvlkg8d1pO9AnQQySxqNRnBzcxNWrlzZYLsZM2YIEyZMaJui2oCfn5/w0UcfNbq9TqcTPDw8hH/961+GbeXl5YJKpRLWr1/fChW2vffff18ICAhosE17/R4MGjRImDNnTo1tPXr0EJYuXVpn+7///e9Cjx49amx78cUXhSFDhrRajW0pOztbACAcP3683jZHjx4VAAj5+fltV1grWrFihdCnT59Gt+/o3wFBEIT58+cLgYGBgk6nq3N/R/sO1Ie3wMzU/v37kZOTg5kzZ9637bFjx+Dm5oZu3brhhRdeQHZ2dusX2Iree+89ODs7o2/fvnjnnXcavP2TmJiIrKwsREREGLYpFAqMGDECUVFRbVFuqyssLISTk9N927W374FGo0FMTEyN3zsAiIiIqPf3Ljo6ulb70aNH4/z586isrGy1WttKYWEhADTq97tfv37w9PTEww8/jKNHj7Z2aa3qxo0b8PLyQkBAAKZMmYKEhIR623b074BGo8GXX36J559//r6LfXek70BdGIDM1ObNmzF69Gj4+Pg02G7MmDH46quvcOTIEXz44Yc4d+4cHnroIVRUVLRRpcY1f/587Ny5E0ePHsXLL7+MNWvWYO7cufW2r15Y98+L6bq7u9dadLc9unXrFj755BPD8jP1aY/fg5ycHGi12ib93mVlZdXZvqqqCjk5Oa1Wa1sQBAGLFi3CsGHDEBwcXG87T09PbNiwAXv27MHevXvRvXt3PPzwwzhx4kQbVms8gwcPxvbt23Hw4EFs3LgRWVlZCAsLQ25ubp3tO/J3AAC+++47FBQUNPiP3472HaiX2F1Q1DIrVqwQADT4OnfuXI1jUlNTBalUKuzevbvJ75eRkSFYWloKe/bsMdYltFhzPoNqu3fvFgAIOTk5de4/deqUAEDIyMiosX327NnC6NGjjX4tzdWczyA9PV3o0qWLMGvWrCa/nyl+D/4sPT1dACBERUXV2P7Pf/5T6N69e53HdO3aVXj33XdrbPv1118FAEJmZmar1doW5s6dK/j5+QmpqalNPvaxxx4Txo0b1wpVtb3i4mLB3d1d+PDDD+vc35G/A4IgCBEREcJjjz3W5OM60negGgdBt3Mvv/wypkyZ0mAbf3//Gr/eunUrnJ2dMX78+Ca/n6enJ/z8/HDjxo0mH9tamvMZVKt+kunmzZtwdnautb/6aZGsrCx4enoatmdnZ9f6V6KYmvoZZGRkYOTIkYZFiJvKFL8Hf+bi4gKZTFart6eh3zsPD48621tYWNT5/Wgv/u///g/79+/HiRMn0KlTpyYfP2TIEHz55ZetUFnbs7GxwQMPPFDvd7ejfgcAIDk5GYcPH8bevXubfGxH+g5UYwBq51xcXODi4tLo9oIgYOvWrZg+fTosLS2b/H65ublITU2tEQbE1tTP4F6xsbEAUO/1BAQEwMPDA5GRkejXrx8A/T3048eP47333mtewa2gKZ9Beno6Ro4ciZCQEGzduhVSadPvhJvi9+DP5HI5QkJCEBkZiUmTJhm2R0ZGYsKECXUeExoaih9++KHGtkOHDmHAgAHN+vMiNkEQ8H//93/Yt28fjh07hoCAgGadJzY21qR/r5uioqIC8fHxCA8Pr3N/R/sO3Gvr1q1wc3PDX/7ylyYf25G+AwZid0FR2zp8+LAAQLhy5Uqd+7t37y7s3btXEARBKCoqEl599VUhKipKSExMFI4ePSqEhoYK3t7eglqtbsuyjSIqKkpYvXq1EBsbKyQkJAi7du0SvLy8hPHjx9dod+9nIAiC8K9//UtQqVTC3r17hYsXLwpPP/204Onp2S4/g+rbXg899JCQlpYmZGZmGl736ijfg507dwqWlpbC5s2bhStXrggLFiwQbGxshKSkJEEQBGHp0qXCtGnTDO0TEhIEa2trYeHChcKVK1eEzZs3C5aWls26XWwKXnrpJUGlUgnHjh2r8XtdWlpqaPPnz+Cjjz4S9u3bJ1y/fl24dOmSsHTpUgGASd/ubMirr74qHDt2TEhISBBOnz4tPPbYY4KdnZ3ZfAeqabVawdfXV1iyZEmtfR39O1AfBiAz8/TTTwthYWH17gcgbN26VRAEQSgtLRUiIiIEV1dXwdLSUvD19RVmzJghpKSktFG1xhUTEyMMHjxYUKlUglKpFLp37y6sWLFCKCkpqdHu3s9AEPSPwq9YsULw8PAQFAqFMHz4cOHixYttXL1xbN26td4xQvfqSN+DTz/9VPDz8xPkcrnQv3//Go+Az5gxQxgxYkSN9seOHRP69esnyOVywd/fX1i3bl0bV2w89f1e3/v9/vNn8N577wmBgYGCUqkUHB0dhWHDhgk//vhj2xdvJJMnTxY8PT0FS0tLwcvLS3j88ceFy5cvG/Z39O9AtYMHDwoAhGvXrtXa19G/A/WRCIIgtHGnExEREZGo+Bg8ERERmR0GICIiIjI7DEBERERkdhiAiIiIyOwwABEREZHZYQAiIiIis8MARERERGaHAYiIiIjMDgMQEdUyc+ZMSCQSHDt2TOxSzMKbb74JiUSCbdu2iV2KyeFnQ62FAYjIhB07dgwSiQQzZ84UuxSzkJSUBIlEggcffFDsUoiolTEAEVEtq1atQnx8PAYNGiR2KWbh5ZdfRnx8fI1V64modVmIXQARmR5PT094enqKXYbZcHFxgYuLi9hlEJkV9gARtcC5c+cgkUgwdOjQetu89dZbkEgk+Oc//9mkc8+cORMjR44EAHz++eeQSCSG15tvvgmg5i0btVqNV199FQEBAbC0tMSCBQsAAAUFBfjkk08wevRo+Pn5QaFQwNnZGY8++igiIyPrfe+6xgD5+/tDIpEAADZt2oTevXvDysoKHh4eePHFF1FQUNCka2yqzMxMWFpawtfXFzqdrs421Z/V7Nmzm3TuN998EwEBAQCA48eP1/i8770FKZFI4O/vD41Gg5UrV6JHjx5QKBSYOHEiAKC8vBybN2/GhAkT0LlzZ1hZWcHBwQHDhw/Hzp07633vusa5PPjgg5BIJEhKSsJ3332HIUOGwMbGBk5OTnj66aeRlpbWpGu815+/O/Pnz4ePjw+USiWCgoLw0Ucf1fkZV38HBEHAJ598gj59+sDa2hp9+/Y1tNFoNPjPf/6DgQMHws7ODjY2Nhg0aBA2b96M+tbfPn78OB588EHY2trC2dkZkyZNwtWrV5t9fUT3wx4gohYYOHAgQkJCEBUVhcuXL6NXr1419ut0OmzduhUymQzPPfdck849bNgwZGVl4eDBgwgMDMSwYcMM++79YQMAZWVlGDFiBJKTkzFixAj0798fjo6OAIDTp0/jlVdegY+PD7p164bQ0FCkpKTg0KFDOHToEDZt2oTnn3++SbX9/e9/N/yAe/TRRxEVFYUNGzYgPj7eEB5ag6enJ8aPH4+9e/fi559/xtixY2u12bRpEwDghRdeaNK5+/btiyeeeAJ79uyBu7s7Hn30UcO+ez97QP/7OnHiRJw4cQIjRoxA79694ezsDEAfLGbPng13d3f06NEDgwYNQlZWFqKionDy5ElcvXrVEGAba+3atfjwww8xYMAAPProozh37hx27tyJmJgYXLhwAVZWVk06370qKirw0EMP4datW3jooYeg0Wjwyy+/YNGiRfj999+xdevWOo+bM2cOtm7dihEjRiAoKAgajQYAUFJSgjFjxuDkyZNwcXHBsGHDIJVKER0djdmzZ+PcuXNYv359jXN9//33eOKJJ6DVahEWFgZfX1+cPXsWgwcPxrhx45p9bUQNEoioRTZs2CAAEBYsWFBr308//SQAEMaNG9escx89elQAIMyYMaPO/YmJiQIAAYAQGhoq5Ofn12qTkJAgnDp1qtb23377TXBwcBDs7e2FoqKiGvtmzJghABCOHj1aY7ufn58AQPD09BRiY2MN2+/cuSN06dJFACD88ssvTb3MJjl06JAAQJg4cWKtffHx8QIAITg4uFnnrv48R4wYUW+b6s+7S5cuQlpaWq39OTk5wsGDBwWtVltje0JCguDv7y9IpVIhMTGxxr4VK1YIAIStW7fW2D5ixAgBgGBjY1Pjcy0pKRHCwsIEAMLmzZubfJ2CUPO707t3b+HOnTuGfTdv3hS8vLwEAML3339f47jq74CLi4tw6dKlWud96aWXBADCtGnTanyvsrOzhcGDBwsAhP/973+G7Wq1WnBxcREACDt27DBsr6ysNHwP6/psiFqKt8CIWmjq1Kmwt7fHF198gYqKihr7mtsb0Rwff/wxHBwcam0PCAhAWFhYre39+vXDvHnzoFarcfTo0Sa919tvv12jF8rFxQUvvfQSAODEiRNNOldTjRo1CoGBgfjf//6HrKysGvuqP++//e1vrVoDoB8o7u3tXWu7s7MzIiIiIJXW/Os1ICAAy5cvh06nww8//NCk91q4cCEeeughw6+tra3x6quvAjDO5/3BBx/UGIMUGBiIN954AwDw6aef1nnMkiVLavV4ZmdnY9OmTQgICMDGjRtha2tr2Ofq6orPPvsMAAz/BYBvv/0WOTk5eOSRR/D0008btltYWOCjjz6qcQ4iY+ItMKIWsrGxwTPPPIN169Zh3759mDJlCgD9D4P9+/fDy8urzls1xuTp6YkBAwbUu1+r1eKXX35BVFQUsrKyUF5eDgC4ceNGjf82VkRERK1t3bp1A6Afp9OaJBIJ/va3v2HJkiXYtm0bli5dCkA/7mT79u1QKpV49tln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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = plt.figure()\n",
    "sns.distplot(res, bins = 15)\n",
    "fig.suptitle('Error Terms', fontsize = 15)                  # Plot heading \n",
    "plt.xlabel('y_train - y_train_pred', fontsize = 15)         # X-label\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The residuals are following the normally distributed with a mean 0. All good!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Looking for patterns in the residuals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiIAAAGdCAYAAAAvwBgXAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAA6HElEQVR4nO3de5BV1Zn38d9pAg0ifQJ0sJtw6yHGSDpegAgo3ogyOGqcOG8qEk1pYkjhC0ZMasZg3hRQ+qYlxktmjBhIhlwYwXcq4qWMGCwUQoRX5RJBEnWwUQa6hwH1HILSYPd+/+A9bV/OZe9z9mWtvb+fqq6yT+/us9nus9ez1nrWs1KO4zgCAACIQFXUJwAAAJKLQAQAAESGQAQAAESGQAQAAESGQAQAAESGQAQAAESGQAQAAESGQAQAAETmY1GfQDEdHR3av3+/Bg0apFQqFfXpAAAAFxzH0eHDhzV8+HBVVRUf8zA6ENm/f79GjhwZ9WkAAIAy7N27VyNGjCh6jNGByKBBgySd+IfU1NREfDYAAMCNbDarkSNHdrbjxRgdiOSmY2pqaghEAACwjJu0CpJVAQBAZAhEAABAZAhEAABAZAhEAABAZAhEAABAZAhEAABAZAhEAABAZAIPRPbt26frrrtOQ4cO1UknnaSzzjpLW7ZsCfptAQCABQItaPbuu+/qvPPO08UXX6ynn35aw4YN0+7du/Xxj388yLcFgNhp73D0YvM7OnD4qIYN6q9zGoaoTxV7cMF+gQYiixcv1siRI7V8+fLO18aMGRPkWwJA7KzZ2aJFT+5SS+Zo52v16f5acOU4zWisj/DMgMoFOjXzxBNPaOLEifryl7+sYcOG6eyzz9ayZcsKHt/W1qZsNtvtCwCSbM3OFt20Ymu3IESSWjNHddOKrVqzsyWiMwP8EWgg8uabb2rJkiU69dRT9cwzz2j27Nn69re/rV//+td5j29qalI6ne78YuddAEnW3uFo0ZO75OT5We61RU/uUntHviMAO6QcxwnsDu7Xr58mTpyoF154ofO1b3/723rppZe0adOmXse3tbWpra2t8/vc7n2ZTIZN7wAkzqbdhzRz2eaSx62cNVlTxg4N4YwAd7LZrNLptKv2O9ARkfr6eo0bN67ba6effrrefvvtvMdXV1d37rTLjrsAku7A4aOlD/JwHGCiQAOR8847T6+99lq3115//XWNHj06yLcFgFgYNqi/r8cBJgo0ELn11lu1efNm/fCHP9R//Md/6OGHH9bSpUs1Z86cIN8WAGLhnIYhqk/3V6FFuimdWD1zTsOQME8L8FWggcjnP/95rV69WitXrlRjY6PuuOMO3X///br22muDfFsAiIU+VSktuPLE9HbPYCT3/YIrx1FPBFYLNFm1Ul6SXQAgrqgjAtt4ab8DLWgGAKjcjMZ6XTqujsqqiCUCEQCwQJ+qFEt0EUvsvgsAACJDIAIAACJDIAIAACJDIAIAACJDsioAJEh7h8PqGxiFQAQAEoJ6JDARUzMAkABrdrbophVbuwUhktSaOaqbVmzVmp0tEZ0Zko5ABABirr3D0aIndylfGe3ca4ue3KX2DmMLbSPGCEQAIOZebH6n10hIV46klsxRvdj8TngnVaH2Dkebdh/S49v3adPuQwRRFiNHBABi7sDhwkFIOcdFjVyXeGFEBABibtig/r4eFyVyXeKHQAQAYu6chiGqT/dXoUW6KZ0YUTinYUiYp+UZuS7xRCACADHXpyqlBVeOk6RewUju+wVXjjO+nkgcc11AIAIAiTCjsV5LrhuvunT36Ze6dH8tuW68FbkVcct1wQkkqwJAQsxorNel4+qsrawap1wXfIRABAASpE9VSlPGDo36NMqSy3VpzRzNmyeS0okRHtNzXXpKetl9AhEAgBVyuS43rdiqlNQtGLEp16UrliKTIwIAsEgccl1yWIp8AiMiAACr2J7rIpVeipzSiaXIl46rs+rfVQ4CEQCAdWzOdZG8LUW2+d/pBlMzAACEjKXIHyEQAQAgZCxF/giBCAAAIYtL2X0/EIgAABCyuJTd9wOBCAAAEYjTUuRKsGoGAICIxGEpcqUIRAAAiJDtS5ErxdQMAACIDCMiABATSd88DXYiEAGAGGDzNNiKqRkAsBybp8FmBCIAYLFSm6dJJzZPa+/IdwQQPQIRALCYl83TABORIwIAFYoySZTN02A7AhEAqEDUSaJsngbbMTUDAGUyIUmUzdNgOwIRACiDKUmibJ4G2xGIAEAZTEoSZfM02IwckYBQ4RCIN9OSRNk8DbYiEAlA1MlrAIJnYpJo0jdPg52YmvGZCclrAIJHkijgDwIRH5mSvAYgeCSJAv4ILRBpampSKpXSvHnzwnrL0JmUvAYgeCSJApULJUfkpZde0tKlS3XGGWeE8XaRMS15DUDwSBIFKhN4IPLXv/5V1157rZYtW6Y777wz6LeLlInJawCCR5IoWClZvsADkTlz5ujyyy/XJZdcUjIQaWtrU1tbW+f32Ww26NPzVS55rTVzNG+eSEonhmxJXgOA+GClZGUCzRFZtWqVtm7dqqamJlfHNzU1KZ1Od36NHDkyyNPzHclrAJAsrJSsXGCByN69e3XLLbdoxYoV6t/f3VTE/PnzlclkOr/27t0b1OkFhuQ1AEgGVkr6I+U4TiBX6LHHHtOXvvQl9enTp/O19vZ2pVIpVVVVqa2trdvP8slms0qn08pkMqqpqQniNAPDfCG84p4B7LJp9yHNXLa55HErZ01OXA6Rl/Y7sByRL3zhC9qxY0e3177+9a/rM5/5jG677baSQYjtSF6DF8wxA/ZhpaQ/AgtEBg0apMbGxm6vDRw4UEOHDu31OuBVnEYPcnPMPYcmc3PMTOkBZmKlpD/YawbWidPoQak55pROzDFfOq7O2kALiCtWSvoj1BLvzz//vO6///4w3xIxE7cMdarxAvZipaQ/2GsG1ohjhjpzzIDdWClZOaZmYA0vowe2JAozxxyOOOUUwTxRl/m3/f4mEIE14jh6wBxz8OKUUwRzRbVSMg73N1MzsEYcRw+YYw5W3HKKgK7icn8TiMAaudGDQk1ySid6AraNHjDHHIw45hQBOXG6v5magTVyowc3rdiqlNTtA2j76EHUc8xxFMecIiAnTvc3IyKwSrHRg59+9WylB/TT49v3adPuQ1b0BLrKzTFfddYnNWXsUIKQCsUxpwjIidP9zYgIrJNv9ODdI8d0x1N2J2zBX3HMKQJy4nR/MyICK3UdPch8cExzHrY/YQv+imtOESDF6/4mEIHV4pSwBX+xIglxFqf7m0AEVguzRHp7h6NNuw9Zm4OSRKxIQpzF5f4mRwRWCythKw5Fg5KKFUmIszjc3wQisFoYCVu5okE9xz9yOSg29TySKqqql/CH7SXMg2b7/U0gAqsFXSK9VA5KSidyUC4dV8eDEVYyvZFnNDL+CERgtaCLnMWpaBDQk+mNPKOR3ZkeNJaLQATWyyVs9Xyg1vnwQI1T0SCgK9MbeUYjuzM9aKwEgQhiIaiErSiKBsW11wNz2NDImzQaGfVn0vSgsVIEIoiNIBK2gs5B6SnOvR6Yw6RGvhBTRiOj/kzaEDRWijoiQBFhFg2Ky5beMJ8pjXwxJpQwN+EzGWatpKgQiAAlhFE0iAqxCJMJjXwpUZcwN+UzaUPQWCmmZgAXgi4aZMNQOeIj7CnHcgS9Iq4UUz6TNgSNlWJEBHCp60Z7U8YO9fUBmIReD8xhyz4lUZYwN+UzGfXIUBgYEQEMkIReD8wS5LJ3P0VVwtyUz2TUI0NhIBABDGDDUDnix5Z9SqIoYW7SZ9KWoLFcBCKAAZLQ64GZbN+nJCimfSZtCRrLkXIcx9g0/Gw2q3Q6rUwmo5qamqhPBwhc1DULAHTHZ7I8XtpvAhHAMFFXcQTQnU2fSVPO1Uv7zdQMYBiGyhFHpjSQ5bDlM2nr6A2BCAAgULY2kDaxeT8a6ogAAAJjQpn0uDOlCmy5CEQAIGDtHY427T6kx7fv06bdhyJpEKI4B9sbSFvYvh8NUzMAECATpiWiOgdTyqTHnSlVYMvFiAgABMSEaYkoz8H2BtIWplSBLReBCAAEwIRpiajPwfYG0ha270dDIAIAATBh3j7qc7C9gbSFLZsYFkIgYhkTkt4AlGbCtETU52B7A2mTKHcqrhTJqhYxIekNgDsmTEuYcA5x37DNJLbuR0MgYgmbi9UASWTC7q0mnINkbwNpI1uqwHbF1IwFok44A+CdCdMSJpxD13OZMnaorjrrk5oydihBCDoRiFgg6oQzAOUxYd7ehHMAimFqxgJRJ5wBKJ8J0xImnANQCIGIBUxIOANQPhPm7cM+B5t32zVJEq4jgYgFTEk4g92S8ECDGVjh54+kXMeU4zjGZjhms1ml02llMhnV1NREfTqRyq2akdQtGMk1I7bO9dI4hiMpDzREr9AKP9ufVWGz/Tp6ab8JRCwSVmMSVnBA4xgO2x9osEd7h6Opi9cVTK7Pjd5uvG0aHY4i4nAdvbTfgU7NNDU16dFHH9Vf/vIXDRgwQOeee64WL16s0047Lci3ja0wEs7CCg6oixKOUku/Uzqx9PvScXXGPtBgD3bb9UfSrmOgy3fXr1+vOXPmaPPmzVq7dq0+/PBDTZ8+XUeOHAnybWMtyLX4Ye3SSV2U8LD0G2FihZ8/knYdAx0RWbNmTbfvly9frmHDhmnLli264IILgnxreBRmzzlp0X6UkvZAQ7RY4eePpF3HUAuaZTIZSdKQIflXd7S1tSmbzXb7Qnm8bo4XZs/ZbaPXmvmg4vdKuqQ90BAtdtv1R9KuY2jLdx3H0Xe+8x1NnTpVjY2NeY9pamrSokWLwjqlWGrvcPTAuje0/I979N4HxztfL5XnEWbP2W2jd8dTf9aAfn3IFakAS78RplxJ+ZtWbFVK+Vf4sdtuaUm7jqGNiMydO1evvPKKVq5cWfCY+fPnK5PJdH7t3bs3rNOLhTU7WzThzrW679k3ugUhUuk8jzB7zqWi/Zx3jxzzNTcliUzaawTJQEl5fyTpOoayfPfmm2/WY489pg0bNqihocH177F8171Cq1C6KrbkK7dcrFTP2a/lYm7ON4j3TSqWSiNs1Ajyh63X0Zg6Io7j6Oabb9bq1av1/PPP69RTT/X0+wQi7pRac97TylmT8yaBVlo0zesHZs3OFt2+eofeOXK84DGlzhnu2fpAA2AfY+qIzJkzRw8//LAef/xxDRo0SK2trZKkdDqtAQMGBPnWiVIq0bSnQnkeuaHAnj3nOhc953J63DMa6/XB8Q7d+sj2ss8Z7pmw3wkKI1BEUgUaiCxZskSSdNFFF3V7ffny5brhhhuCfOtE8dpI7zn4fsGflVM0rZLiZHU1rOoAmDpDkgUaiBhcPT5WvDbS9z/7uk6rO7ngA85Lz7nS+iOs6kCQbBhloMowko7dd2OgVGOejynFyZK2TA3hsWGUgRL84bAhIE2yUAuaIRjFlmjmE0VxsmLHJWmZGsIR1nYFlaIEf/DW7GzR1MXrNHPZZt2yartmLtusqYvXGXMPgBGR2CiUaFpMmMXJSh0XxoZ+SAabRhkowR8spr3swIhIjMxorNfG26bpB5ef7ur4MIqTeSlFHOSGfkgOm0YZKMEfHDbXtAeBSMz0qUrphvMaQtunIOmVO0vt6eN1zx9UzqZRhqTtKRImmwLSpGNqJobCTgCtpP6IzUolQ9qQLBlHNo0ykKwdHJsC0qQLpcR7uaisWpmwG8IkZaYXmnvO/Wu/dUGDlm5oLvhz5qaDE/Z2BX4gaPXfpt2HNHPZ5pLHUbU5GMaUeK8UgUjlkhQchMVNSf2qlFRoFsbEhjBuKt2uIAp8Vv1lY0AaJ8aUeEf0KOvtPzcl9YulgpSqrZJUfjbENk4X8ln1F9Ne9iAQATzya06ZuemPBDE1wZJw2BiQJhGBCOCRX0mOJiRLmiDIWg+MMoCA1HwEIoBHbkrqV6UkxxH755RgU/Ex2IuA1GzUEQHkrd5HqdopKUmzzm8o+HOJuekcaj0AYEQEiVdOfoKbueezRw1mbroEaj3YxWtCMSuB4AaBCBKtkvyEUnPPzE2XZlPxsZ6S1sh6DdipjQK3qCOCxCpVD4Q6A8ELotZDGAFC0hrZUgX8egbsXo9H/Hhpv8kRQWKRnxA9v/cqCmPL91wj2/PeyY2ixW17ea+bx7HZHLwiEIkYm6JFh/wEM+TyberS3adf6tL9PfWcwwgQktjIeg3YCfDhFTkiEUra8K5pbM5PiJtK82nCWgbspZENe7loUFNSXgN2Anx4RSASkSCLOCVJJQ/fUvVAqPcRrkpqPYQVIJjayAbZqfEasBPgwysCkQhQxMkflT582YvCX1GuIgkrQDCxkQ26U+M1YA8iwE/aCqWkIRCJgMnDu7bw6+HLXhT+iHqaMawAwbRRtDA6NV4Ddr8D/KjvLQSPZNUIRD28a3uCbHuHo+89usO3hMEZjfXaeNs0rZw1WT+55iytnDVZG2+bxkPOJRNWkeQChEJNW0onGq9KAwS/V/lUKqzEUK8JxTYlICN6jIhEIMrh3Tj0Lh5Y94bee/94wZ+XM6LEXhTlMWWaMcxpNpNG0cLs1HhNKLYlARnRIxCJQFTDu4WmM1oyRzV7xVbdesmnNXfap4z+ULd3OFr+xz2ujiUrP3gmTTOGGSCYUjU37E6N14DdhgRkRI9AJAJRJEkW613k3Pfs61r54lta+MXPGjs68mLzO3rvg8KjIV2RlR+8qKcZewozQDBhFM20nBU/mXZvxZEpScAEIhEJe3i3VO8ipzXbZvTyYbcPnY+f1NfKh69tTFxFYkKAEJY4r/zac/CIq+PocJTHpGl6ApEIhdl789prMHXu1e1DZ+qnao079ziKc4/cFiblrPilvcPRyhffLnmcHwnISWRaHSsCkYiF1Xvz0muIeu612HDhOQ1DVFdTrdZsW9G/seWtd/XHNw7q4JE26g4EKM49cpuYkrPilxeb3yn5GZekaz4/ytp/Y1RMTAImEEmIUj3XfKKYey01XNinKqWZ54zSfc++UfTvtGSO6tpf/N+8fwOV6xks/vSrZ+uOp/4cmx65jeI0JeX22TOm9qSAzyR+TEwCJhBJiK49V7fCnnt1O1w4pnag579N6Xz/FAoWf3D5OA0e2C8WPXITmZJYGAYTc4/iwsQkYAKRBMnNJS98Ypdas4Vvsijm9b0MF5bz8KHugD+KBYtzHj4R6F111icjObc4Mymx0I1KgyZyj4JjYpBHZdWEmdFYrz9+b5puveTUvD+Pal7fy3BhqSqabv4GvCsVLEreKtrCHduqi67Z2aKpi9dp5rLNumXVds1ctllTF6/zdJ6mVbCNk7CqEHtBIGKgoEuw96lK6ZZLPq2Hrhuv+gpLMPvFy3BhsYeUn++F7sIqJ46P2Bb8+Rk0+VUmHt2ZGOQxNWOYMIdgTcq09zpcWGjJop/vhe5MnFuOOxMTCwsJYjWGSc+oODFtyTeBiEHCWtttYtJbOXPCPR9StSdX67v/Z7v+K9vGvHIATJxbjjubgr+ggqY4rQYyiUlBHoGIIcJa221q0lu59Sh6PqQWfvGz1LQICAmE4bMp+LMpaMIJpgR55IgYIoz5d9OT3vyYE2ZeOThe5paDznNKChMTCwuxKWiCWRgRMUTQvQkTq+nl48dwoUlDjnHjZm7Z1FE3G9lUuZYRM5SLQMQQtSdXuzqu3N6ETUlvfgwXmjLkGEfFAj3T9rCIA9MSCwuxKWiCWQhEDLBmZ4sWPvFq0WMq7U0wfws/5Qv0bBl1s5Eto3y2BE0wC4FIxAr1ILvyozfB/K03pVYWmbjyKGo2jbrZyJZRPluCJpiDQCRAbhqzQj3IrvzoTTB/616pHAdyIPJj1A05tgRNMAOBSEDcNFalepA5P/4fZ+q8U2srOh/mb90plePwrQsatHRDMzkQedg+6sYoFxANApEAuE3Yc9szPHikzZfzYv62ODc5Dsv+0DsI6frzJOdABDnqFnSQwCgXEJ1QApEHH3xQd999t1paWvTZz35W999/v84///ww3jp0Qewi62cP0vb52yAbJDc5Dk6RebSk50AENeoWdJDASh8gWoEHIo888ojmzZunBx98UOedd55+9rOf6bLLLtOuXbs0atSooN8+dOXsIht23oat87dBN0h+5S4kOQfC71G3oIOEKFf6MBUEnBB4IHLvvffqxhtv1De/+U1J0v33369nnnlGS5YsUVNTU9BvH7pydpElb6O0MHqtfo08mZoDERa/Rt3CCBKiWunDVBDwkUBLvB87dkxbtmzR9OnTu70+ffp0vfDCC72Ob2trUzab7fZlm3J3kaUkeWFhbYXuppx2sfbOpHLbUcuNul111ic1ZezQsgKFMLY9iGKlj+lbLQBhC3RE5ODBg2pvb9cpp5zS7fVTTjlFra2tvY5vamrSokWLgjylwPmxiyzDtN2F1Wt1M0I16/wTq2ZU4OeMYPknjCAh7Dwtir4BvYWy6V0q1f0D5ThOr9ckaf78+cpkMp1fe/fuDeP0SvKygZeXjcF6/l6lPci4CrPXWmqEav7fjWMEKyRhBAlhbyoXxigPYJtAR0Rqa2vVp0+fXqMfBw4c6DVKIknV1dWqrna350pYypnLZZmsv8LutZYaoZrRWK9pnzlFv9m0R2+9875GDzlJX5syRv0+xmbWfgojmTvsPC2KvgG9BRqI9OvXTxMmTNDatWv1pS99qfP1tWvX6qqrrgryrX1RKkFy3iWf1pjak/JOpTDd4p8oVhcVW1mULzj9+cbmWAaZUa7sCCtICLPjYHvRN1uwIskuKccpVhmhco888oi+9rWv6aGHHtKUKVO0dOlSLVu2TK+++qpGjx5d9Hez2azS6bQymYxqamqCPM1e2jscTV28zlXlU4mM96DlgkIpf4MU1rRIoeA07PMIgykrO8I6jzAar9xzpVRQvfG2aRW/d1IbY1Pu26Tz0n4HHohIJwqa/ehHP1JLS4saGxt133336YILLij5e1EGIpt2H9LMZZtdHx/Hhsg0UT9gSgWnfjYiUTMt4IpToxpGUB31ZyUqpt23SWZcIFKuKAORx7fv0y2rtnv6nTg1RKaKskFyG5yunDXZyoJxOUEGXDYFFEGea5CBQlIb4yR1FGzgpf1mr5kCypmjLbaM1KYHsMmirAqblETDoJZL29RLD/pcg8ohS/Ly4KiK06FyBCIFlEqQLKZnQ2TTAxiFJSXRMIiAy6b9XMI61yCC6iQ3xknpKMQR6w0LKFYPpJSuDVGSqyh6qb9ig7BrTkTF74ArrMq4frDpXPNJcmOclI5CHBGIFFGouFUhPRsi2x9qlVizs0VTF6/TzGWbdcuq7Zq5bLOmLl5ndeBVbrE6t0wJ3PwOuGwq4mXTueaT5MY4KR2FOCIQKWFGY7023jZNK2dN1k+uOUu3XnKqJHcNke0PtXLFeRQoqL2BTArc/A64bOql23Su+SS5MQ66o4DgkCPiQs+53NPqBrkqfmT7Q60cSUiW8zvR0MT8CT+LfNnUS7fpXPNJ+o7eVLW2E4FIGdw2RLY/1MrhdhTol39s1g3nNVj7QPQr0dDkwM2vgCuKyrjlsulcC0l6Y0xVa/sQiJTJTUMUh4eaV25Hd+546s+xLYvuhemrHPwIuGzqpdt0rsUkvTGOcpk/vCNHJEBJnLP0MroTh5yRSiVl+i6o3Jog2HSuxbCjN2zBiEjAkjZM6qX+StRTDyZI0vSdTb10m84VsB2BSAiS9FArNrSdT9RTD1FL2vSdTUPmNp0rYDOmZkKSpGFSr/VXJPunHsqVxOk7AOiKQASByNVf+cHlp7s6Pg5TD+WKS04C4slLoT1TivLBLkzNIDB9qlK64bwG/Xxjc8mphwmjB2vT7kOxn7oqJEnTd7CHl32y2FML5Uo5jmNsyOplG2GYK1ewS8q/HPJbFzToiT+18AADDFKo0F7uc9t1tM7LsUgGL+03UzMBY6iy+NTDty5o0NINzbEsBw/Yyss+WUneUwv+YGomQAxVfiTf1MOE0YN14d3PGVlVFEgyr/tk+V2Ur73DYZoyQQhEAmLi/iFR67kcctPuQ0ZXFQWSKohCe26PpQOXPEzNBIChSneSUlUUsI2XQnt+FuWLYufusFcFMV3fGyMiAShn/5AkDkUmqaooYBOvhfb8KMoXxQaQYa8KYrQnP0ZEAuC1p79mZ4umLl6nmcs265ZV2zVz2WZNXbwu9omauYddoUdKSic+pHGpKhpH9O7iyUuhPb+K8nnNS6mUl9EXP0ZqohjtsQWBSAC89PSTfHNSVdQuPYOO372SzAA6KbwU2vOjKF+YU7Vhrwpiur44pmYC4HZYs9SqEUm6ffUOfXC8Q3U18ZyuSdqmgDbIN024dldrr/9H+SQ5GTuOvBTa83JsvnsszKnasFcFlTNdnyQEIgEotvFb157+lrfeLflgf+fIcd36yHZJ8Z1LpKqoOfLNYX/8pL567/3jrn6fZdfx42XzPzfHFsqT+MHlp4e2AWTYq4JIzC+OqZmAzGis17cuaFCqx3M4lTpRSXRGY73nmy7O0zVJ2hQwx7T8ikLThG6DkBy/5/IRH8Wmouc8vE1fPPNEJyvoqdqwVwWRmF8cIyIBWbOzRUs3NPeK7DscaemGZp09arDnm47eZnyYlj1fbA67XEnt3SE/N6tinvhTi3761fG646lgp2rDXhXk9f2ShhGRALh5qC96cpcmjB5cdNVIPvQ27WdignKpOexyJLV3h/zc5kkMHthPG2+bppWzJusn15yllbMma+Nt03wN0MNeFURifnEEIgFw+4Hb8ta7BW/OUuht2snU7Hk/7yeWXSMfL3kSYUzVhr0qyI+/EVdMzQTAywfuqrM+mXfVSCn0Nu1kava8X/cTvbtg2Vz40MQ8iaBWBfnxfklCIBIAtx+kPQePSOp+c7ZmPtAdT/1Z7x45xlxiDJmaPV9qDtstll0Hx7S8Iq9MzZPwe1VQGH8jbghEAnBOwxDV1fRXa7Z4Y7Lyxbc1d9qpnfOQuZtzQL8+JZf+Jj2CtpWJvUKp9JJzR72X8eaWXA4eWE3vLmBx2ETTbVkD7h//mT6SlnIcx9hSbtlsVul0WplMRjU1NVGfjic/efYN3ffs6yWPWzlrct7o+HevtOh/Pb5T7xw51vmaTb0f5Nfe4Wjq4nUle4Ubb5sWyYOiWK+bIeVo5O6ZQlN6Ud8zXtk+smObqK63l/abEZGAjKk9ydVx+Ybg1+xs0R1P7eoWhAwZ2Fc/uPx0PqiWM71XWGoOmyHl8AWdVxR2b5k8ifDYMpJGIBKQcofgC9047x45rjkPb9OSqpQRNw7KZ3pZe+awzRJkXlFUvWXuseBFsZtxuQhEAlJOYpZNNw4qQ68QbgWVV2RLbxmFFRvNMnWFXj4EIi6UM3RZzhC8TTcOKkevEG4EsdqETo/9So1mmbpCLx8CkRIqGbr0OgRv041jChOzwU08J9griLwiOj12czOaZeoKvXwIRIrwY+jSyxC8LTeOKQ2tidn3Jp4T7Od3XhGdHnu5Hc1a/48XG1m3JR8CkQL8HLp0OwRvasGfrkxpaE2c3zbxnOAPE4JvP/OKbOn0oDevW4iYukKvK/aaKcDL0KVfTN8YyZTN2kzcr8XEc4I/1uxs0dTF6zRz2Wbdsmq7Zi7brKmL10WyOaFfe7DkOj2Fftu0/YLaOxxt2n1Ij2/fp027DyX6c+RlNMuW/W0YESng2V2tro7ze+jS1KWdJiW3mTi/beI5oXJxHeUyvZ5NV6aMwprC62iWDSv0CETyWLOzRb/44x5XxwYxdGnijWNSQ2vi/LaJ54TKmBR8B8HUTk9XcQ0EK1HOFL7pK/QIRHo49mGHbl+9s+RxQedrmHbjmNTQmji/beI5oTImBd9BMbHTkxP3QLBcNo1muUWOSBdrdrZoctOz3UqrF+LIvv/ZlTCpoTVxftvEc0JlTAq+g+RX3onfosjTs4UtuR9uBRaI7NmzRzfeeKMaGho0YMAAjR07VgsWLNCxY6Ub+SjkhgDfOXK89MGSvnHeGOv+Z1fCpIbWxKReE88JlTEp+E6ipASC5ZrRWK+Nt03TylmT9ZNrztLKWZO18bZpVrZLgQUif/nLX9TR0aGf/exnevXVV3XffffpoYce0u233x7UW5at2BBgIZeOqwvsfExkWkNrYo/AxHNC+UwKvpOIQLA0U0ezvEo5jhPaOqi7775bS5Ys0ZtvvunqeC/bCFdi0+5Dmrlss6tje265bUJ9gTCZlsFu4vU38ZxQntxIqZR/Lp4AMzjtHY6mLl5XMikz9yyGWby036Emq2YyGQ0ZYl7vwevQXq7nb1qjHAbTkttMS+qVzDwnlMeGlSVxFcekTOQX2ojI7t27NX78eN1zzz365je/mfeYtrY2tbW1dX6fzWY1cuRIY0ZEhg7sp//9pUbNaKwvuKyMnhIQP4xyRSeJHb448DIi4jkQWbhwoRYtWlT0mJdeekkTJ07s/H7//v268MILdeGFF+rnP/+5578ddCBSaghQkoYM7KvN8y9Rv49VdR5fKKObIUMA8A+BoH0CDUQOHjyogwcPFj1mzJgx6t//RALR/v37dfHFF2vSpEn65S9/qaqqwvmxUY2ISN7mgt2OoKycNZkhegC+oUGGLQLNEamtrVVtba2rY/ft26eLL75YEyZM0PLly4sGIZJUXV2t6upqr6fkCy9zwSwrQzn8akRojJKJKQpUwuTnRmDJqvv379dFF12kUaNG6cc//rH++7//u/NndXVmLn11m4jJsjJ45VcjQmOUTJQ6RyVMf24Elqz6y1/+Ul//+tfz/sztW4a1fNcrlpXBC78Sm0mQTiZy0lCJqJ4bXtrvwAqa3XDDDXIcJ++X7boW9yqEZWWQSu+XIZ3YL6PUtuZ+/R3Yx9RS5+0djjbtPqTHt+/Tpt2HuPcMZMtzg03vyjSjsV7fuqBBy/7QrK7/D6tS0qzzG+iZQpJ/G6clYQM25GdiTlrQQ/0m5zPYxJbnBoFImdbsbNHSDc29Ik3HkZZuaNbZowYTjMC3RsTExgjhMC0nLeh8FdPzGcJSKBjzEqTZ8twgECkD21PDLb8aEdMaI4Qnt+dNqZy0MPa8CfrZR1LuCYWCsS+eWa8n/tTiOkiz5bkRWI5InJk6Zwvz+LVxGhuwJZdJG04G+eyzJZ8haLlgrOd1bskc1c82NPd6PRekrdnZ0utv2fLcIBApgy3DXYieX42ISY0RwmfKzs5BPvvo4JW3E3yxIM2W5wZTM2WwZbgLZvBr4zQ2YEs2EzacdPtM23PwiOe/TQevdDBWSLGkUxueGwQiLvRMDpowerAxc7awg1+NiAmNEaIT9c7OpfJVcu579g2dVjfIUyNHB6/yIKvQ75v+3CAQKaFY0tDSDc1sTw3X/GpEom6MkFy5of7cvlyFlJO0alJSblQqDbKK/b7Jzw1yRIoolDTUmjmqpRua9a0LGiKfswWAMM1orNe8Sz5d9Jhy8jlsyWcIUqnk0kJMSTotFyMiBbhZpvbEn1q0/h8v1pa33jVyuAsAgjCm9iRXx3mdaiiUzzBkYD9dddZwpQf0U3uHE9tnbNcRp56j7YXEIUgjECnAbQb3lrfeNXa4CwCCEGQ+R9d8hmd3tWr19n06dOSY/vWPe/Svf9wT++JmhYKxQnVETEo6LReBSAFkcANAfkHnc/SpSinzwYngI4nFzYoll/7TjNONTTotF4FIAWRwA0B+xaYQvE4V5CtZLinx1asLJZeanHRaLgKRAsjgBoDC/KhPUWhV4jWfH2XFZm3wB4FIAX5G/AAQR5XUpyi2r8x9z77u6v2ZGo8HApEibKhIBwBRKmeqwM2+Mm4wNR4PBCIlmF6RDgBsU24p8xymxuOFQMSFOCYHAUBUvEypMDUef1RWBQCEyu2Uyq2XnEr16gRgRAQAECq3qxLnTjtVc6edytR4zBGIAABC5XVVIlPj8cbUDAAgdLlViUy9gBERAEAkolyVmK+iK1M+0SAQAQBEJopViYUqulIfKhpMzQAAEiNX0bVnHZPcZnprdrZEdGbJRSACAEgENxVdFz25S+0dXuq7olIEIgCARChV0bXrZnoID4EIACAR3FZ0ZTO9cBGIAAASwW1FVzbTCxeBCAAgEXIVXQst0k3pxOoZNtMLF4EIACARchVdJfUKRthMLzoEIgCAxKCiq3koaAYASJQoK7qiNwIRAEDiRFHRFfkxNQMAACJDIAIAACLD1AwAAGVgB19/EIgAAOARO/j6h6kZAAA8YAdffxGIAADgEjv4+o9ABAAAl9jB138EIgAAuMQOvv4jEAEAwCV28PUfgQgAAC6xg6//CET+v/YOR5t2H9Lj2/dp0+5DJBoBAHphB1//hVJHpK2tTZMmTdKf/vQnbdu2TWeddVYYb+sa68EBAG7ldvDt2W4MGdhPd1zVSLvhUSgjIv/0T/+k4cOHh/FWnrEeHADg1YzGev3g8tM1ZGDfztcOHTmmO57aRbvhUeCByNNPP63f//73+vGPfxz0W3nGenAAQDnW7GzRnIe36Z0jx7u9TifWu0ADkf/6r//SrFmz9Jvf/EYnnXRSyePb2tqUzWa7fQWJ9eAAAK/oxPorsEDEcRzdcMMNmj17tiZOnOjqd5qampROpzu/Ro4cGdTpSWI9OADAOzqx/vIciCxcuFCpVKro18svv6x/+Zd/UTab1fz5813/7fnz5yuTyXR+7d271+vpecJ6cACAV3Ri/eV51czcuXN1zTXXFD1mzJgxuvPOO7V582ZVV1d3+9nEiRN17bXX6le/+lWv36uuru51fJBy68FbM0fzDrGlJNWxHhwoiG3QkUR0Yv3lORCpra1VbW1tyeP++Z//WXfeeWfn9/v379ff/u3f6pFHHtGkSZO8vm0gcuvBb1qxVSmpWzDCenCgOJa9I4naOxx1dDj6+IC+eu+D43mPoRPrTWB1REaNGtXt+5NPPlmSNHbsWI0YMSKot/Ws0HrwOh6oQEG5Ze89RxJbMkc1e8VWPfjV8fq7M/jsIF7yBd890Yn1LpSCZqab0VivS8fVMcQMuFBsxUDO3JVb9YDO1t+dYWb9IMCrQsF3T3RivQstEBkzZowcx9ylTH2qUpoydmjUpwEYr9SKAUnqcKT/+fA2PVSV4oEM67kJvj8+oK9+eu14Tf6boXRiPWKvGQCeeFkJQC0FxIGb4Pu9D46rKpUiCCkDgQgAT7ysBKCWAuKA5brBIhAB4Elu2btbPJxhO5brBotABIAnXbdBd4OHM2yXC74LTbqkdGLpOst1y0MgAsCzGY31evCr41VsOpyHM+Kia/Dd85ZnuW7lCEQAlOXvzqjXAzPPzvszHs6Im1zNqboe05J16f5act14VodVIOUYvKY2m80qnU4rk8mopqYm6tMBkAcVVpEkbGvgjpf2m0AEQMV4OAPoykv7TWVVABWjICCAcpEjAgAAIkMgAgAAIkMgAgAAIkMgAgAAIkMgAgAAIkMgAgAAIkMgAgAAIkMdEQAAYsamIoMEIgAiY9PDErCFbdsuEIgAiIRtD0vABmt2tuimFVvVc++W1sxR3bRiq5Eb9JEjAiB0uYdl1yBE+uhhuWZnS0RnBtirvcPRoid39QpCJHW+tujJXWrvMGuLOQIRAKGy9WEJmO7F5nd6BfddOZJaMkf1YvM74Z2UCwQiAEJl68MSMN2Bw4U/V+UcFxYCEQChsvVhCZhu2KD+vh4XFpJVAYTK1oclEBS/Vo+d0zBE9en+as0czTv1mZJUlz7x901CIAIgVLY+LIEg+Ll6rE9VSguuHKebVmxVSur2+cqFNQuuHGfcEnmmZgCEKvewlD56OOaY/LAE/BbE6rEZjfVact141aW7jyjWpfsbuXRXklKO4xibmp7NZpVOp5XJZFRTUxP16QDwEXVEkGTtHY6mLl5XMHE7NzK48bZpZQXlURcL9NJ+J3JqJur/QQBO9NwuHVfHZxGJ5GX12JSxQz3//T5VqbJ+LwqJC0TohQHmsOlhCfiJ1WMfSVSOCNUcAQAmYPXYRxITiFDNEQBgitzqsUITkSmdGK1PwuqxxAQiVHMEAJiC1WMfSUwgwnwcAMAkNi61DUJiklWZjwMAmIbVYwkKRKjmCAAwUdJXjyVmaob5OAAAzJOYQERiPg4AANMkZmomh/k4AADMkbhARGI+DgAAUyRqagYAAJiFQAQAAESGQAQAAESGQAQAAESGQAQAAESGQAQAAEQm8EDkqaee0qRJkzRgwADV1tbq6quvDvotAQCAJQKtI/Lb3/5Ws2bN0g9/+ENNmzZNjuNox44dQb4lAACwSGCByIcffqhbbrlFd999t2688cbO10877bSg3hIAAFgmsKmZrVu3at++faqqqtLZZ5+t+vp6XXbZZXr11VcL/k5bW5uy2Wy3LwAAkqi9w9Gm3Yf0+PZ92rT7kNo78u0db7/ARkTefPNNSdLChQt17733asyYMbrnnnt04YUX6vXXX9eQIUN6/U5TU5MWLVoU1CkBAGCFNTtbtOjJXWrJHO18rT7dXwuuHBe7DVo9j4gsXLhQqVSq6NfLL7+sjo4OSdL3v/99/cM//IMmTJig5cuXK5VK6d///d/z/u358+crk8l0fu3du7eyfx0AAJZZs7NFN63Y2i0IkaTWzFHdtGKr1uxsiejMguF5RGTu3Lm65pprih4zZswYHT58WJI0bty4zterq6v1N3/zN3r77bfz/l51dbWqq6u9nhIAALHQ3uFo0ZO7lG8SxpGUkrToyV26dFxdbHaN9xyI1NbWqra2tuRxEyZMUHV1tV577TVNnTpVknT8+HHt2bNHo0eP9n6mAADE3IvN7/QaCenKkdSSOaoXm9+JzS7ygeWI1NTUaPbs2VqwYIFGjhyp0aNH6+6775YkffnLXw7qbQEAsNaBw4WDkHKOs0GgdUTuvvtufexjH9PXvvY1ffDBB5o0aZLWrVunwYMHB/m2AABYadig/r4eZ4OU4zjGrgfKZrNKp9PKZDKqqamJ+nQAAAhUe4ejqYvXqTVzNG+eSEpSXbq/Nt42zegcES/tN3vNAABgiD5VKS248sQij55hRu77BVeOMzoI8YpABAAAg8xorNeS68arLt19+qUu3V9LrhsfuzoigeaIAAAA72Y01uvScXV6sfkdHTh8VMMG9dc5DUNiNRKSQyACAICB+lSlYrNEtximZgAAQGQIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQGSMrqya2xg4m81GfCYAAMCtXLuda8eLMToQOXz4sCRp5MiREZ8JAADw6vDhw0qn00WPSTluwpWIdHR0aP/+/Ro0aJBSKf82+slmsxo5cqT27t2rmpoa3/5uXHG9vOF6ecP18o5r5g3Xyxs/rpfjODp8+LCGDx+uqqriWSBGj4hUVVVpxIgRgf39mpoabkoPuF7ecL284Xp5xzXzhuvlTaXXq9RISA7JqgAAIDIEIgAAIDKJDESqq6u1YMECVVdXR30qVuB6ecP18obr5R3XzBuulzdhXy+jk1UBAEC8JXJEBAAAmIFABAAARIZABAAARIZABAAARCZxgciDDz6ohoYG9e/fXxMmTNAf/vCHqE/JCAsXLlQqler2VVdX1/lzx3G0cOFCDR8+XAMGDNBFF12kV199NcIzDteGDRt05ZVXavjw4UqlUnrssce6/dzN9Wlra9PNN9+s2tpaDRw4UF/84hf1n//5nyH+K8JV6prdcMMNve65yZMndzsmKdesqalJn//85zVo0CANGzZMf//3f6/XXnut2zHcY925uWbcYx9ZsmSJzjjjjM4iZVOmTNHTTz/d+fMo769EBSKPPPKI5s2bp+9///vatm2bzj//fF122WV6++23oz41I3z2s59VS0tL59eOHTs6f/ajH/1I9957rx544AG99NJLqqur06WXXtq5H1DcHTlyRGeeeaYeeOCBvD93c33mzZun1atXa9WqVdq4caP++te/6oorrlB7e3tY/4xQlbpmkjRjxoxu99zvfve7bj9PyjVbv3695syZo82bN2vt2rX68MMPNX36dB05cqTzGO6x7txcM4l7LGfEiBG666679PLLL+vll1/WtGnTdNVVV3UGG5HeX06CnHPOOc7s2bO7vfaZz3zG+d73vhfRGZljwYIFzplnnpn3Zx0dHU5dXZ1z1113db529OhRJ51OOw899FBIZ2gOSc7q1as7v3dzfd577z2nb9++zqpVqzqP2bdvn1NVVeWsWbMmtHOPSs9r5jiOc/311ztXXXVVwd9J8jU7cOCAI8lZv3694zjcY270vGaOwz1WyuDBg52f//znkd9fiRkROXbsmLZs2aLp06d3e3369Ol64YUXIjors7zxxhsaPny4GhoadM011+jNN9+UJDU3N6u1tbXbtauurtaFF17ItZO767NlyxYdP3682zHDhw9XY2Njoq/h888/r2HDhunTn/60Zs2apQMHDnT+LMnXLJPJSJKGDBkiiXvMjZ7XLId7rLf29natWrVKR44c0ZQpUyK/vxITiBw8eFDt7e065ZRTur1+yimnqLW1NaKzMsekSZP061//Ws8884yWLVum1tZWnXvuuTp06FDn9eHa5efm+rS2tqpfv34aPHhwwWOS5rLLLtO//du/ad26dbrnnnv00ksvadq0aWpra5OU3GvmOI6+853vaOrUqWpsbJTEPVZKvmsmcY/1tGPHDp188smqrq7W7NmztXr1ao0bNy7y+8vo3XeDkEqlun3vOE6v15Losssu6/zvz33uc5oyZYrGjh2rX/3qV53JXVy74sq5Pkm+hl/5ylc6/7uxsVETJ07U6NGj9dRTT+nqq68u+Htxv2Zz587VK6+8oo0bN/b6GfdYfoWuGfdYd6eddpq2b9+u9957T7/97W91/fXXa/369Z0/j+r+SsyISG1trfr06dMrcjtw4ECvKBDSwIED9bnPfU5vvPFG5+oZrl1+bq5PXV2djh07pnfffbfgMUlXX1+v0aNH64033pCUzGt2880364knntBzzz2nESNGdL7OPVZYoWuWT9LvsX79+ulTn/qUJk6cqKamJp155pn6yU9+Evn9lZhApF+/fpowYYLWrl3b7fW1a9fq3HPPjeiszNXW1qY///nPqq+vV0NDg+rq6rpdu2PHjmn9+vVcO8nV9ZkwYYL69u3b7ZiWlhbt3LmTa/j/HTp0SHv37lV9fb2kZF0zx3E0d+5cPfroo1q3bp0aGhq6/Zx7rLdS1yyfJN9j+TiOo7a2tujvr4pSXS2zatUqp2/fvs4vfvELZ9euXc68efOcgQMHOnv27In61CL33e9+13n++eedN99809m8ebNzxRVXOIMGDeq8NnfddZeTTqedRx991NmxY4czc+ZMp76+3slmsxGfeTgOHz7sbNu2zdm2bZsjybn33nudbdu2OW+99ZbjOO6uz+zZs50RI0Y4zz77rLN161Zn2rRpzplnnul8+OGHUf2zAlXsmh0+fNj57ne/67zwwgtOc3Oz89xzzzlTpkxxPvnJTybymt10001OOp12nn/+eaelpaXz6/333+88hnusu1LXjHusu/nz5zsbNmxwmpubnVdeecW5/fbbnaqqKuf3v/+94zjR3l+JCkQcx3F++tOfOqNHj3b69evnjB8/vttSryT7yle+4tTX1zt9+/Z1hg8f7lx99dXOq6++2vnzjo4OZ8GCBU5dXZ1TXV3tXHDBBc6OHTsiPONwPffcc46kXl/XX3+94zjurs8HH3zgzJ071xkyZIgzYMAA54orrnDefvvtCP414Sh2zd5//31n+vTpzic+8Qmnb9++zqhRo5zrr7++1/VIyjXLd50kOcuXL+88hnusu1LXjHusu2984xudbd8nPvEJ5wtf+EJnEOI40d5fKcdxnMrGVAAAAMqTmBwRAABgHgIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQGQIRAAAQmf8HUW0n4kHPnG8AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(X_train,res)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We are confident that the model fit isn't by chance, and has decent predictive power. The normality of residual terms allows some inference on the coefficients.\n",
    "\n",
    "Although, the variance of residuals increasing with X indicates that there is significant variation that this model is unable to explain."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you can see, the regression line is a pretty good fit to the data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: Predictions on the Test Set\n",
    "\n",
    "Now that you have fitted a regression line on your train dataset, it's time to make some predictions on the test data. For this, you first need to add a constant to the `X_test` data like you did for `X_train` and then you can simply go on and predict the y values corresponding to `X_test` using the `predict` attribute of the fitted regression line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add a constant to X_test\n",
    "X_test_sm = sm.add_constant(X_test)\n",
    "\n",
    "# Predict the y values corresponding to X_test_sm\n",
    "y_pred = lr.predict(X_test_sm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "126     7.374140\n",
       "104    19.941482\n",
       "99     14.323269\n",
       "92     18.823294\n",
       "111    20.132392\n",
       "dtype: float64"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import mean_squared_error\n",
    "from sklearn.metrics import r2_score"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Looking at the RMSE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.019296008966232"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Returns the mean squared error; we'll take a square root\n",
    "np.sqrt(mean_squared_error(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### Checking the R-squared on the test set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.792103160124566"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r_squared = r2_score(y_test, y_pred)\n",
    "r_squared"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Visualizing the fit on the test set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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22w2NTQ0eG1rbGzUWWed5bNHxm3+/PleAaitrU1HjhzROeec4zPoOJ1O9evXTwcPHlReXl6E7wbh4JonB9c98bjmycF1T7x4XHPDMHTs2DEVFRUFPC7ugaW5uVnvv/++rrrqKp/7R4wYoQ0bNnht27Rpky6//HJ17drV73mzs7OVnZ3tta1nz55B25OXl8cHO8G45snBdU88rnlycN0TL9bXPFDPilvMB93ef//9qqysVG1trV5//XXdeOONcjqdmjFjhiRXz8j06dM9x99999365JNPNHfuXL3//vt69tln9cwzz+j++++PddMAAECKinkPy6effqqbb75ZX3zxhc4991yVlZVp165d6t+/vySpvr5edXV1nuOLi4v1yiuv6N/+7d/05JNPqqioSI8//jhTmgEAgEfMA8vKlSsD7l+2bFmnbVdffbWqq6tj3RQv2dnZWrBgQafbSIgfrnlycN0Tj2ueHFz3xEvmNbcYweYRAQAAJBmLHwIAANMjsAAAANMjsAAAANMjsAAAANPLiMDy1FNPqbi4WDk5Obrsssv0l7/8JdlNShsLFy6UxWLxerRfqdswDC1cuFBFRUXq3r27Ro8erffeey+JLU5N27dv16RJk1RUVCSLxaK1a9d67Q/lOjc3N+vee+9V79691aNHD1177bX69NNPE/guUk+w637bbbd1+vyXlZV5HcN1D09FRYWGDh2q3NxcFRQU6LrrrtP+/fu9juHzHluhXHMzfNbTPrCsWrVKc+bM0c9+9jPt2bNHV111lSZMmOBVCwbRueiii1RfX+95vPvuu559Dz/8sB555BEtWbJEb775pmw2m8aOHatjx44lscWp58SJExoyZIiWLFnic38o13nOnDlas2aNVq5cqR07duj48eOaOHGiWltbE/U2Uk6w6y5J5eXlXp//V155xWs/1z08lZWVmjVrlnbt2qXNmzfr9OnTGjdunE6cOOE5hs97bIVyzSUTfNaNNDds2DDj7rvv9tp24YUXGj/5yU+S1KL0smDBAmPIkCE+97W1tRk2m8146KGHPNuampoMq9Vq/O53v0tQC9OPJGPNmjWe56Fc56NHjxpdu3Y1Vq5c6Tnm0KFDRlZWlrFx48aEtT2VdbzuhmEYM2bMMCZPnuz3NVz36DU2NhqSjMrKSsMw+LwnQsdrbhjm+KyndQ/LqVOn9NZbb2ncuHFe28eNG6edO3cmqVXp58CBAyoqKlJxcbFuuukmffTRR5Kk2tpaNTQ0eF3/7OxsXX311Vz/GArlOr/11ltqaWnxOqaoqEilpaX8LqK0bds2FRQUaNCgQbrzzjvV2Njo2cd1j57D4ZAk5efnS+Lznggdr7lbsj/raR1YvvjiC7W2tqqwsNBre2FhYacVohGZ4cOH6/nnn9err76qp59+Wg0NDRo5cqQOHz7sucZc//gK5To3NDSoW7du6tWrl99jEL4JEyboj3/8o7Zu3arf/OY3evPNN3XNNdeoublZEtc9WoZhaO7cubryyitVWloqic97vPm65pI5PutxX63ZDCwWi9dzwzA6bUNkJkyY4PnvwYMHa8SIERowYID+8Ic/eAZkcf0TI5LrzO8iOlOnTvX8d2lpqS6//HL1799fL7/8sq6//nq/r+O6h2b27Nl65513tGPHjk77+LzHh79rbobPelr3sPTu3VtdunTplO4aGxs7pXPERo8ePTR48GAdOHDAM1uI6x9foVxnm82mU6dO6csvv/R7DKJnt9vVv39/HThwQBLXPRr33nuv1q9fr9dee019+/b1bOfzHj/+rrkvyfisp3Vg6datmy677DJt3rzZa/vmzZs1cuTIJLUqvTU3N+v999+X3W5XcXGxbDab1/U/deqUKisruf4xFMp1vuyyy9S1a1evY+rr67V3715+FzF0+PBhHTx4UHa7XRLXPRKGYWj27NlavXq1tm7dquLiYq/9fN5jL9g19yUpn/WYDN01sZUrVxpdu3Y1nnnmGWPfvn3GnDlzjB49ehgff/xxspuWFn70ox8Z27ZtMz766CNj165dxsSJE43c3FzP9X3ooYcMq9VqrF692nj33XeNm2++2bDb7YbT6Uxyy1PLsWPHjD179hh79uwxJBmPPPKIsWfPHuOTTz4xDCO063z33Xcbffv2NbZs2WJUV1cb11xzjTFkyBDj9OnTyXpbphfouh87dsz40Y9+ZOzcudOora01XnvtNWPEiBFGnz59uO5RmDlzpmG1Wo1t27YZ9fX1nsfJkyc9x/B5j61g19wsn/W0DyyGYRhPPvmk0b9/f6Nbt27GpZde6jVVC9GZOnWqYbfbja5duxpFRUXG9ddfb7z33nue/W1tbcaCBQsMm81mZGdnG6NGjTLefffdJLY4Nb322muGpE6PGTNmGIYR2nX+6quvjNmzZxv5+flG9+7djYkTJxp1dXVJeDepI9B1P3nypDFu3Djj3HPPNbp27Wqcd955xowZMzpdU657eHxdb0nGc8895zmGz3tsBbvmZvmsW/7RWAAAANNK6zEsAAAgPRBYAACA6RFYAACA6RFYAACA6RFYAACA6RFYAACA6RFYAACA6RFYAACA6RFYAACA6RFYAACA6RFYAACA6RFYAACA6f3/8VvsJjoWwSwAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(X_test, y_test)\n",
    "plt.plot(X_test, 6.948 + 0.054 * X_test, 'r')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Linear Regression using `linear_model` in `sklearn`\n",
    "\n",
    "Apart from `statsmodels`, there is another package namely `sklearn` that can be used to perform linear regression. We will use the `linear_model` library from `sklearn` to build the model. Since, we hae already performed a train-test split, we don't need to do it again.\n",
    "\n",
    "There's one small step that we need to add, though. When there's only a single feature, we need to add an additional column in order for the linear regression fit to be performed successfully."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train_lm, X_test_lm, y_train_lm, y_test_lm = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(140,)"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train_lm.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train_lm = X_train_lm.values.reshape(-1,1)\n",
    "X_test_lm = X_test_lm.values.reshape(-1,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(140, 1)\n",
      "(140,)\n",
      "(60, 1)\n",
      "(60,)\n"
     ]
    }
   ],
   "source": [
    "print(X_train_lm.shape)\n",
    "print(y_train_lm.shape)\n",
    "print(X_test_lm.shape)\n",
    "print(y_test_lm.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
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
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "# Representing LinearRegression as lr(Creating LinearRegression Object)\n",
    "lm = LinearRegression()\n",
    "\n",
    "# Fit the model using lr.fit()\n",
    "lm.fit(X_train_lm, y_train_lm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6.948683200001357\n",
      "[0.05454575]\n"
     ]
    }
   ],
   "source": [
    "print(lm.intercept_)\n",
    "print(lm.coef_)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The equationwe get is the same as what we got before!\n",
    "\n",
    "$ Sales = 6.948 + 0.054* TV $"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sklearn linear model is useful as it is compatible with a lot of sklearn utilites (cross validation, grid search etc.)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## Addressing some common questions/doubts on Simple Linear Regression\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q: Why is it called 'R-squared'?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Based on what we learnt so far, do you see it? Can you answer this?\n",
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1.         0.90321277]\n",
      " [0.90321277 1.        ]]\n"
     ]
    }
   ],
   "source": [
    "corrs = np.corrcoef(X_train, y_train)\n",
    "print(corrs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8157933136480384"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corrs[0,1] ** 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Correlation (Pearson) is also called **\"r\"** or **\"Pearson's R\"**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q: What is a good RMSE? Is there some RMSE that I should aim for?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<br>\n",
    "\n",
    "<br>\n",
    "\n",
    "You should be able to answer this by now!\n",
    "\n",
    "\n",
    "<br>\n",
    "\n",
    "\n",
    "<br>\n",
    "\n",
    "\n",
    "\n",
    "Look at \"Sharma ji ka beta\"; he could answer this in a moment. How lucky is Sharma ji to have such a smart kid!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " \n",
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The RMSE:\n",
    " - depends on the units of the Y variables\n",
    " - is NOT a normalized measure\n",
    " \n",
    "While it can't really tell you of the gooodness of the particular model, it can help you compare models. \n",
    "\n",
    "A better measure is R squared, which is normalized."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<br>\n",
    "<br>\n",
    "<br>\n",
    "<br>\n",
    "<br>\n",
    "<br>\n",
    "<br>\n",
    "<br>\n",
    "<br>\n",
    "<br>\n",
    "<br>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q: Does scaling have an impact on the model? When should I scale?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<br>\n",
    "<br>\n",
    "<br>\n",
    "<br>\n",
    "<br>\n",
    "<br>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "While the true benefits of scaling will be apparent during future modules, at this juncture we can discuss if it has an impact on the model.\n",
    "\n",
    "We'll rebuild the model after scaling the predictor and see what changes.\n",
    "\n",
    "The most popular methods for scaling:\n",
    "1. Min-Max Scaling\n",
    "2. Standard Scaling"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 100)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### SciKit Learn has these scaling utilities handy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler, MinMaxScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'Series' object has no attribute 'reshape'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_1371/3441656285.py\u001b[0m in \u001b[0;36m?\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# One aspect that you need to take care of is that the 'fit_transform' can be performed on 2D arrays only. So you need to\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;31m# reshape your 'X_train_scaled' and 'y_trained_scaled' data in order to perform the standardisation.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mX_train_scaled\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mX_train\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreshape\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0my_train_scaled\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0my_train\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreshape\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.11/site-packages/pandas/core/generic.py\u001b[0m in \u001b[0;36m?\u001b[0;34m(self, name)\u001b[0m\n\u001b[1;32m   5898\u001b[0m             \u001b[0;32mand\u001b[0m \u001b[0mname\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_accessors\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   5899\u001b[0m             \u001b[0;32mand\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_info_axis\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_can_hold_identifiers_and_holds_name\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   5900\u001b[0m         ):\n\u001b[1;32m   5901\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 5902\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mobject\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__getattribute__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m: 'Series' object has no attribute 'reshape'"
     ]
    }
   ],
   "source": [
    "# One aspect that you need to take care of is that the 'fit_transform' can be performed on 2D arrays only. So you need to\n",
    "# reshape your 'X_train_scaled' and 'y_trained_scaled' data in order to perform the standardisation.\n",
    "X_train_scaled = X_train.reshape(-1,1)\n",
    "y_train_scaled = y_train.reshape(-1,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train_scaled.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a scaler object using StandardScaler()\n",
    "scaler = StandardScaler()\n",
    "#'Fit' and transform the train set; and transform using the fit on the test set later\n",
    "X_train_scaled = scaler.fit_transform(X_train_scaled)\n",
    "y_train_scaled = scaler.fit_transform(y_train_scaled)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"mean and sd for X_train_scaled:\", np.mean(X_train_scaled), np.std(X_train_scaled))\n",
    "print(\"mean and sd for y_train_scaled:\", np.mean(y_train_scaled), np.std(y_train_scaled))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let's fit the regression line following exactly the same steps as done before\n",
    "X_train_scaled = sm.add_constant(X_train_scaled)\n",
    "\n",
    "lr_scaled = sm.OLS(y_train_scaled, X_train_scaled).fit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check the parameters\n",
    "lr_scaled.params"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you might notice, the value of the parameters have changed since we have changed the scale."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's look at the statistics of the model, to see if any other aspect of the model has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(lr_scaled.summary())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Model statistics and goodness of fit remain unchanged.\n",
    "\n",
    "##### So why scale at all?\n",
    "- Helps with interpretation (we'll be able to appreciate this better in later modules)\n",
    "- Faster convergence of gradient descent"
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
 "nbformat_minor": 4
}