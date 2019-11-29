try:
    a=int(input())
except ValueError:
    print("ValueError")
except EOFError:
    print("EOFError Found")
except KeyboardInterrupt:
    print("Keyboard Interrupt error") 

