import requests
import shutil


def get_image(graph, graph_format="ttl", image_format="jpg"):
    url = "http://www.ldf.fi/service/rdf-grapher"
    data = {
        "rdf":graph.serialize(format=graph_format),
        "from":graph_format,
        "to":image_format}

    response = requests.get(url, params=data, stream=True)

    #print(response.content)
    with open(f"image/graph.{image_format}", 'wb') as file:
        shutil.copyfileobj(response.raw, file)

