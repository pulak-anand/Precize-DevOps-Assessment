# Precize-DevOps-Assessment

To create a Docker container that fetches data from the Hugging Face model hub, compiles a list of the top 10 downloaded models, and stops after generating reports, you can follow these steps:

1. Run the following command in the directory where your Dockerfile and Python script are located:
   "docker build -t huggingface-report".
2. Once the image is built, you can run the Docker container using the following command:
   "docker run --rm huggingface-report"

