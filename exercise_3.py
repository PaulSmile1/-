def appearance(intervals):
    LESSON_START = intervals["lesson"][0]
    LESSON_END = intervals["lesson"][1]

    def calc_start_time(list_1, list_2, list_3, list_4):
        for time in list_1:
            index_time = list_1.index(time)
            new_time = list_2[index_time]
            if time <= LESSON_START < new_time:
                list_3.append(LESSON_START)
            elif LESSON_START <= time < LESSON_END:
                list_3.append(time)
            elif LESSON_END <= time:
                list_4.append(time)
            else:
                pass
        list_3 = [item for item in list_3 if item not in list_4]
        return list_3

    def calc_end_time(list_1, list_2, list_3):
        for time in list_1:
            index_time = list_1.index(time)
            new_time = list_2[index_time]
            if LESSON_START < time <= LESSON_END:
                list_3.append(time)
            elif new_time < LESSON_END < time:
                list_3.append(LESSON_END)
            else:
                pass
        return list_3


    sum_index_pupil = len(intervals["pupil"])
    pupil_start = []
    pupil_end = []

    for n in range(sum_index_pupil):
        if n % 2 == 0:
            pupil_start.append(intervals["pupil"][n])
        else:
            pupil_end.append(intervals["pupil"][n])

    pupil_start_lesson = []
    pupil_time_delete = []
    calc_start_time(list_1=pupil_start, list_2=pupil_end, list_3=pupil_start_lesson, list_4=pupil_time_delete)

    pupil_end_lesson = []
    calc_end_time(list_1=pupil_end, list_2=pupil_start, list_3=pupil_end_lesson)

    correct_start_time = []
    correct_end_time = []
    first_start_item = pupil_start_lesson[0]
    first_end_item = pupil_end_lesson[0]
    for item in pupil_start_lesson:
        index_new_item = pupil_start_lesson.index(item)
        new_end_item = pupil_end_lesson[index_new_item]
        if item >= first_end_item:
            correct_end_time.append(first_end_item)
            first_start_item = item
            first_end_item = new_end_item
            if item <= first_start_item:
                if new_end_item >= first_end_item:
                    correct_start_time.append(item)
                    first_start_item = item
                    first_end_item = new_end_item
                else:
                    correct_start_time.append(item)
                    first_start_item = item
            else:
                if new_end_item >= first_end_item:
                    first_end_item = new_end_item
                else:
                    pass
        else:
            if item <= first_start_item:
                if new_end_item >= first_end_item:
                    correct_start_time.append(item)
                    first_start_item = item
                    first_end_item = new_end_item
                else:
                    correct_start_time.append(item)
                    first_start_item = item
            else:
                if new_end_item >= first_end_item:
                    first_end_item = new_end_item
    correct_end_time.append(first_end_item)

    sum_index_tutor = len(intervals["tutor"])
    tutor_start = []
    tutor_end = []

    for n in range(sum_index_tutor):
        if n % 2 == 0:
            tutor_start.append(intervals["tutor"][n])
        else:
            tutor_end.append(intervals["tutor"][n])

    tutor_start_lesson = []
    tutor_time_delete = []
    calc_start_time(list_1=tutor_start, list_2=tutor_end, list_3=tutor_start_lesson, list_4=tutor_time_delete)

    tutor_end_lesson = []
    calc_end_time(list_1=tutor_end, list_2=tutor_start, list_3=tutor_end_lesson)

    common_start = []
    for st_time in correct_start_time:
        index_item1 = correct_start_time.index(st_time)
        st_end_time = correct_end_time[index_item1]
        for th_time in tutor_start_lesson:
            index_item2 = tutor_start_lesson.index(th_time)
            th_end_time = tutor_end_lesson[index_item2]
            if th_time <= st_time:
                if st_time < th_end_time:
                    common_start.append(st_time)
                else:
                    pass
            else:
                if th_time < st_end_time:
                    common_start.append(th_time)

    common_end = []
    for st_exit in correct_end_time:
        index_time = correct_end_time.index(st_exit)
        st_start_time = correct_start_time[index_time]
        for th_exit in tutor_end_lesson:
            th_index_time = tutor_end_lesson.index(th_exit)
            th_start_time = tutor_start_lesson[th_index_time]
            if th_exit >= st_exit:
                if th_start_time <= st_exit:
                    common_end.append(st_exit)
                else:
                    pass
            else:
                if st_start_time <= th_exit:
                    common_end.append(th_exit)
                else:
                    pass

    answer = 0
    for i in common_start:
        index = common_start.index(i)
        n = common_end[index]
        result = n - i
        answer += result

    return answer

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
