import threading
x = 0
flag_x = False

def task1():
	for _ in range(100):
		print("From task1")

def task2():
	for _ in range(100):
		print("From task2")

def increment():
	global x
	x = x + 1


def shared_task():
	global flag_x
	for _ in range(100000):
		#while flag_x:
			#wait = True


		flag_x = True
		increment()
		flag_x = False



if __name__ == "__main__":

	for i in range(10):
		
		x=0

		thrd1 = threading.Thread(target=shared_task)
		thrd2 = threading.Thread(target=shared_task)

		thrd1.start()
		thrd2.start()
		thrd1.join()
		thrd2.join()

		print("Iteration {}:    {}".format(i, x))