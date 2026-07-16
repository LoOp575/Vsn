import numpy as np

class TransitionEngine:
    STATES=["PUMP","DISTRIBUTION","DUMP"]

    @staticmethod
    def transition_matrix(labels):
        n=len(TransitionEngine.STATES)
        matrix=np.ones((n,n),dtype=float)
        idx={s:i for i,s in enumerate(TransitionEngine.STATES)}
        for a,b in zip(labels[:-1],labels[1:]):
            if a in idx and b in idx:
                matrix[idx[a],idx[b]]+=1
        matrix=matrix/matrix.sum(axis=1,keepdims=True)
        return matrix.tolist()

    @staticmethod
    def next_state_prob(current_state,matrix):
        idx={s:i for i,s in enumerate(TransitionEngine.STATES)}
        if current_state not in idx:
            return {}
        row=matrix[idx[current_state]]
        return {s:float(row[i]) for i,s in enumerate(TransitionEngine.STATES)}