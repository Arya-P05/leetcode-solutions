class Solution:
    def bestClosingTime(self, customers: str) -> int:
        '''
        if shop open and 'N' penalty += 1
        if shop closed and 'Y' penalty += 1
        return the index giving us the smallest penalty
        '''

        length = len(customers)

        prefix_n = [0] * (length + 1)
        postfix_y = [0] * (length + 1)

        for idx in range(1, length + 1):
            prefix_n[idx] = prefix_n[idx - 1]
            if (customers[idx - 1] == 'N'):
                prefix_n[idx] += 1
        
        for idx in range(length - 1, -1, -1):
            postfix_y[idx] = postfix_y[idx + 1]
            if customers[idx] == 'Y':
                postfix_y[idx] += 1
        
        min_penalty = float("inf")
        min_idx = 0

        for idx in range(length + 1):
            penalty = prefix_n[idx] + postfix_y[idx]
            if penalty < min_penalty:
                min_penalty = penalty
                min_idx = idx
        
        return min_idx