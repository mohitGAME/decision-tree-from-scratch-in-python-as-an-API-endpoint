from sklearn.metrics import confusion_matrix
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser, FormParser
from rest_framework.views import APIView
from .serializers import FileSerializer
from rest_framework import status, serializers
from rest_framework.response import Response
from .AlgoLib import DecisionTree
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from rest_framework.decorators import api_view
import json
from classifiy.serializers import MlSerial, PurchaseDetailSerializer
import os
import pickle


# Create your views here.


def getAlgorithms(request):
    lst = []
    lst.append({"id": 1, "name": "decision tree(ID3)"})
    lst.append({"id": 2, "name": "decision tree(CART)"})
    return JsonResponse(lst, safe=False)


def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)
        attCol = request.data.get('AttributeColumns')
        attCol = list(json.loads(attCol))

        if file_serializer.is_valid():
            for filename, file in request.FILES.items():
                df = pd.read_csv(request.FILES.get(filename))
                break

            if not set(attCol).issubset(df.columns):
                return Response('Invalid Attribute Columns', status=status.HTTP_400_BAD_REQUEST)

            X = df[attCol].values
            y = df[request.data.get('classColumn')].values
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=1234)
            clf = DecisionTree(
                max_depth=100, Algorithm=request.data.get('algorithm'))
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
            myDict = {}
            myDict["accuracy"] = accuracy(y_test, y_pred)

            import pickle
            import os

            dirname = os.path.dirname(__file__)
            filename = os.path.join(dirname, 'binaryFiles/modle.pkl')
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "wb") as f:
                pickle.dump(clf, f)
            return Response(myDict, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def predictPurchase(request):
    purchase_serializer = PurchaseDetailSerializer(data=request.data)
    if purchase_serializer.is_valid():
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'binaryFiles/modle.pkl')
        model = pickle.load(open(filename, 'rb'))
        gender = request.data["Gender"]
        age = int(request.data["Age"])
        salary = int(request.data["Salary"])

        X_test = np.array([(gender, age,  salary)], dtype=[
                          ('gender', 'U10'), ('age', 'f4'), ('salary', 'f4')])
        y_pred = model.predict(X_test)
    return Response(y_pred[0], status=status.HTTP_201_CREATED)
