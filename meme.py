from PIL import Image, ImageDraw, ImageFont

def caption_image(image_file, caption, caption2, font="impact.ttf"):
    img = Image.open(image_file)
    draw = ImageDraw.Draw(img)
    #font_size = int(img.width/8)


    fs=int(img.size[1]/5)
    font = ImageFont.truetype("impact.ttf", fs)
    tts=font.getsize(caption)
    bts=font.getsize(caption2)
    while tts[0]>img.size[0]-20 or bts[0]>img.size[0]-20:
        fs=fs-1
        font = ImageFont.truetype("impact.ttf", fs)
        tts=font.getsize(caption)
        bts=font.getsize(caption2)




    caption_w, caption_h = draw.textsize(caption, font=font)
    caption2_w, caption_h = draw.textsize(caption2, font=font)
    draw.text(((img.width-caption_w)/2, (img.height-caption_h)/16), # position
              caption, # text
              (255,255,255), # color
              font=font, # font
              stroke_width=2, # text outline width
              stroke_fill=(0,0,0)) # text outline color
    draw.text(((img.width-caption2_w)/2, (img.height-caption_h)*15/16),
             caption2,
             (255,255,255),
             font=font,
             stroke_width=2,
             stroke_fill=(0,0,0))

    img.save("output.png")
    img.close()