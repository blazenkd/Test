# Define the grounding concepts
class Sky:
    def __init__(self, cloudiness):
        self.cloudiness = cloudiness
        
    def is_clear(self):
        return self.cloudiness == 0

class Rain:
    def __init__(self, intensity):
        self.intensity = intensity

# Define the propositions
clear_sky = Sky(0)
cloudy_sky = Sky(1)
raining = Rain(1)
not_raining = Rain(0)

# Define the logical relationships
p = clear_sky
q = not_raining
f = (p.cloudiness == 0) >> (q.intensity == 0)

# Evaluate the logical relationships for different values of the propositions
print("p.q.f")
for i in range(2):
    for j in range(2):
        p = Sky(i)
        q = Rain(j)
        result = f.compose({clear_sky: p, not_raining: q})
        print("{} {} {}".format(p.cloudiness, q.intensity, int(result)))

# Define a new Sky object with 0 clouds (i.e., a clear sky)
clear_sky = Sky(0)

# Translate the statement "The sky is clear" into a logical formula
p = clear_sky.is_clear()