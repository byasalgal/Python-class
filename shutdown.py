import turtle
window = turtle
turtle.write("shutdown")
def shutdown(a):
    if a == "y":
        window.bye()
    else:
        pass

shutdown(turtle.textinput("shutdown?","y or n"))
window.exitonclick()