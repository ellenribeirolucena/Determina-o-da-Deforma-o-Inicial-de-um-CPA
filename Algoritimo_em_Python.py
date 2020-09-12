import numpy as np
import matplotlib.pyplot as plt
#--
#INICIALIZACAO
x0=[]
x=[]
#--
#ENTRADA
x_deform=0.007985756581724
T_limite = 120
Ta = 21.994286
#--
#DADOS
b1 = 4582.79445127
b2 = 1.41608148
b3 = 0.043521
b4 = 1.120235
#--
m=0.05
g=9.81
r0 = 0.5
G0 = 0.0416743501767146
G1 = 0.0001024775134806
a = 0.0030869333975967
#--
#CALCULO DO x0_otimo E i_otimo
x0_otimo = ((b3/b1)*(T_limite-Ta)**b4)**(1/b2)
if x0_otimo > x_deform:
      x0_otimo = x_deform
      T_otimo = ((b1/b3)*x0_otimo**b2)**(1/b4)+Ta
      re = r0*(1 + a*(T_otimo-Ta))
      G = G0+G1*T_otimo
      i_otimo = np.sqrt((G/re)*(T_otimo - Ta))
else:
      T_otimo = T_limite
      re = r0*(1 + a*(T_otimo-Ta))
      G = G0+G1*T_otimo
      i_otimo = np.sqrt((G/re)*(T_otimo - Ta))
print(' x0_otimo = ',x0_otimo,'\n','i_otimo = ',i_otimo,'\n', 'T_otimo = ',T_otimo)
#--
#PLOT X VERSUS X0
for i in range(int(x_deform*10000)+1):
      x0.append(i/10000)
      if x0[i] <= x0_otimo:
          x.append(x0[i])
      else:
          x.append(x0[i]-((-b3*(T_limite-Ta)**b4 + b1*x0[i]**b2)/b1)**(1/b2))
fig,F = plt.subplots()
F.plot(x0,x,'black')
F.plot(x0_otimo,max(x),'ro',label='x0otimo')
F.axvline(x_deform,color='grey',linestyle='--',linewidth=1,label='x_deform')
legenda = F.legend(loc='upper left', shadow=True, fontsize='x-large')
plt.show()
