def checkio(game_result):
    n = len(game_result)
    def check(m):
        for line in m:            
            if line.count('X') == n:
                return 'X'
            if line.count('O') == n:
                return 'O'
        return None
        
    res = check(game_result)
    if res:
        return res
    cols = ['' for i in range(n)]
    for i in range(n):
        for j in range(n):
            cols[j] += game_result[i][j]    
    res = check(cols)
    if res:
        return res
    
    diag = ['', '']
    for i in range(n):
        diag[0] += game_result[i][i]
        diag[1] += game_result[i][n-1-i]
    
    res = check(diag)
    if res:
        return res
    
    return 'D'
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

