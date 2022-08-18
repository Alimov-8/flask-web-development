`A version control` -  system is a tool that records changes in files over time. allows to
revert to an earlier version of the file and identify bugs more easily. You can test new ideas
without fear of breaking your current code, and your team can work using a predefined
workflow without stepping on each others' toes. Git was developed by Linus Torvalds

`Python package manager` - installing third-party libraries can be a huge pain to do correctly. Package X relies on package Y, which in turn relies on Z and Q. (solution for it is Python package manager)

`requirements file and separate virtual envs` - helps us to run different projects which requires different versions of packages in same machine.

    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

    # Windows OS:
    > python -m venv venv
    > venv\Scripts\activate.bat
    > pip install -r requirements.txt


`Docker` - With Docker, you define all of your application components and how to install
and configure them, and you can then share your stack with your team, and send it to
production with the exact same specification

`Dockerfile` - file defines how to set up your application

        FROM python:3.6.5
        # Set the working directory to /app
        WORKDIR /app
        # Copy local contents into the container
        ADD . /app
        # Install all required dependencies
        RUN pip install -r requirements.txt
        EXPOSE 5000
        CMD ["python", "main.py"]

`Image and Running state of image is container` 

    $ docker build -t chapter_1 .
    $ docker run -p 5000:5000 chapter_1
    # List all the running containers
    $ docker container list

### Project structure

`Dockerfile` # Instructions to configure and run our application on a
container

`requirements.txt` # All the dependencies needed to run our application

`/venv` # virtualenv

`.gitignore` # Instruction for Git to ignore files

`main.py` # main Flask application

`config.py` # configuration file (Prod, Dev)