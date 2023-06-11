from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt

diabetes= load_diabetes()

X = diabetes.data
y = diabetes.target

AGE = 0;SEX = 1;MASS_INDEX = 2; BLOOD_PRESSURE = 3;
print(diabetes.DESCR)

print(X.shape)
print(y.shape)

print(X[0:5,:])# muestra las primeras cinco filas de la matriz X completa, incluyendo todas las columnas. Es decir, muestra un subconjunto de la matriz X que contiene las primeras cinco filas y todas las columnas.
print(f"Estos son los datos correspondientes a la salida: {y[0:5]}")

print(X[1, MASS_INDEX])
print(X[1:3,AGE])
print(diabetes.data.shape[0])

x = range(0,diabetes.data.shape[0],1)
plt.figure(figsize=(30,8))
plt.plot(x,X[:,MASS_INDEX],'r-',label='Mass Index')
plt.plot(x,X[:,BLOOD_PRESSURE],'b-',label='Blood Pressure')
plt.rcParams.update({'font.size':25})
plt.legend(prop={'size':25});plt.grid();plt.show()

fig, axs = plt.subplots(1,2,figsize=(12,4))

for fig,feature,label in zip(range(2),[MASS_INDEX,AGE],
                             ['Mass Index','Age']):
    axs[fig].scatter(X[:,feature],X[:,BLOOD_PRESSURE],c='g', marker="o")
    axs[fig].set_xlabel(label);axs[fig].set_ylabel('Blood Pressure');
    axs[fig].grid();
    
plt.show()

