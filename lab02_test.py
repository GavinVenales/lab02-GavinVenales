from lab02 import seconds_to_hms, admission_price, sum_multiples, total_of_positives


def test_seconds_to_hms():
    assert seconds_to_hms(3661) == "1:01:01"
    assert seconds_to_hms(59) == "0:00:59"
    assert seconds_to_hms(3600) == "1:00:00"
    assert seconds_to_hms(7325) == "2:02:05"
    assert seconds_to_hms(0) == "0:00:00"

totalseconds = int(input('Input Seconds: '))
remainder: int = 0
hours: int = (totalseconds // 3600)
remainder = (totalseconds % 3600)
minutes: int = (remainder // 60) 
remainder = (totalseconds % 60)
result = f"{hours:02d}:{minutes:02d}:{remainder:02d}"
print(f"{hours:02d}:{minutes:02d}:{remainder:02d}")

def test_admission_price():
    assert admission_price(3) == 0
    assert admission_price(5) == 8
    assert admission_price(12) == 8
    assert admission_price(13) == 15
    assert admission_price(64) == 15
    assert admission_price(65) == 10
    assert admission_price(30) == 15
    assert admission_price(70) == 10

age = int(input('Enter Age: '))
ticket1: float = 0.00
ticket2: float = 8.00
ticket3: float = 15.00
ticket4: float = 10.00
if age < 5:
    print(f"{ticket1:.2f}")
if 5 <= age <= 12:
    print(f"{ticket2:.2f}")
if 13 <= age <= 64:
    print(f"{ticket3:.2f}")
if age >= 65:
    print(f"{ticket4:.2f}")

def sum_multiples(limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

def test_sum_multiples():
    assert sum_multiples(10) == 23
    assert sum_multiples(1) == 0
    assert sum_multiples(0) == 0
    assert sum_multiples(16) == 60
    assert sum_multiples(20) == 78
    print("Part 3: All tests passed.")
#Was not able to get part 3 properly outputting, so I did part 4.

# STRETCH (optional) - skipping this one still passes the three above.
def total_of_positives(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

def test_total_of_positives():
    assert total_of_positives([1, -2, 3, -4, 5]) == 9
    assert total_of_positives([-1, -2]) == 0
    assert total_of_positives([]) == 0
    assert total_of_positives([10, 20]) == 30
    print("Part 4: All tests passed.")

test_total_of_positives()