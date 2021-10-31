while True:
    try:
        n = int(input("Введите натуральное число: "))
        while n<=0:
            n = int(input("Введите натуральное число: "))
        import turtle
        turtle.shape('turtle')
        i=1
        while i < n+1:
            turtle.forward(70)
            turtle.stamp()
            turtle.left(180)
            turtle.forward(70)
            turtle.right(180-360/n)
            i += 1
    except ValueError:
        #reset variables if necesssary
        pass #if no other code is needed
    else:
        break
