FROM python:3.9-slim

#setting working directory 
WORKDIR /usr/src/app 

#copying contents of the current directory into the container's working 
#dorrectory  
#first dot refers to current directory  
#2nd dot refers to the current working directory into 
COPY . . 

RUN pip install --no-cache-dir -r requirements.txt 

#run 
CMD ["/usr/local/bin/python", "./app.py"]
