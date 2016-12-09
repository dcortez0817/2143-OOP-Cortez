from PIL import Image
import urllib, cStringIO
import random

class ImageEd(object):
    
    def __init__(self, img):
        self.img = img
        self.width = img.size[0]
        self.height = img.size[1]

    def glass_effect(self, img = None, d = 5):
        nums = [x for x in range(0-d, 0+d) if x >=0]
        for x in range(d, self.width-d):
            for y in range(d, self.height-d):
                n = random.choice(nums)
                self.img.getpixel((x,y))
                self.img.putpixel((x+n,y+n))
        return self.img

    def flip(self, img = None):
        for y in range(self.height):
            for x in range(self.width/2):
                img.getpixel((x,y))
                img.putpixel((self.width - x, y))
        return self.img

    def blur(img, blur_power = 3):
        r = 0
        g = 0
        b = 0
        d = 2*blur_power * 2*blur_power
        for x in range(blur_power,width-blur_power):
            for y in range(blur_power,height-blur_power):
                for i in range(-blur_power,blur_power):
                    for j in range(-blur_power,blur_power):
                        pix = img.getpixel((x+i,y+j))
                        r += pix[0]
                        g += pix[1]
                        b += pix[2]
                img.putpixel((x,y),(int(r/d),int(g/d),int(b/d)))
                r = 0
                g = 0
                b = 0
        return self.img

    def posterize(self, img = None, snap_val = 100):
        for x in range(self.width):
            for y in range(self.height):
                color = self.img.getpixel((x,y))
                r = color[0]
                g = color[1]
                b = color[2]

                if (r%snap_val) < (snap_val // 2):
                    r -= r%snap_val
                else:
                    r += (snap_val - r%snap)
                
                if (g%snap) < (snap_val // 2):
                    g -= g%snap_val
                else:
                    g += (snap_val - g%snap_val) 

                if (b%snap_val) < (snap_val // 2):
                    b -= b%snap_val
                else:
                    b += (snap_val - b%snap_val)

                self.img.putpixel((x,y), (r,g,b))
        return self.img
        

    def solarize(self, img = None, threshold = 100):
        for x in range(self.width):
            for y in range(self.height):
                rgb = img.getpixel((x,y))
                r = rgb[0]
                g = rgb[1]
                b = rgb[2]
                
                if r < threshold:
                    r = threshold - r
                else:
                    r = r + threshold
                    
                if g < threshold:
                    g = threshold - g
                else:
                    g = g + threshold

                if b < threshold:
                    b = threshold - b
                else:
                    b = b + threshold                                        
                
                self.img.putpixel((x,y), (r,g,b))
        return self.img

    def warhol(self, img = None, snap_val = 51):
        nums = int(255/snap_val)
        color = [(0,0,0),(255,0,0),(0,255,0),(0,0,255),(128,128,128),(255,255,255)]
        for x in range(self.width):
            for y in range(self.height):
                rgb = img.getpixel((x,y))
                r = rgb[0]
                g = rgb[1]
                b = rgb[2]

                gray = int((r + g + b)/3)
                self.img.putpixel((x,y), (r,g,b)) 

                r = int(r)
                m = r % snap_val
            if m < (snap_val // 2):
                r -= m

            else:
                r += (snap_val - m)
    
                for i in range(1, nums + 1):
                    if ((r < (i * 255) / nums) & (r > ((i - 1) * 255)/ nums)):
                        r2 = color[i]
                        img.putpixel((x, y), r2)

        return self.img       