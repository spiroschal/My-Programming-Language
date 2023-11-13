def main_small():
#{
    #$ const A:=1; #$
    #declare b,g,f

    def P1(X, Y):
    #{
        #declare e,f

        def P11(X):
        #{ #declare e
            e=1;
            X=Y;
            f=b;
            return(e);
        #}
        #$ code for P1 #$
        b=X;
        e=P11(X);
        e=P1(X, Y);
        X=b;
        return(e);
    #}
    
    #$ code for main #$
    if (b>1 and f<2 or g+1<f+b):
    #{
        f=P1(g);
    #}
    else:
    #{
        f=1;
    #}
#}

if __name__ == "__main__":
	#$ call of main functions #$
	main_small();
