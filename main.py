import matplotlib.pyplot as plt
import pandas as pd
import numpy as npy

col_count = 3
bar_width = .1

korea_scores = (554, 536, 522)
canada_scores = (500, 512, 511)
usa_scores = (211, 202, 218)
kenya_scores = (150, 200, 130)

index = npy.arange(col_count)

k1 = plt.bar(index, korea_scores, bar_width , alpha = .4, 
                label = "Korea")
c1 = plt.bar(index + bar_width * 1, canada_scores, 
                bar_width, alpha = .4, label = "Canada")
u1 = plt.bar(index + bar_width * 2, usa_scores, 
                bar_width, alpha = .4, label = "USA")
ke1  = plt.bar(index + bar_width * 3, kenya_scores, 
                bar_width, alpha = .4, label = "Kenya")

def Create_Labels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / 2.,
            height * 1.05, '%d' % int(height),
            ha = 'center', va = 'bottom')

Create_Labels(k1)
Create_Labels(c1)
Create_Labels(u1)
Create_Labels(ke1)

plt.title("Info")
plt.ylabel("Score")
plt.xlabel("Subjects")

plt.xticks(index + .3 / 2, ("Math", "Read", "Science"))
plt.grid(True)
plt.legend(frameon = False, loc = 2, bbox_to_anchor = (1, 1))

plt.show()





# data = [{ # Old method
#     'name': 'Eon',
#     'jan_ir': 124,
#     'feb_ir': 100,
#     'mar_ir': 165
# },
# {
#     'name': 'Panda',
#     'jan_ir': 122,
#     'feb_ir': 143,
#     'mar_ir': 3
# }]

# # With Panda
# raw_data = {'names': ['Joe', 'Paul', 'Guy', 'Mike'],
#             'jan_ir': [143, 122, 101, 365],
#             'feb_ir': [100, 201, 134, 122],
#             'mar_ir': [200, 312, 122, 500]}

# df = pd.DataFrame(raw_data, columns=['names', 'jan_ir',
#                                     'feb_ir', 'mar_ir'])

# df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['mar_ir']

# color = [(1, .4, .4), (1, .6, 1), (.4, 1, 1), (.8, 1, .2)]

# plt.pie(df['total_ir'], 
#             labels = df['names'], 
#             colors =color,
#             autopct ='%1.1f%%')

# lbls = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl'
# size = [33, 52, 12, 17, 62, 48]
# seperator = (.2, .1, .4, .1 ,0 ,.5)

# plt.axis('equal')
# plt.pie(size, labels=lbls, autopct='%1.1f%%', explode=seperator)

# years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 
#         1990, 1995, 2000, 2005, 2010, 2015]
# pops = [2.5, 2.7, 3.0, 3.3, 3.6, 4.0, 4.4, 
#         4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

# deaths = [1.2, 1.7, 2.0, 3.3, 3.0, 3.1, 3.5, 4.0, 4.5,
#             4.3, 1.0, 5.0, 5.3, 5.4]

# plt.grid(True)
# lines = plt.plot(years, pops, years, deaths)

# plt.setp(lines, marker="o")

# # plt.plot(years, pops, '--', color=(255/255,0/255,0/255))
# # plt.plot(years, deaths, color=(0/255,0/255,255/255))

# # plt.ylabel("Population (Billions)")
# # plt.xlabel("Year")
# # plt.title("Population Growth")

plt.show()