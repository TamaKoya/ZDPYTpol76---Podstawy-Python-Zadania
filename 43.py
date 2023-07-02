dict = {"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
ans_1 = dict.get("born")
print(ans_1)

dict["born"] = -428
ans_1 = dict.get("born")
print(ans_1)