import dataclasses


@dataclasses.dataclass
class User:
    repo: str

yurykambur_repo = User(
    repo = "YuryKambur/python_autotests_hw9"
)

eroshenkoam_repo = User(
    repo = "eroshenkoam/allure-example"
)