from neo4j import GraphDatabase
from app.core.config import settings

class Neo4jConnection:
    def __init__(self):
        self._driver = None

    async def connect(self):
        if not self._driver:
            self._driver = GraphDatabase.driver(
                settings.NEO4J_URI,
                auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD)
            )
        return self._driver

    async def close(self):
        if self._driver:
            await self._driver.close()
            self._driver = None

    async def verify_connectivity(self):
        driver = await self.connect()
        try:
            await driver.verify_connectivity()
            return True
        except Exception as e:
            return False

neo4j_connection = Neo4jConnection() 