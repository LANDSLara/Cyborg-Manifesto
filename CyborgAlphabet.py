size(11500, 25500)
translate(x=-500, y=24100)
strokeValue=10
baseLine=0
xHeight=395

sizeFactor=0.6

inset=10
inset2=10
gutter=100

factor=50

x=100
y=100
rectWidth=100
rectHeight=100
letterWidth=4*x

Variable(
    [  dict(name="strokeValue", ui="Slider", args=dict(value=0, minValue=20, maxValue=180)),
    dict(name="gutter", ui="Slider", args=dict(value=100, minValue=0, maxValue=200)),
    dict(name="xHeight", ui="Slider", args=dict(value=395, minValue=250, maxValue=900)),
    dict(name="letterWidth", ui="Slider", args=dict(value=400, minValue=120, maxValue=500)),
    dict(name="dashValue", ui="Slider", args=dict(value=0, minValue=0, maxValue=400)),
    dict(name="dashValue2", ui="Slider", args=dict(value=0, minValue=0, maxValue=400)),
    dict(name="inset", ui="Slider", args=dict(value=10, minValue=0, maxValue=50)),
    dict(name="letterTilt", ui="Slider", args=dict(value=0, minValue=0, maxValue=0)),
    dict(name="roundLineCap", ui="CheckBox" ),
    dict(name="x", ui="Slider", args=dict(value=100, minValue=5, maxValue=500)),
    dict(name="y", ui="Slider", args=dict(value=100, minValue=5, maxValue=1000)),
   
    ], 
globals())


    

translate(500,750)
stroke(0)
strokeWidth(strokeValue)

fill(0,0,0,0)
lineDash(dashValue, dashValue2)
if roundLineCap:
    lineCap('round')
else:
    lineCap('square')



def draw_notdef():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*1, rectHeight)
    
    return letterWidth
    
 


def letter_a():

    fill(1,1,1)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (4*x,1*y, rectWidth, rectHeight)
    
    

    return letterWidth
        
def letter_b():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (3*x,1*y, rectWidth, rectHeight)

    return letterWidth  
    
def letter_c():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (3*x,1*y, rectWidth*2, rectHeight)

    return letterWidth

def letter_d():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (2*x,1*y, rectWidth*1, rectHeight)

    return letterWidth  

    
def letter_e():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (2*x,1*y, rectWidth*1, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)

    return letterWidth 
    
    
def letter_f():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (2*x,1*y, rectWidth*2, rectHeight)

    return letterWidth  
    
    
def letter_g():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (2*x,1*y, rectWidth*3, rectHeight)

    return letterWidth      
    
def letter_h():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)

    return letterWidth 

def letter_i():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)

    return letterWidth  
    
def letter_j():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    rect (3*x,1*y, rectWidth*1, rectHeight)

    return letterWidth    
        
def letter_k():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    rect (3*x,1*y, rectWidth*2, rectHeight)

    return letterWidth       
    
def letter_l():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (1*x,1*y, rectWidth*2, rectHeight)
   
    return letterWidth 


def letter_m():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (1*x,1*y, rectWidth*2, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
   
    return letterWidth  
    
def letter_n():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (1*x,1*y, rectWidth*3, rectHeight)

    return letterWidth  

def letter_o():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth, rectHeight)
    rect (3*x,2*y, rectWidth, rectHeight)
    rect (1*x,1*y, rectWidth*4, rectHeight)

    return letterWidth  

def letter_p():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*3, rectHeight)
    
    return letterWidth 
  
def letter_q():    
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*3, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth 
    
def letter_r():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*3, rectHeight)
    rect (3*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth 
    
def letter_s():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*3, rectHeight)
    rect (3*x,1*y, rectWidth*2, rectHeight)
    
    return letterWidth 

def letter_t():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*3, rectHeight)
    rect (2*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth


def letter_u():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*3, rectHeight)
    rect (2*x,1*y, rectWidth*1, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth

def letter_v():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*3, rectHeight)
    rect (2*x,1*y, rectWidth*1, rectHeight)
    rect (3*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth

    
def letter_w():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*3, rectHeight)
    rect (2*x,1*y, rectWidth*1, rectHeight)
    rect (3*x,1*y, rectWidth*2, rectHeight)
    
    return letterWidth  
      
def letter_x():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*3, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth  

def letter_y():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*3, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth  

    
def letter_z():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*3, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    rect (3*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth
 
 
 
 
# ------------- CAPITALS ------------- 
 
   
def letter_A():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth 

def letter_B(): 
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (3*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth  

def letter_C():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (3*x,1*y, rectWidth*2, rectHeight)
    
    return letterWidth 
    
def letter_D():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (2*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth 
        
def letter_E():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (2*x,1*y, rectWidth*1, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth
    
def letter_F():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (2*x,1*y, rectWidth*2, rectHeight)
    
    return letterWidth  
    
def letter_G():  
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (2*x,1*y, rectWidth*3, rectHeight)
    
    return letterWidth    
      
def letter_H():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth  
    
def letter_I():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth 
        
def letter_J():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    rect (3*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth 
        
def letter_K():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    rect (3*x,1*y, rectWidth*2, rectHeight)
    
    return letterWidth
    
def letter_L():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*2, rectHeight)
   
    return letterWidth 
    
def letter_M():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*2, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
   
    return letterWidth 
       
def letter_N():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*3, rectHeight)
   
    return letterWidth 
    
def letter_O():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*4, rectHeight)
   
    return letterWidth
          
def letter_P():
    
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (4*x,2*y, rectWidth*1, rectHeight)
    
    return letterWidth 
     
def letter_Q():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (4*x,2*y, rectWidth*1, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth 
 
def letter_R():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (4*x,2*y, rectWidth*1, rectHeight)
    rect (3*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth 
    
def letter_S():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (4*x,2*y, rectWidth*1, rectHeight)
    rect (3*x,1*y, rectWidth*2, rectHeight)
    
    return letterWidth  
    
def letter_T():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (4*x,2*y, rectWidth*1, rectHeight)
    rect (2*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth 
    
def letter_U():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (4*x,2*y, rectWidth*1, rectHeight)
    rect (2*x,1*y, rectWidth*1, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth  
    
def letter_V():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (4*x,2*y, rectWidth*1, rectHeight)
    rect (2*x,1*y, rectWidth*2, rectHeight)
    
    return letterWidth
    
def letter_W():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (4*x,2*y, rectWidth*1, rectHeight)
    rect (2*x,1*y, rectWidth*3, rectHeight)
    
    return letterWidth  
 
        
def letter_X():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (4*x,2*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth  
             
def letter_Y():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*1, rectHeight)
    rect (4*x,2*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth
                     
def letter_Z():
    fill(0,0,0)
    rect (2*x,2*y, rectWidth*2, rectHeight)
    
    return letterWidth  
    
    
    
    
def letter_0():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*2, rectHeight)
    
    return letterWidth     
    
def letter_1():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*2, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth   
    
def letter_2():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*2, rectHeight)
    rect (3*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth  
    
def letter_3():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*2, rectHeight)
    rect (3*x,1*y, rectWidth*2, rectHeight)
    
    return letterWidth  
    
def letter_4():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*2, rectHeight)
    rect (2*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth     
    
def letter_5():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*2, rectHeight)
    rect (2*x,1*y, rectWidth*1, rectHeight)
    rect (4*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth  
    
def letter_6():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*2, rectHeight)
    rect (2*x,1*y, rectWidth*2, rectHeight)
    
    return letterWidth   
    
def letter_7():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*2, rectHeight)
    rect (2*x,1*y, rectWidth*3, rectHeight)
    
    return letterWidth      
    
def letter_8():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*2, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    
    return letterWidth  
    
def letter_9():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*2, rectHeight)
    rect (1*x,1*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*4, rectHeight)
    
    return letterWidth                      
  
def punc_period():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*3, rectHeight)
    
    return letterWidth
    
def punc_comma():
    fill(0,0,0)
    rect (3*x,2*y, rectWidth*1, rectHeight)
    rect (1*x,1*y, rectWidth*2, rectHeight)
    
    return letterWidth      


def drawLetter(func):
    with savedState():
        rotate(letterTilt, center=(letterWidth/2, 200))
        width = func()
    translate(width, 0)



characterMap = {
    "a" : letter_a,
    "b" : letter_b,
    "c" : letter_c,
    "d" : letter_d,
    "e" : letter_e,
    "f" : letter_f,
    "g" : letter_g,
    "h" : letter_h,
    "i" : letter_i,
    "j" : letter_j,
    "k" : letter_k,
    "l" : letter_l,
    "m" : letter_m,
    "n" : letter_n,
    "o" : letter_o,
    "p" : letter_p,
    "q" : letter_q,
    "r" : letter_r,
    "s" : letter_s,
    "t" : letter_t,
    "u" : letter_u,
    "v" : letter_v,
    "w" : letter_w,
    "x" : letter_x,
    "y" : letter_y,
    "z" : letter_z,
    
    "A" : letter_A,
    "B" : letter_B,
    "C" : letter_C,
    "D" : letter_D,
    "E" : letter_E,
    "F" : letter_F,
    "G" : letter_G,
    "H" : letter_H,
    "I" : letter_I,
    "J" : letter_J,
    "K" : letter_K,
    "L" : letter_L,
    "M" : letter_M,
    "N" : letter_N,
    "O" : letter_O,
    "P" : letter_P,
    "Q" : letter_Q,
    "R" : letter_R,
    "S" : letter_S,
    "T" : letter_T,
    "U" : letter_U,
    "V" : letter_V,
    "W" : letter_W,
    "X" : letter_X,
    "Y" : letter_Y,
    "Z" : letter_Z,
    
    "0" : letter_0,
    "1" : letter_1,
    "2" : letter_2,
    "3" : letter_3,
    "4" : letter_4,
    "5" : letter_5,
    "6" : letter_6,
    "7" : letter_7,
    "8" : letter_8,
    "9" : letter_9,    
    
   
    "." : punc_period,
    "," : punc_comma
}

# Type yout text between the quote marks
textInput = "ABCDEFHIJ\n\nKLMNOPQRST\n\nUVWXYZ"




save()
for char in textInput:
    if char == "\n":
        restore()
        translate(0, -y*2)
        save()
    else:
        func = characterMap.get(char, draw_notdef)
        drawLetter(func)
 

 
saveImage("~/Desktop/Cyborg-Alphabet.svg")   


