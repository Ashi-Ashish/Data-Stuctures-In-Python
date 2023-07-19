class Solution:
    @staticmethod
    def missingNumber(array, n: int):
        # code here
        total_array = 0
        counter = 0
        while counter < n-1:
            total_array += array[counter]
            counter += 1
        
        expected_total = (n * (n + 1)) // 2
        
        return expected_total - total_array


def main():
    array = [1, 2, 3, 5]
    n = 5
    result = Solution.missingNumber(array, n)
    print(result)


if __name__ == "__main__":
    main()
