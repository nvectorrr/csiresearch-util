import matplotlib.pyplot as plt
import numpy as np

acrr_red_20 = [99.08940397350993, 99.25165562913907, 98.6953642384106, 98.09602649006622, 98.88079470198676, 98.25496688741721, 98.05960264900662, 98.2384105960265, 98.41059602649007, 98.20860927152319, 98.4205298013245, 98.65562913907284, 98.53973509933775, 98.12582781456953, 98.27814569536424, 98.22847682119206, 97.99668874172185, 98.40066225165562, 98.27152317880795, 98.2251655629139, 98.09933774834437, 97.97682119205298, 97.88741721854305, 97.97350993377484, 97.88079470198674, 97.7980132450331, 97.74834437086093, 97.51655629139073, 97.53311258278146]
accr_oob_20 = [97.15894039735099, 97.6225165562914, 97.43377483443709, 97.00993377483444, 96.44701986754967, 96.66225165562913, 96.67880794701986, 97.23178807947019, 97.44701986754967, 97.24834437086093, 96.99668874172185, 96.69205298013244, 96.38741721854305, 96.74172185430464, 96.42384105960264, 96.44039735099338, 96.85761589403974, 96.55629139072848, 96.47350993377484, 96.53311258278146, 95.78476821192054, 96.69867549668875, 96.06953642384106, 96.17880794701986, 95.63245033112582, 95.94701986754967, 96.0728476821192, 96.00331125827815, 95.68543046357615]
n_feat_20 = [5, 6, 7, 9, 10, 11, 13, 15, 16, 18, 20, 23, 25, 27, 31, 32, 36, 40, 42, 45, 52, 55, 60, 68, 71, 80, 87, 97, 110]

accr_oob_40 = [98.16667808923309, 98.10842300047975, 98.0090466726064, 97.98163251319306, 98.20094578849977, 98.1975190185731, 98.16667808923309, 98.13241038996642, 98.14611746967309, 98.7286683572065, 98.74580220683983, 98.74237543691316, 98.87259269412651, 98.93770132273319, 99.04050442053321, 99.0507847303132, 99.00623672126653, 99.08505242957987, 99.17072167774656, 99.08847919950654, 99.04050442053321, 99.08162565965321, 99.12960043862655, 99.15016105818655, 99.21184291686657, 99.17072167774656, 99.2700980056199, 99.13988074840655, 99.21184291686657, 99.25296415598656, 99.31464601466658, 99.2495373860599, 99.22554999657322, 99.32835309437324, 99.3009389349599]
accr_red_40 = [98.02275375231308, 97.54985950243301, 97.23116989925296, 97.37852100609965, 98.2386402576931, 98.14611746967309, 97.73490507847303, 97.78287985744637, 97.61496813103967, 97.41964224521965, 97.73147830854636, 97.54985950243301, 96.71372764032623, 97.31341237749298, 97.51901857309299, 97.24145020903296, 96.94332122541293, 97.10095264203962, 96.6657528613529, 96.9570283051196, 96.94332122541293, 96.84394489753959, 97.08039202247961, 97.47789733397299, 97.09067233225962, 96.87135905695293, 97.09409910218628, 97.08724556233295, 97.12151326159962, 97.01185662394627, 97.13522034130628, 97.10095264203962, 96.62120485230622, 97.11465972174628, 96.4464395860462]
n_feat_40 = [5, 6, 7, 8, 10, 11, 13, 14, 16, 18, 20, 22, 25, 27, 31, 33, 37, 41, 44, 48, 50, 55, 61, 65, 69, 74, 79, 86, 92, 99, 107, 116, 123, 133, 144]

y1 = np.array(acrr_red_20)
y2 = np.array(accr_oob_20)
y3 = np.array(accr_red_40)
y4 = np.array(accr_oob_40)
x1 = np.array(n_feat_20)
x2 = np.array(n_feat_40)

theta1 = np.polyfit(x1, y1, deg=5)
model1 = np.poly1d(theta1)

theta2 = np.polyfit(x1, y2, deg=5)
model2 = np.poly1d(theta2)

theta3 = np.polyfit(x2, y3, deg=5)
model3 = np.poly1d(theta3)

theta4 = np.polyfit(x2, y4, deg=5)
model4 = np.poly1d(theta4)

plt.plot(x1, y1, 'o', color="blue", markersize=4)
plt.plot(x1, model1(x1), color="blue", linewidth=1.5) # blue, our, 20
plt.plot(x1, y2, 'o', color="orange", markersize=4)
plt.plot(x1, model2(x1), color="orange", linewidth=1.5) # orange, scikit, 20
plt.plot(x2, y3, 'o', color="green", markersize=4)
plt.plot(x2, model3(x2), color="green", linewidth=1.5) # green, our, 40
plt.plot(x2, y4, 'o', color="red", markersize=4)
plt.plot(x2, model4(x2), color="red", linewidth=1.5) # red, scikit, 40

plt.axhline(y=97.49, color='black', linestyle='--') # raw 224
plt.axhline(y=96.69, color='grey', linestyle='--') # raw 456
plt.grid(linewidth=1.5)
plt.show()