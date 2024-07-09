FROM ubuntu
RUN apt update && apt install -y python3 
RUN apt install -y python3-pip
RUN pip install -U "ray[data]"  --break-system-packages
