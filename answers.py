chat = {'привет':'И тебе привет!', 'как дела': 'лучше всех', 'пока':'увидимся'}
user_input = input('привет!\n')
user_input = user_input.lower()

def get_answer():
	return chat.get(user_input)

print(get_answer(user_input))
