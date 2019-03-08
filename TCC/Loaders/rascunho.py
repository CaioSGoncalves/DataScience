import Collectors.collector as collector
from DataModelers import mongo_modeler,mysql_modeler
import Connectors
from Connectors import mongo_connector,mysql_connector

class Loader():
        def __init__(self, host_name, database):
                self.modelers = dict()
                self.modelers['mongo'] = mongo_modeler
                self.modelers['mysql'] = mysql_modeler

                self.connectors = dict()
                self.connectors['mongo'] = mongo_connector.MongoDB_Connector('localhost')
                self.connectors['mysql'] = mysql_connector.MySQL_Connector('localhost')

                self.database = database
                self.host_name = host_name

        def collect_data(self, query, number_of_pages):
                repositories = collector.collect_repositories(query, number_of_pages)
                print('Number of Repositories Collected: ', len(repositories))
                github_profiles, github_with_twitter = collector.collect_contributors(repositories)
                print('Number of GitHub Users Collected: ', len(github_profiles))
                print('Number of GitHub Users with Twitter Collected: ', len(github_with_twitter))
                twitter_profiles = collector.collect_twitter_data(github_with_twitter)
                self.modeled_data = self.model_data(github_profiles, twitter_profiles, query)

        def model_data(self, github_profiles, twitter_profiles, query):
                print('Modeling data')
                modeled_data = self.modelers[self.database].model_data(github_profiles, twitter_profiles, query)
                return modeled_data

        def insert_data(self, db_name):
                for col_name, values in self.modeled_data.items():
                        print('Inserting ' + col_name)
                        self.connectors[self.database].bulk_upsert_many(db_name, col_name, values)