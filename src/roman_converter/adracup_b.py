def to_roman(arabic: int) -> str:
    result = ""
    Map_roman = [
        (1000,"M"), (900,"CM"), (500, "D"), (400,"CD"),(100, "C"), (90,"XC"), (50,"L"), (40,"XL"),(10, "X"), (9, "IX"), (5,"V"), (4,"IV"),(1,"I")
    ]
    for number, string in Map_roman:
        while arabic >= number:
            result += string
            arabic -= number
    return result

def from_roman(roman: str) -> int:
    # Map_arabic = dict([
    #     ("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10),
    #     ("XL", 40), ("L", 50), ("XC", 90), ("C", 100),
    #     ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)
    # ])
    Map_arabic = dict([
        ("M",1000),("CM",900),("D",500),("CD",400),("C",100),("XC",90),("L",50),("XL",40),("X",10),("IX",9),("V",5),("IV",4),("I",1)
    ])
    result = 0
    for string, number in Map_arabic.items():
        count = 0
        while roman.startswith(string):
            result += number
            print(result)
            count += 1
            roman = roman[len(string):]
            print(roman)
    return result