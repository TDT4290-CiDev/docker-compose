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
