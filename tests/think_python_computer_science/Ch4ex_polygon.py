import turtle #import the module turtle

bob = turtle.Turtle() #from the module turtle, use the Turtle func to create a Turtle object 
print(bob) #bob refers to an object with type Turtle as defined in the module turtle

'''
available methods include: fd (forward), bk(backward) lt(left turn) rt (right turn)
'''
bob.fd(100) #methods are requests, i.e move forward 100 pixels
bob.lt(100)

#bob moves east and then north, leaving two lines behind
turtle.mainloop() #mainloop means to wait for the user to do something. 

