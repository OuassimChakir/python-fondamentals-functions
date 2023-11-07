# Question 3
def conversion_temps(h,m,s):
    m = m + (h*60)
    return s + (m*60)

# Question 4
time = conversion_temps(22,3,50) - conversion_temps(21,50,1)
print(time);

# Question 5
def conversion_distance(km,m,cm):
    m = m + (km*1000)
    m = m + (cm/100)
    return m

# Question 6
def vitesse(km,m,cm,h,min,s):
    return conversion_distance(km,m,cm)/conversion_temps(h,min,s)