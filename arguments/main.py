# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, msg='Hello, <name>!'):
    new_msg = msg.replace('<name>', name)
    return new_msg

print(greet('Aris'))
print(greet("Bob", "How are you, <name>!"))
print(greet("Bob"))
print(greet("Koos", msg="Hey there!"))

def force(mass, body='earth'):
    gravity_bodies = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6 
    }
    return mass * gravity_bodies[body]

print(force(mass=(5.9736 * 10**24)))
print(force(mass=1.9891 * 10**30, body='sun'))

def pull(m1, m2, d):
    G = 6.674 * (10 ** -11)
    gravitational_pull = G * ((m1*m2)/(d**2))
    return gravitational_pull

print(pull(800, 1500, 3))   # two cars
print(pull(0.1, (5.972 * (10**24)), (6.371 * (10**6)))) # apple and earth
