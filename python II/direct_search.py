class Ordenator:
    def direct_selection(self, list):

        end = len(list)

        for i in range(end - 1):
            minimal_index = i

            for j in range(i + 1, end):
                if list[j] < list[minimal_index]:
                    minimal_index = j

            list[i], list[minimal_index] = list[minimal_index], list[i]

list = [10, 8, 3, -20, -21, 2, 0, 20]
o = Ordenator()
o.direct_selection(list)
print(list)
