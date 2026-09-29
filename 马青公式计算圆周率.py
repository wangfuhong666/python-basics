from decimal import Decimal, getcontext


def calculate_pi(precision=300):


    getcontext().prec = precision + 10  # 额外加10位确保精度


    def arctan(x):
        result = x
        term = x
        n = 1
        while True:
            # 泰勒级数：x - x^3/3 + x^5/5 - x^7/7 + ...
            term *= -x * x * (2 * n - 1) / (2 * n + 1)
            result += term
            # 当项的绝对值小于 1e-(precision+2) 时停止迭代
            if abs(term) < Decimal(10) ** (-(precision + 2)):
                break
            n += 1
        return result

    # 计算 arctan(1/5) 和 arctan(1/239)
    atan1_5 = arctan(Decimal(1) / 5)
    atan1_239 = arctan(Decimal(1) / 239)

    # 应用马青公式
    pi = 16 * atan1_5 - 4 * atan1_239

    # 截取到目标精度并返回
    return pi.quantize(Decimal('1.' + '0' * precision))


# 计算300位精度的π并打印
pi_300 = calculate_pi(300)
print(f"π（300位精度）:\n{pi_300}")
