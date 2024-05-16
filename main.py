from diagrams import Diagram

from diagrams.aws.analytics import *
from diagrams.aws.ar import *
from diagrams.aws.blockchain import *
from diagrams.aws.business import *
from diagrams.aws.compute import *
from diagrams.aws.cost import *
from diagrams.aws.database import *
from diagrams.aws.devtools import *
from diagrams.aws.enablement import *
from diagrams.aws.enduser import *
from diagrams.aws.engagement import *
from diagrams.aws.game import *
from diagrams.aws.general import *
from diagrams.aws.integration import *
from diagrams.aws.iot import *
from diagrams.aws.management import *
from diagrams.aws.media import *
from diagrams.aws.migration import *
from diagrams.aws.ml import *
from diagrams.aws.mobile import *
from diagrams.aws.network import *
from diagrams.aws.quantum import *
from diagrams.aws.robotics import *
from diagrams.aws.satellite import *
from diagrams.aws.security import *
from diagrams.aws.storage import *

import gradio as gr

from fastapi import FastAPI

def generate_diagram(architecture):
    architecture = "with Diagram('Generated Diagram', show=False):\n\t{}".format(architecture)
    exec(architecture)
    return "generated_diagram.png"

iface = gr.Interface(
    generate_diagram,
    gr.Textbox(lines=3, placeholder="Enter architecture:\nELB(\"lb\") >> [EC2(\"worker1\"), EC2(\"worker2\"), EC2(\"worker3\")] >> RDS(\"events\")"),
    gr.Image(type="filepath", label="Diagram"),
    title="AWS Architecture Diagram Generator",
    description="Enter the architecture in the format:\nELB(\"lb\") >> [EC2(\"worker1\"), EC2(\"worker2\"), EC2(\"worker3\")] >> RDS(\"events\")",
    allow_flagging="never"
)

# Create FastAPI app
app = FastAPI()

# Mount Gradio app
app = gr.mount_gradio_app(app, iface, path="/aws_architecture_diagram_generator")

@app.get("/")
def read_root():
    return {"message": "AWS architecture diagram generator is running at /aws_architecture_diagram_generator"}
