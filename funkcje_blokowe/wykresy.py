import matplotlib.pyplot as plt

data_sizes = [1.0, 3.0, 10.0]
modes = ['ECB', 'CBC', 'OFB', 'CFB', 'CTR']
encryption_times = [
    [0.000747, 0.001879, 0.001861, 0.019798, 0.000744],
    [0.001976, 0.005512, 0.006146, 0.058364, 0.002640],
    [0.006979, 0.023874, 0.029980, 0.251175, 0.008241]
]
decryption_times = [
    [0.000642, 0.001445, 0.001862, 0.019706, 0.000791],
    [0.001873, 0.004926, 0.005704, 0.058585, 0.002432],
    [0.007124, 0.022203, 0.029934, 0.244379, 0.008114]
]


fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 18))

for i, size in enumerate(data_sizes):
    axes[i].bar(modes, encryption_times[i], color='skyblue')
    axes[i].set_title(f'Encryption Time for Data Size {size} MB')
    axes[i].set_xlabel('Encryption Mode')
    axes[i].set_ylabel('Time (s)')
    axes[i].grid(True)

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 18))

for i, size in enumerate(data_sizes):
    axes[i].bar(modes, decryption_times[i], color='lightgreen')
    axes[i].set_title(f'Decryption Time for Data Size {size} MB')
    axes[i].set_xlabel('Decryption Mode')
    axes[i].set_ylabel('Time (s)')
    axes[i].grid(True)

plt.tight_layout()
plt.show()
