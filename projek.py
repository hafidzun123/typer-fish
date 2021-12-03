from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rd

pos_x_hiu = +100
pos_y_hiu = 0
kecepatan_hiu = 0.5

pos_y_kapalselam = 0
pos_x_kapalselam = 0

batas_atas = 80
batas_kiri = 465

pos_x_peluru = 0
pos_y_peluru = pos_y_kapalselam
kecepatan_peluru = 0
tembak = False

selesai = False
hit_hiu = 1

darah = 140
demage = False
batu = 1
counter_batu = 10
kondisi_pecah = 0
kondisi_demage = False
demagenya = 0
kecepatan_damage  = 10

batas_depan_X = 99
batas_depan_y = 108 

batas_depan_hiux = 280
batas_depan_hiuy = 199

def latar1():
    glBegin(GL_POLYGON)
    glColor3ub(8, 67, 204)
    glVertex2f(0,500)
    glVertex2f(500,500)
    glVertex2f(500,0)
    glVertex2f(0,0)
    glEnd()
def kapal_selam() :
    global pos_y_kapalselam, pos_x_kapalselam, selesai
    glPushMatrix()
    #memberi pembatas
    if not selesai:
        if pos_y_kapalselam > batas_atas :
            pos_y_kapalselam = batas_atas
        if pos_y_kapalselam < -batas_atas-10:
            pos_y_kapalselam = -batas_atas-10

    glTranslate(pos_x_kapalselam, pos_y_kapalselam, 0)
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

# def damage():
#     global pos_x_kapalselam, pos_y_kapalselam, kecepatan_damage, demagenya, batas_atas
#     # glColor3f(1,1,1)          
#     glPushMatrix()
#     demagenya -= kecepatan_damage
#     if demagenya < pos_y_kapalselam or batas_atas:
#         damagenya = -300
#     glTranslated(0,damagenya,0)
#     glBegin(GL_LINES)

#     for i in range(5):
#         glVertex2f(pos_x_kapalselam+rd.randrange(-10,10),rd.randrange(pos_y_kapalselam+300,pos_y_kapalselam+500)) 
#         glVertex2f(pos_x_kapalselam+rd.randrange(-30,30),pos_y_kapalselam+400) 
    
#     glEnd()
#     glPopMatrix()

def hiu():
    global pos_x_hiu, batas_kiri, pos_y_hiu, pos_y_kapalselam, darah, demage, batu, counter_batu, kondisi_pecah, pos_x_kapalselam, pos_x_peluru, pos_y_peluru
    glPushMatrix()
    #memberi pembatas
    if not False:
        if pos_y_hiu > batas_atas-70:
            pos_y_hiu = batas_atas-70
        if pos_y_hiu < -batas_atas-90:
            pos_y_hiu = -batas_atas-90
    # mengatur kecepatan hiu
    pos_x_hiu -= kecepatan_hiu
    #jika hiu melewati layar maka pergerakan akan diulang
    if pos_x_hiu < -batas_kiri:
        pos_x_hiu = batas_kiri
        # pos_y_hiu = rd.randrange(pos_y_kapalselam-130, pos_y_kapalselam+1)
        p = [pos_y_kapalselam-130, pos_y_kapalselam+1, pos_y_kapalselam-50]
        pos_y_hiu = rd.choice(p)
        
    #colision hiu dengan kapalselam
    # offset = 100
    # if pos_x_hiu in range (pos_x_kapalselam-offset, pos_x_kapalselam+offset) and  pos_x_hiu in range (pos_y_kapalselam-offset, pos_y_kapalselam+offset):
    #     darah -= hit_hiu
    #     demage = True
    #colision hiu dengan peluru
    # offset = 50
    # if pos_x_hiu in range (pos_x_peluru-offset, pos_x_peluru+offset) and  pos_y_hiu in range (pos_y_peluru-offset, pos_y_peluru+offset) :
    #     batu += counter_batu
    #     pos_x_hiu = 2000
    #     demage = False
    #     kondisi_pecah = True
    
    
    glTranslate(pos_x_hiu, pos_y_hiu, 0)

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

def hiu2():
    global pos_x_hiu, batas_kiri, pos_y_hiu, pos_y_kapalselam
    glPushMatrix()
    #memberi pembatas
    if not selesai:
        if pos_y_hiu > batas_atas+60:
            pos_y_hiu = batas_atas+60
        if pos_y_hiu < -batas_atas+60:
            pos_y_hiu = -batas_atas+60
    # mengatur kecepatan hiu
    # pos_x_hiu -= kecepatan_hiu
    #jika hiu melewati layar maka pergerakan akan diulang
    if pos_x_hiu < -batas_kiri:
        pos_x_hiu = batas_kiri
        pos_y_hiu = rd.randrange(pos_y_kapalselam-50, pos_y_kapalselam+10) 

    glTranslate(pos_x_hiu, pos_y_hiu, 0)

    glColor3ub(59, 92, 117)
    glBegin(GL_POLYGON)
    glVertex2f(380, 68)
    glVertex2f(399.9, 74.2)
    glVertex2f(416.9, 76.2)
    glVertex2f(407.3, 59.6)
    glVertex2f(388.1, 62.3)
    glEnd()
    glColor3ub(59, 92, 117)
    glBegin(GL_POLYGON)
    glVertex2f(416.9, 76.2)
    glVertex2f(426.9, 85.7)
    glVertex2f(427.8, 80.2)
    glVertex2f(430.6, 75)
    glEnd()
    glColor3ub(59, 92, 117)
    glBegin(GL_POLYGON)
    glVertex2f(416.9, 76.2)
    glVertex2f(430.6, 75)
    glVertex2f(454.9, 68.5)
    glVertex2f(462.7, 67.7)
    glVertex2f(462.3, 64.4)
    glVertex2f(442.7, 61.1)
    glVertex2f(435.7, 58.9)
    glVertex2f(418.3, 58.7)
    glVertex2f(407.3, 59.6)
    glEnd()
    glColor3ub(59, 92, 117)
    glBegin(GL_POLYGON)
    glVertex2f(462.7, 67.7)
    glVertex2f(472.5, 75.6)
    glVertex2f(480, 79.3)
    glVertex2f(471.8,66.3 )
    glVertex2f(472.7, 60.2)
    glVertex2f(474.9, 55.8)
    glVertex2f(469.2, 58)
    glVertex2f(462.3, 64.4)
    glEnd()
    glColor3ub(59, 92, 117)
    glBegin(GL_POLYGON)
    glVertex2f(442.7, 61.1)
    glVertex2f(446.9, 57)
    glVertex2f(435.7, 58.9)
    glEnd()
    glColor3ub(59, 92, 117)
    glBegin(GL_POLYGON)
    glVertex2f(418.3, 58.7)
    glVertex2f(416.2, 56.3)
    glVertex2f(417.7, 45.3)
    glVertex2f(412.4, 48.5)
    glVertex2f(409, 55.1)
    glVertex2f(407.3, 59.6)
    glEnd()
    glColor3ub(255, 255, 255) #mata
    glBegin(GL_POINTS)
    glVertex2f(389.4, 68.5)
    glEnd()
    glColor3ub(255, 255, 255) #mulut
    glBegin(GL_POLYGON)
    glVertex2f(384, 65)
    glVertex2f(391., 65)
    glVertex2f(388.3, 61.7)
    glEnd()
    glColor3ub(255, 255, 255) #garis
    glBegin(GL_LINES)
    glVertex2f(402, 70)
    glVertex2f(400.2, 63.8)
    glVertex2f(404.1, 70.1)
    glVertex2f(402.3, 63.5)
    glVertex2f(406, 70.1)
    glVertex2f(403.9, 63.2)
    glVertex2f(407.6, 70.2)
    glVertex2f(405.7, 62.7)
    glEnd()
    glPopMatrix()

# def paus():
#     glColor3ub(0, 0, 0)
#     glBegin(GL_POLYGON) # badan
#     glVertex2f(269.5, 130.8)
#     glVertex2f(280, 137.2)
#     glVertex2f(303.2, 135.1)
#     glVertex2f(342.3, 136)
#     glVertex2f(369, 137.5)
#     glVertex2f(386.2, 137.5)
#     glVertex2f(414, 143)
#     glVertex2f(426.2, 142.8)
#     glVertex2f(440, 140)
#     glVertex2f(450.7, 133.1)
#     glVertex2f(449.2, 127.3)
#     glVertex2f(431.5, 124.5)
#     glVertex2f(405.1, 112.8)
#     glVertex2f(380, 100)
#     glVertex2f(359.1, 94.1)
#     glVertex2f(342.3, 93.4)
#     glVertex2f(328.2, 94.6)
#     glVertex2f(310.5, 99.8)
#     glVertex2f(297.1, 103.4)
#     glVertex2f(282.2, 113.3)
#     glVertex2f(270.6, 127.6)
#     glEnd()
#     glColor3f(0, 0, 0)
#     glBegin(GL_POLYGON) # sirip
#     glVertex2f(342.3, 136)
#     glVertex2f(344.7, 138.6)
#     glVertex2f(352.4, 161.9)
#     glVertex2f(357.3, 173.5)
#     glVertex2f(362, 177)
#     glVertex2f(361.6, 167.3)
#     glVertex2f(365.5, 143.8)
#     glVertex2f(369, 137.5)
#     glEnd()
#     glColor3f(0, 0, 0)
#     glBegin(GL_POLYGON) #ekor
#     glVertex2f(450.7, 133.1)
#     glVertex2f(459.9, 137.8)
#     glVertex2f(470, 140)
#     glVertex2f(464.1, 132.1)
#     glVertex2f(464.9, 123.9)
#     glVertex2f(472.1, 113.9)
#     glVertex2f(464, 116.1)
#     glVertex2f(449.2, 127.3)
#     glEnd()
#     glColor3f(0, 0, 0)
#     glBegin(GL_POLYGON)
#     glVertex2f(328.2, 94.6)
#     glVertex2f(332, 86.4)
#     glVertex2f(331.1, 84.1)
#     glVertex2f(330.2, 82.4)
#     glVertex2f(328.7, 81.6)
#     glVertex2f(326.2, 81.6)
#     glVertex2f(320.8, 84.4)
#     glVertex2f(310.5, 99.8)
#     glEnd()
#     glColor3f(0, 0, 0)
#     glBegin(GL_POLYGON)
#     glVertex2f(310.5, 99.8)
#     glVertex2f(320.8, 84.4)
#     glVertex2f(320.8,77.3 )
#     glVertex2f(320, 74.1)
#     glVertex2f(316, 70)
#     glVertex2f(311.2,71.4 )
#     glVertex2f(303.7, 79.5)
#     glVertex2f(299.3, 87.9)
#     glVertex2f(297.1, 103.4)
#     glEnd()
#     glColor3ub(255, 255, 255)
#     glBegin(GL_POLYGON) # mata
#     glVertex2f(289.3, 128.4 )
#     glVertex2f(292.3, 129.7)
#     glVertex2f(304.2, 126.1)
#     glVertex2f(304.1, 124.0)
#     glVertex2f(300.9, 122.4)
#     glVertex2f(293.3, 124.0)
#     glVertex2f(289.8, 125.9)
#     glEnd()
#     glColor3ub(255, 255, 255)
#     glBegin(GL_POLYGON)# putih
#     glVertex2f(270.6, 127.6)
#     glVertex2f(292.7, 120.9)
#     glVertex2f(294.5, 119)
#     glVertex2f(300, 110)
#     glVertex2f(301, 107.8)
#     glVertex2f(297.1, 103.4)
#     glVertex2f(282.2, 113.3)
#     glEnd()
#     glColor3ub(255, 255, 255)
#     glBegin(GL_POLYGON)# putih
#     glVertex2f(316.5, 98.9)
#     glVertex2f(332.5, 96.3)
#     glVertex2f(340.8, 95.5)
#     glVertex2f(359.2, 96.7 )
#     glVertex2f(359.1, 94.1)
#     glVertex2f(342.3, 93.4)
#     glVertex2f(328.2, 94.6)
#     glVertex2f(317, 96.9)
#     glEnd()    
#     glColor3ub(255, 255, 255)
#     glBegin(GL_POLYGON)# putih
#     glVertex2f(359.2, 96.7 )
#     glVertex2f(367.0, 98.8 )
#     glVertex2f(381.7, 103.3)
#     glVertex2f(383.4, 103.9 )
#     glVertex2f(390.5, 106.9 )
#     glVertex2f(401.8, 112.4 )
#     glVertex2f(404.4, 113.8 )
#     glVertex2f(405.1, 113.7 )
#     glVertex2f(405.1, 112.8)
#     glVertex2f(380, 100)
#     glVertex2f(359.1, 94.1)
#     glEnd() 
#     glColor3ub(255, 255, 255)
#     glBegin(GL_POLYGON)# putih
#     glVertex2f(371, 104.5)
#     glVertex2f(382.1, 105.8 )
#     glVertex2f(381.7, 103.3)
#     glVertex2f(367.0, 98.8 )
#     glEnd()
#     glColor3ub(255, 255, 255)
#     glBegin(GL_POLYGON)# putih
#     glVertex2f(371, 104.5)
#     glVertex2f(375.5, 111.0)
#     glVertex2f(380.1, 116.0)
#     glVertex2f(387,  119.9)
#     glVertex2f(399.4, 122.8)
#     glVertex2f(404.0, 122.6)
#     glVertex2f(406.5, 121.7)
#     glVertex2f(406.4, 120.1)
#     glVertex2f(405.6, 119.0)
#     glVertex2f(402.5, 116.7)
#     glVertex2f(385.0, 108.1)
#     glVertex2f(382.1, 105.8)
#     glEnd()
#     glColor3ub(255, 255, 255)
#     glBegin(GL_POLYGON)# putih
#     glVertex2f(360.8, 120.9)
#     glVertex2f(357.2, 124.8)
#     glVertex2f(356.4, 129.5)
#     glVertex2f(360.8, 133.7)
#     glVertex2f(365.0, 136.0)
#     glVertex2f(367.4, 136.4)
#     glVertex2f(375.4, 136.5)
#     glVertex2f(376.8, 134.0)
#     glVertex2f(373.1, 131.2)
#     glVertex2f(370.2, 127.8)
#     glVertex2f(366.9, 125.3)
#     glVertex2f(365 , 120)
#     glVertex2f(362.0, 117.9)
#     glVertex2f(360.5, 118.3)
#     glEnd()
def bar_darah_kapalselam():
    global darah, hit_hiu 

    if darah < 60:
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


def bar_darah_hiu():
    # global darah, hit_meteor 

    # if darah < 60:
    #     hit_meteor = 0



    glPushMatrix()
    glColor3ub(37, 255, 8) #RGB
    # glBegin(GL_QUADS) 
    # glVertex2f(60,60)
    # glVertex2f(1+darah,60)
    # glVertex2f(1+darah,80)
    # glVertex2f(60,80)
    # glEnd()

    glBegin(GL_LINE_LOOP) 
    glVertex2f(385, 245)
    glVertex2f(480, 245)
    glVertex2f(480, 235)
    glVertex2f(385, 235)
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
        
    glTranslated(pos_x_peluru, pos_y_peluru, 0)
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


def bottons(key,x,y) :
    global pos_y_kapalselam, pos_x_hiu, pos_y_hiu, pos_x_peluru, tembak, kecepatan_peluru,batas_depan_X,batas_depan_y
    if key == GLUT_KEY_UP:
        pos_y_kapalselam += 5
        batas_depan_y += 5 
    elif key == GLUT_KEY_DOWN:
        pos_y_kapalselam -= 5
        batas_depan_y -=5
    elif key == b'w': pos_y_kapalselam += 5 #kapal selam keatas
    elif key == b's': pos_y_kapalselam -= 5 #kapal selam kebawah
    # elif key == b'a': pos_x_hiu -= 5
    # elif key == b'd': pos_y_hiu += 5
    elif key == GLUT_KEY_RIGHT:
        tembak = not tembak
        if tembak == True:
            kecepatan_peluru = 0.5

    
def iterate():
    glViewport(0, 0, 1370, 1370)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

# def showScreen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     latar1()
#     if selesai:
#         kapal_selam()
   
#     if not selesai:
#         kapal_selam()
#         peluru()
#         if kondisi_demage:
#             damage()
#         hiu()
#         bar_darah_kapalselam()
#         bar_darah_hiu()
#     glutSwapBuffers()

    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    latar1()
    peluru()
    kapal_selam()
    # damage()
    hiu()
    # hiu2()
    # paus()
    bar_darah_kapalselam()
    bar_darah_hiu()
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
glutMainLoop()


