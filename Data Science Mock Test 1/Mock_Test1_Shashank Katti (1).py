{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "03e04c32-6ca8-4197-8eab-55ef966dde28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "YES\n"
     ]
    }
   ],
   "source": [
    "X = 12\n",
    "if (X>10 & X<15):\n",
    "  print('YES') \n",
    "else: \n",
    "  print('No')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f203e403-f310-4c4a-b5a2-f7046f3be816",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=16 \n",
    "c=20\n",
    "if a < b:\n",
    "  print(\"a\")\n",
    "elif b < c:\n",
    "  print(\"b\")\n",
    "else:\n",
    "  print(\"c\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "df641daa-1c1e-42b1-800b-910a44431a45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n"
     ]
    }
   ],
   "source": [
    "a=10 \n",
    "b=16 \n",
    "c=20\n",
    "if(\"missing part 1\"): \n",
    "   print(\"a\")\n",
    "elif(\"missing part 2\"): \n",
    "   print(\"b\")\n",
    "else:\n",
    "   print(\"c\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "4ab3e839-1974-4061-9cda-7ad962b33dcd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b\n"
     ]
    }
   ],
   "source": [
    "a=10 \n",
    "b=16 \n",
    "c=20\n",
    "if(\"missing part 2\"): \n",
    "   print(\"b\")\n",
    "elif(\"missing part 1\"): \n",
    "   print(\"a\")\n",
    "else:\n",
    "   print(\"c\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "251f02f1-ad4e-4a73-a07e-f0f2a87687eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "YES\n",
      "NO\n"
     ]
    }
   ],
   "source": [
    "def check_vowel_start(input_string):\n",
    "    vowels = \"AEIOUaeiou\"\n",
    "    if input_string[0] in vowels:\n",
    "        print(\"YES\")\n",
    "    else:\n",
    "        print(\"NO\")\n",
    "\n",
    "# Sample inputs\n",
    "check_vowel_start(\"Alpha\")\n",
    "check_vowel_start(\"Time\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b75c2942-bf45-4de1-94ba-89ba5281b2f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 1 0 1 0 1]\n",
      " [1 0 1 0 1 0]\n",
      " [0 1 0 1 0 1]\n",
      " [1 0 1 0 1 0]\n",
      " [0 1 0 1 0 1]\n",
      " [1 0 1 0 1 0]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "def create_checkerboard(n):\n",
    "    # Create a (n x n) checkerboard pattern\n",
    "    checkerboard = np.zeros((n, n), dtype=int)\n",
    "    checkerboard[1::2, ::2] = 1\n",
    "    checkerboard[::2, 1::2] = 1\n",
    "    return checkerboard\n",
    "\n",
    "# Sample input\n",
    "n = 6\n",
    "print(create_checkerboard(n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a70a831-ffdf-4aad-9815-d37ec21a1391",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
