from PIL import Image

im = Image.open("charset.bmp")
print(im.mode)



def letter_toHex(letter:int, desc:str):
    toReturn = "# "+str(letter)+" - "+desc
    row = letter//8
    col = letter - row*8
    bounds = (col*8, row*9, col*8+8, row*9+9 )
    cropped =im.crop(bounds)

    for i in range(0, 9):
        toReturn += "\n"+line_toHex(cropped, i)

    return toReturn

def line_toHex(image:Image, line:int):
    toReturn = "0x"
    for i in (0, 4):
        toReturn += pixelGroup_toChar(image, line, i)
    return toReturn

def pixelGroup_toChar(image:Image, line:int, pos:int):
    # yes, I'm aware all of this is terrible, but I'm very tired, and it will do.
    first  = image.getpixel((pos, line)) == 255
    second = image.getpixel((pos+1, line)) == 255
    third = image.getpixel((pos+2, line))==255
    fourth = image.getpixel((pos+3, line))==255
    arr = [first, second, third, fourth]

    val = 0
    for bool in arr:
        val *= 2
        if bool:
            val+=1

    hexArr = [ '0', '1','2','3',"4","5","6","7","8","9","A", "B", "C", "D", "E", "F"]
    return hexArr[val]

arr = ["[END]", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N","O", "P", "Q", "R", "S", "T", "U", "V",
       "W", "X", "Y", "Z", "0","1","2","3","4","5","6","7","8","9", "[SPACE]", "[ENTER]", "[BACK]",".",",","!","?",":",
       "+", "-", "[UNUSED]","[UNUSED]","[UNUSED]","[UNUSED]","[UNUSED]","[UNUSED]","[UNUSED]","[UNUSED]",
       "[UNUSED]","[UNUSED]","[UNUSED]","[UNUSED]","[UNUSED]","[UNUSED]","[UNUSED]","[UNUSED]","[UNUSED]","[UNUSED]",
       "[UNUSED]","[UNUSED]"]


for i in range (0, 64):
    print(letter_toHex(i,arr[i]))