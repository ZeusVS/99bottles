# 99 Bottles project
# https://web.archive.org/web/20180612183650/https://github.com/jorgegonzalez/beginner-projects#99-bottles
def bottle(n):
    if n == 1:
        return "bottle"
    else:
        return "bottles"

txt = "{0} {2} of beer on the wall. {0} {2} of beer.\nTake one down, pass it around, {1} {3} of beer on the wall."
for i in range(99,0,-1):
    print(txt.format(i, i - 1, bottle(i), bottle(i - 1)))