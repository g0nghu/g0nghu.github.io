"""Monitor the latest GitHub Actions workflow run and display progress."""
import json
import time
import urllib.request
import ssl
import sys

REPO = "g0nghu/g0nghu.github.io"
API = f"https://api.github.com/repos/{REPO}/actions"

# SSL workaround for restricted networks
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def api(url):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "hugo-deploy-monitor/1.0",
        "X-GitHub-Api-Version": "2022-11-28"
    })
    with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
        return json.loads(r.read())

def status_icon(status, conclusion):
    icons = {
        "queued": "⏳", "in_progress": "🔄", "waiting": "⏸ ",
        "completed": "✅" if conclusion == "success" else "❌" if conclusion == "failure" else "⚠️ ",
        "skipped": "⏭ ", "cancelled": "🚫"
    }
    return icons.get(status, "❓")

def main():
    print()

    # Get the latest workflow run (triggered by our push)
    try:
        data = api(f"{API}/runs?per_page=1&event=push")
        if not data["workflow_runs"]:
            print("No workflow runs found. Check the Actions tab manually.")
            return
        run = data["workflow_runs"][0]
    except Exception as e:
        print(f"Cannot access GitHub API: {e}")
        print("Check status at: https://github.com/g0nghu/g0nghu.github.io/actions")
        return

    run_id = run["id"]
    run_url = run["html_url"]
    print(f"Workflow: {run['name']}  |  {run_url}")
    print()

    # Poll until completion
    last_jobs_state = ""
    while True:
        try:
            run_data = api(f"{API}/runs/{run_id}")
            jobs_data = api(f"{API}/runs/{run_id}/jobs")
        except Exception:
            time.sleep(3)
            continue

        status = run_data["status"]
        conclusion = run_data.get("conclusion")

        # Build job status lines
        lines = []
        for job in jobs_data["jobs"]:
            icon = status_icon(job["status"], job.get("conclusion"))
            name = job["name"]
            for step in job.get("steps", []):
                if step["status"] == "in_progress":
                    lines.append(f"  {icon} {name}: {step['name']}")
                    break
            else:
                job_icon = status_icon(job["status"], job.get("conclusion"))
                lines.append(f"  {job_icon} {name}")

        current_state = "\n".join(lines)
        if current_state != last_jobs_state:
            # Clear and redraw
            icon = status_icon(status, conclusion)
            print(f"\033[2J\033[H{icon} Status: {status}")  # Clear screen
            print(current_state)
            last_jobs_state = current_state

        if status == "completed":
            print()
            if conclusion == "success":
                print("✅ Deploy successful! https://g0nghu.github.io/")
            else:
                print(f"❌ Deploy failed: {conclusion}")
                print(f"Details: {run_url}")
            break

        time.sleep(3)

if __name__ == "__main__":
    main()
