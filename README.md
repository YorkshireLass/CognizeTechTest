
# Cognize - Coding Challenge

Cognize *[verb]*:
> to know or become aware of

This is a Django web application that:
* allows you to upload documents;
* analyses the text within those documents to extract the interesting words; and 
* displays those interesting words and where they were extracted from (sentences and documents). 

By using this app, you will become *cognizant* of your documents.


## How to get up and running

Firstly, ensure you have [Git](https://git-scm.com/downloads) installed.

```bash
# Clone this repository
> git clone https://github.com/YorkshireLass/CognizeTechTest.git

# Change directory
> cd CognizeTechTest
```

### If you have Docker installed...

Enter the following in command line/terminal:

```bash
# Build and run the application
> ./dockerbuild.sh
```

### To run on MacOS...

To run this application, you'll need [Python](https://www.python.org/downloads/) installed. Then enter the following in terminal:

```bash
# Activate the virtual environment and run the server
> ./macosbuild.sh
```

### To run on Windows...

To run this application, you'll need [Python](https://www.python.org/downloads/) installed. Then enter the following in command line:

```bash
# Activate the virtual environment and run the server
> ./windowsbuild.sh
```

## How to use

Once loaded, the homepage should appear like this...

![Cognize-Home](https://github.com/YorkshireLass/CognizeTechTest/blob/master/media/images/CognizeHome.PNG)

Some test documents are located [here](https://github.com/YorkshireLass/CognizeTechTest/blob/master/TestDocs) that can be uploaded. Follow the instructions on the homepage and have fun!



