{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Interview Questions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import all the necessary libraries\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Supress warnings\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### I - Virat Kohli Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"virat.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
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
       "      <th>Runs</th>\n",
       "      <th>Mins</th>\n",
       "      <th>BF</th>\n",
       "      <th>4s</th>\n",
       "      <th>6s</th>\n",
       "      <th>SR</th>\n",
       "      <th>Pos</th>\n",
       "      <th>Dismissal</th>\n",
       "      <th>Inns</th>\n",
       "      <th>Opposition</th>\n",
       "      <th>Ground</th>\n",
       "      <th>Start Date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>12</td>\n",
       "      <td>33</td>\n",
       "      <td>22</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>54.54</td>\n",
       "      <td>2</td>\n",
       "      <td>lbw</td>\n",
       "      <td>1</td>\n",
       "      <td>v Sri Lanka</td>\n",
       "      <td>Dambulla</td>\n",
       "      <td>18-Aug-08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>37</td>\n",
       "      <td>82</td>\n",
       "      <td>67</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>55.22</td>\n",
       "      <td>2</td>\n",
       "      <td>caught</td>\n",
       "      <td>2</td>\n",
       "      <td>v Sri Lanka</td>\n",
       "      <td>Dambulla</td>\n",
       "      <td>20-Aug-08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>25</td>\n",
       "      <td>40</td>\n",
       "      <td>38</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>65.78</td>\n",
       "      <td>1</td>\n",
       "      <td>run out</td>\n",
       "      <td>1</td>\n",
       "      <td>v Sri Lanka</td>\n",
       "      <td>Colombo (RPS)</td>\n",
       "      <td>24-Aug-08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>54</td>\n",
       "      <td>87</td>\n",
       "      <td>66</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>81.81</td>\n",
       "      <td>1</td>\n",
       "      <td>bowled</td>\n",
       "      <td>1</td>\n",
       "      <td>v Sri Lanka</td>\n",
       "      <td>Colombo (RPS)</td>\n",
       "      <td>27-Aug-08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>31</td>\n",
       "      <td>45</td>\n",
       "      <td>46</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>67.39</td>\n",
       "      <td>1</td>\n",
       "      <td>lbw</td>\n",
       "      <td>2</td>\n",
       "      <td>v Sri Lanka</td>\n",
       "      <td>Colombo (RPS)</td>\n",
       "      <td>29-Aug-08</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Runs Mins  BF  4s  6s     SR  Pos Dismissal  Inns   Opposition  \\\n",
       "0   12   33  22   1   0  54.54    2       lbw     1  v Sri Lanka   \n",
       "1   37   82  67   6   0  55.22    2    caught     2  v Sri Lanka   \n",
       "2   25   40  38   4   0  65.78    1   run out     1  v Sri Lanka   \n",
       "3   54   87  66   7   0  81.81    1    bowled     1  v Sri Lanka   \n",
       "4   31   45  46   3   1  67.39    1       lbw     2  v Sri Lanka   \n",
       "\n",
       "          Ground Start Date  \n",
       "0       Dambulla  18-Aug-08  \n",
       "1       Dambulla  20-Aug-08  \n",
       "2  Colombo (RPS)  24-Aug-08  \n",
       "3  Colombo (RPS)  27-Aug-08  \n",
       "4  Colombo (RPS)  29-Aug-08  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Spread in Runs\n",
    "Question 1: Analyse the spread of Runs scored by Virat in all his matches and report the difference between the scores at the 50th percentile and the 25th percentile respectively.\n",
    "\n",
    "    a)16.5\n",
    "    b)22.5\n",
    "    c)26.5\n",
    "    d)32.5\n",
    "\n"
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
      "RangeIndex: 132 entries, 0 to 131\n",
      "Data columns (total 12 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   Runs        132 non-null    object\n",
      " 1   Mins        132 non-null    object\n",
      " 2   BF          132 non-null    int64 \n",
      " 3   4s          132 non-null    int64 \n",
      " 4   6s          132 non-null    int64 \n",
      " 5   SR          132 non-null    object\n",
      " 6   Pos         132 non-null    int64 \n",
      " 7   Dismissal   132 non-null    object\n",
      " 8   Inns        132 non-null    int64 \n",
      " 9   Opposition  132 non-null    object\n",
      " 10  Ground      132 non-null    object\n",
      " 11  Start Date  132 non-null    object\n",
      "dtypes: int64(5), object(7)\n",
      "memory usage: 12.5+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
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
       "      <th>BF</th>\n",
       "      <th>4s</th>\n",
       "      <th>6s</th>\n",
       "      <th>Pos</th>\n",
       "      <th>Inns</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>132.000000</td>\n",
       "      <td>132.000000</td>\n",
       "      <td>132.000000</td>\n",
       "      <td>132.000000</td>\n",
       "      <td>132.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>50.871212</td>\n",
       "      <td>4.371212</td>\n",
       "      <td>0.545455</td>\n",
       "      <td>3.303030</td>\n",
       "      <td>1.575758</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>38.729716</td>\n",
       "      <td>4.404032</td>\n",
       "      <td>1.086795</td>\n",
       "      <td>0.873174</td>\n",
       "      <td>0.496110</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>17.750000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>42.500000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>82.250000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>140.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               BF          4s          6s         Pos        Inns\n",
       "count  132.000000  132.000000  132.000000  132.000000  132.000000\n",
       "mean    50.871212    4.371212    0.545455    3.303030    1.575758\n",
       "std     38.729716    4.404032    1.086795    0.873174    0.496110\n",
       "min      0.000000    0.000000    0.000000    1.000000    1.000000\n",
       "25%     17.750000    1.000000    0.000000    3.000000    1.000000\n",
       "50%     42.500000    3.000000    0.000000    3.000000    2.000000\n",
       "75%     82.250000    7.000000    1.000000    4.000000    2.000000\n",
       "max    140.000000   18.000000    7.000000    7.000000    2.000000"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Runs'] = df['Runs'].apply(lambda x: int(x[:-1]) if isinstance(x,str) and x[-1] == '*'else int(x))\n",
    "df['Runs'] = pd.to_numeric(df['Runs'], errors='coerce')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    132.000000\n",
       "mean      46.848485\n",
       "std       41.994635\n",
       "min        0.000000\n",
       "25%       10.000000\n",
       "50%       32.500000\n",
       "75%       80.250000\n",
       "max      154.000000\n",
       "Name: Runs, dtype: float64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Runs'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "22.5"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "difference = 32.500000 - 10.000000\n",
    "difference"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hence answer for Q1 is option (b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Box Plots\n",
    "\n",
    "Question 2: Plot a Box Plot to analyse the spread of Runs that Virat has scored. The upper fence in the box plot lies in which interval?\n",
    "\n",
    "    a)100-120\n",
    "    b)120-140\n",
    "    c)140-160\n",
    "    d)160-180\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAyUAAAIhCAYAAABQchU9AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAsAElEQVR4nO3de5zVdZ348fdh7sAABigQCpi3ElET1NQUJVHzklcUb5i2uypqaBmWW9rWilp5KTPTFHNZkdwQUdaEUkkfkpIIZlbahrfQWEW5D8zl8/vDH2cdQZkZhvnA8Hw+HjycOed7vvM57zky5zXf7zkUUkopAAAAMumQewEAAMCWTZQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQA7cKdd94ZhUKh0Z+ePXvG0KFD48EHH2zz9Tz22GON1lJSUhLbbLNNnHTSSfGnP/2puN3LL78chUIh7rzzzmZ/jRdeeCGuvPLKePnll1tv4f/fb37zmxg8eHB06tQpCoVCTJkyZa1tbrzxxigUCvGrX/3qQ/dz2223RaFQiMmTJ2/Qff0oHzWHs846K4YOHdoqX+eDj68uXbrEfvvtFxMnTmyV/QNsyUQJ0K6MHz8+Zs2aFU8++WTceuutUVJSEkcffXQ88MADWdZz1VVXxaxZs+LRRx+NsWPHxowZM2L//fePv//97xu87xdeeCG+/e1vt3qUpJRixIgRUVZWFlOnTo1Zs2bFQQcdtNZ2p59+elRUVMQdd9zxofsaP3589OzZM44++ujo3bt3zJo1K4488shWXe/GmsO6nHjiicXH1y233BJLliyJU089Ne6+++6N/rUB2rPS3AsAaE0DBw6MwYMHFz8//PDDY6uttoqJEyfG0Ucf3ebr2XHHHWPfffeNiIgDDzwwunXrFuecc07ceeedcfnll7f5eppiwYIFsWjRojjuuONi2LBhH7pd9+7d4wtf+EJMmTIl3n777ejevXuj6//85z/HrFmz4itf+UqUlZVFRBRn8VFWrFgRHTt23LA7sZFss802xfvwmc98Jvbff//o379//PSnP41TTz018+oANl+OlADtWmVlZZSXlxefFK+xaNGiOP/88+PjH/94lJeXx/bbbx+XX355rFq1KiIiampqYs8994wddtghFi9eXLzdm2++Gb169YqhQ4dGfX19s9ez5gntK6+88pHbPfHEEzFs2LCorq6Ojh07xn777RfTpk0rXn/nnXfGSSedFBERBx98cPGUovWdGrW+/V555ZXRt2/fiIgYO3ZsFAqF6N+//4fu75xzzonVq1ev80jB+PHjIyLi7LPPjoh1n6p25ZVXRqFQiDlz5sSJJ54YW221VXziE5+IiIjf//73ccopp0T//v2jqqoq+vfvHyNHjmw0u5bM4Sc/+Unsvvvu0blz56iuro5ddtklvvGNb3zk3D5Mv379omfPnvGPf/yj0ZoKhcJaR27WnNL32GOPFS8bOnRoDBw4MGbPnh2f/exno2PHjrH99tvH1VdfHQ0NDcXtGhoa4rvf/W7svPPOUVVVFd26dYtBgwbFjTfe2KJ1A2xqRAnQrtTX10ddXV3U1tbG66+/HmPGjInly5c3+i12TU1NHHzwwXHXXXfFJZdcEtOmTYvTTz89rr322jj++OMj4r2Y+cUvfhELFy4sPqluaGiI0047LVJKMXHixCgpKWn2+v76179GRETPnj0/dJuZM2fGIYccEosXL47bb789Jk6cGNXV1XH00UfHpEmTIiLiyCOPjKuuuioiIn784x/HrFmz1ntqVFP2+6UvfSkmT54cEREXXnhhzJo1K+67774P3efnPve56Nev31qncNXX18d//Md/xL777huf+tSn1juX448/PnbYYYe4995745ZbbomI9yJm5513jhtuuCEefvjhuOaaa+KNN96IIUOGxFtvvdWkOdx5552NIuCee+6J888/Pw466KC47777YsqUKXHxxRfH8uXL17vGdVm8eHEsWrQodtpppxbdPuK90D3ttNPi9NNPj6lTp8YRRxwRX//612PChAnFba699tq48sorY+TIkTFt2rSYNGlSnHPOOfHuu++2+OsCbFISQDswfvz4FBFr/amoqEg333xzo21vueWWFBHpF7/4RaPLr7nmmhQRafr06cXLJk2alCIi3XDDDelb3/pW6tChQ6PrP8yjjz6aIiJNmjQp1dbWphUrVqTf/va3aYcddkglJSVp3rx5KaWU5s+fnyIijR8/vnjbfffdN2299dZp6dKlxcvq6urSwIEDU9++fVNDQ0NKKaV77703RUR69NFHmzSjpu53zZq+973vNWm/V1xxRYqINGfOnOJlDzzwQIqIdNtttxUvW9d9XXPbb33rW+v9OnV1dWnZsmWpU6dO6cYbbyxe3pw5XHDBBalbt25Nul8fFBHp/PPPT7W1tWn16tXpxRdfTMccc0yqrq5Ov//974vbrXkszp8/v9Ht1zwm3r/Ogw46KEVEeuqppxpt+6lPfSoddthhxc+POuqotMcee7Ro3QCbA0dKgHblrrvuitmzZ8fs2bPjoYceilGjRsXo0aPjpptuKm7zyCOPRKdOneLEE09sdNuzzjorIt5756k1RowYEeedd15ceuml8d3vfje+8Y1vxKGHHtrk9Zx88slRVlYWHTt2jAMPPDDq6+vjv/7rv2LQoEHr3H758uXx1FNPxYknnhidO3cuXl5SUhJnnHFGvP766/GXv/ylyV9/Y+83IuKLX/xidOjQodHRkvHjx0enTp3i5JNPbtI+TjjhhLUuW7ZsWYwdOzZ22GGHKC0tjdLS0ujcuXMsX7680TuYNcfee+8d7777bowcOTLuv//+4hGXprr55pujrKwsysvLY6eddoqHHnooJk6cGHvttVeL1hMR0atXr9h7770bXTZo0KBGp6ntvffeMW/evDj//PPj4YcfjiVLlrT46wFsikQJ0K588pOfjMGDB8fgwYPj8MMPj5/+9KcxfPjw+NrXvlY81eXtt9+OXr16RaFQaHTbrbfeOkpLS+Ptt99udPnZZ58dtbW1UVpaGhdddFGz1nPNNdfE7NmzY86cOfHqq6/G3/72tzj22GM/dPt33nknUkrRu3fvta7r06dPcf3NtbH2G/He6yqGDRsWd999d6xatSreeuutePDBB+Okk06K6urqJu1jXes69dRT46abboovfelL8fDDD8fTTz8ds2fPjp49e8bKlStbtNYzzjgj7rjjjnjllVfihBNOiK233jr22WefmDFjRpNuP2LEiJg9e3Y8+eST8dOf/jSqq6vjlFNOiZdeeqlF64mItd4gICKioqKi0X38+te/Ht///vfjd7/7XRxxxBHRvXv3GDZsWPz+979v8dcF2JSIEqDdGzRoUKxcuTJefPHFiHjvSeA//vGPSCk12m7hwoVRV1cXPXr0KF62fPnyOOOMM2KnnXaKqqqq+NKXvtSsr7399tvH4MGDY88994xtt912vdtvtdVW0aFDh3jjjTfWum7BggUREY3W11Qba79rnHPOObFo0aK4//77Y8KECbF69eo455xzmnz7Dwbi4sWL48EHH4yvfe1rcdlll8WwYcNiyJAhsdtuu8WiRYtavM6I947sPPnkk7F48eKYNm1apJTiqKOOWu+bD0S891qgwYMHx2c+85n453/+55gyZUosX748Lr744uI2lZWVERHFN01Yo7lHZd6vtLQ0LrnkkpgzZ04sWrQoJk6cGK+99locdthhsWLFihbvF2BTIUqAdm/u3LkR8X8vLh82bFgsW7ZsrX8Q8K677ipev8a5554br776akyePDluv/32mDp1alx//fUbba2dOnWKffbZJyZPntzoN+UNDQ0xYcKE6Nu3b/FF1RUVFRERTTpq0Jz9tsSxxx4b3bt3jzvuuCPGjx8fO+20UxxwwAEt3l+hUIiUUvE+rvGzn/1srXc9a84c3q9Tp05xxBFHxOWXXx6rV6+OP/7xj81e52c/+9k488wzY9q0aTFr1qyIiOK7lT333HONtp06dWqz978u3bp1ixNPPDFGjx4dixYtapN/nwVgY/PvlADtyvPPPx91dXUR8d7pSJMnT44ZM2bEcccdFwMGDIiIiDPPPDN+/OMfx6hRo+Lll1+O3XbbLZ544om46qqr4vOf/3x87nOfi4j3ngBPmDAhxo8fH7vuumvsuuuuccEFF8TYsWNj//33X+t1AK1l3Lhxceihh8bBBx8cX/3qV6O8vDxuvvnmeP7552PixInFowoDBw6MiIhbb701qquro7KyMgYMGLDO04Gas9+WqKioiNNOOy1+9KMfRUoprr766hbvKyKiS5cuceCBB8b3vve96NGjR/Tv3z9mzpwZt99+e3Tr1q3Rts2Zwz/90z9FVVVV7L///tG7d+948803Y9y4cdG1a9cYMmRIi9b6ne98JyZNmhTf/OY349e//nUMGTIkdt555/jqV78adXV1sdVWW8V9990XTzzxRIv2HxFx9NFHF/8Nnp49e8Yrr7wSN9xwQ/Tr1y923HHHFu8XYJOR81X2AK1lXe++1bVr17THHnuk6667LtXU1DTa/u23307nnntu6t27dyotLU39+vVLX//614vbPffcc6mqqiqNGjWq0e1qamrSXnvtlfr375/eeeedD13Pmndauvfeez9y3et6R6qUUnr88cfTIYcckjp16pSqqqrSvvvumx544IG1bn/DDTekAQMGpJKSknXu54Oast/mvvvWGvPmzUsRkUpKStKCBQuadF/XvPvW//7v/661/euvv55OOOGEtNVWW6Xq6up0+OGHp+effz7169dvre9LU+fw85//PB188MFpm222SeXl5alPnz5pxIgR6bnnnlvv/YuINHr06HVed+mll6aISDNnzkwppfTiiy+m4cOHpy5duqSePXumCy+8ME2bNm2d77616667rrW/UaNGpX79+hU//8EPfpD222+/1KNHj1ReXp622267dM4556SXX355vesG2BwUUvrASdUAAABtyGtKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFm1+B9PbGhoiAULFkR1dfUG/YNbAADA5i2lFEuXLo0+ffpEhw7NP+7R4ihZsGBBbLvtti29OQAA0M689tpr0bdv32bfrsVRUl1dXfzCXbp0aeluWkVtbW1Mnz49hg8fHmVlZVnXsiUw77Zj1m3LvNuOWbct8247Zt22zLvtrG/WS5YsiW233bbYCM3V4ihZc8pWly5dNoko6dixY3Tp0sUDsg2Yd9sx67Zl3m3HrNuWebcds25b5t12mjrrlr6swwvdAQCArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEpzL2BLlVKKmpqa3Mtokbq6uoiIqKmpKX7cnqSUYtWqVRERUVFREYVCIdta2vusNzXm3XbeP+vS0tKs/58BkJ8oyaSmpiaOOOKI3MtokfLy8hg9enSccMIJsXr16tzLadfMum2Zd9t5/6zvv//+qKqqyr0kADJy+hYAAJCVIyWbgGV7jIzUYfP5VpSXvHeaxdLdT4nV9SnzajaC+tqonndPRLx3H6OkLNtS2v2sNzHm3XYqCvW5lwDAJmTzeSbcjqUOpVmf+DZbyZr/bgEPn5KyvN+bLWnWmwLzbjMpvIYEgP/j9C0AACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADIqjT3AjZUSilWrlwZtbW1kVLKvRwAANjoUkpRU1MTERGVlZVRKBQyr2jDbPZRUlNTE8ccc0xERAwfPjzKy8szrwgAADaumpqaOOKIIyIi4qGHHoqqqqrMK9owTt8CAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMiqNPcCNlRKqfhxTU1NlJWVZVxN09XU1PzfJ++7DwBbhJSitrY2UkqN/z5ko6itrY3a2tpYuXJl1NXV5V5Ou2bWbWtLnvf7/+5M7eC5ZJOjZNWqVbFq1ari50uWLImI/3sw5LJs2bLixyNGjMi2jg1RXqiPKMm9iqYrL2n83/asvCSyfm+2pFlvCsy77ZTX18dNN90UERHHHXdc5tVsOdbMnI3PrNvWlj7vZcuWbfRfzK95vv9hz/s3tAeaHCXjxo2Lb3/722tdPn369OjYseMGLWJDrFixItvXbi1f2a/7ZnOE5/0u2btr7iVsFLW1tXHT7Pc+/so+XTeJ7017nfWmyrw3vtrajsX/zwDYML/5zW/a7Pn4jBkz1nn5hj4nL6QmHu9Z15GSbbfdNt56663o0qXLBi1iQ6xYsSK+8IUvRETE3XffHZ07d862luZYtWpVnHrqqRERsWz3UyJK8z/xbarykveetF339OJYXZ97NRtBfW1UzP6PiIhYNeSMiJJ835t2P+tNjHm3nfJUFxcO6RJ33HFH/PznP4+KiorcS2rX6urq4pFHHolDDjkkSks3+zO3N2lm3ba25HnX1NQUzxK6//77N3qU1NbWxowZM+LQQw9d5y9slyxZEj169IjFixe3qA2a/N2rqKhY5w+NsrKyrL9JLi8vL37cuXPnrIHUHCtXriwe5lrdEBGb4ROg1fXRPp+41UeseaRvKvev3c56E2XebaOsrCzq6uqic+fOUVVVlXs57VptbW2UlZVFdXX1JnH0tz0z67a1Jc/7/fe3vLy8ze7/hz3339Cv7923AACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQVWnuBWyoysrKmDp1akyfPj0qKytzLwcAADa6ysrKeOihh4ofb+42+ygpFApRVVUVZWVlUSgUci8HAAA2ujXPgdsLp28BAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAshIlAABAVqIEAADIqjT3AogoNNRFyr2IZim895/6uoj6zWvlTVJfu+6Ps2jns97kmHdbKRTqcy8BgE2IKNkEdJ47MfcSmqW8vDzigNFRPe+eWL16de7lbFTV8+7J+vW3pFlvCsy77ZSXl0ccODr3MgDYRDh9CwAAyMqRkkwqKyvjoYceyr2MFqmrq4tHHnkkfvnLX0Zpaft7CKWUYtWqVRERUVFREYVCIdta2vusNzXm3XbeP+vKysrcywEgMz91MykUClFVVZV7GS1SW/ve6ywqKyujrKws82o2jo4dO+ZeQkRsGbPelJh323n/rHOGPwCbBqdvAQAAWYkSAAAgK1ECAABkJUoAAICsRAkAAJCVKAEAALISJQAAQFaiBAAAyEqUAAAAWYkSAAAgK1ECAABkJUoAAICsRAkAAJCVKAEAALISJQAAQFaiBAAAyEqUAAAAWYkSAAAgK1ECAABkJUoAAICsRAkAAJCVKAEAALISJQAAQFaiBAAAyEqUAAAAWYkSAAAgK1ECAABkJUoAAICsRAkAAJCVKAEAALISJQAAQFaiBAAAyEqUAAAAWYkSAAAgK1ECAABkJUoAAICsRAkAAJCVKAEAALISJQAAQFaiBAAAyEqUAAAAWYkSAAAgq9KW3jClFBERS5YsabXFtFRtbW2sWLEilixZEmVlZbmX0+6Zd9sx67Zl3m3HrNuWebcds25b5t121jfrNU2wphGaq8VRsnTp0oiI2HbbbVu6CwAAoB1ZunRpdO3atdm3K6QW5kxDQ0MsWLAgqquro1AotGQXrWbJkiWx7bbbxmuvvRZdunTJupYtgXm3HbNuW+bddsy6bZl32zHrtmXebWd9s04pxdKlS6NPnz7RoUPzXyHS4iMlHTp0iL59+7b05htFly5dPCDbkHm3HbNuW+bddsy6bZl32zHrtmXebeejZt2SIyRreKE7AACQlSgBAACyahdRUlFREVdccUVUVFTkXsoWwbzbjlm3LfNuO2bdtsy77Zh12zLvtrOxZ93iF7oDAAC0hnZxpAQAANh8iRIAACArUQIAAGQlSgAAgKzaRZTcfPPNMWDAgKisrIy99torHn/88dxL2uyNGzcuhgwZEtXV1bH11lvHscceG3/5y18abZNSiiuvvDL69OkTVVVVMXTo0PjjH/+YacXtx7hx46JQKMSYMWOKl5l16/r73/8ep59+enTv3j06duwYe+yxRzzzzDPF6827ddTV1cW//uu/xoABA6Kqqiq23377+Ld/+7doaGgobmPWLffb3/42jj766OjTp08UCoWYMmVKo+ubMttVq1bFhRdeGD169IhOnTrFMcccE6+//nob3ovNw0fNura2NsaOHRu77bZbdOrUKfr06RNnnnlmLFiwoNE+zLrp1vfYfr9/+Zd/iUKhEDfccEOjy827aZoy6z/96U9xzDHHRNeuXaO6ujr23XffePXVV4vXt9asN/somTRpUowZMyYuv/zyePbZZ+Ozn/1sHHHEEY2GRfPNnDkzRo8eHb/73e9ixowZUVdXF8OHD4/ly5cXt7n22mvjuuuui5tuuilmz54dvXr1ikMPPTSWLl2aceWbt9mzZ8ett94agwYNanS5Wbeed955J/bff/8oKyuLhx56KF544YX4wQ9+EN26dStuY96t45prrolbbrklbrrppvjTn/4U1157bXzve9+LH/3oR8VtzLrlli9fHrvvvnvcdNNN67y+KbMdM2ZM3HfffXHPPffEE088EcuWLYujjjoq6uvr2+pubBY+atYrVqyIOXPmxDe/+c2YM2dOTJ48OV588cU45phjGm1n1k23vsf2GlOmTImnnnoq+vTps9Z15t0065v1//zP/8QBBxwQu+yySzz22GMxb968+OY3vxmVlZXFbVpt1mkzt/fee6dzzz230WW77LJLuuyyyzKtqH1auHBhiog0c+bMlFJKDQ0NqVevXunqq68ublNTU5O6du2abrnlllzL3KwtXbo07bjjjmnGjBnpoIMOSl/+8pdTSmbd2saOHZsOOOCAD73evFvPkUcemc4+++xGlx1//PHp9NNPTymZdWuKiHTfffcVP2/KbN99991UVlaW7rnnnuI2f//731OHDh3Sr371qzZb++bmg7Nel6effjpFRHrllVdSSma9IT5s3q+//nr6+Mc/np5//vnUr1+/dP311xevM++WWdesTz755OLf2evSmrPerI+UrF69Op555pkYPnx4o8uHDx8eTz75ZKZVtU+LFy+OiIiPfexjERExf/78ePPNNxvNvqKiIg466CCzb6HRo0fHkUceGZ/73OcaXW7WrWvq1KkxePDgOOmkk2LrrbeOPffcM2677bbi9ebdeg444ID4zW9+Ey+++GJERMybNy+eeOKJ+PznPx8RZr0xNWW2zzzzTNTW1jbapk+fPjFw4EDz30CLFy+OQqFQPAJr1q2roaEhzjjjjLj00ktj1113Xet6824dDQ0NMW3atNhpp53isMMOi6233jr22WefRqd4teasN+soeeutt6K+vj622WabRpdvs8028eabb2ZaVfuTUopLLrkkDjjggBg4cGBERHG+Zt867rnnnpgzZ06MGzdurevMunX97W9/i5/85Cex4447xsMPPxznnntuXHTRRXHXXXdFhHm3prFjx8bIkSNjl112ibKysthzzz1jzJgxMXLkyIgw642pKbN98803o7y8PLbaaqsP3Ybmq6mpicsuuyxOPfXU6NKlS0SYdWu75pprorS0NC666KJ1Xm/erWPhwoWxbNmyuPrqq+Pwww+P6dOnx3HHHRfHH398zJw5MyJad9alrbbyjAqFQqPPU0prXUbLXXDBBfHcc8/FE088sdZ1Zr/hXnvttfjyl78c06dPb3SO5geZdetoaGiIwYMHx1VXXRUREXvuuWf88Y9/jJ/85Cdx5plnFrcz7w03adKkmDBhQtx9992x6667xty5c2PMmDHRp0+fGDVqVHE7s954WjJb82+52traOOWUU6KhoSFuvvnm9W5v1s33zDPPxI033hhz5sxp9uzMu3nWvCnJF77whbj44osjImKPPfaIJ598Mm655ZY46KCDPvS2LZn1Zn2kpEePHlFSUrJWiS1cuHCt3w7RMhdeeGFMnTo1Hn300ejbt2/x8l69ekVEmH0reOaZZ2LhwoWx1157RWlpaZSWlsbMmTPjhz/8YZSWlhbnadato3fv3vGpT32q0WWf/OQni2+O4bHdei699NK47LLL4pRTTonddtstzjjjjLj44ouLRwTNeuNpymx79eoVq1evjnfeeedDt6HpamtrY8SIETF//vyYMWNG8ShJhFm3pscffzwWLlwY2223XfFn5iuvvBJf+cpXon///hFh3q2lR48eUVpaut6fma016806SsrLy2OvvfaKGTNmNLp8xowZsd9++2VaVfuQUooLLrggJk+eHI888kgMGDCg0fUDBgyIXr16NZr96tWrY+bMmWbfTMOGDYs//OEPMXfu3OKfwYMHx2mnnRZz586N7bff3qxb0f7777/W21u/+OKL0a9fv4jw2G5NK1asiA4dGv+YKSkpKf72zaw3nqbMdq+99oqysrJG27zxxhvx/PPPm38zrQmSl156KX79619H9+7dG11v1q3njDPOiOeee67Rz8w+ffrEpZdeGg8//HBEmHdrKS8vjyFDhnzkz8xWnXWzXha/CbrnnntSWVlZuv3229MLL7yQxowZkzp16pRefvnl3EvbrJ133nmpa9eu6bHHHktvvPFG8c+KFSuK21x99dWpa9euafLkyekPf/hDGjlyZOrdu3dasmRJxpW3D+9/962UzLo1Pf3006m0tDT9+7//e3rppZfSf/7nf6aOHTumCRMmFLcx79YxatSo9PGPfzw9+OCDaf78+Wny5MmpR48e6Wtf+1pxG7NuuaVLl6Znn302Pfvssyki0nXXXZeeffbZ4js+NWW25557burbt2/69a9/nebMmZMOOeSQtPvuu6e6urpcd2uT9FGzrq2tTcccc0zq27dvmjt3bqOfmatWrSruw6ybbn2P7Q/64LtvpWTeTbW+WU+ePDmVlZWlW2+9Nb300kvpRz/6USopKUmPP/54cR+tNevNPkpSSunHP/5x6tevXyovL0+f/vSni29bS8tFxDr/jB8/vrhNQ0NDuuKKK1KvXr1SRUVFOvDAA9Mf/vCHfItuRz4YJWbduh544IE0cODAVFFRkXbZZZd06623NrrevFvHkiVL0pe//OW03XbbpcrKyrT99tunyy+/vNETNbNuuUcffXSdf0+PGjUqpdS02a5cuTJdcMEF6WMf+1iqqqpKRx11VHr11Vcz3JtN20fNev78+R/6M/PRRx8t7sOsm259j+0PWleUmHfTNGXWt99+e9phhx1SZWVl2n333dOUKVMa7aO1Zl1IKaXmHVsBAABoPZv1a0oAAIDNnygBAACyEiUAAEBWogQAAMhKlAAAAFmJEgAAICtRAgAAZCVKAACArEQJAACQlSgBIM4666woFApRKBSitLQ0tttuuzjvvPPinXfeyb00ALYAogSAiIg4/PDD44033oiXX345fvazn8UDDzwQ559/fu5lAbAFECUARERERUVF9OrVK/r27RvDhw+Pk08+OaZPnx4REUOHDo0xY8Y02v7YY4+Ns846q/h5//7946qrroqzzz47qqurY7vttotbb721eP3q1avjggsuiN69e0dlZWX0798/xo0b1xZ3DYBNnCgBYC1/+9vf4le/+lWUlZU163Y/+MEPYvDgwfHss8/G+eefH+edd178+c9/joiIH/7whzF16tT4xS9+EX/5y19iwoQJ0b9//42wegA2N6W5FwDApuHBBx+Mzp07R319fdTU1ERExHXXXdesfXz+858vnvI1duzYuP766+Oxxx6LXXbZJV599dXYcccd44ADDohCoRD9+vVr9fsAwObJkRIAIiLi4IMPjrlz58ZTTz0VF154YRx22GFx4YUXNmsfgwYNKn5cKBSiV69esXDhwoh478X0c+fOjZ133jkuuuii4qlhACBKAIiIiE6dOsUOO+wQgwYNih/+8IexatWq+Pa3vx0RER06dIiUUqPta2tr19rHB0/3KhQK0dDQEBERn/70p2P+/Pnxne98J1auXBkjRoyIE088cSPdGwA2J6IEgHW64oor4vvf/34sWLAgevbsGW+88Ubxuvr6+nj++eebvc8uXbrEySefHLfddltMmjQpfvnLX8aiRYtac9kAbIa8pgSAdRo6dGjsuuuucdVVV8UhhxwSl1xySUybNi0+8YlPxPXXXx/vvvtus/Z3/fXXR+/evWOPPfaIDh06xL333hu9evWKbt26bZT1A7D5ECUAfKhLLrkkvvjFL8Zf//rXmDdvXpx55plRWloaF198cRx88MHN2lfnzp3jmmuuiZdeeilKSkpiyJAh8d///d/RoYOD9gBbukL64EnCAAAAbcivpwAAgKxECQAAkJUoAQAAshIlAABAVqIEAADISpQAAABZiRIAACArUQIAAGQlSgAAgKxECQAAkJUoAQAAsvp/WWyM4DB3ZD8AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10, 6))\n",
    "sns.boxplot(x=df['Runs'])\n",
    "\n",
    "plt.title(\"Box Plot of Virat's Runs\")\n",
    "plt.xlabel(\"Runs\")\n",
    "plt.grid(True)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Q1 =  10.0\n",
      "Q3 = 80.25\n",
      "IQR =  70.25\n",
      "Upper Fence = 185.625\n"
     ]
    }
   ],
   "source": [
    "# Calculate the upper fence\n",
    "Q1 = df['Runs'].quantile(0.25)\n",
    "Q3 = df['Runs'].quantile(0.75)\n",
    "IQR = Q3 - Q1\n",
    "upper_fence = Q3 + 1.5 * IQR\n",
    "print(\"Q1 = \",Q1)\n",
    "print('Q3 =', Q3)\n",
    "print(\"IQR = \", IQR)\n",
    "print(\"Upper Fence =\",upper_fence)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q2.None of the options given is correct"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### False Statement\n",
    "\n",
    "Q3:Consider the following statements and choose the correct option\n",
    "\n",
    "     I - Virat has played the maximum number of matches in 2011\n",
    "     II - Virat has the highest run average in the year 2017\n",
    "     III - Virat has the maximum score in a single match and the highest run average in the year 2016.\n",
    "\n",
    "Which of the above statements is/are false?\n",
    "\n",
    "    a)I and II\n",
    "    b)I and III\n",
    "    c)II\n",
    "    d)III\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Lets us check for the statement I \"Virat has played the maximum number of matches in 2011\"\n",
    "df['Start Date'] = df['Start Date'].apply(lambda x: x[-2:])"
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
       "11    31\n",
       "13    23\n",
       "14    17\n",
       "10    16\n",
       "12    11\n",
       "15    10\n",
       "16    10\n",
       "09     6\n",
       "08     5\n",
       "17     3\n",
       "Name: Start Date, dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Start Date'].value_counts() \n",
    "# Statement I is correct "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
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
       "      <th>Start Date</th>\n",
       "      <th>08</th>\n",
       "      <th>09</th>\n",
       "      <th>10</th>\n",
       "      <th>11</th>\n",
       "      <th>12</th>\n",
       "      <th>13</th>\n",
       "      <th>14</th>\n",
       "      <th>15</th>\n",
       "      <th>16</th>\n",
       "      <th>17</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Runs</th>\n",
       "      <td>31.8</td>\n",
       "      <td>38.333333</td>\n",
       "      <td>45.375</td>\n",
       "      <td>42.0</td>\n",
       "      <td>40.363636</td>\n",
       "      <td>47.826087</td>\n",
       "      <td>58.529412</td>\n",
       "      <td>30.4</td>\n",
       "      <td>73.9</td>\n",
       "      <td>61.666667</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Start Date    08         09      10    11         12         13         14  \\\n",
       "Runs        31.8  38.333333  45.375  42.0  40.363636  47.826087  58.529412   \n",
       "\n",
       "Start Date    15    16         17  \n",
       "Runs        30.4  73.9  61.666667  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Lets us see \"Virat has the highest run average in the year 2017\"\n",
    "pd.pivot_table(df, values = 'Runs', columns = ['Start Date'], aggfunc=np.mean)\n",
    "\n",
    "# Statement II is incorrect "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
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
       "      <th>Start Date</th>\n",
       "      <th>08</th>\n",
       "      <th>09</th>\n",
       "      <th>10</th>\n",
       "      <th>11</th>\n",
       "      <th>12</th>\n",
       "      <th>13</th>\n",
       "      <th>14</th>\n",
       "      <th>15</th>\n",
       "      <th>16</th>\n",
       "      <th>17</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Runs</th>\n",
       "      <td>54</td>\n",
       "      <td>107</td>\n",
       "      <td>118</td>\n",
       "      <td>117</td>\n",
       "      <td>128</td>\n",
       "      <td>115</td>\n",
       "      <td>139</td>\n",
       "      <td>138</td>\n",
       "      <td>154</td>\n",
       "      <td>122</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Start Date  08   09   10   11   12   13   14   15   16   17\n",
       "Runs        54  107  118  117  128  115  139  138  154  122"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Virat has the maximum score in a single match and the highest run average in the year 2016.\n",
    "pd.pivot_table(df, values = 'Runs', columns = ['Start Date'], aggfunc=np.max)\n",
    "# Statement III is correct "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hence answer for Q3 is option (c) or option (a) which is partially correct"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Maximum Frequency\n",
    "\n",
    "Q4:Plot a histogram for the Mins column with 15 bins. Among the three ranges mentioned below, which one has the highest frequency?\n",
    "\n",
    "A - [54.6,68)\n",
    "\n",
    "B - [68,81.4)\n",
    "\n",
    "C - [121.6,135)\n",
    "\n",
    "    a)A - [54.6,68)\n",
    "    b)B - [68,81.4)\n",
    "    c)C - [121.6,135)\n",
    "    d)None of the bin ranges have the same frequency\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Change the data type for Mins column \n",
    "\n",
    "df2 = df[-(df['Mins'] == '-')]\n",
    "df2['Mins']= df2['Mins'].apply(lambda x:int(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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+OCDD3Kdximd7vzefffdeOWVV+J73/tevPLKK/HEE0/Ef//3f8ctt9wyYN+FCxeWzekPf/jDHMMflDPNYcSZn5PVOocRUXZe+/fvjx//+MdRKBTitttuK9tvNM7hYN4PRv1rMI1hf/mXf5nuuuuusnWf/vSn0/Lly0doRJVz4MCBFBFp48aNpXXz589Pn//850duUB/Bvffem2bOnHnSbcePH08NDQ3p/vvvL637wx/+kGpra9O//uu/ZhphZX3rW99KF110UTp+/HhKqbrnLiLSk08+WXo8mPk6dOhQGjduXFq3bl1pn//5n/9Jn/jEJ9Kzzz6bbeyD8eHzO5mf//znKSLSG2+8UVp37bXXpm9961vDO7gKOdk5nuk5Odbm8POf/3yaO3du2bpqmcMPvx9Uw2twzF75OHr0aGzbti3a2trK1re1tcXmzZtHaFSV09vbGxERkydPLlu/YcOGqKuri4svvjgWLlwYBw4cGInhnZXdu3dHU1NTtLa2xh133BGvv/56RER0d3dHT09P2VwWi8W49tprq3Iujx49Gj/5yU/iq1/9atnNE6t57v7UYOZr27ZtcezYsbJ9mpqaYvr06VU5p729vVEoFAbcl+rRRx+NKVOmxCWXXBJ333131VypO+F0z8mxNIe///3vY/369fG1r31twLZqmMMPvx9Uw2tw2O5qO9Leeuut+OCDDwbczK6+vn7ATe+qTUopli1bFldffXVMnz69tL69vT2++MUvRktLS3R3d8f3vve9mDt3bmzbtm3U/XW7D7viiivikUceiYsvvjh+//vfxz/90z/F7NmzY+fOnaX5OtlcvvHGGyMx3I/kqaeeikOHDsWCBQtK66p57j5sMPPV09MT48ePjz//8z8fsE+1vT7/8Ic/xPLly+POO+8su3HXl7/85WhtbY2Ghob49a9/HStWrIhf/vKXA+57NVqd6Tk5luZw7dq1UVNTE/PmzStbXw1zeLL3g2p4DY7Z+DjhT//PMuKPE/XhddVm8eLF8atf/SpefvnlsvW333576d/Tp0+Pyy67LFpaWmL9+vUDXlSjTXt7e+nfM2bMiKuuuiouuuiiWLt2belDbmNlLh9++OFob28vu+10Nc/dqZzNfFXbnB47dizuuOOOOH78eDz00ENl2xYuXFj69/Tp02PatGlx2WWXxSuvvBKXXnpp7qEO2dk+J6ttDiMifvzjH8eXv/zlOO+888rWV8Mcnur9IGJ0vwbH7I9dpkyZEuecc86Agjtw4MCAGqwmS5YsiaeffjpefPHFmDp16mn3bWxsjJaWlti9e3em0VXOxIkTY8aMGbF79+7Sb72Mhbl844034vnnn4+vf/3rp92vmuduMPPV0NAQR48ejbfffvuU+4x2x44di7/5m7+J7u7u6OrqOuPtyi+99NIYN25cVc5pxMDn5FiYw4iIl156KXbt2nXG12TE6JvDU70fVMNrcMzGx/jx42PWrFkDLo91dXXF7NmzR2hUZy+lFIsXL44nnngiXnjhhWhtbT3j1xw8eDD27dsXjY2NGUZYWf39/fHb3/42GhsbS5c9/3Qujx49Ghs3bqy6uVyzZk3U1dXFjTfeeNr9qnnuBjNfs2bNinHjxpXts3///vj1r39dFXN6Ijx2794dzz//fHzyk58849fs3Lkzjh07VpVzGjHwOVntc3jCww8/HLNmzYqZM2eecd/RModnej+oitfgsH+kdQStW7cujRs3Lj388MPpN7/5TVq6dGmaOHFi2rNnz0gPbcj+7u/+LtXW1qYNGzak/fv3l5Z33303pZTS4cOH07e//e20efPm1N3dnV588cV01VVXpb/4i79IfX19Izz6M/v2t7+dNmzYkF5//fW0ZcuWdNNNN6WamprSXN1///2ptrY2PfHEE2nHjh3pS1/6UmpsbKyKczvhgw8+SBdccEH67ne/W7a+Gufu8OHDafv27Wn79u0pItLKlSvT9u3bS7/tMZj5uuuuu9LUqVPT888/n1555ZU0d+7cNHPmzPT++++P1GmVnO78jh07lm655ZY0derU9Oqrr5a9Hvv7+1NKKb322mvp+9//ftq6dWvq7u5O69evT5/+9KfTZz/72VFxfimd/hwH+5ys1jk8obe3N51//vlp9erVA75+NM/hmd4PUhr9r8ExHR8ppfQv//IvqaWlJY0fPz5deumlZb+aWk0i4qTLmjVrUkopvfvuu6mtrS196lOfSuPGjUsXXHBBmj9/ftq7d+/IDnyQbr/99tTY2JjGjRuXmpqa0rx589LOnTtL248fP57uvffe1NDQkIrFYrrmmmvSjh07RnDEQ/fcc8+liEi7du0qW1+Nc/fiiy+e9Pk4f/78lNLg5uu9995LixcvTpMnT04TJkxIN91006g559OdX3d39ylfjy+++GJKKaW9e/ema665Jk2ePDmNHz8+XXTRRenv//7v08GDB0f2xP7E6c5xsM/Jap3DE374wx+mCRMmpEOHDg34+tE8h2d6P0hp9L8GC//vRAAAshizn/kAAEYn8QEAZCU+AICsxAcAkJX4AACyEh8AQFbiAwDISnwAAFmJDwAgK/EBAGQlPgCArMQHAJDV/wGShrSpRS38BAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(df2.Mins, bins = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Option (d) is the correct answer"
   ]
  },
  {
   "attachments": {
    "c1343684-8a99-4adf-b78b-5bb3b048d0df.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Coding Question : \n",
    "\n",
    "1) Given a positive integer 'n' less than or equal to 26, you are required to print the below pattern \n",
    "\n",
    "Sample Input: 5 \r\n",
    " \r\n",
    "Sample Output \n",
    ":![image.png](attachment:c1343684-8a99-4adf-b78b-5bb3b048d0df.png)-e-------- \r\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------e--------\n",
      "------e-d-e------\n",
      "----e-d-c-d-e----\n",
      "--e-d-c-b-c-d-e--\n",
      "e-d-c-b-a-b-c-d-e\n",
      "--e-d-c-b-c-d-e--\n",
      "----e-d-c-d-e----\n",
      "------e-d-e------\n",
      "--------e--------\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "alpha=\"abcdefghijklmnopqrstuvwxyz\"\n",
    "s=\"\"\n",
    "l=[]\n",
    "for i in range(n):\n",
    "    s=\"-\".join(alpha[i:n])\n",
    "    l.append(s[::-1]+s[1:])\n",
    "length=len(l[0])\n",
    "for i in range(n-1,0,-1):\n",
    "    print(l[i].center(length,\"-\"))\n",
    "for i in range(n):\n",
    "    print(l[i].center(length,\"-\"))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2) Given an integer, print whether it is Even or Odd.\n",
    "\n",
    "----------------------------------------------------------------------\n",
    "Input:\n",
    "An integer\n",
    "\n",
    "Output:\n",
    "'Even' or 'Odd'\n",
    "\n",
    "----------------------------------------------------------------------\n",
    "Sample input:\n",
    "3\n",
    "\n",
    "Sample output:\n",
    "Odd\n",
    "\n",
    "----------------------------------------------------------------------\n",
    "Sample input:\n",
    "6\n",
    "\n",
    "Sample output:\n",
    "Even\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Even\n"
     ]
    }
   ],
   "source": [
    "num=int(input())\n",
    "if num%2==0:\n",
    "    print(\"Even\")\n",
    "else:\n",
    "    print(\"Odd\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3) You're trying to automate your alarm clock by writing a function for it. You're given a day of the week encoded as 1=Mon, 2=Tue, ... 6=Sat, 7=Sun, and whether you are on vacation as a boolean value (a boolean object is either True or False. Google \"booleans python\" to get a better understanding). Based on the day and whether you're on vacation, write a function that returns a time in form of a string indicating when the alarm clock should ring. \n",
    "\n",
    "When not on a vacation, on weekdays, the alarm should ring at \"7:00\" and on the weekends (Saturday and Sunday) it should ring at \"10:00\". \n",
    "\n",
    "While on a vacation, it should ring at \"10:00\" on weekdays. On vacation, it should not ring on weekends, that is, it should return \"off\".\n",
    "\n",
    "----------------------------------------------------------------------\r\n",
    "Input:\r\n",
    "The input will be a list of two elements. The first element will be an integer from 1 to 7, and the second element will be a boolean value.\r\n",
    "\r\n",
    "Output:\r\n",
    "The output will be a string denoting the time alarm will ring or 'off'\r\n",
    "\r\n",
    "----------------------------------------------------------------------\r\n",
    "Sample input:\r\n",
    "[7, True]\r\n",
    "\r\n",
    "Sample output:\r\n",
    "off\r\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a list of two elements [day_of_the_week, is_on_vacation]:  6,True\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Off\n"
     ]
    }
   ],
   "source": [
    "def alarm_time(day_of_the_week, is_on_vacation):\n",
    "    weekend = {6, 7}  \n",
    "    if is_on_vacation:\n",
    "        if day_of_the_week in weekend:\n",
    "            return 'Off'\n",
    "        else:\n",
    "            return '10:00'\n",
    "    else:\n",
    "        if day_of_the_week in weekend:\n",
    "            return '10:00'\n",
    "        else:\n",
    "            return '07:00'\n",
    "input_str = input(\"Enter a list of two elements [day_of_the_week, is_on_vacation]: \")\n",
    "input_list = eval(input_str)  \n",
    "if len(input_list) != 2 or not isinstance(input_list[0], int) or not isinstance(input_list[1], bool):\n",
    "    print(\"Invalid input. Please provide a list with an integer from 1 to 7 and a boolean value.\")\n",
    "else:\n",
    "    print(alarm_time(input_list[0], input_list[1]))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4) Any number, say n is called an Armstrong number if it is equal to the sum of its digits, where each is raised to the power of number of digits in n.\r\n",
    "For example:\r\n",
    "153=13+53+33\r\n",
    "\r\n",
    "Write Python code to determine whether an entered three digit number is an Armstrong number or not. \r\n",
    "Assume that the number entered will strictly be a three digit number.\r\n",
    "Print \"True\" if it is an Armstrong number and print \"False\" if it is not.\r\n",
    "Sample Input:\r\n",
    "153\r\n",
    "Sample Output:\r\n",
    "True\r\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "sum = 0\n",
    "temp = n\n",
    "while temp > 0:\n",
    "   digit = temp % 10\n",
    "   sum += digit ** 3\n",
    "   temp //= 10\n",
    "if n == sum:\n",
    "   print(\"True\")\n",
    "else:\n",
    "   print(\"False\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5) A pascal's triangle is a very interesting mathematical concept.\n",
    "Each number here is a sum of the two numbers directly above it. Following is an 8 level Pascal's triangle:\n",
    " \n",
    "\n",
    "\n",
    "You can read about Pascal's triangle here.\n",
    "Your task is to print an nth level of Pascal's triangle.\n",
    "The input will contain an integer n.\n",
    "The output will contain 1 line of the list of numbers representing the nth row of Pascal's triangle.\n",
    "\n",
    "Sample Input:\n",
    "6\n",
    "Sample Output:\n",
    "\n",
    "[1, 5, 10, 10, 5, 1]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 6, 4, 1]\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "def generate_pascals_triangle_row(n):\n",
    "    row = [1]\n",
    "    for k in range(1, n):\n",
    "        row.append(row[-1] * (n - k) // k)\n",
    "    return row\n",
    "print(generate_pascals_triangle_row(n))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6) Given two strings, one of the strings will contain an extra character. Find the extra character. The number of all the other characters in both the strings will be the same. Check the sample input/output for more clarification.\n",
    "\n",
    "The code will be case sensitive.\n",
    "\n",
    "----------------------------------------------------------------------\n",
    "Input:\n",
    "Two strings on two separate lines. \n",
    "\n",
    "Output:\n",
    "One Character which is extra in one of the strings\n",
    "\n",
    "----------------------------------------------------------------------\n",
    "Sample input:\n",
    "abcd\n",
    "cedab\n",
    "\n",
    "Sample output:\n",
    "e\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " abcd \n",
      " cedab\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "e\n"
     ]
    }
   ],
   "source": [
    "string1 = input().strip()\n",
    "string2 = input().strip()\n",
    "\n",
    "\n",
    "#write code to find the extra character here\n",
    "from collections import Counter\n",
    "\n",
    "# Count occurrences of each character in both strings\n",
    "count1 = Counter(string1)\n",
    "count2 = Counter(string2)\n",
    "\n",
    "# Find the extra character\n",
    "extra_char = (count2 - count1) or (count1 - count2)\n",
    "\n",
    "# Print the extra character\n",
    "if extra_char:\n",
    "    print(extra_char.popitem()[0])\n",
    "else:\n",
    "    print(\"No extra character found.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6) While extracting data from different sources, often numeric values come in string format and with commas like 1,000 or 23,321 and also sometimes with spaces in start and beginning of the string. For simplicity, we will consider only integer values imbedded with commas. You will take the input and print the cleaned integer without commas and spaces.\n",
    "\n",
    "----------------------------------------------------------------------\n",
    "Input:\n",
    "One line input of string, it will consist of only spaces commas and digits\n",
    "\n",
    "Output:\n",
    "Cleaned number\n",
    "\n",
    "----------------------------------------------------------------------\n",
    "Sample input:\n",
    "         3,213\n",
    "\n",
    "Sample output:\n",
    "3213\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3,213\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3213\n"
     ]
    }
   ],
   "source": [
    "value=input().strip()\n",
    "cleaned_number = value.replace(',', '').replace(' ', '')\n",
    "print(cleaned_number)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7) Write a program that computes the value of n+nn+nnn+nnnn+... nn...n ntimes with a given number as the value of n.\n",
    "\n",
    "For example, if n=3 , then you have to find the value of 3+33+333\n",
    "if n=10, then you have to find the value of 10 + 1010 + 101010 + 10101010 + 1010101010 + 101010101010 + 10101010101010 + 1010101010101010 +101010101010101010+ 10101010101010101010\n",
    "\n",
    "\n",
    "Note: n will always be a positive number\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "369\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "current_term = str(n)\n",
    "total_sum = 0\n",
    "for i in range(1, n + 1):\n",
    "    # Add the current term to the total sum\n",
    "    total_sum += int(current_term)\n",
    "    current_term += str(n)\n",
    "print(total_sum)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
 "nbformat_minor": 4
}
