from __future__ import (absolute_import, division, print_function, unicode_literals)
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from scipy import stats
import statsmodels.formula.api as sm



data = pd.read_excel(r'last.xlsx', encoding='utf-8')
cols = ['part_sound_id', 'time', 'pitch', 'intonation', 'part_curve_position', 'session', 'verb_lexical_tone', 'translate']
data_new = data[cols]
pcp = data_new.loc[data_new['part_curve_position'] == '_n_']
pcp = pcp.loc[pcp['intonation'] == 'AFF']

#groupby_vlt = data_new.groupby('verb_lexical_tone')
#for verb_lexical_tone, value in groupby_vlt['pitch']:
   # print(groupby_vlt.mean())
#h_pitch = pcp[pcp['verb_lexical_tone'] == 'H']['pitch']
#l_pitch = pcp[pcp['verb_lexical_tone'] == 'L']['pitch']
time_rel = list(pcp['time'])
time_beginning = time_rel[0]
time_abs = [round(i - time_beginning, 6) for i in time_rel]
pcp['time_abs'] = pd.Series(time_abs)
#print(stats.ttest_1samp(h_pitch, 0.05))
from statsmodels.formula.api import ols
#model = pcp("pitch ~ time_abs", pcp).fit()
#
#model = ols("pitch ~ verb_lexical_tone + 1", pcp).fit()
#model = ols('pitch ~ C(verb_lexical_tone)', pcp).fit()
model = ols('pitch ~ verb_lexical_tone + intonation +1', pcp).fit()
print(model.summary())
#seaborn.lmplot(y='pitch', x='', data=data)
result = ols(formula='pitch ~ time_abs + verb_lexical_tone + time_abs * pitch',
              data=pcp).fit()
#fig, ax = plt.subplots()
sns.lmplot(y='pitch', x='time_abs', hue='verb_lexical_tone', data=pcp)

#print(model.summary())
#data = pandas.read_csv('examples/iris.csv')
#model = ols('sepal_width ~ name + petal_length', pcp).fit()
#print(model.summary())
print(result.summary())
plt.show()