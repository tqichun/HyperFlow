import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.preprocessing import LabelEncoder as SklearnLabelEncoder

from hyperflow.utils.data import arraylize

__all__ = ["LabelEncoder"]


class LabelEncoder(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        X=arraylize(X)
        encoders = []
        for i in range(X.shape[1]):
            cur = X[:, i]
            encoder = SklearnLabelEncoder().fit(cur[cur != -999])
            encoders.append(encoder)
        self.encoders = encoders
        return self

    def transform(self, X, y=None):
        X=arraylize(X)
        arrs = []
        assert X.shape[1] == len(self.encoders)
        for i in range(X.shape[1]):
            cur = X[:, i]
            arr = np.zeros_like(cur)
            encoder = self.encoders[i]
            arr[cur != -999] = encoder.transform(cur[cur != -999])
            arr[cur == -999] = -999
            arrs.append(arr)
        return np.vstack(arrs).T


