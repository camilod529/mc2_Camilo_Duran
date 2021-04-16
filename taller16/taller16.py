def main():
    x = [0,1,3,5,6,8,9,12] #0
    y = [14,10,12,6,8,5,4,1] #1
    A = [x,y]
    n = len(A[0])
    sumX = 0.0
    sumY = 0.0
    sumXY = 0.0
    sumX2 = 0.0
    for i in range(n):
        
        sumX += A[0][i]
        sumY += A[1][i]
        sumXY += (A[0][i]*A[1][i])
        sumX2 += (A[0][i]*A[0][i])
    
    promX = sumX/n
    promY = sumY/n
    
    #formulita

    a1 = (n*sumXY-sumX*sumY)/(n*sumX2-pow(sumX,2))
    a0 = promY - a1*promX
    
    #respuesta
    print(f"respuesta :y = {a0} + {a1}x")


if __name__ == '__main__':
    main()