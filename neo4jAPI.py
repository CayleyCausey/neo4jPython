#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Neo4j Homework Assignment: REST API
# Created by Cayley Causey 07/15/23

# Importing dependencies
get_ipython().system('pip install neo4j')
from neo4j import GraphDatabase, RoutingControl

# Defining the API class
class neo4jAPI:
    
    ## Setting up the connection details ##
    def __init__(self, URI, username, password):
        
        self.__URI = URI
        self.__username = username
        self.__password = password
    
        # Setting up the connection or, if failed, returning the error to the client
        try:
            self.__driver = GraphDatabase.driver(self.__URI,auth=(self.__username,self.__password))
        except Exception as error:
            print('Driver failed with the following error: ', error)
    
    ## Database manipulation functions ##
    
    def add_employee(self, name:str, emp_id:int):
        '''
        This function creates a new employee node in the database.
        This function expects two employee attributes: a name (string) and an employee id (int).
        '''
        try:
            self.__driver.execute_query(
                "CREATE (a:Employee {name: $name,emp_id:$emp_id}) ",
                name=name, emp_id=emp_id, database_="neo4j",
            )
        except NameError as error:
            print('Driver unable to locate database.')
        except Exception as error:
            print('Query failed with the following error: ', error)
        
    def return_employees(self):
        '''
        This function prints all employees from the database.
        '''
        try:
            records, _, _ = self.__driver.execute_query(
                "MATCH (a:Employee)"
                "RETURN a.name,a.emp_id",
                database_="neo4j", routing_=RoutingControl.READ,
            )
            for record in records:
                print(f'Name: {record["a.name"]} \tEmployee ID: {record["a.emp_id"]}')
        except NameError as error:
            print('Driver unable to locate database.')
            

