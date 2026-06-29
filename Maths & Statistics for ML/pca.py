from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

data = {
    "study_hours" : [2,4,6,8,10],
    "sleep_hours" : [8,7,6,5,4],
    "Marks" : [50,60,70,85,95]
}

df = pd.DataFrame(data)

scalar = StandardScaler()

x_scaled = scalar.fit_transform(df)

pca = PCA(n_components=2)

x_pca = pca.fit_transform(x_scaled)

print(x_pca)
print("\n", pca.explained_variance_ratio_)