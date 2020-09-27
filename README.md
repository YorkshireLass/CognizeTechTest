
# Cognize - Coding Challenge for Eigen Technology

Cognize *[verb]*:
> to know or become aware of

This is a Django web application that:
* allows you to upload documents;
* analyses the text within those documents to extract the interesting words; and 
* displays those interesting words and where they were extracted from (sentences and documents). 

By using this app, you will become *cognizant* of your documents.


## How to get up and running

### Run locally

To clone and run this application, you'll need [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/) installed on your computer.

This app was built on a Windows machine and has a SQLite database for ease of transfer. To run the project on Windows do the following in command line:

```bash
# Clone this repository
> git clone https://github.com/YorkshireLass/CognizeTechTest.git

# Activate the virtual environment
> djangovenv\Scripts\activate

# Run the app
> python manage.py runserver
```

### See a running version

A version of this application has also been deployed to PythonAnywhere. This can be accessed [here](http://yorkshirelass.pythonanywhere.com/).

Once loaded, the homepage should appear like this...

![Cognize-Home](./media/images/HomeScreenshot.jpg)



