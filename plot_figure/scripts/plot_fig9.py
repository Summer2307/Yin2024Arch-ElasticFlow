# This file can draw the subfigures for Figure 9 in our paper.
# Usage: 
# 1. Change the raw values accordingly (existing numbers are our test results)
# 2. python3 draw_fig9.py
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

fontsizeValue=28

label = ["64 GPUs", "128 GPUs", "256 GPUs"]

# edf=[0.026,0.118,0.118]
# edfplus = [0.203,0.326,0.658]
# efminus = [0.452,0.835,0.939]
# ef=[0.926,0.949,0.944]
edf=[0.026,0.126,0.296]
edfplus = [0.146,0.337,0.485]
efminus = [0.235,0.902,0.687]
ef=[0.953,0.94,0.931]

x = np.arange(len(edf))  # the label locations

total_width, n = 0.6, 4
width = total_width / n
x = x - (total_width - width) / 2

fig, (ax1) = plt.subplots(1, 1, sharex=True)

plt.figure(figsize=(10, 7))
plt.grid(True, color="#D3D3D3", zorder=0)
l1 = plt.bar(x-1.5*width, edf, width, zorder=100,edgecolor='purple',hatch='//', color='white')
l2 = plt.bar(x-0.5*width, edfplus, width, zorder=100,edgecolor='orange', hatch='\\', color='white')
l3 = plt.bar(x+0.5*width, efminus, width, zorder=100,edgecolor='green', hatch='-', color='white')
l4 = plt.bar(x+1.5*width, ef, width, zorder=100)

plt.xticks(x, label, fontsize=fontsizeValue)

plt.xlabel("Cluster Size", fontsize=fontsizeValue)
plt.ylabel("Deadline Satisfactory Ratio", fontsize=fontsizeValue)

plt.tick_params(axis='both', which='major', labelsize=fontsizeValue)
#plt.tick_params(bottom=False, top=False, left=False, right=False)

d = .5  # proportion of vertical to horizontal extent o

plt.legend([l1, l2, l3, l4], [
  'EDF', 'EDF + Admission Control', 'EDF + Elastic Scaling', 'ElasticFlow'],fontsize=fontsizeValue,
  ncol=1,loc=3,bbox_to_anchor=(1,0),borderaxespad=0, frameon=False)
plt.savefig("fig9.pdf")

