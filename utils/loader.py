import time
import sys


def loader_animation(message='Loading...', duration=15):
    print(message)
    animation = [
        "[■□□□□□□□□□□□□□]", "[■■□□□□□□□□□□□□]", "[■■■□□□□□□□□□□□]",
        "[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]",
        "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]",
        "[■■■■■■■■■■■□□□]", "[■■■■■■■■■■■■□□]", "[■■■■■■■■■■■■■□]",
        "[■■■■■■■■■■■■■■]"
    ]
    for i in range(duration):
        time.sleep(0.4)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
