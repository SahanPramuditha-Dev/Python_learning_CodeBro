def day_of_the_week(day):
    if day == "Monday" or day == 1:
        return "Monday is the first day of the week.It is associated with the moon and is often considered a day for new beginnings and fresh starts."
    elif day == "Tuesday" or day == 2:
        return "Tuesday is the second day of the week. It is named after the Norse god Tyr and is often associated with energy, action, and determination."
    elif day == "Wednesday" or day == 3:
        return "Wednesday is the third day of the week. It is named after the Norse god Odin and is often associated with communication, learning, and wisdom."
    elif day == "Thursday" or day == 4:
        return "Thursday is the fourth day of the week. It is named after the Norse god Thor and is often associated with strength, protection, and good fortune."
    elif day == "Friday" or day == 5:
        return "Friday is the fifth day of the week. It is named after the Norse goddess Frigg and is often associated with love, beauty, and creativity."
    elif day == "Saturday" or day == 6:
        return "Saturday is the sixth day of the week. It is named after the Roman god Saturn and is often associated with rest, relaxation, and leisure."
    elif day == "Sunday" or day == 7:
        return "Sunday is the seventh day of the week. It is named after the sun and is often associated with warmth, light, and positivity."
    else:
        return "Invalid input. Please enter a valid day of the week (e.g., 'Monday' or 1)."

day = int(input("Enter a day of the week (e.g., 'Monday' or 1): "))
result = day_of_the_week(day)
print(result)


def day_of_the_week(day):
    match day:
        case "Monday" | 1:
            return "Monday is the first day of the week.It is associated with the moon and is often considered a day for new beginnings and fresh starts."
        case "Tuesday" | 2:
            return "Tuesday is the second day of the week. It is named after the Norse god Tyr and is often associated with energy, action, and determination."
        case "Wednesday" | 3:
            return "Wednesday is the third day of the week. It is named after the Norse god Odin and is often associated with communication, learning, and wisdom."
        case "Thursday" | 4:
            return "Thursday is the fourth day of the week. It is named after the Norse god Thor and is often associated with strength, protection, and good fortune."
        case "Friday" | 5:
            return "Friday is the fifth day of the week. It is named after the Norse goddess Frigg and is often associated with love, beauty, and creativity."
        case "Saturday" | 6:
            return "Saturday is the sixth day of the week. It is named after the Roman god Saturn and is often associated with rest, relaxation, and leisure."
        case "Sunday" | 7:
            return "Sunday is the seventh day of the week. It is named after the sun and is often associated with warmth, light, and positivity."
        case _:
            return "Invalid input. Please enter a valid day of the week (e.g., 'Monday' or 1)."
        

day = int(input("Enter a day of the week (e.g., 'Monday' or 1): "))
result = day_of_the_week(day)
print(result)