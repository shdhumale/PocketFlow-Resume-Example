# flow.py
from pocketflow import Flow
from nodes import LoadResumes, AnalyzeResume, GenerateShortlist

def create_resume_flow():
    load = LoadResumes()
    analyze = AnalyzeResume()
    shortlist = GenerateShortlist()

    load >> analyze >> shortlist
    return Flow(start=load)