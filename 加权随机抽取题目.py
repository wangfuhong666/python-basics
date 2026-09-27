import random

problems = ["2024B", "2023B", "2025B", "2024A", "2023A", "2025A"]
pool = []

for i in range(6):
    pool += [problems[i]] * (60 - i * 10)

random.shuffle(pool)

index = random.randint(0, len(pool) - 1)
print("抽到的题目:", pool[index])