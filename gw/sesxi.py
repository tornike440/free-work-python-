amount = input("ramdenis shemotana gsurt?")
months= input("ramdentviani sesxi gvnebavt?")


if months in [3,6,9,12,15,18,21,24]:
  if amount <= 1500:
    annual_rate = 0.12  #  წლიური განაკვეთი 12%
    monthly_rate = 0.03  # ყოველთვიური 3%
  if 1500 < amount <= 10000:
        annual_rate = 0.09  # წლიური განაკვეთი 9%
        monthly_rate = 0.017  # ყოველთვიური 1.7%
  if 10000 < amount <= 50000:
        annual_rate = 0.078  # წლიური განაკვეთი 7.8%
        monthly_rate = 0.012  # ყოველთვიური 1.2%
  if 50000 < amount <= 500000:
        annual_rate = 0.018  # წლიური განაკვეთი 1.8%
        monthly_rate = 0.0012 # ყოველთვიური 0.012%

if months in [27,30,33,36,39,42,45,48,51,54,57,60]:
   if amount <= 1500:
    annual_rate = 0.15  #  წლიური განაკვეთი 15%
    monthly_rate = 0.04  # ყოველთვიური 3%
   if 1500 < amount <= 10000:
        annual_rate = 0.10  # წლიური განაკვეთი 10%
        monthly_rate = 0.02 # ყოველთვიური 2 %
   if 10000 < amount <= 50000:
        annual_rate = 0.09  # წლიური განაკვეთი 9%
        monthly_rate = 0.015  # ყოველთვიური 1.5%
   if 50000 < amount <= 500000:
        annual_rate = 0.02  # წლიური განაკვეთი 2%
        monthly_rate = 0.0012 # ყოველთვიური 0.012%