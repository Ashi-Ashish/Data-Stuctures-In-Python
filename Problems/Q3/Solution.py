class Solution:
    @staticmethod
    def sort012(arr,n):
        count_arr = [0,0,0]
        counter = 0       
        
        while counter < n:
            count_arr[arr[counter]] += 1
        
        i = 0
        j = 0
        
        # while counter < count_arr:
            


def main():
    array = [0, 2, 1, 2, 0]
    n = 5
    result = Solution.sort012(array, n)
    print(result)


if __name__ == "__main__":
    main()
