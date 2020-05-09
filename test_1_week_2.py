{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "test-1-week-2.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyN/OZCAew6nHf0X1jhW8Cvc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/cohuori/Repository_test_1/blob/master/test_1_week_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5HDuSuQ8Xtv8",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 127
        },
        "outputId": "f36b25b1-c965-4f89-ae8b-f6f37f30366b"
      },
      "source": [
        "from google.colab import drive \n",
        "drive.mount('/content/drive')\n"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Go to this URL in a browser: https://accounts.google.com/o/oauth2/auth?client_id=947318989803-6bn6qk8qdgf4n4g3pfee6491hc0brc4i.apps.googleusercontent.com&redirect_uri=urn%3aietf%3awg%3aoauth%3a2.0%3aoob&response_type=code&scope=email%20https%3a%2f%2fwww.googleapis.com%2fauth%2fdocs.test%20https%3a%2f%2fwww.googleapis.com%2fauth%2fdrive%20https%3a%2f%2fwww.googleapis.com%2fauth%2fdrive.photos.readonly%20https%3a%2f%2fwww.googleapis.com%2fauth%2fpeopleapi.readonly\n",
            "\n",
            "Enter your authorization code:\n",
            "··········\n",
            "Mounted at /content/drive\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sGbeBLSrYO9E",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "7940a23b-4bac-4f7b-b7a2-713bfe8978af"
      },
      "source": [
        "! pwd"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/content/drive/My Drive\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "b3RJbwqVYR5D",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "4e0570a2-1bce-45fd-a6a0-b7185e6823d8"
      },
      "source": [
        "cd /content/drive/My\\ Drive"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/content/drive/My Drive\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "io0gEPrZYWER",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "93718c14-686d-4222-c0b7-83b54b874ebe"
      },
      "source": [
        "! ls"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "data2.txt  data.txt  dhfr.csv  new_folder  solution_3.py  weather-weka.csv\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uooYjmtwYZ7Y",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "3a9ff304-3230-4593-fa4d-6d6941aa961e"
      },
      "source": [
        "cd my_coding/"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/content/drive/My Drive/my_coding\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oyTakPRbYdyI",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 557
        },
        "outputId": "5f7bd34c-e93c-4bd9-c7c5-6b80d4e48d21"
      },
      "source": [
        "!python solution_3.py 30"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "                             #\n",
            "                            ##\n",
            "                           ###\n",
            "                          ####\n",
            "                         #####\n",
            "                        ######\n",
            "                       #######\n",
            "                      ########\n",
            "                     #########\n",
            "                    ##########\n",
            "                   ###########\n",
            "                  ############\n",
            "                 #############\n",
            "                ##############\n",
            "               ###############\n",
            "              ################\n",
            "             #################\n",
            "            ##################\n",
            "           ###################\n",
            "          ####################\n",
            "         #####################\n",
            "        ######################\n",
            "       #######################\n",
            "      ########################\n",
            "     #########################\n",
            "    ##########################\n",
            "   ###########################\n",
            "  ############################\n",
            " #############################\n",
            "##############################\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hO1w3kVPb1br",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 179
        },
        "outputId": "783c6cd9-66c9-4d83-9a8d-2330965f3712"
      },
      "source": [
        "!cat solution_3.py"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "import sys \n",
            "  \n",
            "number = int(sys.argv[1])\n",
            "x = ' '  \n",
            "\n",
            "for i in range(1,number): \n",
            "    print(x*((number-i)-1),\"#\"*i)\n",
            "print(\"#\"*number)\n",
            "    \n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CjyM6cVod-Ok",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "7e1ff385-b116-4359-b4b0-3685fc1da8f9"
      },
      "source": [
        ""
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "UsageError: %%writefile is a cell magic, but the cell body is empty.\n"
          ],
          "name": "stderr"
        }
      ]
    }
  ]
}