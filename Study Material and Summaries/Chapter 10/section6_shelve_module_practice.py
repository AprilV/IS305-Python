# SECTION 6: SHELVE MODULE - Practice

# Q1: Import shelve module, create variable shelf by opening shelve 'mydata', save ['dog', 'cat', 'bird'] under key 'pets', close
# Example: shelf = shelve.open('data')
# Example: shelf['animals'] = ['lion', 'tiger']
# Example: shelf.close()
import shelve
shelf = shelve.open('mydata')
shelf['pets'] = ['dog', 'cat', 'bird']
shelf.close()



# Q2: Create variable shelf by opening 'mydata', print shelf['pets'], close
# Example: shelf = shelve.open('data')
# Example: print(shelf['animals'])
# Example: shelf.close()
shelf = shelve.open('mydata')
print(shelf['pets'])
shelf.close()



# Q3: Create variable shelf by opening 'mydata', save list [1,2,3] as 'numbers', 42 as 'count', dict {'name':'Alice','age':30} as 'info', close
# Example: shelf = shelve.open('data')
# Example: shelf['items'] = [4, 5]
# Example: shelf['total'] = 99
# Example: shelf['user'] = {'id': 'Bob'}
# Example: shelf.close()
shelf = shelve.open('mydata')
shelf['numbers'] = [1,2,3]
shelf['count'] = 42
shelf['info'] = {'name':'Alice','age':30}
shelf.close()


# Q4: Create variable shelf by opening 'mydata', print all keys using list(shelf.keys()), close
# Example: shelf = shelve.open('data')
# Example: print(list(shelf.keys()))
# Example: shelf.close()




# Q5: Use with statement to open 'mydata' as variable shelf, set shelf['test']='value', print it
# Example: with shelve.open('data') as shelf:
# Example:     shelf['item'] = 'data'
# Example:     print(shelf['item'])



