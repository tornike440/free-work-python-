import re
from collections import defaultdict

# Polynomial multiplication
def pollinomeMultiplication(c, d):
    a = c[0]
    b = d[0]
    realanswer = []
    answer = []

    for i in range(len(c)):
        first = []
        first.append(a + b + i)
        for j in d:
            first.append(c[i] * j)
        answer.append(first)

    for m in range(1, len(answer)):
        answer[m] = [0] * (m + 1) + answer[m][1:]

    max_length = max(len(row) for row in answer)
    for row in answer:
        while len(row) < max_length:
            row.append(0)

    for i in range(len(answer[0])):  # Sum columns
        total = 0
        for j in range(len(answer)):
            total += answer[j][i]
        realanswer.append(total)

    return realanswer

# Polynomial addition with different starting powers
def diffpowerpollinomeaddition(c, d):
    answer = []
    if c[0] < d[0]:
        answer.append(c[0])
        diff = d[0] - c[0]
        d[0] = 0
    else:
        answer.append(d[0])
        diff = c[0] - d[0]
        c[0] = 0

    if len(c) < len(d):
        for i in range(diff):
            d.insert(1, 0)
    else:
        for i in range(diff):
            c.insert(1, 0)

    if len(c) > len(d):
        for i in range(len(c) - len(d)):
            d.append(0)
    else:
        for i in range(len(d) - len(c)):
            c.append(0)

    for i in range(len(c)):
        a = c[i] + d[i]
        answer.append(a)

    return answer

# Matrix multiplication
def matrixMultiplication(c, d):
    answer = []
    for i in range(0, 9, 3):
        firstmul = pollinomeMultiplication(c[i], d[0])
        secondmul = pollinomeMultiplication(c[i + 1], d[3])
        thirdmul = pollinomeMultiplication(c[i + 2], d[6])
        firstadd = diffpowerpollinomeaddition(firstmul, secondmul)
        secondadd = diffpowerpollinomeaddition(firstadd, thirdmul)
        answer.append(secondadd)
    return answer

# Remove zero terms from symbolic expressions
def removeZeroes(string):
    if not isinstance(string, str):
        return string  # Return the input unchanged if it's not a string
    terms = string.split(" + ")
    terms = [term for term in terms if not term.startswith("0*")]
    return " + ".join(terms) if terms else "0"

# Distribute symbolic terms
def distribute_symbolic(symbol_str, multiplier):
    terms = symbol_str.replace("-", "+-").split("+")
    result_terms = []

    for term in terms:
        term = term.strip()
        if not term:
            continue
        match = re.match(r"(-?\d*)([a-zA-Z].*)", term)
        if match:
            coeff_str, var_part = match.groups()
            coeff = int(coeff_str) if coeff_str not in ("", "+", "-") else int(coeff_str + "1") if coeff_str else 1
            new_coeff = coeff * multiplier
            result_terms.append(f"{new_coeff}{var_part}")
        else:
            result_terms.append(f"{multiplier}*{term}")
    return " + ".join(result_terms)

# Symbolic polynomial multiplication
def symbolicPolynomialMultiplication(c, d):
    if not isinstance(c[0], int) or not isinstance(d[0], int):
        raise ValueError("First elements of both lists must be integers (starting powers)")

    a = c[0]
    b = d[0]
    poly_c = c[1:]
    poly_d = d[1:]

    for val in poly_d:
        if not isinstance(val, int):
            raise ValueError("All elements in d (after the first) must be integers")

    terms = defaultdict(lambda: defaultdict(int))  # {power: {symbol: coefficient}}

    for i, coeff_c in enumerate(poly_c):
        for j, coeff_d in enumerate(poly_d):
            power = a + b + i + j
            symbol_expr = coeff_c

            if isinstance(symbol_expr, str):
                distributed = distribute_symbolic(symbol_expr, coeff_d)
                for term in distributed.split(" + "):
                    match = re.match(r"(-?\d+)\*?(.+)", term.strip())
                    if match:
                        count, symbol = match.groups()
                        terms[power][symbol] += int(count)
            else:
                symbol = str(symbol_expr)
                terms[power][symbol] += coeff_d

    result = []
    min_power = min(terms)
    max_power = max(terms)

    for p in range(min_power, max_power + 1):
        if p in terms:
            parts = []
            for symbol, count in terms[p].items():
                if count == 1:
                    parts.append(f"{symbol}")
                else:
                    parts.append(f"{count}*{symbol}")
            result.append(" + ".join(parts))
        else:
            result.append("0")

    result.insert(0, min_power)

    for i in range(1, len(result)):
        result[i] = removeZeroes(result[i])

    return result

# Combine symbolic terms
def combineTerms(term1, term2):
    terms = defaultdict(int)  # Dictionary to store coefficients of variables

    # Parse and add terms from term1
    for part in term1.split(" + "):
        match = re.match(r"(-?\d*)\*?([a-zA-Z].*)?", part.strip())
        if match:
            coeff, var = match.groups()
            coeff = int(coeff) if coeff not in ("", "+", "-") else int(coeff + "1")
            terms[var] += coeff

    # Parse and add terms from term2
    for part in term2.split(" + "):
        match = re.match(r"(-?\d*)\*?([a-zA-Z].*)?", part.strip())
        if match:
            coeff, var = match.groups()
            coeff = int(coeff) if coeff not in ("", "+", "-") else int(coeff + "1")
            terms[var] += coeff

    # Reconstruct the combined term
    combined = []
    for var, coeff in terms.items():
        if coeff == 0:
            continue
        elif coeff == 1:
            combined.append(f"{var}")
        elif coeff == -1:
            combined.append(f"-{var}")
        else:
            combined.append(f"{coeff}*{var}")

    return " + ".join(combined) if combined else "0"

# Add symbolic polynomials
def addSymbolicPolynomials(c, d):
    power_c = c[0]
    power_d = d[0]
    min_power = min(power_c, power_d)

    # Pad the shorter polynomial with zeroes
    pad_c = ["0"] * (power_d - power_c) if power_c < power_d else []
    pad_d = ["0"] * (power_c - power_d) if power_d < power_c else []

    coeffs_c = pad_c + c[1:]
    coeffs_d = pad_d + d[1:]

    # Pad shorter list to match lengths
    max_len = max(len(coeffs_c), len(coeffs_d))
    coeffs_c += ["0"] * (max_len - len(coeffs_c))
    coeffs_d += ["0"] * (max_len - len(coeffs_d))

    # Combine symbolic terms
    result = [min_power]
    for term_c, term_d in zip(coeffs_c, coeffs_d):
        if term_c == "0" and term_d == "0":
            result.append("0")
        elif term_c == "0":
            result.append(term_d)
        elif term_d == "0":
            result.append(term_c)
        else:
            combined = combineTerms(term_c, term_d)
            result.append(combined)

    # Simplify each term using removeZeroes
    for i in range(1, len(result)):
        result[i] = removeZeroes(result[i])

    return result

def clean_polynomial(v):
    for poly in v:
        if len(poly) > 1:
            # Step 1: Find first real (non-"0") coefficient
            first_real_idx = None
            for idx in range(1, len(poly)):
                if poly[idx] != '0':
                    first_real_idx = idx
                    break

            # Step 2: If we found a real term
            if first_real_idx is not None:
                zeros_before = first_real_idx - 1  # Don't include power
                poly[0] += zeros_before  # Increase power
                poly[:] = [poly[0]] + poly[first_real_idx:]  # Trim leading '0's

            # Step 3: Remove trailing '0's (but only if we still have more than the power)
            while len(poly) > 1 and poly[-1] == '0':
                poly.pop()

    poly[0]-=1

    #now check if v has more than 6 elements
    #if so cut it to 6 elements
    if len(v) > 6:
        v = v[:6]
    return v



v = [-5, '0', '0','0', '0','2a+3b', '0', '0', '0', '-4a+9b', '0', '0', '0', '0', 'a', '0', '0']

# Clean the polynomial
v = clean_polynomial([v])

print(v)






