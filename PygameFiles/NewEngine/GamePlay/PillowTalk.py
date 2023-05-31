from PIL import Image, ImageDraw


def GenerateImage(output_path,moveset):
    
    image = Image.new("RGB", (400, 400), "white")

    draw = ImageDraw.Draw(image)
    colors = ["red", "green", "blue", "yellow",
              "purple", "orange"]
    row = 5
    col = 5
    # columns
    for x in range(1,col):
        location = image.width/col * x
        draw.line((location,0) + (location,image.height), width=10,fill="Black")
        image.save(output_path)
    # rows
    for x in range(1,row):
        location = image.height/row * x
        draw.line((0,location) + (image.width,location), width=10,fill="Black")
        image.save(output_path)

    # Rectangle top left
    # row,col-
    xy = [2,2]
    draw.rectangle( (xy[1]*image.width/col,xy[0]*image.height/row, (xy[1]+1)*image.width/col, (xy[0]+1)*image.height/row), fill="red")
    # custom moveset the first is y then x

    for x in range(len(moveset)):
        holder = [0,0]
        holder[0] = moveset[x][0]*-1+2        
        holder[1] = moveset[x][1]*-1+2

        draw.rectangle( (holder[1]*image.width/col,holder[0]*image.height/row, (holder[1]+1)*image.width/col, (holder[0]+1)*image.height/row), fill="Green")
    image.save(output_path)

'''if __name__ == "__main__":
    GenerateImage( "crab.jpg",moveset=([-1,0], [2, 0]))'''