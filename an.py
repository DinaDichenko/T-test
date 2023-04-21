from scipy import stats


rsv1 = stats.norm.rvs(loc=89.9,scale=11.3,size=20)
rsv2 = stats.norm.rvs(loc=80.7,scale=11.7,size=20)
rez = stats.ttest_ind(rsv1,rsv2)
print(rez)


#Индивидуальное задание
"""
Предположим, мы хотим узнать, равен ли средний вес черепах двух разных видов. 
Чтобы проверить это, выполним t-критерий с двумя выборками на уровне значимости α = 0,05.
"""
#Выборка 1:
M1 = 300
sd1=18.5
N1=40
#Выборка 2:
M2=305
sd2=16.7
N2=38
#H0 - средние значения двух популяций равны
#H1 - средние значения двух популяций не равны
rvs1 = stats.norm.rvs(loc=M1,scale=sd1,size=N1)
rvs2 = stats.norm.rvs(loc=M2,scale=sd2,size=N2)
rez2 = stats.ttest_ind(rvs1,rvs2)

print(rez2)