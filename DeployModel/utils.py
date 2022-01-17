import matplotlib.pyplot as plt
import base64
from io import BytesIO
import seaborn as sns

from sklearn.metrics import confusion_matrix

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_png = buffer.getvalue()
    graph = base64.b64encode(img_png)
    print(graph)
    graph = graph.decode('utf-8')
    print(graph)
    buffer.close()
    return graph

def get_plot(x, y):
    plt.switch_backend('AGG')
    cm = confusion_matrix(x, y)
    f, ax = plt.subplots(figsize=(5, 5))
    sns.heatmap(cm, annot=True, linewidth=0.5, linecolor="red", fmt=".0f", ax=ax)
    plt.xlabel("y_pred")
    plt.ylabel("y_true")
    graph = get_graph()
    return graph

