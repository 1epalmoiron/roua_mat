
class Piece:
    
    def __init__(self,color,name):
        self.color=color
        self.name=name
        self.row=-1
        self.col=-1
        

    def show_position(self):
        print "{:5} {:7} : sthn grammi {:2} sthn sthlh {:2}".format(
        self.color,self.name,self.row,self.col)
    
    def pithana_tetragwna(self):
        return []    
        
    def __str__(self):
        return self.color[0]+self.name[0]
     
class King(Piece):
   
    def __init__(self,color):
        Piece. __init__(self,color,"King")
        
     #def pithana_tetragwna(self):
        #return [[self.row-1, self.col], [self.row+1], [self.col], [self.row],[self.col+1]]    

class Queen(Piece):
    def __init__(self,color):
        Piece. __init__(self,color,"Queen")
class Bishop(Piece):
    def __init__(self,color):
        Piece. __init__(self,color,"Bishop")
class Knight(Piece):
    def __init__(self,color):
        Piece. __init__(self,color,"Knight")
    def __str__(self):
        return self.color[0]+self.name[0:2]
class Rook(Piece):
    def __init__(self,color):
        Piece. __init__(self,color,"Rook")
class pawn(Piece):
    def __init__(self,color):
        Piece. __init__(self,color,"pawn")

