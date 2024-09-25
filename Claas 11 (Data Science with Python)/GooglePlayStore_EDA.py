{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4cd53474-cfa4-411d-a6c8-184f9fa4d008",
   "metadata": {},
   "source": [
    "**Problem Statement**\n",
    "\n",
    "The team at Google Play Store wants to develop a feature that would enable them to boost visibility for the most promising apps. Now, this analysis would require a preliminary understanding of the features that define a well-performing app. You can ask questions like:\n",
    "- Does a higher size or price necessarily mean that an app would perform better than the other apps? \n",
    "- Or does a higher number of installs give a clear picture of which app would have a better rating than others?\n",
    "\n",
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
   "execution_count": null,
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
   "execution_count": null,
   "id": "157b501f-b0f5-4aa9-89c9-f8620f2f3a6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Reading the csv file\n",
    "data = pd.read_csv(\"googleplaystore_v2.csv\")\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d39d9d56-16ae-410e-b598-61ef7ff6fd34",
   "metadata": {},
   "outputs": [],
   "source": [
    "# data inspection \n",
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4db9c574-1adc-4b78-bd11-02071c727a78",
   "metadata": {},
   "outputs": [],
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
    "\n",
    "The first few steps involve making sure that there are no __missing values__ or __incorrect data types__ before we proceed to the analysis stage. These aforementioned problems are handled as follows:\n",
    "\n",
    " - For Missing Values: Some common techniques to treat this issue are\n",
    "    - Dropping the rows containing the missing values\n",
    "    - Imputing the missing values\n",
    "    - Keep the missing values if they don't affect the analysis\n",
    " \n",
    "    \n",
    " - Incorrect Data Types:\n",
    "    - Clean certain values \n",
    "    - Clean and convert an entire column\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88b58387-abc0-4d7c-9cd5-c5dbbb840f8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f63952d3-eddb-48d1-ba8d-a9d41150bdf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Since Rating column has lot of missing values i will delete those rows \n",
    "data = data[-data.Rating.isnull()]\n",
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "efb77a48-740a-4820-9fbb-a6de9014abce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fetching the 3 null rows in the \"Android Ver\" column\n",
    "data[data['Android Ver'].isnull()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5442497c-b7ff-4e93-a106-8646b3401f20",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 10472 row is having shifted values so will drop this row \n",
    "data.loc[10472,:]\n",
    "data[(data['Android Ver'].isnull() & (data.Category == '1.9'))]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec17c133-a5a0-40b4-b542-85f23f88f12d",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = data[-(data['Android Ver'].isnull() & (data.Category == '1.9'))]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d8f3cee-5853-4e2b-82bb-f3af186460c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Cross checking if its dropped \n",
    "data[data['Android Ver'].isnull()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a8e9ebb-6be8-4ce9-af25-0ae3a9458529",
   "metadata": {},
   "outputs": [],
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
   "execution_count": null,
   "id": "56a3ee18-9023-4c11-8322-aa111d127299",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"Android Ver\"] = data[\"Android Ver\"].fillna(data[\"Android Ver\"].mode()[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dfc4aa44-abe8-4b49-ab48-863b1655ad07",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de5651b6-de87-4b70-88e3-58b523bc5636",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data[\"Current Ver\"].isnull()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62a288b3-7426-4e3f-96d2-c5cb1f376186",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"Current Ver\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe82d428-1418-48a1-860e-c1b2c63a1233",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"Current Ver\"] = data[\"Current Ver\"].fillna(data[\"Current Ver\"].mode()[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9c67207-2045-494b-a073-bf65a68954e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8fe5be88-5a26-4057-96d2-84e7beef0f5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Handling incorrect data types\n",
    "data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f77a2ddf-6aae-419e-8487-fe1f834f24c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.Price.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec319d47-fd76-477f-9daa-95b68b014500",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.Price = data.Price.apply(lambda x: 0 if x == '0' else float(x[1:]))\n",
    "data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a82526b-56f0-4eda-94fa-5d0ac5aaa21b",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.Reviews.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3792eb93-a42e-4575-ae03-cab5dd6723f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.Reviews = data.Reviews.astype(\"int32\")\n",
    "data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bd9e4db-cc17-498a-b331-7c1891bec1f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.Reviews.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a1061ed-7846-4d8b-aa4d-d9bd700181e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3784b79e-c52f-46d3-8bbb-e2c94ff401df",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.Installs.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "execution_count": null,
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
   "execution_count": null,
   "id": "de3481e0-0576-421e-bae3-47fb9e771f82",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.Installs.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "abcf9509-55b4-4c6c-9baf-9705cf7a71c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d36a1c5c-3fe8-477d-87ff-b2ab92546c39",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57a3961a-37d4-433e-9908-200316f454fd",
   "metadata": {},
   "outputs": [],
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
   "execution_count": null,
   "id": "fcc50057-2a91-44df-b241-8d4fdb4f9268",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[(data.Type == \"Free\") & (data.Price > 0)].shape\n",
    "\n",
    "# Here its showing 0 which means data points are sitting correctly "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "115c34b1-45e6-41e0-8135-54d3ac84404c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Reviews > data.Installs].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5d21005-3610-4180-afe7-2d5c86277bc5",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.Rating.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ade531e-387f-448f-9c09-06fcf2f804ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data[\"Reviews\"] > data[\"Installs\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4a885d1-26a1-4f88-a634-5e995c6abfb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "condition = data[\"Reviews\"] > data[\"Installs\"]\n",
    "data = data.drop(data[condition].index)\n",
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cad0670-d26f-490f-9eb0-66e0779f5728",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data[\"Reviews\"] > data[\"Installs\"]].shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17c98a35-c024-4838-a8de-78d30a430127",
   "metadata": {},
   "source": [
    "# Data Visulizations \n",
    "### Univariate analysis\n",
    "\n",
    "Now you need to start identifying and removing extreme values or __outliers__ from our dataset. These values can tilt our analysis and often provide us with a biased perspective of the data available. This is where you’ll start utilising visualisation to achieve your tasks. And the best visualisation to use here would be the box plot. Boxplots are one of the best ways of analysing the spread of a numeric variable\n",
    "\n",
    "\n",
    "Using a box plot you can identify the outliers as follows:\n",
    "![BoxPlots to Identify Outliers](images/Boxplot.png)\n",
    "- Outliers in data can arise due to genuine reasons or because of dubious entries. In the latter case, you should go ahead and remove such entries immediately. Use a boxplot to observe, analyse and remove them.\n",
    "- In the former case, you should determine whether or not removing them would add value to your analysis procedure.\n",
    "- - You can create a box plot directly from pandas dataframe or the matplotlib way as you learnt in the previous session. Check out their official documentation here:\n",
    "   - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html\n",
    "   - https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7608c96-371f-4307-83fd-08d307d31e95",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Outlier Analysis\n",
    "plt.boxplot(data.Price)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de468ef7-b419-4de0-9ba4-fa7510a4857b",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Price>200].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1607bbd-f462-4716-b4be-a638912ce766",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Price<200].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "094a2cad-5e08-44c5-bd9b-f05f6d19ca71",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.Price.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf0d8a10-93af-41a7-989a-5d66e8dfbb1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Price>200].Price.plot.box()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85cdb05d-da88-4ff4-b8f6-a15fcc31a144",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Price<200].Price.plot.box()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0a968ee-16f6-4a5d-85c1-3bcb395c183b",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Price>30].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a34ff10-f8aa-47c0-b6ad-00a9b8539757",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Price>30].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a32a9c16-b9b1-428b-9806-6aff4548d19b",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Price<=30].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f922b8ce-188d-4516-8f64-fca38d6b0ad8",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Price<=30].describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "89e2155e-a8b9-427b-9912-3cb5992100d6",
   "metadata": {},
   "source": [
    "### Inference : Public choose to install applications from the Google Playstore that have nominal price. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "edb440aa-c718-4f18-8193-d02f2d739867",
   "metadata": {},
   "source": [
    "### Histograms\n",
    "\n",
    "Histograms can also be used in conjuction with boxplots for data cleaning and data handling purposes. You can use it to check the spread of a numeric variable. Histograms generally work by bucketing the entire range of values that a particular variable takes to specific __bins__. After that, it uses vertical bars to denote the total number of records in a specific bin, which is also known as its __frequency__.\n",
    "\n",
    "\n",
    "![Histogram](images\\Histogram.png)\n",
    "\n",
    "\n",
    "You can adjust the number of bins to improve its granularity\n",
    "![Bins change](images\\Granular.png)\n",
    "\n",
    "You'll be using plt.hist() to plot a histogram. Check out its official documentation:https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.hist.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f1e3b8f9-6ca8-4066-8b05-7e274c0cb299",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.hist(data.Reviews)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d92996cf-8a59-458e-8c7b-8447dbc2ef29",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.boxplot(data.Reviews)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82cba630-0eeb-4115-b267-001c358ec5b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Reviews >= 10000000].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b91d513-fdb2-4058-ab29-f80326e42817",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Reviews <= 10000000].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db8350a6-4c84-41cb-bc65-6d9e6c62a576",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Reviews <= 10000000].Reviews.plot.box()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "720e636c-4de4-4109-ae91-f0a36eb701b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Reviews >= 10000000].Reviews.plot.box()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afcbb81f-d0a6-49d7-9839-158cdb9ce583",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.boxplot(data.Installs)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29e52a86-94fc-4716-9238-1751417e8326",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.Installs.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "02909a82-ad6c-4015-9aa0-8bd953a3289d",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[data.Installs <= 10000000].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a315387-9005-4d2c-8543-977dff0b72f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.hist(data.Installs)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0efcf34f-6a2d-4d97-8a97-6e9b78b9149d",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.hist(data.Size)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c88f5ab-d900-44ad-ab7a-53f56aa706e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.Size.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36ee2f82-3f87-4c80-b8ba-723e17934723",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.boxplot(data.Size)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "24da6c25-91c0-4212-b49f-1703e41916d5",
   "metadata": {},
   "source": [
    "#### Styling Options\n",
    "\n",
    "One of the biggest advantages of using Seaborn is that you can retain its aesthetic properties and also the Matplotlib functionalities to perform additional customisations. Before we continue with our case study analysis, let’s study some styling options that are available in Seaborn."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a69d978d-6464-4d7d-949f-971668dc2eb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.style.available"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6c0107eb-2d62-4541-ab87-d729c98f19cc",
   "metadata": {},
   "source": [
    "Seaborn is Python library to create statistical graphs easily. It is built on top of matplotlib and closely integrated with pandas.\n",
    "\n",
    "_Functionalities of Seaborn_ :\n",
    "\n",
    "- Dataset oriented API\n",
    "- Analysing univariate and bivariate distributions\n",
    "- Automatic estimation and plotting of  linear regression models\n",
    "- Convenient views for complex datasets\n",
    "- Concise control over style\n",
    "- Colour palettes\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25de1759-662d-47a8-a6f1-66d33831e156",
   "metadata": {},
   "source": [
    "A distribution plot is pretty similar to the histogram functionality in matplotlib. Instead of a frequency plot, it plots an approximate probability density for that rating bucket. And the curve (or the __KDE__) that gets drawn over the distribution is the approximate probability density curve. \n",
    "\n",
    "The following is an example of a distribution plot. Notice that now instead of frequency on the left axis, it has the density for each bin or bucket.\n",
    "\n",
    "You'll be using sns.distplot for plotting a distribution plot. Check out its official documentation: https://seaborn.pydata.org/generated/seaborn.distplot.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d62b6663-dcc1-4285-a316-50410874e4d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.distplot(data.Rating)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3dc224be-049a-4239-a1a6-3914f18f20fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.distplot(data.Rating, bins = 20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f0713aa-0aab-4909-a50f-b828d9019204",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.distplot(data.Rating, bins = 20, color = 'g')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef8f7103-b3b2-4569-a491-e7ab31ac030d",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.set_style\n",
    "sns.set_style(\"dark\")\n",
    "sns.distplot(data.Rating, bins = 20, color = 'g')\n",
    "plt.title(\"Distribution of Rating\", fontsize = 20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4874fe90-42ce-4595-b014-e1694ffd33ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.style.use(\"grayscale\")\n",
    "sns.distplot(data.Rating, bins = 20, color = 'g')\n",
    "plt.title(\"Distribution of Rating\", fontsize = 20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc7593c4-65d0-48e5-bddc-78928f9f1299",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.style.use(\"grayscale\")\n",
    "sns.set_style(\"white\")\n",
    "sns.distplot(data.Rating, bins = 20, color = 'g')\n",
    "plt.title(\"Distribution of Rating\", fontsize = 20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2208ed80-e9c0-484c-9333-86fc1a3aca3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.style.use(\"ggplot\")\n",
    "#sns.set_style(\"white\")\n",
    "sns.distplot(data.Rating, color = 'g')\n",
    "plt.title(\"Distribution of Rating\", fontsize = 20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61d42edc-dbdc-419b-a768-0da24bc4ad82",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.style.use(\"dark_background\")\n",
    "\n",
    "sns.distplot(data.Rating, bins = 20,color = 'g')\n",
    "plt.title(\"Distribution of Rating\", fontsize = 20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8caf2be-e7c2-4796-b4b8-2920bf7eb48a",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"Content Rating\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdd0dacd-f1ad-4f3b-8ade-4a38c7f36025",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = data[-data[\"Content Rating\"].isin([\"Adults only 18+\",\"Unrated\"])]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38eae7ca-7342-4b9f-875b-045f130bf85b",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"Content Rating\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae7b6539-58b9-49b8-b5df-4cfefdb148f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e352730e-48d4-4a4b-9db1-aa1726ce72b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.reset_index(inplace = True, drop = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29ea8732-dd77-4d11-8778-9601149962c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63f1d536-ee11-4371-88c9-1a9468604678",
   "metadata": {},
   "source": [
    "#### Pie-Chart and Bar Chart\n",
    "\n",
    "For analysing how a numeric variable changes across several categories of a categorical variable you utilise either a pie chart or a box plot\n",
    "\n",
    "For example, if you want to visualise the responses of a marketing campaign, you can use the following views:\n",
    "![PieChart](images\\pie.png)\n",
    "\n",
    "![barChart](images\\bar.png)\n",
    "\n",
    "- You'll be using the pandas method of plotting both a pie chart and a bar chart. Check out their official documentations:\n",
    "   - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html\n",
    "   - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.pie.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d71348a7-9b4e-409e-aa95-1b4a887ad1c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"Content Rating\"].value_counts().plot.pie()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc5ad85c-3e7a-42e6-9553-898b6da63a1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"Content Rating\"].value_counts().plot.pie(labels = data[\"Content Rating\"].value_counts().index, \n",
    "                                              autopct = '%1.1f%%',\n",
    "                                              explode = (0,0.1,0,0),\n",
    "                                              startangle = 90,\n",
    "                                              shadow = True)\n",
    "plt.xlabel(\"Percentage of Content Ratings\")\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ebb68615-b882-4942-a63c-898134d82a6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "values = data[\"Content Rating\"].value_counts()\n",
    "total = values.sum()\n",
    "\n",
    "def auctpct_format(pct):\n",
    "    absolute = int(round(pct/100 * total))\n",
    "    return f'{pct:.1f}%\\n({absolute})'\n",
    "\n",
    "values.plot.pie(\n",
    "    labels = values.index,\n",
    "    autopct = auctpct_format,\n",
    "    explode = (0,0.1,0,0),\n",
    "    startangle = 90,\n",
    "    shadow = True)\n",
    "\n",
    "plt.legend(\n",
    "    labels = [f'{label}({count})' for label, count in zip(values.index,values)],\n",
    "    title = 'Content Rating',\n",
    "    loc = 'center left',\n",
    "    bbox_to_anchor = (1,0.5)\n",
    ")\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f9ac48e-e8e6-4803-a037-c28a64475773",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"Content Rating\"].value_counts().plot.bar()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3ef0bb61-1d09-4250-9bd2-6279a08451b0",
   "metadata": {},
   "source": [
    "#### Scatter Plots\n",
    "\n",
    "Scatterplots are perhaps one of the most commonly used as well one of the most powerful visualisations you can use in the field of machine learning. They are pretty crucial in revealing relationships between the data points and you can generally deduce some sort of trends in the data with the help of a scatter plot. \n",
    "\n",
    "![Scatterplot](images\\scatter.png)\n",
    "\n",
    "- They're pretty useful in regression problems to check whether a linear trend exists in the data or not. For example, in the image below, creating a linear model in the first case makes far more sense since a clear straight line trend is visible.\n",
    "\n",
    "![Scatterplot-Reg](images\\regression3.png)\n",
    "\n",
    "- - Also, they help in observing __naturally occuring clusters__. In the following image, the marks of students in Maths and Biology has been plotted.You can clearly group the students to 4 clusters now. Cluster 1 are students who score very well in Biology but very poorly in Maths, Cluster 2 are students who score equally well in both the subjects and so on.\n",
    " \n",
    "![Scatter-Clusters](images\\Clusters.png)\n",
    " \n",
    "  - **Note**: You'll be studying about both Regression and Clustering in greater detail in the machine learning modules\n",
    "  - You'll be using **sns.jointplot()** for creating a scatter plot. Check out its documentation:\n",
    "https://seaborn.pydata.org/generated/seaborn.jointplot.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a22ff2c-9738-4697-a59f-add9daf54039",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Bivariate Analysis \n",
    "\n",
    "plt.scatter(data.Size, data.Rating)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e98fd23c-63ee-4248-977a-6a8547bc58a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.set_style(\"white\")\n",
    "\n",
    "plt.scatter(data.Size, data.Rating)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e8e0223-b545-437d-a871-d7bea3490fbc",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.jointplot(x= 'Size', y = 'Rating', data = data)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4682e0d2-6ce0-4457-be30-e88f0cab4441",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.jointplot(x= 'Price', y = 'Rating', data = data)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de1d66bf-1ef8-4a85-897f-b6c83b70232a",
   "metadata": {},
   "source": [
    "\n",
    "**Reg Plots**\n",
    "\n",
    "These are an extension to the jointplots, where a regression line is added to the view "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fbd72c4-ff18-46fb-96f7-e10219389c6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.jointplot(x= 'Price', y = 'Rating', data = data, kind = 'reg')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fca77850-d048-4401-8a5f-9dc77c032ad3",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.jointplot(x= 'Size', y = 'Rating', data = data, kind = 'reg')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7bf2da6-4289-4684-baa3-79eddc711bd9",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.jointplot(x= 'Price', y = 'Rating', data = data[data.Price>50], kind = 'reg')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27108584-90ef-422b-bb38-ab304f28b010",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.jointplot(x= 'Price', y = 'Rating', data = data[data.Price<50], kind = 'reg')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "506ba682-1272-4474-b87a-becaf98ee02e",
   "metadata": {},
   "source": [
    "### Pair Plots \n",
    "\n",
    "- When you have several numeric variables, making multiple scatter plots becomes rather tedious. Therefore, a pair plot visualisation is preferred where all the scatter plots are in a single view in the form of a matrix\n",
    " - For the non-diagonal views, it plots a **scatter plot** between 2 numeric variables\n",
    " - For the diagonal views, it plots a **histogram**\n",
    "\n",
    " - Pair Plots help in identifying the trends between a target variable and the predictor variables pretty quickly. For example, say you want to predict how your company’s profits are affected by three different factors. In order to choose which you created a pair plot containing profits and the three different factors as the variables. Here are the scatterplots of profits vs the three variables that you obtained from the pair plot.\n",
    "\n",
    " - It is clearly visible that the left-most factor is the most prominently related to the profits, given how linearly scattered the points are and how randomly scattered the rest two factors are.\n",
    " - You'll be using **sns.pairplot()** for this visualisation. Check out its official documentation:https://seaborn.pydata.org/generated/seaborn.pairplot.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d47b957b-8380-4bb8-ba92-d043e9533214",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pairplots \n",
    "sns.pairplot(data[[\"Reviews\", \"Size\",\"Rating\",\"Price\"]])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9225eba-4109-45b5-9576-52b83250bbc4",
   "metadata": {},
   "source": [
    "**Bar Charts Revisited**\n",
    "- Here, you'll be using bar charts once again, this time using the **sns.barplot()** function. Check out its official documentation:https://seaborn.pydata.org/generated/seaborn.barplot.html\n",
    "- You can modify the **estimator** parameter to change the aggregation value of your barplot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c5cd1ae-f536-4bc3-8423-26cc2ce77200",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.groupby([\"Content Rating\"])[\"Rating\"].mean().plot.barh()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f50d9df0-bce3-45cb-9ef3-157956972e38",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.groupby([\"Content Rating\"])[\"Rating\"].median().plot.bar()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25c3a240-ed44-4cac-b50a-5f6c158aa8c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.barplot(data = data , x = \"Content Rating\", y = \"Rating\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bbd0d644-7d9b-4d4c-8a7d-92276e7e87a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.barplot(data = data , x = \"Content Rating\", y = \"Rating\", estimator = np.median)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50b7cb1a-42ba-433f-a644-3d626b57cd45",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.barplot(data = data , x = \"Content Rating\", y = \"Rating\", estimator = lambda x : np.quantile(x,0.05))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b49f678e-b217-4bc2-b491-b70827fa19c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.barplot(data = data , x = \"Content Rating\", y = \"Rating\", estimator = lambda x : np.quantile(x,0.95))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7cdcc771-0059-42fe-8952-b6e6f4004966",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.barplot(data = data , x = \"Content Rating\", y = \"Rating\", estimator = np.min)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b24376a7-cd94-44b7-af05-c8305b3d58c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.barplot(data = data , x = \"Content Rating\", y = \"Rating\", estimator = np.max)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4f073da8-ef34-46f3-91bb-fbd25d128dda",
   "metadata": {},
   "source": [
    "__Box Plots Revisited__\n",
    "\n",
    "- Apart from outlier analysis, box plots are great at comparing the spread and analysing a numerical variable across several categories\n",
    "- Here you'll be using **sns.boxplot()** function to plot the visualisation. Check out its documentation: https://seaborn.pydata.org/generated/seaborn.boxplot.html\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "acfed2a8-04c2-432a-8dfc-b866ec82d395",
   "metadata": {},
   "outputs": [],
   "source": [
    "# revist box plots \n",
    "\n",
    "plt.figure(figsize=[10,7])\n",
    "sns.boxplot(x='Content Rating',y='Rating',data = data)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b7bee36-0efb-4c5c-bf1a-9cd7d749a1f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.boxplot(data.Rating)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2564f8e0-16d5-4850-86cf-45ad03447e68",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Geners \n",
    "data['Genres'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bad00cf8-00d4-4f3a-8c25-6b3e8cf3d983",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=[10,7])\n",
    "a = ['Tools','Entertainment','Education','Action','Productivity']\n",
    "data1 = data[data['Genres'].isin(a)]\n",
    "sns.boxplot(x = data1['Genres'], y= data.Rating)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68269a22-7778-4e95-863a-16e7536eebeb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Heat Maps\n",
    "\n",
    "# Rating Vs Size Vs Content Rating \n",
    "\n",
    "# Prepare buckets for Size column using pd.qcut\n",
    "data['Size_Bucket'] = pd.qcut(data.Size, [0,0.2,0.4,0.6,0.8,1],[\"VL\",\"L\",\"M\",\"H\",\"VH\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b16b00d3-e17b-4b05-bea3-613dbb6478ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7fb01072-887f-4342-aa13-d307c51d9402",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.pivot_table(data = data, index = 'Content Rating',columns = 'Size_Bucket',values = 'Rating')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bf4d10d-6b21-47d3-994b-f8eeef11918a",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.pivot_table(data = data, index = 'Content Rating',columns = 'Size_Bucket',values = 'Rating', aggfunc=np.median)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70a85901-0ec7-4afb-b555-86906254ddf5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Suppose you want to see the 20th percentile \n",
    "pd.pivot_table(data = data, index = 'Content Rating',columns = 'Size_Bucket',values = 'Rating', aggfunc= lambda x:np.quantile(x,0.2))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81899ac4-c0c1-46f0-bf09-2fba79da353d",
   "metadata": {},
   "source": [
    "### Heat Maps\n",
    "Heat mapsutilise the concept of using colours and colour intensities to visualise a range of values. You must have seen heat maps in cricket or football broadcasts on television to denote the players’ areas of strength and weakness.\n",
    "\n",
    "![HeatMap](images\\heatmap1.png)\n",
    "\n",
    "- In python, you can create a heat map whenever you have a rectangular grid or table of numbers analysing any two features\n",
    "- - You'll be using **sns.heatmap()** to plot the visualisation. Checkout its official documentation :https://seaborn.pydata.org/generated/seaborn.heatmap.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b76a8a49-7919-4f69-8c31-6a2fbe0cd607",
   "metadata": {},
   "outputs": [],
   "source": [
    "result = pd.pivot_table(data = data, index = 'Content Rating',columns = 'Size_Bucket',values = 'Rating', aggfunc= lambda x:np.quantile(x,0.2))\n",
    "sns.heatmap(result)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1bbee521-bf81-4ba6-b9e3-a57c430d23fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "result = pd.pivot_table(data = data, index = 'Content Rating',columns = 'Size_Bucket',values = 'Rating', aggfunc= lambda x:np.quantile(x,0.2))\n",
    "sns.heatmap(result, annot = True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a8d6cb88-aa2b-4b41-b883-89e6179d5fc7",
   "metadata": {},
   "outputs": [],
   "source": [
    "result = pd.pivot_table(data = data, index = 'Content Rating',columns = 'Size_Bucket',values = 'Rating', aggfunc= lambda x:np.quantile(x,0.2))\n",
    "sns.heatmap(result, annot = True, cmap = 'Reds')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cece5c32-0026-4b98-80b1-3f06ea8e6554",
   "metadata": {},
   "outputs": [],
   "source": [
    "result = pd.pivot_table(data = data, index = 'Content Rating',columns = 'Size_Bucket',values = 'Rating', aggfunc= lambda x:np.quantile(x,0.2))\n",
    "sns.heatmap(result, annot = True, cmap = 'Greens')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18f22023-76ec-4a4c-a01b-f0772aaf6bec",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Line Graphs\n",
    "\n",
    "data['Last Updated'].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2dfdf575-1cab-44f5-9ad3-00ad6e327c68",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Last_Updated_Month'] = pd.to_datetime(data['Last Updated']).dt.month\n",
    "data.groupby(['Last_Updated_Month'])['Rating'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3731b47c-705a-48ba-b12f-70c29dac61a4",
   "metadata": {},
   "source": [
    "### Session 3: Additional Visualisations\n",
    "- A line plot tries to observe trends using time dependent data.\n",
    "-  For this part, you'll be using **pd.to_datetime()** function. Check out its documentation:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb3cc8e5-891b-41d4-9a22-787960b2cb30",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize = [10,5])\n",
    "data.groupby(['Last_Updated_Month'])['Rating'].mean().plot()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8db5686e-6318-4d10-a18a-70113cae1ff2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Stacked Bars \n",
    "pd.pivot_table(data = data , values = 'Installs', index = 'Last_Updated_Month',columns = \"Content Rating\", aggfunc = sum)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "364ac756-de20-44b5-ac47-19f6e49dffba",
   "metadata": {},
   "source": [
    "#### Stacked Bar Charts\n",
    "- A stacked bar chart breaks down each bar of the bar chart on the basis of a different category\n",
    "- For example, for the Campaign Response bar chart you saw earlier, the stacked bar chart is also showing the Gender bifurcation as well\n",
    "- ![Stacked](images\\stacked.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bfae474-2ac0-4af2-984d-3cfc3090b822",
   "metadata": {},
   "outputs": [],
   "source": [
    "monthly = pd.pivot_table(data = data , values = 'Installs', index = 'Last_Updated_Month',columns = \"Content Rating\", aggfunc = sum)\n",
    "monthly.plot(kind = 'bar', stacked = 'True', figsize=[10,8])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ac10751-116f-4ab8-b05b-b9f484d49b1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "monthly_precent = monthly[[\"Everyone\", \"Everyone 10+\", \"Mature 17+\",\"Teen\"]].apply(lambda x:x/x.sum(),axis =1)\n",
    "monthly_precent.plot(kind = 'bar', stacked = 'True', figsize = [10,6])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d7787d5-179a-4554-896c-80f6b9b3b2b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# plotly library \n",
    "\n",
    "\n",
    "res = data.groupby([\"Last_Updated_Month\"])[[\"Rating\"]].mean()\n",
    "res.reset_index(inplace = True)\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c0532cbc-1a77-44b3-b7f6-68cd96c35c7b",
   "metadata": {},
   "source": [
    "#### Plotly\n",
    "\n",
    "Plotly is a Python library used for creating interactive visual charts. You can take a look at how you can use it to create aesthetic looking plots with a lot of user-friendly functionalities like hover, zoom, etc.\n",
    "\n",
    "Check out this link for installation and documentation:https://plot.ly/python/getting-started/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8c3c50f-f913-4eea-953c-b1df0753987b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import plotly.express as px \n",
    "fig = px.line(res, x = 'Last_Updated_Month', y = 'Rating', title = 'Monthly Average Ratings')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb629e6e-78e8-4a91-a21b-834e458ef087",
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = px.bar(res, x = 'Last_Updated_Month', y = 'Rating', title = 'Monthly Average Ratings')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "744c36da-910f-47ca-9f9c-ce7eb74a1df9",
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = px.box(res, x = 'Last_Updated_Month', y = 'Rating', title = 'Monthly Average Ratings')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6072e8e4-998c-4c3e-ae8b-d57c5d209f8b",
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = px.histogram(res, x = 'Last_Updated_Month', y = 'Rating', title = 'Monthly Average Ratings')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "642ba7d3-9223-49b6-959a-26466b874fbb",
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = px.scatter(res, x = 'Last_Updated_Month', y = 'Rating', title = 'Monthly Average Ratings')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a45cf22-0c57-400c-b144-48bc58621adb",
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
