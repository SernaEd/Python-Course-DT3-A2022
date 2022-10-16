# Instructions

Consider the following code:

    x = 25
    epsilon = 0.01
    step = 0.1
    guess = 0.0

    while guess <= x:
        if abs(guess**2 -x) < epsilon:
            break
        else:
            guess += step
        
        if abs(guess**2 - x) >= epsilon:
            print('failed')
        else:
            print('succeeded: ' + str(guess))

If this code is executed, it will print `succeeded: 5.0` after several failed attempts.

Now suppose we try the following:

    x = 25
    epsilon = 0.01
    step = 0.1
    guess = 0.0

    while guess <= x:
        if abs(guess**2 -x) >= epsilon:
            guess += step
        
        if abs(guess**2 - x) >= epsilon:
            print('failed')
        else:
            print('succeeded: ' + str(guess))

Select the answer that best describes what occurs when the above code is executed:

<div class="hint">
  If the options shown confuse you, try running the code on your own machine and inserting print statements to print out intermediate values of variables so you can examine what happens to certain variables - for example, <code>guess</code> - as the program is executed. 
</div>
