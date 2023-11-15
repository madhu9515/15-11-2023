print('integer to roman')
class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        r_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                r_num += syb[i]
                num -= val[i]
            i += 1
        return r_num


print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(4000))
