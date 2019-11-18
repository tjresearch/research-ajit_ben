from math import hypot, pi, cos, sin
from PIL import Image


def hough(im, ntx=460, mry=360):
    "Calculate Hough transform."
    pim = im.load()
    nimx, mimy = im.size
    mry = int(mry/2)*2          #Make sure that this is even
    him = Image.new("L", (ntx, mry), 255)
    phim = him.load()

    rmax = hypot(nimx, mimy)
    dr = rmax / (mry/2)
    dth = pi / ntx

    for jx in range(nimx):
        for iy in range(mimy):
            col = pim[jx, iy]
            if col == 255: continue
            for jtx in range(ntx):
                th = dth * jtx
                r = jx*cos(th) + iy*sin(th)
                iry = mry/2 + int(r/dr+0.5)
                phim[jtx, iry] -= 1
    return him


def test():
    "Test Hough transform with cube."
    im = Image.open("cube.png").convert("L")
    him = hough(im)
    him.save("ho4.bmp")


if __name__ == "__main__": test()



# http://me.umn.edu/courses/me5286/vision/Notes/2015/ME5286-Lecture9.pdf

# https://pdfs.semanticscholar.org/ae2f/1e490748a6fa3b859f124c763d4556d2930b.pdf
