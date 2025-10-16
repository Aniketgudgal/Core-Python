#Q19. Given a score out of 100, print Excellent (≥90), Good (≥75), Average (≥50), Poor (< 50) — using nested ternary operators.

score = int(input("Enter the score: "))

if score >= 90 and score <= 100:
	print("Score is Excellent")
elif score >= 75 and score < 90:
	print("Score is Good")
elif score >= 50 and score < 75:
	print("Score is Average")
elif score >= 0 and score < 50:
	print("Score is Poor")
else:
    print("Enter Valid Score")