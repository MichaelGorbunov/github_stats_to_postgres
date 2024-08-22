import requests


def get_repos_stats(username):
    """Собирает статистику по репозиториям заданного username на Github"""
    response = requests.get(f'https://api.github.com/users/{username}/repos')
    repos = response.json()
    stats = []
    while True:
        for repo in repos:
            stats.append({
                'name': repo['name'],
                'stars': repo['stargazers_count'],
                'forks': repo['forks_count'],
                'language': repo['language'],
                'updated_at': repo['updated_at']
            })
        if 'next' in response.links:
            response = requests.get(response.links['next']['url'])
            repos = response.json()
        else:
            break
    return stats
