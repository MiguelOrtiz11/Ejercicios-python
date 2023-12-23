#hacer una nota que lea una nota definitiva y clasifique al alumno asi: su la nota esta entre 4.5 y 5 
# es excelente si esta entre 4 y 4.4 es spbresaliente si esta entre 3.0 y 3.9 es aceptable si esta 
#menos a 2.9 es deficiente
nota=float(input("digite su nota definitiva: "))
if nota>=45 and nota<=50:
   print("su nota es excelente")
if nota>=40 and nota<=44:
    print("su nota es sobresaliente")
if nota>=30 and nota<=39:
    print("su nota es aceptable")
if nota>=29 and nota<=0:
    print("su nota es deficiente")