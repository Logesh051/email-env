from tasks import TASKS
from grader import grade

class EmailEnv:
    def __init__(self):
        self.task = None

    def reset(self):
        self.task = TASKS[0]
        return {
            "emails": self.task["emails"],
            "context": self.task["context"]
        }

    def step(self, action):
        correct = self.task["answer"]
        reward = grade(action, correct)
        return {}, reward, True, {}

    def state(self):
        return self.task