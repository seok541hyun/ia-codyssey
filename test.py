try:
    number = float(input("밑(숫자)을 입력하세요: "))
except ValueError:
    print("숫자가 아닙니다.")

try:
    exponent = int(input("지수(몇 번 곱할지)를 입력하세요: "))
except ValueError:
    print("숫자가 아닙니다.")
result = 1
for _ in range(exponent):
    result = number * result

print("당신이 입력한 숫자는:", number)
print("당신이 입력한 지수는:", exponent)
print("결과는:", result)

  


