import json


def load_candidates():
    with open("candidates.json", encoding="utf-8") as f:
         return json.load(f)


def get_all():
    return load_candidates()

def get_by_pk(pk):
    for candidate in load_candidates():
        if candidate["pk"] == pk:
            return candidate
    return

def get_by_skill(skill_name):
    candidates_by_skill = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate["skills"].split(', '):
            candidates_by_skill.append(candidate)
    return candidates_by_skill


