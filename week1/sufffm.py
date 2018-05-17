import numpy as np
s = []
for i in range(20):
    s.append((256/255)**i*(1/256)*(1-(255/256)**(16+i))*(1-(255/256)**(20-i)))
print(s,sum(s)*100)# 1/3700


for i in range(42):
    s.append((256/255)**i*(1/256)*(1-(255/256)**(16+i))*(1-(255/256)**(42-i)))
print(s,sum(s))# 1/555

