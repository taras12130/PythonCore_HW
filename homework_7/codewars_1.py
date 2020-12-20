# Count of positives / sum of negatives

def count_positives_sum_negatives(arr):
    if arr:
        count_of_positives = 0
        sum_of_negatives = 0
        for i in arr:
            if i == 0:
                pass
            elif i > 0:
                count_of_positives += 1
            elif i < 0:
                sum_of_negatives += i
        res = [count_of_positives, sum_of_negatives]
        return res
    else:
        return []
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))