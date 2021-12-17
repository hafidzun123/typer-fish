from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rd
import os
from latar import *


pos_x_hiu = +100
pos_y_hiu = 0
kecepatan_hiu = 0.5

pos_y_kapalselam = 0
pos_x_kapalselam = 0

batas_atas = 80
batas_kiri = 150


pos_x_peluru = -10
pos_y_peluru = pos_y_kapalselam
kecepatan_peluru = 0
tembak = False

selesai = False
hit_hiu = 5

darah = 140  
value = 0

colisionkapalselam = False
kondisi = "main_menu"

def skr():
    xpos = 400
    ypos = 237
    text = "Skor :"
    glColor3ub(0, 0, 0)
    glRasterPos2f(xpos,ypos)
    for i in range(len(text)):

        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(text[i]))

def skor():
    global value
    glColor3f( 0, 0, 0 )   #-> kalo mau diubah warna nya bisa
    glRasterPos(430,237)
    glColor3ub(37, 255, 8)
    glBegin(GL_POLYGON) 
    glVertex2f(385, 245)
    glVertex2f(480, 245)
    glVertex2f(480, 235)
    glVertex2f(385, 235)
    glEnd()
    for c in str(value):
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )

def NOTE():
    xpos = 200
    ypos = 75
    txt  ="Petunjuk :"
    glColor3ub(255, 255, 255)
    glRasterPos2f(xpos,ypos)
    for i in range(len(txt)):

        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(txt[i]))

def satu():
    xpos = 200
    ypos = 60
    txt  ="1. Gunakan w/panah atas untuk mengerakan kapal selam keatas"
    glColor3ub(255, 255, 255)
    glRasterPos2f(xpos,ypos)
    for i in range(len(txt)):

        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(txt[i]))

def dua():
    xpos = 200
    ypos = 50
    txt  ="2. Gunakan s/panah bawah untuk mengerakan kapal selam kebawah"
    glColor3ub(255, 255, 255)
    glRasterPos2f(xpos,ypos)
    for i in range(len(txt)):

        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(txt[i]))

def tiga():
    xpos = 200
    ypos = 40
    txt  ="3. Gunakan panah kanan untuk menembak hiu"
    glColor3ub(255, 255, 255)
    glRasterPos2f(xpos,ypos)
    for i in range(len(txt)):

        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(txt[i]))

def kapal_selam() :
    global pos_y_kapalselam, pos_x_kapalselam, selesai
    glPushMatrix()
    #memberi pembatas
    if not selesai:
        if pos_y_kapalselam > batas_atas-80 :
            pos_y_kapalselam = batas_atas-80
        if pos_y_kapalselam < -batas_atas-10-80:
            pos_y_kapalselam = -batas_atas-10-80

    glTranslate(pos_x_kapalselam, pos_y_kapalselam+80, 0)
    glColor3ub(158, 117, 14)
    glBegin(GL_POLYGON) #ekor
    glVertex2f(33.9, 103.9)
    glVertex2f(33.9, 101.6)
    glVertex2f(31.8, 98.2)
    glVertex2f(22.5, 98.4)
    glVertex2f(21.1, 105.9)
    glVertex2f(21.1, 118.7)
    glVertex2f(22.2, 124.0)
    glVertex2f(32.0, 124.0)
    glVertex2f(34.2, 120.6)
    glVertex2f(34.2, 117.6)
    glEnd()
    glBegin(GL_POLYGON) #ekor
    glVertex2f(33.9, 103.9)
    glVertex2f(34.2, 117.6)
    glVertex2f(36.8, 117.7)
    glVertex2f(36.8, 103.9)
    glEnd()
    glBegin(GL_POLYGON) # badan
    glVertex2f(36.8, 117.7)
    glVertex2f(37.3, 120.6)
    glVertex2f(42.9, 126.8)
    glVertex2f(49.2, 129.4)
    glVertex2f(51.8, 130.4)
    glVertex2f(76.2, 130.3)
    glVertex2f(79.5, 128.7)
    glVertex2f(84.8, 127.1)
    glVertex2f(88.3, 124.6)
    glVertex2f(88.3, 97.0)
    glVertex2f(83.5, 93.6)
    glVertex2f(74.3, 90.9)
    glVertex2f(62.6, 90.6)
    glVertex2f(48.3, 91.5)
    glVertex2f(41.4, 94.6)
    glVertex2f(37.5, 100.5)
    glVertex2f(36.8, 103.9)
    glEnd()
    glColor3ub(125, 44, 4)
    glBegin(GL_POLYGON) # badan
    glVertex2f(51.7, 130.4)
    glVertex2f(51.9, 131.6)
    glVertex2f(52.8, 131.9)
    glVertex2f(58, 132)
    glVertex2f(70.0, 132.2)
    glVertex2f(75.6, 132.5)
    glVertex2f(76.2, 130.3)
    glEnd()
    glBegin(GL_POLYGON) # badan
    glVertex2f(58, 132)
    glVertex2f(59.2, 134.3)
    glVertex2f(61.6, 134.9)
    glVertex2f(66.5, 134.8)
    glVertex2f(68.8, 134.6)
    glVertex2f(70.0, 132.2)
    glEnd()
    glColor3ub(158, 117, 14)
    glBegin(GL_POLYGON) # badan
    glVertex2f(61.6, 134.9)
    glVertex2f(62.4, 145.5)
    glVertex2f(65.0, 148.1)
    glVertex2f(66.3, 143.5)
    glVertex2f(66.5, 134.8)
    glEnd()
    glBegin(GL_POLYGON) # badan
    glVertex2f(65.0, 148.1)
    glVertex2f(67.1, 148.3)
    glVertex2f(67.4, 144.4)
    glVertex2f(66.3, 143.5)
    glVertex2f(66.5, 134.8)
    glEnd()
    glColor3ub(125, 44, 4)
    glBegin(GL_POLYGON) # badan
    glVertex2f(67.1, 148.3)
    glVertex2f(67.1, 149.6)
    glVertex2f(68.9, 149.8)
    glVertex2f(71.0, 148.5)
    glVertex2f(71.9, 147.6)
    glVertex2f(72.1, 145.3)
    glVertex2f(70., 143.45)
    glVertex2f(69.2, 143.4)
    glVertex2f(67.4, 143.3)
    glVertex2f(67.4, 144.4)
    glEnd()
    glColor3ub(163, 213, 214)
    glBegin(GL_POLYGON) # depan
    glVertex2f(88.3, 124.6)
    glVertex2f(90.8, 123.6)
    glVertex2f(94.9, 120.7)
    glVertex2f(97.1, 118.1)
    glVertex2f(98.6, 114.9)
    glVertex2f(99.2, 112.1)
    glVertex2f(99.1, 108.0)
    glVertex2f(98.3, 105.0)
    glVertex2f(97.4, 103.1)
    glVertex2f(95, 100)
    glVertex2f(91.1, 98.2)
    glVertex2f(88.3, 97.0)
    glEnd()
    glColor3ub(125, 44, 4)
    glBegin(GL_POLYGON)
    glVertex2f(90.8, 123.6)
    glVertex2f(88.3, 124.6)
    glVertex2f(88.3, 97.0)
    glVertex2f(91.1, 98.2)
    glEnd()
    glBegin(GL_POLYGON) # jendela
    glVertex2f(67.9, 100.3)
    glVertex2f(74.1, 104.8)
    glVertex2f(76.3, 111.9)
    glVertex2f(74.0, 119.2)
    glVertex2f(67.9, 123.7)
    glVertex2f(60.4, 123.7)
    glVertex2f(54.1, 119.2)
    glVertex2f(52, 112)
    glVertex2f(54.1, 104.7)
    glVertex2f(60.3, 100.3)
    glEnd()
    glColor3ub(163, 213, 214)
    glBegin(GL_POLYGON) # jendela
    glVertex2f(67.0, 102.7)
    glVertex2f(71.9, 106.1)
    glVertex2f(73.9, 111.9)
    glVertex2f(71.9, 117.6)
    glVertex2f(67.1, 121.2)
    glVertex2f(61.0, 121.2)
    glVertex2f(56.1, 117.6)
    glVertex2f(54.3, 111.9)
    glVertex2f(56.1, 106.0)
    glVertex2f(61.0, 102.7)
    glEnd()
    glColor3ub(125, 44, 4)
    glBegin(GL_POLYGON) #baling baling
    glVertex2f(24.0, 104.7)
    glVertex2f(27.4, 104.5)
    glVertex2f(29.6, 106.0)
    glVertex2f(29.4, 109.0)
    glVertex2f(29.4, 112.1)
    glVertex2f(29.6, 116.1)
    glVertex2f(28.1, 117.2)
    glVertex2f(24.0, 117.2)
    glVertex2f(22.7, 115.3)
    glVertex2f(22.7, 106.3)
    glEnd()
    glColor3ub(163, 213, 214)
    glBegin(GL_POLYGON) # baling
    glVertex2f(29.4, 109.0)
    glVertex2f(29.4, 112.1)
    glVertex2f(26., 112.)
    glVertex2f(25.0, 111.2)
    glVertex2f(25.1, 109.9)
    glVertex2f(25.9, 109.3)
    glEnd()
    glColor3ub(163, 213, 214)
    glBegin(GL_TRIANGLES)
    glVertex2f(26.4, 112.1)
    glVertex2f(27.4, 117.2)
    glVertex2f(25.6, 117.1)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(26.5, 109.2)
    glVertex2f(25.8, 104.6)
    glVertex2f(27.4, 104.6)
    glEnd()
    glPopMatrix()

def hiu():
    global value,pos_x_hiu, batas_kiri, pos_y_hiu, pos_y_kapalselam, darah, pos_x_kapalselam, pos_x_peluru, pos_y_peluru, colisionkapalselam
    os.system('cls')
    # print("pos hiu:        ", pos_x_hiu,',',pos_y_hiu)
    # print("pos kapalselam:     ", pos_x_kapalselam,',', pos_y_kapalselam)
    
    glPushMatrix()
    #memberi pembatas
    if not False:
        if pos_y_hiu > batas_atas-70:
            pos_y_hiu = batas_atas-70
        if pos_y_hiu < -batas_atas-90:
            pos_y_hiu = -batas_atas-90
    # mengatur kecepatan hiu
    pos_x_hiu -= kecepatan_hiu*15
    #jika hiu melewati layar maka pergerakan akan diulang
    if pos_x_hiu < -batas_kiri:
        pos_x_hiu = 300
        # pos_y_hiu = pos_y_hiu-10
        p = [pos_y_kapalselam+10, pos_y_kapalselam+1, pos_y_kapalselam-50]
        pos_y_hiu = rd.choice(p)
        colisionkapalselam = False
        
    
    # colision hiu dengan kapalselam
    toleransi = 15
    if pos_x_hiu in range (pos_x_kapalselam-toleransi, pos_x_kapalselam+toleransi) and  pos_y_hiu in range (pos_y_kapalselam-toleransi, pos_y_kapalselam+toleransi):
        darah -= hit_hiu
        colisionkapalselam = True
        
    #colision hiu dengan peluru
    toleransi = 10
    if pos_x_hiu in range (pos_x_peluru-toleransi, pos_x_peluru+toleransi) and  pos_y_hiu in range (pos_y_peluru-toleransi, pos_y_peluru+toleransi) and colisionkapalselam == False :
        pos_x_hiu = 500
        value += 50
    
    
    
    glTranslate(pos_x_hiu-290, pos_y_hiu, 0)
    

    glColor3ub(59, 92, 117)
    glBegin(GL_POLYGON)
    glVertex2f(380, 198)
    glVertex2f(399.9, 204.2)
    glVertex2f(416.9, 206.2)
    glVertex2f(407.3, 189.6)
    glVertex2f(388.1, 192.3)
    glEnd()
    glColor3ub(59, 92, 117)
    glBegin(GL_POLYGON)
    glVertex2f(416.9, 206.2)
    glVertex2f(426.9, 215.7)
    glVertex2f(427.8, 210.2)
    glVertex2f(430.6, 205)
    glEnd()
    glColor3ub(59, 92, 117)
    glBegin(GL_POLYGON)
    glVertex2f(416.9, 206.2)
    glVertex2f(430.6, 205)
    glVertex2f(454.9, 198.5)
    glVertex2f(462.7, 197.7)
    glVertex2f(462.3, 194.4)
    glVertex2f(442.7, 191.1)
    glVertex2f(435.7, 188.9)
    glVertex2f(418.3, 188.7)
    glVertex2f(407.3, 189.6)
    glEnd()
    glColor3ub(59, 92, 117)
    glBegin(GL_POLYGON)
    glVertex2f(462.7, 197.7)
    glVertex2f(472.5, 205.6)
    glVertex2f(480, 209.3)
    glVertex2f(471.8,196.3 )
    glVertex2f(472.7, 190.2)
    glVertex2f(474.9, 185.8)
    glVertex2f(469.2, 188)
    glVertex2f(462.3, 194.4)
    glEnd()
    glColor3ub(59, 92, 117)
    glBegin(GL_POLYGON)
    glVertex2f(442.7, 191.1)
    glVertex2f(446.9, 187)
    glVertex2f(435.7, 188.9)
    glEnd()
    glColor3ub(59, 92, 117)
    glBegin(GL_POLYGON)
    glVertex2f(418.3, 188.7)
    glVertex2f(416.2, 186.3)
    glVertex2f(417.7, 175.3)
    glVertex2f(412.4, 178.5)
    glVertex2f(409, 185.1)
    glVertex2f(407.3, 189.6)
    glEnd()
    glColor3ub(255, 255, 255) #mata
    glBegin(GL_POINTS)
    glVertex2f(389.4, 198.5)
    glEnd()
    glColor3ub(255, 255, 255) #mulut
    glBegin(GL_POLYGON)
    glVertex2f(384, 195)
    glVertex2f(391., 195)
    glVertex2f(388.3, 191.7)
    glEnd()
    glColor3ub(255, 255, 255) #garis
    glBegin(GL_LINES)
    glVertex2f(402, 200)
    glVertex2f(400.2, 193.8)
    glVertex2f(404.1, 200.1)
    glVertex2f(402.3, 193.5)
    glVertex2f(406, 200.1)
    glVertex2f(403.9, 193.2)
    glVertex2f(407.6, 200.2)
    glVertex2f(405.7, 192.7)
    glEnd()
    glPopMatrix()


def bar_darah_kapalselam():
    global darah, hit_hiu 

    if darah < 20:
        hit_hiu = 0


    glPushMatrix()
    glColor3ub(255, 8, 8) #RGB
    glBegin(GL_QUADS) 
    glVertex2f(15,245)
    glVertex2f(1+darah,245)
    glVertex2f(1+darah,235)
    glVertex2f(15,235)
    glEnd()

    glBegin(GL_LINE_LOOP) 
    glVertex2f(15, 245)
    glVertex2f(140, 245)
    glVertex2f(140, 235)
    glVertex2f(15, 235)
    glEnd()
    glPopMatrix()


def peluru():
    global pos_x_peluru, pos_y_peluru, kecepatan_peluru, pos_y_kapalselam, pos_x_kapalselam, tembak
    glPushMatrix()
    #mengatur kecepatan peluru
    pos_x_peluru += kecepatan_peluru
    #memberi pembatas
    if pos_x_peluru > 440:
        kecepatan_peluru = 0
        tembak = False
    #penempatan peluru
    if kecepatan_peluru == 0:
        pos_x_peluru = pos_x_kapalselam
        pos_y_peluru = pos_y_kapalselam
        
    glTranslated(pos_x_peluru, pos_y_peluru+80, 0)
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(46.0, 107.9)
    glVertex2f(46.0, 112.9)
    glVertex2f(76.0, 112.9)
    glVertex2f(76.0, 107.9)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(48, 112.9)
    glVertex2f(48, 115)   
    glVertex2f(50, 115)
    glVertex2f(53, 112.9)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(48, 108)
    glVertex2f(48, 106)
    glVertex2f(50, 106)
    glVertex2f(53, 108)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(76, 112.9)
    glVertex2f(76.5, 113)
    glVertex2f(76.9, 112.9)
    glVertex2f(77.6, 112.7)
    glVertex2f(78.3, 112.1)
    glVertex2f(78.7, 111.4)
    glVertex2f(78.9, 110.8)
    glVertex2f(79.0, 109.9)
    glVertex2f(78.6, 109.1)
    glVertex2f(77.7, 108.4)
    glVertex2f(77, 107.9)
    glVertex2f(76.5, 108)
    glVertex2f(76, 107.9)
    glEnd()
    glPopMatrix()

def mouse(key,state,x,y) :
    # print (x,y)
    global kondisi
    if key == GLUT_LEFT_BUTTON :
        if x >= 311 and x <= 1127 and y >= 292 and y <= 370 :
            kondisi = "star"


def bottons(key,x,y) :
    global pos_y_kapalselam, pos_x_hiu, pos_y_hiu, pos_x_peluru, tembak, kecepatan_peluru
    if key == GLUT_KEY_UP:
        pos_y_kapalselam += 7
    elif key == GLUT_KEY_DOWN:
        pos_y_kapalselam -= 7
    elif key == b'w': pos_y_kapalselam += 7 #kapal selam keatas
    elif key == b's': pos_y_kapalselam -= 7 #kapal selam kebawah
    elif key == GLUT_KEY_RIGHT:
        tembak = not tembak
        if tembak == True:
            kecepatan_peluru = 5


    
def iterate():
    glViewport(0, 0, 1370, 1370)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    if kondisi == "main_menu" :
        latar1()
        press_start()
        NOTE()
        satu()
        dua()
        tiga()
    if kondisi == "star" :
    
        if darah > 15:
            latar1()
            skor()
            skr ()
            peluru()
            kapal_selam()
            hiu()
            bar_darah_kapalselam()
        if value >= 200 :
            latar1()
            youwin()
        if darah <= 15 :
            latar1()
            kapal_selam()
            skor()
            skr ()
            bar_darah_kapalselam()
            GAMEOVER()
    
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(1360, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("game")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutKeyboardFunc(bottons)
glutSpecialFunc(bottons)
glutMouseFunc(mouse)
glutMainLoop()


