"""
*            * * * * *  * * * * *    * * * * *           *        *           *
* *          * * * *      * * * *     * * * *          * *       * *         * * 
* * *        * * *          * * *      * * *         * * *      * * *       * * * 
* * * *      * *              * *       * *        * * * *     * * * *     * * * * 
* * * * *    *                  *        *       * * * * *    * * * * *   * * * * *
                                                                           * * * * 
                                                                            * * *
                                                                             * * 
                                                                              *

"""

# row  = 5  col = 5
# 1 :
"""
for i in range(1,6):# row 
    for j in range (1,i+1):
        print("*",end=" ")
    print()
"""
# 2
"""
for i in range(5,0,-1):# row 
    for j in range (1,i+1):
        print("*",end=" ")
    print()
"""

# 3 : 
"""
for i in range(1,6):#   2 , 6 
    for  k in range(1,i):  # 1 ,2 
        print(" ",end=" ")
    for j in range (5,i-1,-1): # 5 ,1 
        print("*",end=" ")    # * * * * * 
    print()                   #   * * * *
"""

# 4 : 
"""
for i in range(1,6):#   2 , 6 
    for  k in range(1,i):  # 1 ,2 
        print("",end=" ")
    for j in range (5,i-1,-1): # 5 ,1 
        print("* ",end="")    # * * * * * 
    print()                   #   * * * *
"""

#5 : 
"""
for i in range(1,6):#   2 , 6 
    for  k in range(5,i,-1):  # 1 ,2 
        print(" ",end=" ")
    for j in range (1,i+1,): # 5 ,1 
        print("*",end=" ")    # * * * * * 
    print()                   #   * * * *
"""

#6 : 
"""
for i in range(1,6):#   2 , 6 
    for  k in range(5,i,-1):  # 1 ,2 
        print("",end=" ")
    for j in range (1,i+1): # 5 ,1 
        print("* ",end="")    # * * * * * 
    print()                   #   * * * *
"""

#7 : 
for i in range(1,6):#   2 , 6 
    for  k in range(5,i,-1):  # 1 ,2 
        print("",end=" ")
    for j in range (1,i+1): # 5 ,1 
        print("* ",end="")    # * * * * * 
    print()                   #   * * * *
for i in range(1,6):#   2 , 6 
    for  k in range(1,i):  # 1 ,2 
        print("",end=" ")
    for j in range (5,i-1,-1): # 5 ,1 
        print("* ",end="")    # * * * * * 
    print()                   #   * * * *
