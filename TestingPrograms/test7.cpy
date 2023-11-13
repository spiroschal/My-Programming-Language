def main_finalCodeExample():
#{
    #declare A,B
    #declare C

    def proc(a, b):
    #{
        #declare c
        
        def func():
        #{
            #declare d
            d=4;
            A=B;
            #$B=A; den xreiazetai#$
            print(A);
            return(c+d);
        #}

        #$ body of proc #$
        c=3;
        print(A);
        print(B);
        C=func();
        print(A);
        print(B);
        print(C);

        #$ #$
        return(0);
        #$ #$
    #}

    #$ body of finalCodeExample #$
    A=1;
    B=2;

    #$ call proc(A, B); #$
    C = proc(A, B);

    print(A);
    print(B);
#}

if __name__ == "__main__":
	#$ call of main functions #$
	main_finalCodeExample();