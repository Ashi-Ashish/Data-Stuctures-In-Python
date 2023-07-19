class Solution:
    @staticmethod
    def subarraySum(arr, N, S):
        start = 0
        end = 0
        curr_sum = 0

        if S == 0:
            return [-1]

        while end < N:
            curr_sum += arr[end]

            while curr_sum > S:
                curr_sum -= arr[start]
                start += 1

            if curr_sum == S:
                return [start + 1, end + 1]

            end += 1

        return [-1]


def main():
    arr = [1, 2, 3, 4]
    N = 4
    S = 0
    result = Solution.subarraySum(arr, N, S)
    print(result)


if __name__ == "__main__":
    main()
