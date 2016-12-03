book_lowers = {'masha':'tolstoy', 'alexey':'Pelevin', 'victor':'balsak', 'petr':'Cool girl', 'vika':'penthouse'}
user_input = input('Узнай идеального для тебя автора по имени. Как тебя зовут? \n')
user_input = user_input.lower()

def get_answer(bot_answer):
	return book_lowers.get(bot_answer)
	
print(get_answer(user_input))