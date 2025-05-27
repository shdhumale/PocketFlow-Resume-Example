# main.py
from flow import create_resume_flow

def main():
    shared = {}
    flow = create_resume_flow()
    flow.run(shared)

    print("\n--- SHORTLIST ---")
    for score, fname, explanation in shared["shortlist"]:
        print(f"{fname}: {score}/10 – {explanation}")

if __name__ == "__main__":
    main()