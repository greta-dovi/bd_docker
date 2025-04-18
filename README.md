### Assignment 2
### Creating a Python Code and Packaging it into a Docker Container

##### 1. Choose a Python project
For this project I decided to run a sentiment analysis, since it is closely related with my master thesis topic. Sentiment analysis is a supervised machine learning classification task, used to determine the mood and emotional tone of the message. To implement it for this assignment I used Kindle book reviews dataset.

##### 2. Develop code
Develop the Python code: Write the necessary Python code to implement the functionality of your chosen project. Ensure that the code is well-structured, follows best practices, and is adequately commented.
Code development for sentiment analysis can be split into the following parts: <br>
- Data loading and preprocessing (recoding labels, applying regex, removing stop words and lemmatizing)
- Vectorizing data (creating a numeric text representation (vectors). Used Bag of Words and Term frequency - Inverse Document Frequency methods)
- Running supervised ML model and daving the results (Used logistic regression model, results were saved as follows: metrics to .txt file, images to .jpg files)
##### 3. Requirements file
Create a requirements.txt file: Identify the external libraries or dependencies that your Python code relies on. Create a requirements.txt file listing all the dependencies along with their versions. This file will be used later to install the dependencies inside the Docker container.

##### 4. Set up Docker
Set up a Docker environment: Install Docker on your machine if you haven't already. Familiarize yourself with Docker commands and concepts such as images, containers, and Dockerfiles.

##### 5. Write Dockerfile
Write a Dockerfile: Create a Dockerfile, which is a text file that contains instructions to build a Docker image. Specify the base image, copy the Python code and the requirements.txt file into the image, and define any necessary configurations or environment variables.

##### 6. Build the Docker image
Build the Docker image: Use the Docker command-line interface to build the Docker image based on the Dockerfile you created in the previous step. Verify that the image builds successfully without any errors.

##### 7. Test the Docker image
Test the Docker image: Create and run a Docker container from the image you built. Ensure that the container starts up correctly and that your Python code functions as expected within the container.

##### 8. 
Document the process: Write a brief report or README file documenting the steps you followed to create the Docker image. Include any relevant information, such as the Dockerfile contents, the commands used to build and run the image, and any issues you encountered during the process.

##### 9.
Push the Docker image to a container registry. Please create access to a container registry (such as Docker Hub or a private registry), push your Docker image to the registry, and share the tag of this image.




Python code: Submit the Python code script you developed for your chosen project.

Dockerfile: Provide the Dockerfile that you created to package your Python code into a Docker image.

requirements.txt: Include the requirements.txt file that lists the dependencies required by your Python code.

Report/README: Write a report or README file documenting the steps you followed and any additional information about the process.
