
def model_data(github_profiles, twitter_profiles, query):
    values_dict = dict()
    user_data = list()
    for github_login, _ in github_profiles.items():
        user = dict()
        user['_id'] = github_profiles[github_login]['id']
        user['github_login'] = github_login
        user['have_twitter'] = github_profiles[github_login]['have_twitter']
        user['twitter_collected'] = github_login in twitter_profiles.keys()
        user['github'] = github_profiles[github_login]
        user['twitter'] = twitter_profiles.get(github_login)
        user['tag'] = query
        user_data.append(user)
    values_dict['user'] = user_data  
    return values_dict