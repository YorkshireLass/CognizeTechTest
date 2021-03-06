
# Cognize - Coding Challenge

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

# Change directory
> cd CognizeTechTest

# Activate the virtual environment
> djangovenv\Scripts\activate

# Run the app
> python manage.py runserver
```

### See a running version

A version of this application has also been deployed to PythonAnywhere. This can be accessed [here](http://yorkshirelass.pythonanywhere.com/).

**Note:** PythonAnywhere only allows limited CPU power to be used, so please don't upload too many documents at once or it may break! This isn't a problem when run locally.

## How to use

Once loaded, the homepage should appear like this...

![Cognize-Home](https://github.com/YorkshireLass/CognizeTechTest/blob/master/media/images/CognizeHome.PNG)

Some test documents are located [here](https://github.com/YorkshireLass/CognizeTechTest/blob/master/TestDocs) that can be uploaded. Follow the instructions on the homepage and have fun!



