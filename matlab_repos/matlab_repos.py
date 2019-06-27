import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:matlab&sort=stars'
r = requests.get(url)

# 状态码 200表示请求成功
print("Status code:",r.status_code)

response_dict = r.json()
print(response_dict.keys())

print("Total repositories:",response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repositories nums:",len(repo_dicts))

#第一个仓库的信息
# repo_dict = repo_dicts[0]
# print("\nKeys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
# print("Stars:",repo_dict['stargazers_count'])

#***********************************************************
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print("\nName:",repo_dict['name'])
#     print("Owner:", repo_dict['owner']['login'])
#     print("Stars:", repo_dict['stargazers_count'])
#     print("Repository:", repo_dict['html_url'])
#     print("Description:", repo_dict['description'])

#************************************************************
# names, stars = [],[]
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink':repo_dict['html_url'],
    }

    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 30
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = 'GitHub上最受欢迎的matlab项目'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('matlab_repos.svg')