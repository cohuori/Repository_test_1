{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "navidad-arbol.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOZFQH2PwJ1t7QedoVRM36I",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/cohuori/Repository_test_1/blob/master/navidad_arbol.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N6ffxO9Rfkqe",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import sys \n",
        "  \n",
        "number = int(sys.argv[1])\n",
        "x = ' '  \n",
        "\n",
        "for i in range(1,number): \n",
        "    print(x*((number-i)-1),\"#\"*i)\n",
        "print(\"#\"*number)"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}