Track [X] Challenge [Y]
================


# Setup

## Dependencies

install `renv`:

```
install.packages("renv")
```

### Install/update dependencies
```
renv::restore()
```

### Adding new dependencies
1. install package as usual (with `install.packages`)
2. run `renv::snapshot()`
3. commit and push the updated `renv.lock`

## Access data
To access the data for this challenge, you first need to get secrets/passwords.

To get them, proceed as follows:

1. Check the Slack channel for the "secret link" for your challenge
2. We'll share the password to decrypt the message on-site 
3. Click on the link and enter the password to decrypt the message
4. Follow the specific instructions for your data below.

### Supabase/Postgres

To connect to the Supabase Postgres database, you need to store your credentials in the `.Renviron` file:

```
# set up passwords in .Renviron
usethis::edit_r_environ()
```

Copy the content from the decrypted secret link. It should look something like this:

```
# logins for supabase
SUPAB_NAME='postgres'
SUPAB_HOST='your-supabase-url' 
SUPAB_PORT='5432'
SUPAB_USER='postgres'
SUPAB_PASSWORD='your-supabase-pw'
```

Restart your R session (Session -> Restart R Session or `.rs.restartR()`)

Run `code/00-setup-supabase.R`

### Limesurvey
To access the data from Limesurvey, you need to:

1. connect to the virtual machine/server that Limesurvey is running on. This you do using SSH.
2. then you can connect to the SQL database where the data is stored

To do this, let's first store some information in the `.Renviron` file so that we don't accidentally commit secret information to GitHub:

```
# set up information in .Renviron
usethis::edit_r_environ()
```

Copy the content from the decrypted secret link. It should look something like this:

```
LIMESURVEY_SSH_IP="102.203.20.10"
LIMESURVEY_SSH_USER="user"
LIMESURVEY_SSH_PASSWORD="password"
LIMESURVEY_SQL_USER="test"
LIMESURVEY_SQL_PASSWORD="password"
```

Restart your R session (Session -> Restart R Session or `.rs.restartR()`)

Now you have to create the SSH tunnel - don't worry if you don't know what this means. In essence, it allows us to a) connect from our laptop to the server and then b) use this connection to connect and interact with the Limesurvey database. 

In the R console, run: 

```
glue::glue("ssh -L localhost:5555:127.0.0.1:3306 {ssh_user}@{ssh_ip}")
```

this builds a "tunnel" from your local machine on port 5555 to the port 3306 (the MySQL port) on the server. We can then use port 5555 on our machine to connect and communicate with MySQL.

#### MacOS/Linux/Windows with WSL or working SSH 
If you have:

- MacOS
- Linux
- a Windows machine but have a way to run SSH commands in the console (e.g. in [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install))

Copy the command to your terminal of choice and run it. You'll be prompted to enter a password which you can copy from the `.Renviron` file (`LIMESURVEY_SSH_PASSWORD`)


Once you have successfully opened the connection, run `code/00-setup-limesurvey.R`

:warning: the SSH connection might close after a couple of minutes, so you might have to reconnect in the terminal.

#### Windows 
If you have never worked with SSH before, ask Frie or one of the coaches about it. They'll have a look together with you.

# Developer information
Just kept here for continuing after the hackathon :)

## Definition of Done

Default Definition of Done can be found
[here](https://github.com/CorrelAid/definition-of-done). Adapt if
needed.

