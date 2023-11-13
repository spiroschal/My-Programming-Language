def main_symbol():
#{
    #declare a,i

    def P1(x):
    #{
        def F11(xx):
        #{
            #$ body of F11 #$
            return (xx);
        #}

        def F12():
        #{
            #declare y
            #$ body of F12 #$
            y=5;
            return (F11(x));
        #}

        #$ body of P1 #$
        return (F12());
    #}

    #$ main program #$
    i = 11;
    a = P1(i);
    print(a);
#}

if __name__ == "__main__":
	#$ call of main functions #$
	main_symbol();