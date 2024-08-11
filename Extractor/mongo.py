from pymongo import MongoClient, errors


class MongoExtractor:

    def __init__(self, client: str = 'localhost:27017'):
        try:
            self.client = MongoClient(client)
        except errors.ConnectionError as e:
            print(f"Could not connect to MongoDB: {e}")
            raise


    def extract(self, db_name, collection_name, query = None, projection = None):
        """
        Extracts data from the specified collection based on the given query.

        :param db_name: Name of the database to connect to.
        :param collection_name: Name of the collection within the database.
        :param query: A dictionary representing the MongoDB query.
        :return: A list of documents that match the query.
        """
        try:
            db = self.client[db_name]
            collection = db[collection_name]

            if query is None:
                query = {}
            if projection is None:
                projection = {}

            # Perform the query and return the results as a list.
            results = collection.find(query, projection)
            return list(results)

        except errors.PyMongoError as e:
            print(f"An error occurred while extracting data: {e}")
            return []


    def close(self):
        """
        Closes the MongoDB client connection.
        """
        self.client.close()
