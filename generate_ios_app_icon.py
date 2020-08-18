# in terminal call pip3 install pillow before run this script

# change logoPath here
logoPath = r"logo.png"

from PIL import Image
import json
import os

def make_icon_set(dirName, orginImage):
    if os.path.isdir(dirName):
        print("Remove old dir")
        os.removedirs(dirName)
    os.makedirs(dirName)

    with open(r'Contents.json') as f:
        dJson = json.load(f)
        contents = {
            "info" : {
                "author" : "xcode",
                "version" : 1
            },
            "images":[]
            }
        for img in dJson["images"]:
            size = float(img["size"].split("x")[0])
            size *= float(img["scale"].split("x")[0])
            newImg = orginImage.resize((int(size), int(size)))
            imageName = img["idiom"]+img["size"]+"@"+img["scale"]+".png"
            newImg.save(dirName+"/"+imageName)
            img["filename"] = imageName
            contents["images"] += [img]
    
        with open(dirName+ "/" + "Contents.json", 'w') as content:
            content.write(json.dumps(contents, indent=4))

        print("Done")




orginImg = Image.open(logoPath)

width, height = orginImg.size

print("width: {}, height: {}".format(width, height))

if width != height or width != 1024:
    print("Invalid input")
    exit()

directoryName = "AppIcon{}.appiconset".format("")

make_icon_set(directoryName, orginImg)


