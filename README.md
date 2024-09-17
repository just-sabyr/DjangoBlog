# Web Blog using Django 5
Taken from the book Django5 by Example

# Clone the repository
```
    
```

# Install the required Python libraries
```bash
    python -m pip install requirements.py
```

# Install PostgreSQL docker image
```bash
    docker pull postgres:16.2
```

# Start the PostgreSQL Server 
    - RUN this if for the first time
```bash
    docker run --name=blog_db -e POSRGRES_DB=blog -e POSTGRES_USER=blog -e POSTGRES_PASSWORD=xxxxx -p 5432:5432 -d postgres:16.2
```
    - RUN the following snippet if you had already run the previously (you have a docker container named *blog_db*)
```bash
    docker start blog_db
```

# Create .env file and Store your sensitive env variables (secrets) there (example file is env)
```bash
    touch .env
```

# Make migrations & migrate
```bash
    python manage.py makemigrations
    python manage.py migrate
```

# Load sample data from a fixture 
```bash
    python manage.py loaddata mysite_data.json
```
