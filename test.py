__author__ = 'Pascal'


minAreaInput = raw_input("Min Area: ")
maxAreaInput = raw_input("Max Area: ")
shapeIndexInput= raw_input("Shape Index >=: ")


selectByArea =  "'"+ '"Ai" >= '+minAreaInput+' AND "Ai" <= '+ maxAreaInput + ' AND "ShapeIndex" >= ' + shapeIndexInput +"'"

print selectByArea
print '''"Ai" >= 6 AND "Ai" <= 50 AND "ShapeIndex" >=0.5'''