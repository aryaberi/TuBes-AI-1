def MakeBoard (ukuran):
        a= 0
        b= 0
        c = ukuran -1
        d = ukuran -1
        Board = ['O'] * ukuran

        for i in range (ukuran):
                Board[i] = ['O'] * ukuran
        for a in range (int(ukuran/2) - (b)):
                 for b in range (int(ukuran/2) - (a)):
                        Board[a][b] = 'R'
        
        for c in range (ukuran-1,(int(ukuran/2)-(ukuran - (d))),-1):
                for d in range(ukuran-1,(int(ukuran/2)+(ukuran - (c+2))),-1):
                        
                        Board[c][d] = 'G'
        
        return(Board)


def Goal_P(state):
        kondisi = True
        i = len(state) -1
        j = len(state) -1
        while(kondisi == True and i > int(len(state)/2)-(len(state) - (i))):
                while(j > (int(len(state)/2)+(len(state) - (j+2)))):
                        if(state[i][j] == 'R'):
                                kondisi = True
                                j = j-1
                        else:
                                kondisi = False
                i= i-1
        return(kondisi)

def Goal_A(state):
        kondisi = True
        i = 0
        j = 0
        while(kondisi == True and i < int(len(state)/2) - (j)):
                while(j < int(len(state)/2) - (i)):
                        if(state[i][j] == 'G'):
                                kondisi = True
                                j = j+1
                        else:
                                kondisi = False
                i= j+1
        return(kondisi)

def Home_P(state):
        a= 0
        b = 0
        count = 0
        for a in range (int(len(state)/2) - (b)):
                 for b in range (int(len(state)/2) - (a)):
                        if(state[a][b] == 'R'):
                                count = count +1
        return(count)

def Finish_A(state):
        a= 0
        b = 0
        count = 0
        for a in range (int(len(state)/2) - (b)):
                 for b in range (int(len(state)/2) - (a)):
                        if(state[a][b] == 'G'):
                                count = count +1
        return(count)


def Home_A(state):
        c = len(state) -1
        d = len(state) -1
        count = 0
        for c in range (len(state)-1,(int(len(state)/2)-(len(state) - (d))),-1):
                for d in range(len(state)-1,(int(len(state)/2)+(len(state) - (c+2))),-1):
                        if(state[c][d] == 'G'):
                                count = count +1
        return(count)

def Finish_P(state):
        c = len(state) -1
        d = len(state) -1
        count = 0
        for c in range (len(state)-1,(int(len(state)/2)-(len(state) - (d))),-1):
                for d in range(len(state)-1,(int(len(state)/2)+(len(state) - (c+2))),-1):
                        if(state[c][d] == 'R'):
                                count = count +1        
        return(count)

def Move_Red(ordinat,absis,state,move):
        ordinat_lama = ordinat
        absis_lama = absis
        if(move == "Up" and ((ordinat-1)>= 0) and state[ordinat][absis] == 'R'):
                kondisi = True
                while(kondisi == True):
                        if(state[ordinat-1][absis] == 'R' or state[ordinat-1][absis] == 'G' ):
                                if((ordinat -1) >= 0):
                                        ordinat = ordinat -1
                                else:
                                        kondisi = False
                                        print("langkah tidak valid")
                                        run(0)
                        else:
                                kondisi = False
                state[ordinat-1][absis] = 'R'
                state[ordinat_lama][absis] = 'O'
        elif(move == "Down" and ((ordinat+1) <= len(state)) and state[ordinat][absis] == 'R'):
                kondisi = True
                while(kondisi == True):
                        if(state[ordinat+1][absis] == 'R' or state[ordinat+1][absis] == 'G' ):
                                if(ordinat +1 <= len(state)):
                                        ordinat = ordinat +1
                                       
                                else:
                                        kondisi = False
                                        print("langkah tidak valid")
                                        run(0)
                        else:
                                kondisi = False

                state[ordinat+1][absis] = 'R'
                state[ordinat_lama][absis] = 'O'
        elif(move == "Left" and ((absis-1) >= 0) and state[ordinat][absis] == 'R'):
                kondisi = True
                while(kondisi == True):
                        if(state[ordinat1][absis-1] == 'R' or state[ordinat][absis-1] == 'G' ):
                                if((absis -1) >= 0):
                                        absis = absis -1
                                else:
                                        kondisi = False
                                        print("langkah tidak valid")
                                        run(0)
                        else:
                                kondisi = False
                state[ordinat][absis-1] = 'R'
                state[ordinat][absis_lama] = 'O'
        elif(move == "Right" and ((absis+1) <= len(state)) and state[ordinat][absis] == 'R'):
                kondisi = True
                while(kondisi == True):
                        if(state[ordinat][absis+1] == 'R' or state[ordinat][absis+1] == 'G' ):
                                if(absis +1 <= len(state)):
                                        absis = absis +1
                                else:
                                        kondisi = False
                                        print("langkah tidak valid")
                                        run(0)
                        else:
                                kondisi = False
                state[ordinat][absis+1] = 'R'
                state[ordinat][absis_lama] = 'O'
        else:
                print("langkah tidak valid bidak tidak ditemukan")
                run(0)
def Move_Green(ordinat,absis,state,move):
        ordinat_lama = ordinat
        absis_lama = absis
        if(move == "Up" and ((ordinat-1)>= 0) and state[ordinat][absis] == 'G'):
                kondisi = True
                while(kondisi == True):
                        if(state[ordinat-1][absis] == 'R' or state[ordinat-1][absis] == 'G' ):
                                if((ordinat -1) >= 0):
                                        ordinat = ordinat -1
                                else:
                                        kondisi = False
                                        print("langkah tidak valid")
                                        run(1)
                        else:
                                kondisi = False
                state[ordinat-1][absis] = 'G'
                state[ordinat_lama][absis] = 'O'
        elif(move == "down" and ((ordinat+1) <= len(state)) and state[ordinat][absis] == 'G'):
                kondisi = True
                while(kondisi == True):
                        if(state[ordinat+1][absis] == 'R' or state[ordinat+1][absis] == 'G' ):
                                if(ordinat +1 <= len(state)):
                                        ordinat = ordinat +1
                                else:
                                        kondisi = False
                                        print("langkah tidak valid")
                                        run(1)
                        else:
                                kondisi = False
                state[ordinat+1][absis] = 'G'
                state[ordinat_lama][absis] = 'O'
        elif(move == "Left" and ((absis-1) >= 0) and state[ordinat][absis] == 'G'):
                kondisi = True
                while(kondisi == True):
                        if(state[ordinat][absis-1] == 'R' or state[ordinat][absis-1] == 'G' ):
                                if((absis -1) >= 0):
                                        absis = absis -1
                                else:
                                        kondisi = False
                                        print("langkah tidak valid")
                                        run(1)
                        else:
                                kondisi = False
                state[ordinat][absis-1] = 'G'
                state[ordinat][absis_lama] = 'O'
        elif(move == "Right" and ((absis+1) <= len(state)) and state[ordinat][absis] == 'G'):
                kondisi = True
                while(kondisi == True):
                        if(state[ordinat][absis+1] == 'R' or state[ordinat][absis+1] == 'G' ):
                                if(absis +1 <= len(state)):
                                        absis = absis +1
                                else:
                                        kondisi = False
                                        print("langkah tidak valid")
                                        run(1)
                        else:
                                kondisi = False
                state[ordinat][absis+1] = 'G'
                state[ordinat][absis_lama] = 'O'
        else:
                print("langkah tidak valid bidak tidak ditemukan")
                run(1)
def print_papan(state):
        for i in range (len(state)):
                print(state[i])
def run(pemain):
        if(pemain/2 == 0):
                print("Pemain Red jalan")
                kordinat = int(input("masukan koordinat:"))
                absis = int(input("masukan absi:"))
                Gerak = input("masukan Move:")
                Move_Red(kordinat,absis,board,Gerak)
                print_papan(board)
                if(Goal_P == True):
                        print("permainan selsai R menang")
                else:
                        pemain = pemain+1
                        run(pemain)
        else:
                print("Pemain Grenn  jalan")
                kordinat = int(input("masukan koordinat:"))
                absis = int(input("masukan absi:"))
                Gerak = input("masukan Move:")
                Move_Green(kordinat,absis,board,Gerak)
                print_papan(board)
                if(Goal_A == True):
                        print("permainan selsai G menang")
                else:
                        pemain = pemain-1
                        run(pemain) 
                
size = int(input("Masukan ukuran papan:"))
board = MakeBoard(size)
print_papan(board)
pemain = 0
run(pemain)

        
        



