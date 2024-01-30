# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpeg', 30)
#
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34
#
# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# #red = rgb.r
# #saturation = hsl[1]
# saturation = hsl.s
# #colors.sort(key=lambda c: c.hls.h)
# lista = []
# mi_dupla = ()
# for color in colors:
#     if color.rgb.r < 230 and color.rgb.g < 230 and color.rgb.b < 230:
#         mi_dupla = (color.rgb.r, color.rgb.g, color.rgb.b)
#         lista.append(mi_dupla)
#
# print(lista)
