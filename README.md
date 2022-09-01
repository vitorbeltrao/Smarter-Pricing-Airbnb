# Smarter Pricing

![Airbnb App](https://github.com/vitorbeltrao/Pictures/blob/main/airbnbanalysis.png?raw=true)

## Table of Contents

1. [Installation](#installation)
2. [Project Motivation, Development and Conclusion](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing and Authors](#licensingandauthors)

## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. 
The code should run with no issues using Python versions 3.*.

## Project Motivation, Development and Conclusion<a name="motivation"></a>

**Project Motivation:**

The motivation for this project was to create a web application, to serve as a product both for companies 
(such as Airbnb, which was the example) and for people who want to use the company's service.

The idea was to create an application that has an integrated machine learning system and also an exploratory analysis, 
so that it becomes a very complete product. We don't have to stop there, we can add many things to this application.

***

**Development:**

In this project, we went through several necessary steps of a data science project, which were:

* We address the problem and analyze the big picture (described above in the project motivation).
* We collect data from [Airbnb](http://insideairbnb.com/get-the-data/).
* We did an initial ETL (you can see at ETL notebook).
* We did a quick exploratory data analysis (you can see at EDA notebook)
* We clean and pre-process the data (from there you can at ML notebook).
* We create a baseline model and did many tests with other models.
* We optimize the final model and save the best parameters.
* We evaluate the best model in the test set.
* Finally, we create our web app.

***

**Conclusion:**

We need to improve the performance of the model. To do this, we can perform other iterations and try new 
alternatives for cleaning and pre-processing, feature selection and feature engineering.

But the ultimate goal, which was to create a product for the company or for the users, was successfully completed!

## File Descriptions <a name="files"></a>

We have the following files here:

* One Python file (Hello.py) which makes the structure of the first page web application. 
* A folder (assets) with the images used in the web app.
* A folder (pages) with the other two tabs of our web app.
* A folder (utils) with all the functions needed to make the web app.
* A folder (Notebooks) with the respective notebooks: ETL, EDA and ML.
* Data files such as "listings.csv.gz", "train_set.csv", "test_set.csv".
* A txt file where are all the libraries and their versions needed for the web application to work (requirements.txt).
* A txt file about the license to use the entire project developed (license.txt).
* The pickle file with the best model and its entire execution pipeline, saved.

## Results<a name="results"></a>

The final web application for this job is available at the following link: https://vitorbeltrao-smarter-pricing-airbnb-hello-2b2us0.streamlitapp.com/ 

## Licensing and Authors <a name="licensingandauthors"></a>

Licensing: [MIT license](https://github.com/vitorbeltrao/Image-Classifier/blob/main/license.txt)

Authors: [Vitor Beltrão](https://www.linkedin.com/in/v%C3%ADtor-beltr%C3%A3o-56a912178/)
