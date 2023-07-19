"""
Eduardo Solano Jaime. 0213663. Ing Mecatronica 1er semestre.
"""

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math

corrosive = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0.]
dangerous = [6.94000000e-01, 6.00000000e-04, 2.14444444e-03, 1.45555556e-03,
            1.02222222e-03, 9.11111111e-03, 1.87777778e-03, 3.08888889e-03,
            1.21111111e-03, 5.44444444e-04, 4.03333333e-03, 1.31111111e-03,
            2.38888889e-03, 1.05555556e-03, 1.97777778e-03, 7.55555556e-03,
            1.62222222e-03, 2.83333333e-03, 3.15555556e-03, 4.72222222e-03,
            1.86955556e-01, 2.00000000e-03, 2.78888889e-03, 4.85888889e-02,
            8.66666667e-04, 1.05111111e-02, 2.11111111e-04, 5.77777778e-04,
            1.34444444e-03, 4.44444444e-04]
dangerousw = [4.73733333e-01, 3.77777778e-04, 3.83988889e-01, 3.15444444e-02,
             2.65000000e-02, 3.18777778e-02, 4.41111111e-03, 8.93333333e-03,
             1.82222222e-03, 6.55555556e-04, 5.94444444e-03, 5.33333333e-04,
             2.11111111e-03, 3.98888889e-03, 4.31111111e-03, 1.26666667e-02,
             4.66666667e-04, 1.81111111e-03, 3.00000000e-04, 7.77777778e-05,
             0.00000000e+00, 1.07777778e-03, 3.33333333e-05, 8.00000000e-04,
             1.11111111e-05, 0.00000000e+00, 1.48888889e-03, 2.22222222e-05,
             1.33333333e-04, 3.77777778e-04]
explosives = [4.44811111e-01, 7.66666667e-04, 1.04444444e-03, 8.11111111e-04,
             3.77777778e-04, 4.30000000e-03, 1.43333333e-03, 5.30000000e-03,
             2.11111111e-04, 5.55555556e-04, 2.12222222e-03, 3.38888889e-03,
             1.07777778e-03, 1.43333333e-03, 3.03333333e-03, 1.04111111e-02,
             2.80000000e-03, 5.02222222e-03, 3.41933333e-01, 7.45777778e-02,
             7.84444444e-02, 5.44444444e-03, 1.47777778e-03, 4.42222222e-03,
             3.66666667e-04, 2.22222222e-03, 2.22222222e-04, 6.55555556e-04,
             8.55555556e-04, 4.77777778e-04,]
flammable = [5.76888889e-01, 1.00000000e-03, 1.85555556e-03, 1.17777778e-03,
            4.55555556e-04, 5.10000000e-03, 1.78888889e-03, 5.74444444e-03,
            3.11111111e-04, 8.88888889e-05, 3.07777778e-03, 1.55555556e-04,
            2.76666667e-03, 9.00000000e-04, 6.44444444e-04, 8.40000000e-03,
            1.11111111e-03, 3.16666667e-03, 7.42222222e-03, 1.05666667e-02,
            3.36088889e-01, 2.23777778e-02, 1.62222222e-03, 2.51111111e-03,
            4.11111111e-04, 2.67777778e-03, 1.11111111e-05, 4.66666667e-04,
            9.66666667e-04, 2.44444444e-04]
flammableg = [4.45177778e-01, 5.11111111e-04, 1.66666667e-03, 1.03333333e-03,
             1.44444444e-04, 1.54000000e-02, 1.37777778e-03, 2.15555556e-03,
             9.88888889e-04, 7.11111111e-04, 4.90000000e-03, 6.00000000e-04,
             4.45555556e-03, 2.28888889e-03, 2.12222222e-03, 1.54555556e-02,
             3.07777778e-03, 4.88888889e-03, 1.05666667e-02, 8.35555556e-03,
             3.87511111e-01, 4.56333333e-02, 6.55555556e-03, 7.87777778e-03,
             3.48888889e-03, 1.79555556e-02, 8.88888889e-05, 1.51111111e-03,
             2.67777778e-03, 8.22222222e-04]
flamables = [0.60522222, 0.00345556, 0.00334444, 0.00323333, 0.0031    , 0.01407778,
            0.00435556, 0.00367778, 0.0036    , 0.00306667, 0.01408889, 0.0032    ,
            0.00415556, 0.00248889, 0.00094444, 0.01606667, 0.00414444, 0.00543333,
            0.00495556, 0.01485556, 0.23478889, 0.01096667, 0.00597778, 0.00347778,
            0.00514444, 0.01646667, 0.00204444, 0.00158889, 0.00088889, 0.00118889]
nfg = [5.13333333e-01, 1.36666667e-03, 2.10000000e-03, 2.17777778e-03,
      9.33333333e-04, 1.45555556e-02, 1.51000000e-02, 6.94888889e-02,
      3.30900000e-01, 4.96666667e-03, 7.03333333e-03, 1.21111111e-03,
      4.08888889e-03, 9.44444444e-04, 4.33333333e-04, 6.07777778e-03,
      2.22222222e-04, 1.28888889e-03, 1.55555556e-03, 5.44444444e-04,
      3.72222222e-03, 4.44444444e-04, 9.33333333e-04, 3.96666667e-03,
      1.15555556e-03, 7.76666667e-03, 6.66666667e-05, 1.01111111e-03,
      1.93333333e-03, 6.77777778e-04]
oxidizer = [4.97544444e-01, 4.44444444e-05, 7.77777778e-05, 0.00000000e+00,
           0.00000000e+00, 1.77777778e-04, 1.11111111e-05, 8.88888889e-05,
           4.44444444e-05, 0.00000000e+00, 2.44444444e-04, 4.44444444e-05,
           2.11111111e-04, 6.00000000e-04, 9.00000000e-04, 3.70433333e-01,
           1.43111111e-02, 7.96666667e-03, 6.71111111e-03, 4.14444444e-03,
           6.56666667e-03, 5.37555556e-02, 9.55555556e-03, 3.78888889e-03,
           3.32222222e-03, 6.67777778e-03, 5.01111111e-03, 4.27777778e-03,
           2.33333333e-03, 1.15555556e-03]
oxygen = [4.51866667e-01, 1.45555556e-03, 1.72222222e-03, 6.66666667e-04,
         8.88888889e-05, 8.73333333e-03, 8.33333333e-04, 2.18888889e-03,
         7.33333333e-04, 3.11111111e-04, 1.26222222e-02, 1.38888889e-03,
         8.61111111e-03, 4.60000000e-03, 6.07777778e-03, 4.18922222e-01,
         1.87000000e-02, 8.76666667e-03, 1.28000000e-02, 4.04444444e-03,
         1.08333333e-02, 4.77777778e-04, 7.22222222e-04, 2.16666667e-03,
         7.11111111e-04, 1.40666667e-02, 1.66666667e-04, 1.13333333e-03,
         2.67777778e-03, 1.91111111e-03]
poison = [9.99311111e-01, 0.00000000e+00, 1.11111111e-05, 1.11111111e-05,
         0.00000000e+00, 1.22222222e-04, 1.11111111e-05, 1.11111111e-05,
         1.11111111e-05, 1.11111111e-05, 5.55555556e-05, 0.00000000e+00,
         1.11111111e-05, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
         1.00000000e-04, 0.00000000e+00, 0.00000000e+00, 1.11111111e-05,
         2.22222222e-05, 5.55555556e-05, 0.00000000e+00, 2.22222222e-05,
         4.44444444e-05, 3.33333333e-05, 0.00000000e+00, 1.33333333e-04,
         0.00000000e+00, 1.11111111e-05]
radioactive = [8.56511111e-01, 7.55555556e-04, 7.55555556e-04, 2.00000000e-04,
              4.44444444e-05, 1.61111111e-03, 3.11111111e-04, 3.22222222e-04,
              3.22222222e-04, 3.33333333e-05, 3.75555556e-03, 5.88888889e-04,
              1.47777778e-03, 2.34444444e-03, 5.88888889e-04, 1.05411111e-01,
              4.93333333e-03, 1.56666667e-03, 1.37777778e-03, 1.62222222e-03,
              2.71111111e-03, 5.66666667e-04, 5.55555556e-04, 3.11111111e-04,
              2.00000000e-04, 7.73333333e-03, 3.00000000e-04, 1.48888889e-03,
              8.88888889e-04, 7.11111111e-04]

corrosiveinfo = ("HAZMAT Class 8: Corrosive substances, means substances which, by chemical "
                 "action, will cause severe damage when in contact with living tissue or, in the case of leakage, "
                 "will materially damage, or even destroy, other goods or the means of transport.")
dangerousinfo = ("Dangerous Placards, like this one, are for substances that enter in two or more categories of hazardous "
                 "materials that require different placards")
dangerouswinfo = ("HAZMAT Class 4 division 4.3: Dangerous when wet material is a substance that, by contact with "
                  "water, is liable to become spontaneously flammable or to give off flammable or toxic gas at a "
                  "rate greater than 1 liter per kilogram of the material, per hour, when tested in accordance with"
                  " the UN Manual of Tests and Criteria. Pure alkali metals are known examples of this.")
explosivesinfo = ("HAZMAT Class 1 division 1.4. Explosives with a major fire hazard (includes ammunition "
                  "and most consumer fireworks).")
flammableinfo = ("HAZMAT Class 3. A flammable liquid is a liquid with flash point of not more than 60.5 °C (141 °F), "
                 "or any material in a liquid phase with a flash point at or above 37.8 °C (100 °F) that is "
                 "intentionally heated and offered for transportation or transported at or above its flash point "
                 "in a bulk packaging.")
flammableginfo = ("HAZMAT Class 2 division 2.1. Flammable Gases. Any material which is a gas at 20 °C (68 °F) "
                  "or less and 101.3 kPa (14.7 psia) of pressure and ignitable and flammable range  at 101.3 kPa")
flammablesinfo = ("HAZMAT Class 4 division 4.1. Flammable solids included in any of the following four types "
                  "of materials: densesitized explosives, self-reactive materials, generic types and readily "
                  "combustible solids.")
nfginfo = ("HAZMAT Class 2 division 2.2 Non-flammable, non-toxic gas. Includes compressed gas, liquefied gas, "
           "pressurized cryogenic gas, compressed gas in solution, asphyxiant gas and oxidizing gas, if they don’t "
           "match the definition 2.1 or 2.")
oxidizerinfo = ("HAZMAT Class 5 division 5.1. An oxidizer is a material that may, generally by yielding oxygen, "
                "cause or enhance the combustion of other materials.")
oxygeninfo = ("HAZMAT Class 2 division 2.2 (Alternative Placard). Non-flammable, non-toxic. "
              "Oxygen")
poisoninfo = ("HAZMAT Class 6 division 6.1. Poisonous material is a material, other than a gas, which "
              "is known to be so toxic to humans as to afford a hazard to health during transportation, "
              "or which, in the absence of adequate data on human toxicity")
radioactiveinfo = ("HAZMAT Class 7. Radioactive substances are materials that "
                   "emit radiation.")

symbols = [corrosive, dangerous, dangerousw, explosives, flammable, flammableg, flamables, nfg, oxidizer, oxygen,
                poison, radioactive]


def euclidiana(x, y):
    y = np.array(y)
    r = math.sqrt(np.dot(x-y, x-y))
    return r

def end():
    quit()
def color_image():
    file_path = filedialog.askopenfilename()
    im = cv2.imread(file_path, -1)
    image = cv2.resize(im, (300, 300))

    array = np.asarray(image)#converts 2 array
    arr = (array.astype(float)) / 255.0 #float array
    img_hsv = colors.rgb_to_hsv(arr[..., :3]) #coverts 2 hsv (0-1)

    lu1 = img_hsv[..., 0].flatten() #compacts 2 1D

    H = np.histogram(lu1*256, bins=30)[0]
    v1 = (H/sum(H))

    r = np.zeros(12, float)
    j = 0
    for i in symbols:
        r[j] = euclidiana(v1, i)
        j += 1

    index_min = np.argmin(r)
    if index_min == 0:
        print(corrosiveinfo)
    elif index_min == 1:
        print(dangerousinfo)
    elif index_min == 2:
        print(dangerouswinfo)
    elif index_min == 3:
        print(explosivesinfo)
    elif index_min == 4:
        print(flammableinfo)
    elif index_min == 5:
        print(flammableginfo)
    elif index_min == 6:
        print(flammablesinfo)
    elif index_min == 7:
        print(nfginfo)
    elif index_min == 8:
        print(oxidizerinfo)
    elif index_min == 9:
        print(oxygeninfo)
    elif index_min == 10:
        print(poisoninfo)
    elif index_min == 11:
        print(radioactiveinfo)

    quit()

root = tk.Tk()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))

label = tk.Label(root, width="20", height="3", text="Insert the Image", bg="#2E86C1").pack()
colorbutton = tk.Button(root, text="JPG or PNG format", command=color_image, bg="#F1C40F")
colorbutton.pack()
quitbutton = tk.Button(root, text="Quit", command=end, bg="#CB4335")
quitbutton.pack()

root.mainloop()

