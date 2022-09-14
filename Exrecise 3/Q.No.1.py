length = float(input("enter length of zander in centimeter:"))
if length <= 42:
    print(f"the fish is undersized, release it back to the lake.The missing length is  {42-length:.1f}cm ")
else:
    print("you can take the zander.")
