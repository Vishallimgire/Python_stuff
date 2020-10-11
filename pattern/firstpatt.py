''' First pattern '''

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# 6 6 6 6 6 6
# n = 6

# for  i in range(1,n+1):
#     j = str(i) * i
#     print(j)

''' second pattern '''
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print('\n')


''' Third pattern '''
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1
# for i in range(0, n+1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print('\n')


''' Fourth pattern'''
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * *
# n = 5

# for i in range(n):
#     for j in range(i, n-1):
#         print(' ', end="")
    
#     for j in range(i+1):
#         print('* ', end="")
#     print()

