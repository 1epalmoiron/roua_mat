#-*- encoding:utf-8 -*-
from pieces import *

class Chessboard:
    def __init__(self):
        grammi1= [" "," "," "," "," "," "," "," "]
        grammi2= [" "," "," "," "," "," "," "," "]
        grammi3= [" "," "," "," "," "," "," "," "]
        grammi4= [" "," "," "," "," "," "," "," "]
        grammi5= [" "," "," "," "," "," "," "," "]
        grammi6= [" "," "," "," "," "," "," "," "]
        grammi7= [" "," "," "," "," "," "," "," "]
        grammi8= [" "," "," "," "," "," "," "," "]
        self.board=[grammi1,grammi2,grammi3,grammi4,
        grammi5,grammi6,grammi7,grammi8]
        
    def prepare(self):
        K=King("white")
        K.row =1 
        K.col =5

        Q=Queen("white")
        Q.row=1
        Q.col=4

        B=Bishop("white")
        B.row=1
        B.col=6

        B2=Bishop("white")
        B2.row=1
        B2.col=3

        N=Knight("white")
        N.row=1
        N.col=7

        N2=Knight("white")
        N2.row=1
        N2.col=2

        R=Rook("white")
        R.row=1
        R.col=1

        R2=Rook("white")
        R2.row=1
        R2.col=8

        P=pawn("white")
        P.row=2
        P.col=1

        P2=pawn("white")
        P2.row=2
        P2.col=2

        P3=pawn("white")
        P3.row=2
        P3.col=3

        P4=pawn("white")
        P4.row=2
        P4.col=4

        P5=pawn("white")
        P5.row=2
        P5.col=5

        P6=pawn("white")
        P6.row=2
        P6.col=6

        P7=pawn("white")
        P7.row=2
        P7.col=7

        P8=pawn("white")
        P8.row=2
        P8.col=8

        k=King("black")
        k.row=8
        k.col=5

        q=Queen("black")
        q.row=8
        q.col=4

        b=Bishop("black")
        b.row=8
        b.col=6

        b2=Bishop("black")
        b2.row=8
        b2.col=3

        n=Knight("black")
        n.row=8
        n.col=7

        n2=Knight("black")
        n2.row=8
        n2.col=2

        r=Rook("black")
        r.row=8
        r.col=1

        r2=Rook("black")
        r2.row=8
        r2.col=8

        p=pawn("black")
        p.row=7
        p.col=1

        p2=pawn("black")
        p2.row=7
        p2.col=2

        p3=pawn("black")
        p3.row=7
        p3.col=3

        p4=pawn("black")
        p4.row=7
        p4.col=4

        p5=pawn("black")
        p5.row=7
        p5.col=5

        p6=pawn("black")
        p6.row=7
        p6.col=6

        p7=pawn("black")
        p7.row=7
        p7.col=7

        p8=pawn("black")
        p8.row=7
        p8.col=8


        self.place(K)
        self.place(Q)
        self.place(B)
        self.place(N)
        self.place(R)
        self.place(P)
        self.place(B2)
        self.place(N2)
        self.place(R2)
        self.place(P2)
        self.place(P3)
        self.place(P4)
        self.place(P5)
        self.place(P6)
        self.place(P7)
        self.place(P8)

        self.place(k)
        self.place(q)
        self.place(b)
        self.place(n)
        self.place(r)
        self.place(p)
        self.place(b2)
        self.place(n2)
        self.place(r2)
        self.place(p2)
        self.place(p3)
        self.place(p4)
        self.place(p5)
        self.place(p6)
        self.place(p7)
        self.place(p8)

    
    def place(self, k):
        self.board[k.row-1][k.col-1] = k
        
    #def move(self, acol, arow, tcol, trow):
    def move(self, apopou, pros, xroma):
        apopou=apopou.replace(' ','')
        pros=pros.replace(' ','')
        acol=ord(apopou[0])-ord("a")
        if apopou[1]<'0' or apopou[1]>'9':
            print 'Λαθος κινηση'
            return False
        arow=int(apopou[1])-1
        tcol=ord(pros[0])-ord("a") 
        if pros[1]<'0' or pros[1]>'9':
            print 'Λαθος κινηση'
            return False
        trow=int(pros[1])-1
        
        if acol<0 or acol>=8:
            print 'Λαθος κινηση'
            return False
        
        if arow<0 and acol >=8:
            print 'Λαθος κινηση'
            return False
            
        if tcol<0 and acol >=8:
            print 'Λαθος κινηση'
            return False
        
        if trow<0 and acol >=8:
            print 'Λαθος κινηση'
            return False
            
        if self.board[arow][acol] == ' ':
            print 'Λαθος κινηση'
            return False    
        
        if self.board[arow][acol].color=='white' and xroma==1:
            print 'Λαθος κινηση'
            return False
            
        if self.board[arow][acol].color=='black' and xroma==0:
            print 'Λαθος κινηση'
            return False
        
        #print "prohgoumenos:",self.board[arow][acol].row, " ", self.board[arow][acol].col
        self.board[trow][tcol] = self.board[arow][acol]
        self.board[arow][acol] = " "
        self.board[trow][tcol].row = trow+1
        self.board[trow][tcol].col = tcol+1
        #print "meta:",self.board[trow][tcol].row, " ", self.board[trow][tcol].col
        
        return True
        

    def show_board(self,x):
    
        if x==0:
            print "{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}".format(
            "A","B","C","D","E","F","G","H")
    
            print '  ',"-"*8*5
            for i in range(len(self.board)-1,-1,-1):
                print "{:2} |{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|".format(
                    i+1,
                    self.board [i] [0], self.board [i] [1],
                    self.board [i] [2], self.board [i] [3],
                    self.board [i] [4], self.board [i] [5],
                    self.board [i] [6], self.board [i] [7])
                print '  ',"-"*8*5      
           
            print "{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}".format(
                "A","B","C","D","E","F","G","H")	                       
            
            
            
        if x==1:  
    
    
            print "{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}".format(
                "A","B","C","D","E","F","G","H")
    
            print '  ',"-"*8*5
            for i in range(len(self.board)):
                print "{:2} |{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|{:^4}|".format(
                    i+1,
                    self.board [i] [0], self.board [i] [1],
                    self.board [i] [2], self.board [i] [3],
                    self.board [i] [4], self.board [i] [5],
                    self.board [i] [6], self.board [i] [7])
                print '  ',"-"*8*5      
           
            print "{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}".format(
                "A","B","C","D","E","F","G","H")
    
    
    
    
    
    
    
    
    
    def show_board_old(self):
        print self.board
