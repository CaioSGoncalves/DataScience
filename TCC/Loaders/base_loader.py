import Collectors.collector as collector

class Loader():   
        modeler = None
        connector = None
        modeled_data = None

        def __init__(self, modeler, connector):
                self.modeler = modeler
                self.connector = connector

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
                modeled_data = self.modeler.model_data(github_profiles, twitter_profiles, query)
                return modeled_data