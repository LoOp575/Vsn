import numpy as np

class AnomalyEngine:
    @staticmethod
    def median_absolute_deviation(values):
        x=np.asarray(values,dtype=float)
        med=np.median(x)
        return float(np.median(np.abs(x-med)))

    @staticmethod
    def modified_z_score(values):
        x=np.asarray(values,dtype=float)
        mad=AnomalyEngine.median_absolute_deviation(x)
        if mad==0:
            return np.zeros(len(x)).tolist()
        med=np.median(x)
        return (0.6745*(x-med)/mad).tolist()

    @staticmethod
    def detect(values,threshold=3.5):
        scores=AnomalyEngine.modified_z_score(values)
        return [abs(s)>threshold for s in scores]
