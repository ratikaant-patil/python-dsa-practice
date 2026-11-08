# Recurssion Stack Example

def recurssionStack(n):
    # This is base stack which means recurssion stop here if condition get true
    if n == 0:
        return

    # This much block it get called recurssion stack which means unexcuted code execute in last that why you seeing answer 1 2 3 4 5
    # See what happing here when we call our recurssionStack(5) then in function we again calling that same function which was recurrsive
    # now problem is print(n,end=" ") not executing because we are skipping that before calling it we are calling function
    # so do you think program skip it no it will place that code in Recursive Stack in which it get stored like
    # print(1) , print(2) , print(3) , print(4), print(5)
    # But you think number should be print from 5 4 3 2 1 
    # but as you know in memory values get stored in stack way means first execute and set last then second execute and set second last
    # execute third and it will be third last 
    # like that that was correct but in recursive Stack it will get execute from top to bottom thats why you see it as 1 2 3 4 5
    recurssionStack(n-1)
    print(n,end=" ")

recurssionStack(5)