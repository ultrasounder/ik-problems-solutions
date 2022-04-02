from curses.ascii import isdigit


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = [] # global bag

        def helper(S, i, slate):
            if i == len(S):
                result.append(slate) # Append the partial solution to the result
            else: # recursive case
                if S[i].isdigit:
                    helper(S,i+1, slate + S[i].upper())
                    helper(S, i+1, slate + S[i].lower())
        helper(S, 0, "")
        return result


