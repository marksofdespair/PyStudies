train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write code below: 
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

print(f_to_c(100))

def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)   # Should print 32.0

def get_force(mass, acceleration):
    return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c=3*10**8):
    return mass * c**2

bomb_energy = get_energy(bomb_mass)
print(bomb_energy)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work

train_work = get_work(train_mass, train_acceleration, 100)
print(train_work)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
