# nodes.py
from pocketflow import Node, BatchNode
from utils import call_llm
import os

class LoadResumes(Node):
    def post(self, shared, *_):
        data_dir = "data"
        shared["resumes"] = {}
        for file in os.listdir(data_dir):
            with open(os.path.join(data_dir, file), "r") as f:
                shared["resumes"][file] = f.read()
        return "default"

class AnalyzeResume(BatchNode):
    def prep(self, shared):
        return list(shared["resumes"].items())  # [(filename, content), ...]

    def exec(self, item):
        filename, content = item
        prompt = f"""
You are a recruiter. Evaluate this resume and score it from 0 to 10 for the following job:

Job: Data Scientist
Requirements:
- Python and SQL skills
- Experience with ML or Data Analysis
- Clear communication

Resume:
{content}

Return ONLY a score (0-10) and a one-line explanation.
"""
        return filename, call_llm(prompt)

    def post(self, shared, prep_res, exec_res_list):
        shared["results"] = {filename: result for filename, result in exec_res_list}
        return "default"

class GenerateShortlist(Node):
    def prep(self, shared):
        return shared["results"]

    def exec(self, results):
        # Sort by score in the response
        scored = []
        for fname, result in results.items():
            try:
                score = float(result.split()[0])
                scored.append((score, fname, result))
            except:
                pass
        scored.sort(reverse=True)
        return scored[:3]  # top 3 resumes

    def post(self, shared, _, exec_res):
        shared["shortlist"] = exec_res
        return "default"