def final_comun_mayor(a,b):
  comun=''
  c=-1
  for i in a[::-1]:
    if i==b[c]:
      comun+=i
      c+=-1
    else:
      break
  return comun[::-1]

print(final_comun_mayor('camión', 'ración'))
print(final_comun_mayor('Python', 'PyCon'))
print(final_comun_mayor('teclado', 'mezclado'))
print(final_comun_mayor('harina', 'arroz'))