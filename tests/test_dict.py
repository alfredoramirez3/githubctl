list_of_dict = [  {
    "id": 443260811,
    "name": "mTLS",
    "url": "https://github.com/haoel/mTLS",
    "description": "golang mTLS example",
    "language": "Go",
    "stars": 213,
    "forks": 32,
    "fork": "False",
    "created_at": "2021-12-31T05:23:42Z"
  },
  {
    "id": 16971588,
    "name": "regression-algorithm",
    "url": "https://github.com/haoel/regression-algorithm",
    "description": "Python  Regression Algorithms",
    "language": "Python",
    "stars": 23,
    "forks": 22,
    "fork": "False",
    "created_at": "2014-02-19T02:39:50Z"
  },
  {
    "id": 16833644,
    "name": "websockify-nginx-module",
    "url": "https://github.com/haoel/websockify-nginx-module",
    "description": "Embed websockify into Nginx",
    "language": "C",
    "stars": 0,
    "forks": 3,
    "fork": "True",
    "created_at": "2014-02-14T10:03:07Z"
  }
]
# repo = list_of_dict[0]
# print(repo)
# # print(list_of_dict.index(repo))
# num_cols = len(repo)
# print([str(i) for i in range(1, num_cols+1)])

for repo in list_of_dict:
    row = (
        [str(list_of_dict.index(repo) + 1)] + [str(r) for r in repo.values()]
    )
    print(*row)






