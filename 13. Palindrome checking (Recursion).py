a = str(input("Enter any string you want to check: "))

#Few examples to use as "s":
# 1) Able was I, ere I saw Elba
# 2) eve
# 3)Is this a palindrome

#for changing in lowecase and removing spaces
def isPalindrome(a):

    def toChars(a):
        a = a.lower()
        ans = ''
        for c in a:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    #for checking if palindrome or not
    def isPal(a):
        if len(a) <= 1:
            return True
        else:
            return a[0] == a[-1] and isPal(a[1:-1])

    return isPal(toChars(a))

print(isPalindrome(a))