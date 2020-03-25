import numpy as np
from sklearn.preprocessing import  LabelEncoder
from autopipeline.pipeline.components.feature_engineer.encode.base import BaseEncoder

__all__ = ["HashingEncoder"]


class HashingEncoder(BaseEncoder):
    class__ = "HashingEncoder"
    module__ = "category_encoders"

    def fit(self, X_train, y_train=None,
            X_valid=None, y_valid=None,
            X_test=None, y_test=None):
        df = X_train.filter_feat_grp(self.in_feat_grp)
        cardinality = 0
        for i in range(df.shape[1]):
            cardinality += np.unique(df.iloc[:, i].astype("str")).size
        self.cardinality = cardinality
        return super(HashingEncoder, self).fit(X_train, y_train, X_valid, y_valid, X_test, y_test)