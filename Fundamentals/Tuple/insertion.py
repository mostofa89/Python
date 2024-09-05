given_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
new_tuple = ()

for i in range(len(given_tuple)):
  if i %2 == 0:
    new_tuple += given_tuple[i],

print(new_tuple)