import os
import io
import sys

# Disable ANSI colors for web demo
os.environ["ANSI_COLORS_DISABLED"] = "1"

from flask import Flask, Response

from battleships import Board

app = Flask(__name__)


@app.route("/")
def single_shot_demo():
    # Run one-shot demo
    enemy = Board(size=5)
    status, length = enemy.register_shot(0, 0)

    lines = []
    result = f"Shot at (0,0): {status}"
    if status == "sunk":
        result += f" (sunk size {length})"
    lines.append(result)

    lines.append("")  # blank line

    # Capture board display
    buf = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buf
    enemy.display(reveal=False)
    sys.stdout = old_stdout

    lines.append(buf.getvalue())

    text = "\n".join(lines)
    return Response(f"<pre>{text}</pre>", mimetype="text/html")


if __name__ == "__main__":
    # Local dev: listens on port 5000
    app.run(host="0.0.0.0", port=5000)
