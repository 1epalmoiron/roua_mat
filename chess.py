#-*- encoding:utf-8 -*-
from pieces import *
from board import Chessboard


cb = Chessboard()
cb.prepare()


paiktis=[]

a=raw_input("Δωσε ονομα του λευκου:")
paiktis.append(a)

b=raw_input("Δωσε ονομα του μαυρου:")
paiktis.append(b)


while True:
    cb.show_board(0)
    while True:
        apopou=raw_input("(λευκος: "+paiktis[0]+")Δωσε θεση κομματιου:").lower()
        pros=raw_input("(λευκος: "+paiktis[0]+")Δωσε που θες να μετακινηθει:").lower()
    
        olaok = cb.move(apopou,  pros, 0)
        if olaok==True:
            break
    
    
    cb.show_board(1)
    
    
    apopou=raw_input("(μαυρος: "+paiktis[1]+")Δωσε θεση κομματιου:").lower()
    pros=raw_input("(μαυρος: "+paiktis[1]+")Δωσε που θες να μετακινηθει:").lower()
    
    cb.move(apopou,  pros, 1)





