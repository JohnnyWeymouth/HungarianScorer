from typing import Callable, Any
from scipy.optimize import linear_sum_assignment

class HungarianScorer():
    @staticmethod
    def getBestCombo(listA:list, listB:list, scoringFunc:Callable, *args) -> list[tuple[Any, Any, float]]:
        bestCombo = HungarianScorer.getBestComboAsIndices(listA, listB, scoringFunc, *args)
        decodedCombo = []
        for i, j, score in bestCombo:
            tup = (listA[i], listB[j], score)
            decodedCombo.append(tup)
        return decodedCombo

    @staticmethod
    def getBestComboAsIndices(listA:list, listB:list, scoringFunc:Callable, *args) -> list[tuple[Any, Any, float]]:    
        # Ensure the same number of items for both lists, padding with dummy values if necessary
        if len(listA) != len(listB):
            if len(listA) < len(listB):
                listA += [None] * (len(listB) - len(listA))
            else:
                listB += [None] * (len(listA) - len(listB))

        # Score each matchup
        scores = [[0 for _ in range(len(listB))] for _ in range(len(listA))]
        for i, itemA in enumerate(listA):
            for j, itemB in enumerate(listB):
                if (itemA is not None) and (itemB is not None):
                    scores[i][j] = scoringFunc(itemA, itemB, *args)
                else:
                    scores[i][j] = -1e9  # Assign a very low finite score to dummy pairings

        # Use the Hungarian algorithm to find the optimal assignments
        rowInd, colInd = linear_sum_assignment([[-score for score in row] for row in scores])

        # Format the best combination into a readable form
        bestCombination = []
        for i, j in zip(rowInd, colInd):
            if (listA[i] is not None) and (listB[j] is not None):
                matchupScore = scores[i][j]
                bestCombination.append((i, j, matchupScore))
        return bestCombination