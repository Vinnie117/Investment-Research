import numpy as np
import numpy_financial as npf

# 9930 ist Einkaufssumme aller WPs
flows = [-9930, 2946.83, 1330.25, 1408.43, 2122.72, 1635.28, 486.4]

irr = npf.irr(flows)
print(irr)


print('END')