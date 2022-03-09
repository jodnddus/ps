from test import check_test_case


def solution(record):
    answer = []
    userDB = dict()
    actions = []

    for log in record:
        info = log.split()
        action, user_id = info[0], info[1]
        if action in ('Enter', 'Change'):
            username = info[2]
            userDB[user_id] = username
        actions.append((action, user_id))

    for (action, user_id) in actions:
        if action == 'Enter':
            answer.append(userDB[user_id] + '님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(userDB[user_id] + '님이 나갔습니다.')

    return answer


check_test_case(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]), ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."])
