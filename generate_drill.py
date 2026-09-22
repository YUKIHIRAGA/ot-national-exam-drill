import argparse
import csv
import random


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=3)
    args = parser.parse_args()

    with open("sample_questions.csv", "r", encoding="utf-8-sig") as f:
        questions = list(csv.DictReader(f))

    if not questions:
        print("No questions found.")
        return

    count = min(args.count, len(questions))
    selected = random.sample(questions, count)

    question_fields = [
        "id",
        "category",
        "question",
        "option1",
        "option2",
        "option3",
        "option4",
        "option5",
    ]

    with open("drill.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=question_fields)
        writer.writeheader()
        for q in selected:
            writer.writerow({key: q.get(key, "") for key in question_fields})

    with open("answer_key.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "answer"])
        writer.writeheader()
        for q in selected:
            writer.writerow({
                "id": q.get("id", ""),
                "answer": q.get("answer", "")
            })

    print(f"Generated {count} questions.")
    print("Created: drill.csv")
    print("Created: answer_key.csv")


if __name__ == "__main__":
    main()
