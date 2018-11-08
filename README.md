# CiDev Citizen Developer Platform

This repository contains the `docker-compose` file necessary to build and run the CiDev application, along with a
convenience script to fetch all necessary repositories at once.

# Installation

1. Make sure that [Docker](https://www.docker.com/get-started) is installed on your computer.
2. Clone this repository. (Preferably clone it into an empty parent directory, as the entire project requires quite a
few repositories, each constituting an additional folder.)
3. Clone all the other repositories. If you have Python installed, this can be done quite easily by running the
`pull_all_repos.py` script.
4. Open a terminal window in the `docker-compose` folder, and build the project by running `docker-compose build`. This
will take some time the first time you build, but subsequent builds will go quicker due to caching.
5. Run `docker-compose up` to start the application. It is configured to bind to port 8080, and should be available at
`localhost:8080` after successfully booting. If you want the server to continue running after closing the terminal, you
can instead run `docker-compose up -d`. The `-d` flag starts the application detached from the current terminal.

## Set environment variables
Some services need additional environment variables. These should be set in the .env-file.

If no such file exist, docker-compose will not run. To build the system without any environment variables, create an empty .env-file

Mac/Linux:
```cp example.env .env```

Windows:
```copy example.env .env```

The example-file is filled with nonsense variables. This is done to not track sensitive information in the git-repo. Replace it with the necessary information.

In particular, the `send_mail` block of the `WorkflowBlockService` requires an NTNU username and password to be set in
order to send mails. Note also that the server used is only available from within the NTNU network.
