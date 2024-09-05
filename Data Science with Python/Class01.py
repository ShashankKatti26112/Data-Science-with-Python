{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e0a395b5-827f-462f-aba3-f771225504e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to NUCOT\n"
     ]
    }
   ],
   "source": [
    "print(\"Welcome to NUCOT\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "10b5598c-b8b5-408e-88fe-32f0df6fb6d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Data Science Program\n"
     ]
    }
   ],
   "source": [
    "print(\"Welcome to Data Science Program\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0edb61a4-4c68-42dd-8d8c-e156b204bb77",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$\n"
     ]
    }
   ],
   "source": [
    "print(\"$\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "89e7fd53-ac03-42a5-ab5d-9f7c973003b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$$$\n"
     ]
    }
   ],
   "source": [
    "print(\"$\"* 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b215988e-b10d-48a0-83d9-a0da32ad867e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mike\n"
     ]
    }
   ],
   "source": [
    "var1 = \"Mike\"\n",
    "print(var1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f9799a4d-9b77-483d-b219-0ff4af0d8934",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "var2 = 6\n",
    "print(var2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "22bcc1bc-653d-4c1d-8143-adafa066dfe3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What is your favourite number? 79887098\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "79887098\n"
     ]
    }
   ],
   "source": [
    "number = input(\"What is your favourite number?\")\n",
    "print(number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "afed7fec-ceb8-4574-9d2d-779b484b7173",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What is your name? XQYH\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "XQYH\n"
     ]
    }
   ],
   "source": [
    "name = input(\"What is your name?\")\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7545b161-f73b-4cf8-916d-09354e83ce50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your age 30\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You are  360 months old\n"
     ]
    }
   ],
   "source": [
    "age = input(\"Enter your age\")\n",
    "age = int(age)\n",
    "print(\"You are \", age*12, \"months old\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "dbb2b83e-8427-4d92-a954-731068c5a116",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your age 30\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You are  360 months old\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"Enter your age\"))\n",
    "print(\"You are \", age*12, \"months old\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "473fba6c-fa58-4a7e-8f74-58cdf87d8d09",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your number 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "answer 720\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter your number\"))\n",
    "if num > 0:\n",
    "    fac = 1\n",
    "    for i in range (1,num+1):\n",
    "        fac = fac * i\n",
    "    print(\"answer\", fac)\n",
    "elif num < 0:\n",
    "    print(\"Invalid input\")\n",
    "else:\n",
    "    print(\"Zero factorial is 1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "8862bbda-48d3-45e5-a019-a8f71c4fe27a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# change data types \n",
    "integer = 1\n",
    "float_num = 1.6\n",
    "a = \"Mike\"\n",
    "boolean = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0377325a-2620-4909-a0cc-e2f932235d11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "print(type(integer))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "3e3915c8-86b4-426d-a674-e34503c20d8c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "print(type(float_num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "4b962fb5-f83e-4e64-a558-e972e431e04f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "71a871b6-c23f-4328-bd86-1bbe4d5250e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "print(type(boolean))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "e28dfc13-ab8a-49b9-b429-b253e840df22",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Arthemetic oprations\n",
    "a = 6\n",
    "b = 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "48c68d34-70df-4e37-bb3e-0f6a6d2d4362",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13\n"
     ]
    }
   ],
   "source": [
    "add = a+b\n",
    "print(add)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "fe07791d-cfbc-4cfd-86d0-b1e2f6aa748e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sub = a - b \n",
    "sub"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "f916efda-e459-4b99-a404-fba9610e7210",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "float = a // b\n",
    "float"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "3bdc818d-320c-452c-b097-2a3781c59c5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8571428571428571"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "div = a/b\n",
    "div"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "2a9a7602-b651-4d1c-9d25-acefa27b26aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rem = a%b # remainder value is shown as output\n",
    "rem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "ccca9172-d8c1-474b-b75e-9804f7b480b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "279936"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "power = a ** b # a to the power of b\n",
    "power"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "77a437d6-5004-4ba8-8141-ba6d77ab9185",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11.857142857142858\n"
     ]
    }
   ],
   "source": [
    "print((4*5)-9 + 6/7) # PEDMAS "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "f10108cc-82b8-4cf7-ae30-32e8cd11be7c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter you favourite flavour vanilla\n",
      "enter your favourite dessert ice cream\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You Ordered vanilla-ice cream\n"
     ]
    }
   ],
   "source": [
    "# string Manipulation \n",
    "flavour = input(\"enter you favourite flavour\")\n",
    "dessert_type = input(\"enter your favourite dessert\")\n",
    "print(\"You Ordered\", flavour+ \"-\"+dessert_type)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "9bba207b-69ae-4ba9-8d71-95b1d2eddfe8",
   "metadata": {},
   "outputs": [],
   "source": [
    "string = \"I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison\" "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "7779a37c-750b-48f4-b3ef-f8c7feb71c13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "82"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "af9098ef-923b-410d-b565-a83bb2dda9f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'I'"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string[-82]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "346579dc-e2e7-49de-87b7-63ba06366d4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'n'"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "ade7fda8-dc71-4561-9c3c-db7ae676f03c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'I'"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "d02fe59f-6899-4fac-add7-fd0d3b5d7606",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'h'"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "b2038844-5a3b-4192-a245-0c03d6f7c1f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' '"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "1f099220-332d-4355-8af1-deaeed8d17c2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"I have not failed. I've just found 10,000 ways that won't work. \""
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "slice = string[0:64]\n",
    "slice"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "1977e80a-3204-488c-84e8-e22634f59326",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison\""
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string[0:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "54a5bd2e-28b4-4cfc-bc87-65c631fa05dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Ediso\""
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string[:-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "7e461c57-f907-4d0b-beb4-882d94b83a50",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"I have not failed. I've just found 10,000 ways that won't work. \""
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string[:64]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "5aa14a48-bfc9-4c28-8a6d-cb7e2f63e131",
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
    "str = \"John! did you attend the conference on advanced machine learning\"\n",
    "print(\"Lincon\" in str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "5ed045b9-e190-40fc-8505-472bde332d38",
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
    "print(\"John\" in str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "2c65e264-f8a9-4b40-aed3-1a4eac3a4fb8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I AM A STUDENT OF NUCOT\n"
     ]
    }
   ],
   "source": [
    "small = \"i am a student of NUCOT\"\n",
    "print(small.upper())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "5fc547d0-9383-41a4-8a97-395db0aa0c4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i am a student of nucot\n"
     ]
    }
   ],
   "source": [
    "print(small.lower())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "c9255066-9460-47f7-8182-1e1289b0a011",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'          This a moment to cherish!'"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "some_sentence = \"          This a moment to cherish!             \"\n",
    "some_sentence.rstrip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "114a89a5-75c8-49cb-aad5-eff08c978bb3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'This a moment to cherish!             '"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "some_sentence.lstrip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "910235e8-7802-4a9b-bfb9-6a5e32bff8bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'This a moment to cherish!'"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "some_sentence.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "124be443-2f0b-477a-94a7-35e346ebdd37",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string1 = \"This is a sample sentence\"\n",
    "string1.count('i')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "a5d71fef-52f0-43f3-b3cf-70f8200faf16",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string1.count('i', 4,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "2e133b14-5cad-4b6a-b998-a4d561386e7d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = \"This is a coding class in Python\"\n",
    "a.count(\"o\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "1c49da5d-e641-4e16-9328-25d08e92ab8c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.count('o',10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "259af620-3733-46a1-b1a0-c8fb42099266",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "id": "5f3ff9ad-b4e5-429c-a775-8ab3f731313d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data Analysis using Pandas\n"
     ]
    }
   ],
   "source": [
    "A = \"Data\"\n",
    "B = \"Analysis\"\n",
    "C = \"Pandas\"\n",
    "print(\"{0} {1} using {2}\". format(A,B,C))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed9a01ec-40a7-4629-b2a4-92ccdb5e1cc4",
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
