def main_factorial():
#{
	#$ declarations #$
	#declare x
    #declare i,fact

	#$ body of main_factorial #$
#}

def main_fibonacci():
#{
	#declare x,fact

	def fibonacci(x):
	#{
		#declare y
		def fibonacciINSIDE():
		#{
			#declare a
		#}
	#}

	def fibonacciTWO():
	#{
		#declare z
	#}

	x = int(input());
	fact = 1;
	i = 1 + 2 * 3;
	y = i + (1 + 2 * 3);
	y = -i + (1 + 2 * 3);
	print(fact);
	print(fibonacciTWO(fact,i));
	
	return (fibonacci(x-1)+fibonacci(x-2));
#}

if __name__ == "__main__":
	#$ START call of main functions #$
	main_factorial();
	main_fibonacci();
	#$ END call of main functions #$

