def main_symbol():
#{
    #$ const A=1; #$
    #declare a,b,c,f1,f2

    def P1(x,y):
    #{
        #declare a
        def F11(x):
        #{
            #declare a
            #$ body of F11 #$
            b = a;
            a = x;
            c = F11(x);
            return (c);
        #}

        def F12(x):
        #{
            #$ body of F12 #$
            c = F11(x);
            return (c);
        #}

        #$ body of P1 #$
        y = x;
        return (y);
    #}

    def P2(x):
    #{
        #declare y
        #$ body of P2 #$
        y = 1;
        y = P1(x,y);
        return (c);
    #}

    #$ main program #$
    f1 = P1(a,b);
    f2 = P2(c);
#}

if __name__ == "__main__":
	#$ call of main functions #$
	main_symbol();