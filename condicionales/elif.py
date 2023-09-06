ingreso_mensual = 70000
gasto_mensual = 2000

# if anidados y else if (elif)

if ingreso_mensual > 10000:
  if ingreso_mensual - gasto_mensual < 0:
    print("estas en déficit")
    
  elif ingreso_mensual - gasto_mensual > 3000:
    print("bien pa, estás bien")
  else:
    print("estas gastando mucho, hay que mirar si te llega el dinero")

elif ingreso_mensual > 1000:
  print("estas bien economicamente en latinoamérica")

elif ingreso_mensual > 500:
  print("estas bien economicamente en argentina")

elif ingreso_mensual > 200:
  print("estas bien economicamente en venezuela")

else:
  print("eres pobre")