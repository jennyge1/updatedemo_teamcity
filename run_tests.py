import subprocess
import sys

subprocess.run(
    [sys.executable, "-m", "pytest", "tests", "--html=report.html"],
    check=True
)