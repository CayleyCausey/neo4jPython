# neo4jPython

This is a basic API that will allow you to create a connection between Python and a Neo4j database to perform basic operations.

## How to Use

To use this API, you will download the neo4jAPI.py file and upload to your local Python instance. To access the API from your notebook, import the neo4jAPI class using the following line of code:

```python
from neo4jAPI import *
```

## Examples

### Connecting to Neo4j through the API

To create a connection to a neo4j database, create an instance of the neo4jAPI class with the unique bolt driver and credentials for your neo4j instance.

```python
connection = neo4jAPI(URI = "bolt://11.11.11.11:7687", username = "neo4j", password = "password")
```

#### Adding an employee

To add an employee to the database, use neo4jAPI.add_employee(). This function takes an employee name as a string and their employee number as an integer.

```python
connection.add_employee('Gina',2)
```

#### Getting all employees from the database

To see all employees in the database, use neo4jAPI.return_employee(). This function will return all employees in the database.

```python
connection.return_employees()
>Name: Bob 	Employee ID: 1
>Name: Gina 	Employee ID: 2
```
