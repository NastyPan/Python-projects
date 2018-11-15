import numpy as np
import matplotlib.pyplot as plt

n_groups = 14

productions = (739, 756, 16844, 43529, 30863, 47922, 60642,
               50601, 62744, 79721, 92418, 45494, 18587, 3909)


fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.25

opacity = 0.3
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, productions, bar_width,
                alpha=opacity, color=['green'],
                error_kw=error_config)

ax.text(6.5, -8500, 'Years', fontsize=15)
ax.text(5, 98000, 'Production of asbestos', fontsize=15)
ax.text(-2, 45000, 'Tonnes', fontsize=15, rotation=90)
ax.set_xticks(index + bar_width /200)
ax.set_xticklabels(('1970', '1971', '1972', '1973',
                    '1974', '1975', '1976', '1977', '1978',
                    '1979', '1980', '1981', '1982', '1983'))

ax.legend()

fig.tight_layout()
plt.show()
