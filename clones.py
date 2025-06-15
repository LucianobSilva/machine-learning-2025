# %%

import pandas as pd

df = pd.read_parquet("data/dados_clones.parquet")

df['General Jedi encarregado'].unique()

# %%

features = ['Massa(em kilos)', 'Estatura(cm)']
target = 'Status '

X = df[features]
y = df[target]

df.groupby('Status ')[features].mean()
# %%

from sklearn import tree

model = tree.DecisionTreeClassifier()
model.fit(X=X, y=y)

# %%

import matplotlib.pyplot as plt

plt.figure(dpi=400)

tree.plot_tree(
    model,
    feature_names=features,
    class_names=model.classes_,
    filled=True,
    max_depth=5
)
# %%
