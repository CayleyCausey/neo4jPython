# neo4jPython

This is a basic API that will allow you to create a connection between Python and a Neo4j database to perform basic operations.

## How to Use

To use this API, you will download the neo4jAPI.py file and upload to your local Python instance. To access the API from your notebook, import the neo4jAPI class using the following line of code:

```python
from neo4jAPI import neo4j_API
```

## Examples

### Connecting to Neo4j through the API

To create a connection to a neo4j database, create an instance of the neo4j_API class with the unique bolt driver and credentials for your neo4j instance.

```python
connection = neo4j_API(URI = "bolt://11.11.11.11:7687", username = "neo4j", password = "password")
```

#### Adding an employee

To add an employee to the database, use the method neo4j_API.add_employee(). This method takes an employee name as a string and their employee number as an integer.

```python
connection.add_employee('Gina',2)
```

#### Getting all employees from the database

To see all employees in the database, use the method neo4j_API.return_employee(). This method will return all employees in the database in a json format.

```python
connection.return_employees()
>{'employees': [{'Name': 'Bob', 'Emp_id': '1'},
>{'Name': 'Gina', 'Emp_id': 2}]}
```
