def main():

  try:
    a = int(input("Enter a number here: "))
    print(a)

  except Exception as b:
    print(b)

  finally:
    print("Hey i am inside finally")

main()

# Finally ka mtlb chalega he chalega it override return

