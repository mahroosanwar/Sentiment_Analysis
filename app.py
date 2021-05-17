{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "app.py",
      "provenance": [],
      "authorship_tag": "ABX9TyMxYeKMw3oD5qcERWdhZofj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/mahroosanwar/Sentiment_Analysis/blob/main/app_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sPw00fBsJilC"
      },
      "source": [
        "!pip install streamlit --quiet\n",
        "!pip install pyngrok==4.1.1 --quiet\n",
        "from pyngrok import ngrok"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BFtbVINzbLub",
        "outputId": "00c65816-cc9a-45cb-9328-9b4983ee840e"
      },
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "import sklearn\n",
        "import joblib\n",
        "model = joblib.load('/content/Email_model')\n",
        "st.title('Sentiment Analysis')\n",
        "ip = st.text_input(\"Enter the message\")\n",
        "op = model.predict([ip])\n",
        "if st.button('Predict'):\n",
        "  st.title(op[0])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Overwriting app.py\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DPwqoQSgdnQ9"
      },
      "source": [
        "!nohup streamlit run app.py &\n",
        "url=ngrok.connect(port='8501')\n",
        "url"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
