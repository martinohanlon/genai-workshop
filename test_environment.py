# This will test the environment to ensure that the .env file is set up 
# correctly and that the OpenAI and Neo4j connections are working.
import os
import unittest

from dotenv import load_dotenv
load_dotenv()

class TestEnvironmentVariables(unittest.TestCase):
    def env_variable_exists(self, variable_name):
        self.assertIsNotNone(
            os.getenv(variable_name),
            f"{variable_name} not found in .env file")

    def test_openai_variable(self):
        self.env_variable_exists('OPENAI_API_KEY')
    
    def test_neo4j_variables(self):
        self.env_variable_exists('NEO4J_URI')
        self.env_variable_exists('NEO4J_USERNAME')
        self.env_variable_exists('NEO4J_PASSWORD')
        
class TestLangchainOpenAI(unittest.TestCase):

    def test_openai_connection(self):
            from openai import OpenAI, AuthenticationError

            llm = OpenAI()
            
            try:
                models = llm.models.list()
            except AuthenticationError as e:
                models = None
            self.assertIsNotNone(
                models,
                "OpenAI connection failed. Check your API key in .env file.")
            
class TestNeo4jConnection(unittest.TestCase):

    def test_neo4j_connection(self):
        from neo4j import GraphDatabase

        driver = GraphDatabase.driver(
            os.getenv('NEO4J_URI'),
            auth=(os.getenv('NEO4J_USERNAME'), 
                  os.getenv('NEO4J_PASSWORD'))
        )
        try:
            driver.verify_connectivity()
            connected = True
        except Exception as e:
            connected = False

        driver.close()

        self.assertTrue(
            connected,
            "Neo4j connection failed. Check your NEO4J_URI, NEO4J_USERNAME, and NEO4J_PASSWORD in .env file."
            )


if __name__ == '__main__':
    unittest.main()