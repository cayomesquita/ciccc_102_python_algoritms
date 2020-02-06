
def score_to_letter_grade(mark):
    result = "F"

    if mark >= 90:
        result = "A"
    elif mark >= 80:
        result = "B"
    elif mark >= 70:
        result = "C"
    elif mark >= 60:
        result = "D"

    return f"Your grade id {result}"

print(score_to_letter_grade(62))
print(score_to_letter_grade(82))
print(score_to_letter_grade(78))
print(score_to_letter_grade(48))
print(score_to_letter_grade(90))
