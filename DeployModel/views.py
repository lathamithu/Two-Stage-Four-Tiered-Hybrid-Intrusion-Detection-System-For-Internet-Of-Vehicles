from django.http import HttpResponse
from django.shortcuts import render
import joblib
from .utils import get_plot
import json
from sklearn.metrics import precision_recall_fscore_support, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from .utils import get_plot


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def team(request):
    return render(request, "team.html")

def tab1(request):
    cls = joblib.load('finalized_model_xg.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    y_true = df2
    chart = get_plot(y_true, y_predict)
    return render(request, "tab1.html", {'chart': chart})

def tab2(request):
    cls = joblib.load('finalized_model_rf.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    y_true = df2
    chart = get_plot(y_true, y_predict)
    return render(request, "tab2.html", {'chart': chart})

def tab3(request):
    cls = joblib.load('finalized_model_dt.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    y_true = df2
    chart = get_plot(y_true, y_predict)
    return render(request, "tab3.html", {'chart': chart})

def tab4(request):
    cls = joblib.load('finalized_model_et.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    y_true = df2
    chart = get_plot(y_true, y_predict)
    return render(request, "tab4.html", {'chart': chart})

def tab5(request):
    cls = joblib.load('finalized_model_st.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    y_true = df2
    chart = get_plot(y_true, y_predict)
    return render(request, "tab5.html", {'chart': chart})

def res1(request):
    cls = joblib.load('finalized_model_xg.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    print(y_predict)
    xg_score = cls.score(df, df2)
    y_predict = cls.predict(df)
    y_true = df2
    precision, recall, fscore, none = precision_recall_fscore_support(y_true, y_predict, average='weighted')
    context = {
        "accuracy" : str(xg_score),
        "precision" : str(precision),
        "recall" : str(recall),
        "f1score": str(fscore),
    }
    return render(request, "res1.html", context)

def res2(request):
    cls = joblib.load('finalized_model_rf.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    print(y_predict)
    xg_score = cls.score(df, df2)
    y_predict = cls.predict(df)
    y_true = df2
    precision, recall, fscore, none = precision_recall_fscore_support(y_true, y_predict, average='weighted')
    context = {
        "accuracy": str(xg_score),
        "precision": str(precision),
        "recall": str(recall),
        "f1score": str(fscore),
    }
    return render(request, "res2.html", context)


def res3(request):
    cls = joblib.load('finalized_model_dt.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    print(y_predict)
    xg_score = cls.score(df, df2)
    y_predict = cls.predict(df)
    y_true = df2
    precision, recall, fscore, none = precision_recall_fscore_support(y_true, y_predict, average='weighted')
    context = {
        "accuracy": str(xg_score),
        "precision": str(precision),
        "recall": str(recall),
        "f1score": str(fscore),
    }
    return render(request, "res3.html", context)


def res4(request):
    cls = joblib.load('finalized_model_et.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    print(y_predict)
    xg_score = cls.score(df, df2)
    y_predict = cls.predict(df)
    y_true = df2
    precision, recall, fscore, none = precision_recall_fscore_support(y_true, y_predict, average='weighted')
    context = {
        "accuracy": str(xg_score),
        "precision": str(precision),
        "recall": str(recall),
        "f1score": str(fscore),
    }
    return render(request, "res4.html", context)


def res5(request):
    cls = joblib.load('finalized_model_st.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    print(y_predict)
    xg_score = cls.score(df, df2)
    y_predict = cls.predict(df)
    y_true = df2
    precision, recall, fscore, none = precision_recall_fscore_support(y_true, y_predict, average='weighted')
    context = {
        "accuracy": str(xg_score),
        "precision": str(precision),
        "recall": str(recall),
        "f1score": str(fscore),
    }
    return render(request, "res5.html", context)

def res6(request):
    cls = joblib.load('finalized_model_an.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    print(y_predict)
    xg_score = cls.score(df, df2)
    y_predict = cls.predict(df)
    y_true = df2
    precision, recall, fscore, none = precision_recall_fscore_support(y_true, y_predict, average='weighted')
    context = {
        "accuracy": str(xg_score),
        "precision": str(precision),
        "recall": str(recall),
        "f1score": str(fscore),
    }
    return render(request, "res6.html", context)


def tablexg(request):
    cls = joblib.load('finalized_model_xg.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    y_true = df2
    context = classification_report(y_true, y_predict, output_dict=True)
    df1 = pd.DataFrame(context).transpose()
    df1 = df1.rename({'f1-score' : 'fscore'},axis=1)
    json_records = df1.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'classrep.html', context)

def tabledt(request):
    cls = joblib.load('finalized_model_dt.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    y_true = df2
    context = classification_report(y_true, y_predict, output_dict=True)
    df1 = pd.DataFrame(context).transpose()
    df1 = df1.rename({'f1-score' : 'fscore'},axis=1)
    json_records = df1.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'classrep.html', context)

def tablerf(request):
    cls = joblib.load('finalized_model_rf.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    y_true = df2
    context = classification_report(y_true, y_predict, output_dict=True)
    df1 = pd.DataFrame(context).transpose()
    df1 = df1.rename({'f1-score' : 'fscore'},axis=1)
    json_records = df1.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'classrep.html', context)

def tableet(request):
    cls = joblib.load('finalized_model_et.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    y_true = df2
    context = classification_report(y_true, y_predict, output_dict=True)
    df1 = pd.DataFrame(context).transpose()
    df1 = df1.rename({'f1-score' : 'fscore'},axis=1)
    json_records = df1.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'classrep.html', context)

def tablest(request):
    cls = joblib.load('finalized_model_st.sav')
    df = pd.read_csv('x_test.csv')
    df2 = pd.read_csv('y_test.csv')
    y_predict = cls.predict(df)
    y_true = df2
    context = classification_report(y_true, y_predict, output_dict=True)
    df1 = pd.DataFrame(context).transpose()
    df1 = df1.rename({'f1-score' : 'fscore'},axis=1)
    json_records = df1.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'classrep.html', context)