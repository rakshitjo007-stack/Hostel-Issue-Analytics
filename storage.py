import json
import os

FILE_PATH = "data/issues.json"


def save_issues(issues):
    file = open(FILE_PATH, "w")
    json.dump(issues, file, indent=4)
    file.close()


def load_issues():
    if os.path.exists(FILE_PATH):
        file = open(FILE_PATH, "r")
        issues = json.load(file)
        file.close()
        return issues

    return []