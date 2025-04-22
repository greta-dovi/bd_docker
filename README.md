### Assignment 2
### Creating a Python Code and Packaging it into a Docker Container

##### 1. Choose a Python project
For this project I decided to run a sentiment analysis, since it is closely related with my master thesis topic. Sentiment analysis is a supervised machine learning classification task, used to determine the mood and emotional tone of the message. To implement it for this assignment I used Kindle book reviews dataset.

##### 2. Develop the code
Code development for sentiment analysis can be split into the following parts: <br>
- Data loading and preprocessing (recoding labels, applying regex, removing stop words and lemmatizing)
- Vectorizing data (creating a numeric text representation (vectors). Used Bag of Words and Term frequency - Inverse Document Frequency methods)
- Running supervised ML model and daving the results (Used logistic regression model, results were saved as follows: metrics to .txt file, images to .jpg files)

##### 3. Requirements file
Requirements file was created using pip freeze > requirements.txt command. 

##### 4. Write Dockerfile
Dockerfile was created by specifying all the necessary information, like specifying directory in docker, copying the data and scrip, copying and installing requirements: <br>

FROM python:3.12 <br>
WORKDIR /usr/local/app <br><br>

COPY requirements.txt ./ <br>
RUN pip install --no-cache-dir -r requirements.txt <br><br>

COPY sentiments.py ./<br>
COPY all_kindle_review.csv ./<br><br>

CMD ["python", "sentiments.py"]


##### 5. Build the Docker image and run the Container
Build the Docker image: Use the Docker command-line interface to build the Docker image based on the Dockerfile you created in the previous step. Verify that the image builds successfully without any errors.

Docker image was built using command "build .", which finds the Dockerfile in the current directory and creates a Docker image. <br>
Once the image is created, it appears in docker.desktop app "Images" section. From there I ran the image in the Container. <br>
In the Optional settings amd Volumes section I indicated the path for the results in my computer as well as in Docker Container. <br>
While Container was running, I was able to see the file structure inside the Docker Container.  

##### 6. Issues encountered
There were not many issues in the simple container running process. However, I also wanted to save the generated output file to be saved on the local machine, therefore needed to explore the volumes and mount options. 

##### 7. Container registry
To push my Docker image to a container registry I followed these steps: <br>
docker login <br>
docker images and found my latest image <br>
docker tag b9c75d9245cb (my image) gretadov/sentiment:latest2 (my repository)  <br>
docker push gretadov/sentiment:latest2 <br>
link to copy the Docker image from DockerHub: docker pull gretadov/sentiment:latest2 <br>

