#defining the base image
FROM python:3.12-alpine

#set the working directory
WORKDIR /app

#copy the contents over
COPY server.py index.html /app/

#expose this port (documentation)
EXPOSE 8000

#the command to run
CMD ["python", "-u", "server.py"]
