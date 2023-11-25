from typing import List

def unique_names(persons: List[List[str]]) -> str:
    all_list = [m for person in persons for m in person]
    all_names_sorted = sorted(set([person.split()[0] for person in all_list]))
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'

def top_3_person(persons: List[List[str]]) -> str:
    all_list = [m for person in persons for m in person]
    names = [person.split()[0] for person in all_list]
    unique_names = set(names)
    popular = [[name, names.count(name)] for name in unique_names]
    popular.sort(key=lambda x:x[1], reverse=True)
    return(f"{popular[0][0]}: {popular[0][1]} раз(а), {popular[1][0]}: {popular[1][1]} раз(а), {popular[2][0]}: {popular[2][1]} раз(а)")

def supre_name(course:  List[str], persons: List[List[str]]) ->  List[str]:
    mentors_names = [set([name[:name.index(' ')]for name in m])for m in persons]
    course_info = [f"На курсах {course[i]} и {course[_]} преподают: \
{', '.join(sorted(mentors_names[_] & mentors_names[i]))}." for i in range(len(course)-1) for _ in range(i+1, len(course))]
    return course_info