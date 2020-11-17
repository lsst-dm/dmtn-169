"""Source for architecture.png, the architecture diagram."""

import os

from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.compute import KubernetesEngine
from diagrams.gcp.database import SQL
from diagrams.gcp.storage import Storage
from diagrams.onprem.client import Client, User

os.chdir(os.path.dirname(__file__))

graph_attr = {
    "label": "",
}

with Diagram(
        "Butler",
        show=False,
        filename="architecture",
        outformat="png",
        graph_attr=graph_attr,
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
