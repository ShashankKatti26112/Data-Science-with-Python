{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "collapsed": true,
        "id": "nnzE2aF3EWKi"
      },
      "outputs": [],
      "source": [
        "# List of order ID’s which are processed\n",
        "processed_orders = [1152, 1154, 1155, 1156, 1157, 1160, 1161, 1162, 1166, 1169, 1170, 1172, 1176, 1050, 1178, 1051, 1052, 1054, 1058, 1060, 1061, 1062, 1065, 1066, 1067, 1068, 1069, 1076, 1077, 1080, 1081, 1083, 1091, 1085, 1088, 1089, 1131, 1092, 1094, 1095, 1099, 1102, 1103, 1104, 1106, 1107, 1108, 1109, 1111, 1117, 1119, 1121, 1150, 1128, 1129, 1136, 1137, 1139, 1140, 1141, 1144, 1148, 1124]\n",
        "\n",
        "# List of order ID’s which are returned\n",
        "returned_orders = [1153, 1158, 1159, 1163, 1164, 1165, 1167, 1168, 1171, 1173, 1174, 1175, 1177, 1053, 1055, 1056, 1057, 1059, 1063, 1064, 1070, 1071, 1072, 1073, 1074, 1075, 1078, 1079, 1082, 1084, 1086, 1087, 1090, 1093, 1096, 1097, 1098, 1100, 1101, 1105, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1138, 1142, 1143, 1145, 1146, 1147, 1149, 1151]\n",
        "\n",
        "# Consider the information available in the above two lists and answer the question given below"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zALrxK3SEWKn"
      },
      "source": [
        "#### Count the total number of orders [ Orders include both processed and returned orders]\n",
        "\n",
        "- 63\n",
        "- 66\n",
        "- 126\n",
        "- 129"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "collapsed": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V2jNJBErEWKp",
        "outputId": "d3b368e5-f354-4531-8c26-05bef08623f4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total number of orders: 129\n"
          ]
        }
      ],
      "source": [
        "# List of order ID’s which are processed\n",
        "processed_orders = [1152, 1154, 1155, 1156, 1157, 1160, 1161, 1162, 1166, 1169, 1170, 1172, 1176, 1050, 1178, 1051, 1052, 1054, 1058, 1060, 1061, 1062, 1065, 1066, 1067, 1068, 1069, 1076, 1077, 1080, 1081, 1083, 1091, 1085, 1088, 1089, 1131, 1092, 1094, 1095, 1099, 1102, 1103, 1104, 1106, 1107, 1108, 1109, 1111, 1117, 1119, 1121, 1150, 1128, 1129, 1136, 1137, 1139, 1140, 1141, 1144, 1148, 1124]\n",
        "\n",
        "# List of order ID’s which are returned\n",
        "returned_orders = [1153, 1158, 1159, 1163, 1164, 1165, 1167, 1168, 1171, 1173, 1174, 1175, 1177, 1053, 1055, 1056, 1057, 1059, 1063, 1064, 1070, 1071, 1072, 1073, 1074, 1075, 1078, 1079, 1082, 1084, 1086, 1087, 1090, 1093, 1096, 1097, 1098, 1100, 1101, 1105, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1138, 1142, 1143, 1145, 1146, 1147, 1149, 1151]\n",
        "\n",
        "#Count the total number of orders [Orders include both processed and returned orders]\n",
        "total_orders = len(set(processed_orders + returned_orders))\n",
        "print(\"Total number of orders:\", total_orders)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Yz2tonjcEWKp"
      },
      "source": [
        "#### In the total orders, identify the 50th order [ Note: Assume the order ID’s are being generated in a consecutive manner]\n",
        "\n",
        "- 1152\n",
        "- 1099\n",
        "- 1154\n",
        "- 1100\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "collapsed": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zoSZcQxCEWKq",
        "outputId": "2e771e0b-e844-4ab1-9085-efb8f252120f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "50th order: 1099\n"
          ]
        }
      ],
      "source": [
        "# List of order ID’s which are processed\n",
        "processed_orders = [1152, 1154, 1155, 1156, 1157, 1160, 1161, 1162, 1166, 1169, 1170, 1172, 1176, 1050, 1178, 1051, 1052, 1054, 1058, 1060, 1061, 1062, 1065, 1066, 1067, 1068, 1069, 1076, 1077, 1080, 1081, 1083, 1091, 1085, 1088, 1089, 1131, 1092, 1094, 1095, 1099, 1102, 1103, 1104, 1106, 1107, 1108, 1109, 1111, 1117, 1119, 1121, 1150, 1128, 1129, 1136, 1137, 1139, 1140, 1141, 1144, 1148, 1124]\n",
        "\n",
        "# List of order ID’s which are returned\n",
        "returned_orders = [1153, 1158, 1159, 1163, 1164, 1165, 1167, 1168, 1171, 1173, 1174, 1175, 1177, 1053, 1055, 1056, 1057, 1059, 1063, 1064, 1070, 1071, 1072, 1073, 1074, 1075, 1078, 1079, 1082, 1084, 1086, 1087, 1090, 1093, 1096, 1097, 1098, 1100, 1101, 1105, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1138, 1142, 1143, 1145, 1146, 1147, 1149, 1151]\n",
        "\n",
        "# In the total orders, identify the 50th order (generated in a consecutive manner)\n",
        "all_orders = sorted(set(processed_orders + returned_orders))\n",
        "fiftieth_order = all_orders[49]  # 50th order (index starts at 0)\n",
        "print(\"50th order:\", fiftieth_order)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2MPzLrXzEWKr"
      },
      "source": [
        "#### Is 50th order a returned order or processed order?\n",
        "\n",
        "- Returned Order\n",
        "- Processed Order\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "collapsed": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ft124abwEWKr",
        "outputId": "fbc9bb31-e666-423d-a771-2ed0bff3dd78"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "50th order is a Processed Order\n"
          ]
        }
      ],
      "source": [
        "# List of order ID’s which are processed\n",
        "processed_orders = [1152, 1154, 1155, 1156, 1157, 1160, 1161, 1162, 1166, 1169, 1170, 1172, 1176, 1050, 1178, 1051, 1052, 1054, 1058, 1060, 1061, 1062, 1065, 1066, 1067, 1068, 1069, 1076, 1077, 1080, 1081, 1083, 1091, 1085, 1088, 1089, 1131, 1092, 1094, 1095, 1099, 1102, 1103, 1104, 1106, 1107, 1108, 1109, 1111, 1117, 1119, 1121, 1150, 1128, 1129, 1136, 1137, 1139, 1140, 1141, 1144, 1148, 1124]\n",
        "\n",
        "# List of order ID’s which are returned\n",
        "returned_orders = [1153, 1158, 1159, 1163, 1164, 1165, 1167, 1168, 1171, 1173, 1174, 1175, 1177, 1053, 1055, 1056, 1057, 1059, 1063, 1064, 1070, 1071, 1072, 1073, 1074, 1075, 1078, 1079, 1082, 1084, 1086, 1087, 1090, 1093, 1096, 1097, 1098, 1100, 1101, 1105, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1138, 1142, 1143, 1145, 1146, 1147, 1149, 1151]\n",
        "\n",
        "# Is the 50th order a returned or processed order?\n",
        "if fiftieth_order in returned_orders:\n",
        "    print(\"50th order is a Returned Order\")\n",
        "else:\n",
        "    print(\"50th order is a Processed Order\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CInNmdPvEWKs"
      },
      "source": [
        "#### What is the last processed order ID ? [ Note: Assume the order ID’s are being generated in a consecutive manner]\n",
        "\n",
        "- 1050\n",
        "- 1178\n",
        "- 1124\n",
        "- 1177\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "collapsed": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "56tstsLkEWKs",
        "outputId": "a08b3410-8cc7-4127-b9e8-934ea57d0742"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Last processed order ID: 1178\n"
          ]
        }
      ],
      "source": [
        "# List of order ID’s which are processed\n",
        "processed_orders = [1152, 1154, 1155, 1156, 1157, 1160, 1161, 1162, 1166, 1169, 1170, 1172, 1176, 1050, 1178, 1051, 1052, 1054, 1058, 1060, 1061, 1062, 1065, 1066, 1067, 1068, 1069, 1076, 1077, 1080, 1081, 1083, 1091, 1085, 1088, 1089, 1131, 1092, 1094, 1095, 1099, 1102, 1103, 1104, 1106, 1107, 1108, 1109, 1111, 1117, 1119, 1121, 1150, 1128, 1129, 1136, 1137, 1139, 1140, 1141, 1144, 1148, 1124]\n",
        "\n",
        "# List of order ID’s which are returned\n",
        "returned_orders = [1153, 1158, 1159, 1163, 1164, 1165, 1167, 1168, 1171, 1173, 1174, 1175, 1177, 1053, 1055, 1056, 1057, 1059, 1063, 1064, 1070, 1071, 1072, 1073, 1074, 1075, 1078, 1079, 1082, 1084, 1086, 1087, 1090, 1093, 1096, 1097, 1098, 1100, 1101, 1105, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1138, 1142, 1143, 1145, 1146, 1147, 1149, 1151]\n",
        "\n",
        "# What is the last processed order ID? (Assume IDs generated in a consecutive manner)\n",
        "last_processed_order = max(processed_orders)\n",
        "print(\"Last processed order ID:\", last_processed_order)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "doDz1nKTEWKt"
      },
      "source": [
        "#### Identify the first 4 orders which are processed?\n",
        "\n",
        "- 1152, 1154, 1155, 1156\n",
        "- 1051, 1152, 1153, 1154\n",
        "- 1050, 1051, 1052, 1054\n",
        "- 1050, 1051, 1052, 1053"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "collapsed": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oln_Ka67EWKt",
        "outputId": "1f00bae1-c0db-4bf5-8435-4874bfc11547"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "First 4 processed orders: [1050, 1051, 1052, 1054]\n"
          ]
        }
      ],
      "source": [
        "# List of order ID’s which are processed\n",
        "processed_orders = [1152, 1154, 1155, 1156, 1157, 1160, 1161, 1162, 1166, 1169, 1170, 1172, 1176, 1050, 1178, 1051, 1052, 1054, 1058, 1060, 1061, 1062, 1065, 1066, 1067, 1068, 1069, 1076, 1077, 1080, 1081, 1083, 1091, 1085, 1088, 1089, 1131, 1092, 1094, 1095, 1099, 1102, 1103, 1104, 1106, 1107, 1108, 1109, 1111, 1117, 1119, 1121, 1150, 1128, 1129, 1136, 1137, 1139, 1140, 1141, 1144, 1148, 1124]\n",
        "\n",
        "# List of order ID’s which are returned\n",
        "returned_orders = [1153, 1158, 1159, 1163, 1164, 1165, 1167, 1168, 1171, 1173, 1174, 1175, 1177, 1053, 1055, 1056, 1057, 1059, 1063, 1064, 1070, 1071, 1072, 1073, 1074, 1075, 1078, 1079, 1082, 1084, 1086, 1087, 1090, 1093, 1096, 1097, 1098, 1100, 1101, 1105, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1138, 1142, 1143, 1145, 1146, 1147, 1149, 1151]\n",
        "\n",
        "# First 4 orders which are processed\n",
        "first_4_processed_orders = sorted(processed_orders)[:4]\n",
        "print(\"First 4 processed orders:\", first_4_processed_orders)"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
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
      "version": "3.7.3"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}