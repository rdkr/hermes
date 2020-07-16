FROM python
RUN apt update && apt install -y protobuf-compiler
RUN pip install grpcio-tools
