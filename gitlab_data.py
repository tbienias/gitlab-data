"""Example script for showing example usage of python-gitlab package."""
import csv
import gitlab


def build_csv(object_list, csv_name):
    """Writes objects in list to CSV."""
    keys = object_list[0].attributes.keys()
    with open(csv_name + '.csv', 'w') as file:
        writer = csv.DictWriter(file, keys)
        writer.writeheader()
        for obj in object_list:
            writer.writerow(obj.attributes)


def main():
    """Main method showing usage of gitlab module."""
    auth_token = 'TOKEN'
    project_id = 12345

    # Establish GitLab connection and get project
    git = gitlab.Gitlab('https://gitlab.com', private_token=auth_token)
    git.auth()
    project = git.projects.get(project_id)

    # Build project member database
    members = project.members.list(all=True)
    users = []
    for member in members:
        users.append(git.users.get(member.id))
    build_csv(members, 'members')
    build_csv(users, 'users')

    # Build issue database
    issues = project.issues.list(all=True)
    build_csv(issues, 'issues')

    # Build note database
    notes = list()
    for issue in issues:
        issue_notes = issue.notes.list(all=True)
        notes += issue_notes  # Merge lists instead of appending
    build_csv(notes, 'notes')

    # Build milestone database
    milestones = project.milestones.list(all=True)
    build_csv(milestones, 'milestones')

    # Build label database
    labels = project.labels.list(all=True)
    build_csv(labels, 'labels')

    # Build commit database
    commits = project.commits.list(all=True)
    build_csv(commits, 'commits')


if __name__ == "__main__":
    main()
