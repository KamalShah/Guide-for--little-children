def show_all(func):
	def wrapper(*args, **kwargs):
		print("Имя нашей функции:", __name__)
		print("Позиционные аргументы:", args)
		print("Именованные аргументы:", kwargs)
		result = func(*args,**kwargs)
		print("Результат:", result)
		return result
	return wrapper

def summ5(x,y):
	return (x+y)*5

@show_all
def beauty(me):
	print(me ,"Красавчик")

def beauty2(me):
	print(me ,"Кр2савчик")

summ5_beauty = show_all(summ5)

summ5_beauty(5,6)

show_all(beauty)("Магомед")

beauty2(me="Магомед")