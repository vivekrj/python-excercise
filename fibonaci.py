def fib(n):
 if n == 0:
  return 0
 elif n == 1:
  return 1

 else:
  return fib(n-1) + fib(n-2)

def main():
 n = input ("enter the number:")
 print "the fibonacci number is :",fib(n)

main()
