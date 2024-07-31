def reverse(stri):
  mylist=[]
  for i in range(len(stri)-1,-1,-1):
    mylist.append(stri[i])
  return ''.join(mylist)


x = reverse('hello')
print(x)  


def another_rev(stri):
    rev = stri[::-1]

    return rev


print(another_rev('louie'))
