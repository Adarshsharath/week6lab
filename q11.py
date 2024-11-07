feedback = {
    "Work Environment": ["Great work culture", "Need more team activities"],
    "Salary": ["Fair pay, but bonuses are inconsistent"],
    "Management": ["Leadership can improve", "Need more transparency"],
}


theme_to_add = "Work Environment"  
new_feedback = "Love the new office layout!"


if theme_to_add in feedback:
    feedback[theme_to_add].append(new_feedback)
else:
    feedback[theme_to_add] = [new_feedback]  

max_feedback_count = 0
theme_with_most_feedback = ""


for theme, messages in feedback.items():
    if len(messages) > max_feedback_count:
        max_feedback_count = len(messages)
        theme_with_most_feedback = theme


print(f"Updated Feedback Dictionary: {feedback}")


print("\nTheme with the most feedback:")
print(f"Theme: {theme_with_most_feedback}, Number of feedbacks: {max_feedback_count}")

