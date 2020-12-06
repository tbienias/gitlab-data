# GitLab Data #

Scraping GitLab Data using Python.
This example Python script shows the usage of `python-gitlab` module and
serves as supplementary material to my blog post about scraping data from
GitLab:
https://github.com/tbienias/blog/blob/master/posts/gitlab-data-scraping.md

## Usage ##

In `gitlab_data.py` change variables `auth_token` and `project_id` to your
corresponding authentication token obtained from GitLab and project ID of the
project you want to analyze.

```bash
pip install python-gitlab
python gitlab_data.py
```

## License ##

MIT
