"""
Codeforces Solution Organizer
------------------------------
Sorts solution files (named like '123A.cpp', '1500B2.py', '987C.java')
into topic folders (implementation, greedy, dp, graphs, etc.) based on
each problem's official tags from the Codeforces API.

USAGE:
1. Put this script in the SAME folder as your solution files
   (e.g. alongside 123A.cpp, 24B.py, ...)
2. Run:  python organize_cf_solutions.py
3. It will create topic subfolders and MOVE each file into the
   folder matching its primary tag, then generate a README.md
   with a full table of all problems (name, rating, tags, link).

Requires: pip install requests
"""

import os
import re
import time
import shutil
import requests

# ---- CONFIG ----
SOLUTIONS_DIR = "."          # folder containing your solution files
CF_API_URL = "https://codeforces.com/api/problemset.problems"

# Maps raw Codeforces tags -> a smaller set of clean folder names.
# Feel free to edit this mapping to group things how you like.
TAG_TO_FOLDER = {
    "dp": "dp",
    "dynamic programming": "dp",
    "graphs": "graphs",
    "graph matchings": "graphs",
    "dfs and similar": "graphs",
    "shortest paths": "graphs",
    "trees": "graphs",
    "greedy": "greedy",
    "implementation": "implementation",
    "brute force": "implementation",
    "math": "math",
    "number theory": "math",
    "combinatorics": "math",
    "strings": "strings",
    "string suffix structures": "strings",
    "binary search": "binary-search",
    "two pointers": "two-pointers",
    "sortings": "sorting",
    "data structures": "data-structures",
    "geometry": "geometry",
    "bitmasks": "bitmasks",
    "constructive algorithms": "constructive",
}
DEFAULT_FOLDER = "misc"

# ---- STEP 1: fetch all problem metadata from Codeforces ----
print("Fetching problem tags from Codeforces API...")
resp = requests.get(CF_API_URL, timeout=30)
resp.raise_for_status()
data = resp.json()

if data["status"] != "OK":
    raise RuntimeError(f"CF API error: {data}")

problems = data["result"]["problems"]

# Build a lookup: "123A" -> problem dict
problem_lookup = {}
for p in problems:
    code = f"{p['contestId']}{p['index']}"
    problem_lookup[code] = p

print(f"Loaded {len(problem_lookup)} problems from Codeforces.")

# ---- STEP 2: find ALL solution files, wherever they are ----
# Scans root AND every topic subfolder, so re-running never "loses" files
# that were already sorted in a previous run.
FILENAME_RE = re.compile(r"^(\d+[A-Za-z]\d?)\.(cpp|py|java|c|cc)$", re.IGNORECASE)
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".vscode"}

solution_files = []  # (full_path, filename, code, current_folder_or_None_if_root)
for root, dirs, files in os.walk(SOLUTIONS_DIR):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    rel_root = os.path.relpath(root, SOLUTIONS_DIR)
    for fname in files:
        m = FILENAME_RE.match(fname)
        if m:
            current_folder = None if rel_root == "." else rel_root
            solution_files.append((os.path.join(root, fname), fname, m.group(1).upper(), current_folder))

print(f"Found {len(solution_files)} solution files total (root + subfolders).")

# ---- STEP 3: move any NEW root-level files into a topic folder; ----
# ---- collect README rows for ALL files (old + new) ----
readme_rows = []
not_found = []

for full_path, fname, code, current_folder in solution_files:
    problem = problem_lookup.get(code)
    if not problem:
        not_found.append(fname)
        continue

    tags = problem.get("tags", [])
    rating = problem.get("rating", "N/A")
    name = problem.get("name", "Unknown")

    if current_folder is None:
        # File is loose at root -> figure out its folder and move it
        folder = DEFAULT_FOLDER
        for t in tags:
            if t in TAG_TO_FOLDER:
                folder = TAG_TO_FOLDER[t]
                break
        os.makedirs(os.path.join(SOLUTIONS_DIR, folder), exist_ok=True)
        dest = os.path.join(SOLUTIONS_DIR, folder, fname)
        shutil.move(full_path, dest)
        print(f"  {fname} -> {folder}/ (newly sorted)")
    else:
        # Already sorted in a previous run -> leave it, just record it
        folder = current_folder

    link = f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']}"
    readme_rows.append(
        (code, name, rating, ", ".join(tags), folder, link)
    )

# ---- STEP 4: write README.md summary table ----
readme_path = os.path.join(SOLUTIONS_DIR, "README.md")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write("# Codeforces Solutions\n\n")
    f.write(
        f"{len(readme_rows)}+ Codeforces problems solved as part of ongoing "
        f"competitive programming practice, organized by topic (dynamic "
        f"programming, graphs, greedy, implementation, math, strings, and "
        f"more). This collection reflects consistent algorithmic practice "
        f"built up over my university years, alongside 3 university-level "
        f"programming contest awards.\n\n"
    )
    f.write("| Problem | Name | Rating | Tags | Folder |\n")
    f.write("|---|---|---|---|---|\n")
    for code, name, rating, tags, folder, link in sorted(readme_rows, key=lambda r: r[0]):
        f.write(f"| [{code}]({link}) | {name} | {rating} | {tags} | `{folder}/` |\n")

print(f"\nDone. README.md written with {len(readme_rows)} problems.")
if not_found:
    print(f"\nWARNING: {len(not_found)} files didn't match a known problem "
          f"(check filename format): {not_found}")