def lcs(s1,s2):
    if s1 == '' or s2 == '':
        return ''

    elif s1[0] == s2[0]:
        return s1[0] + lcs(s1[1:],s2[1:])

    elif s1[0] not in s2:
        return lcs(s1[1:],s2)

    elif s2[0] not in s1:
        return lcs(s1,s2[1:])

    else:
        if len(lcs(s1[1:],s2)) > len(lcs(s1,s2[1:])):
            return lcs(s1[1:],s2)

        else:
            return lcs(s1,s2[1:])
