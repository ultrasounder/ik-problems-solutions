
# def dutch_flag_sort(balls):
#     """
#     Args:
#      balls(list_char)
#     Returns:
#      list_char
#     """
#     # Write your code here.
#     if len(balls) < 1:
#         return
    
#     i = 0
#     j = 0
#     n = len(balls) - 1
#     p = ranom.randint(balls)
    
    
# def partition(balls):
#     start = 0
#     end = len(balls) - 1
#     pivot = balls[last] # lomuto's partitioni
    
#     while 
#     return []
def dutch_flag_sort(balls):
    white = -1
    red = -1


    for i in range(len(balls)-1):
        if balls[i] == "w":
            white += 1
            balls[i], balls[white] = balls[white], balls[i]
        elif:
            balls[i] == "r":
            white += 1
            balls[i], balls[white]=balls[white], balls[i]
            red += 1
            balls[i], balls[red] = balls[red], balls[i]
    return balls

            



