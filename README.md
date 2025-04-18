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
mention mount!!!!!!!!!!!!!!!!!!!!!!!! <br>
While Container was running, I was able to see the file structure inside the Docker Container.  

##### 6. Issues encountered
Maybe here mention about the mount

##### 8.
Push the Docker image to a container registry. Please create access to a container registry (such as Docker Hub or a private registry), push your Docker image to the registry, and share the tag of this image.




Python code: Submit the Python code script you developed for your chosen project.

Dockerfile: Provide the Dockerfile that you created to package your Python code into a Docker image.

requirements.txt: Include the requirements.txt file that lists the dependencies required by your Python code.

Report/README: Write a report or README file documenting the steps you followed and any additional information about the process.
