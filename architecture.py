"""Source for architecture.png, the architecture diagram."""

import os

from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.compute import KubernetesEngine
from diagrams.gcp.database import SQL
from diagrams.gcp.storage import Storage
from diagrams.onprem.client import Client, User

graph_attr = {
    "label": "",
    "labelloc": "bbc",
    "nodesep": "0.2",
    "pad": "0.2",
    "ranksep": "0.75",
    "splines": "spline",
}

node_attr = {
    "fontsize": "12.0",
}

with Diagram(
        "Butler",
        show=False,
        filename="architecture",
        outformat="png",
        graph_attr=graph_attr,
        node_attr=node_attr,
):
    user = User("End user")
    client = Client("Butler client")

    with Cluster("IDF"):
        butler = KubernetesEngine("Butler server")
        database = SQL("Registry")
        storage = Storage("Object storage")

        user >> client >> butler >> database
        butler >> storage
        client >> Edge(label="signed URL") >> storage
