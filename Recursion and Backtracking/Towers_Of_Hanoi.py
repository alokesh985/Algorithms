# n is number of disks, 3 rods: "from", "to" and "auxillary"

def TowersOfHanoi(n, from_rod, to_rod, auxillary_rod):
    if(n == 1):
        print(f"Move disk 1 from rod {from_rod} to {to_rod} through {auxillary_rod}")
        return
    else:

        # Move (n-1) rods from "from_rod" to "auxillary_rod" through "to_rod"
        TowersOfHanoi(n-1, from_rod, auxillary_rod, to_rod)
        
        print(f"Move disk {n} from rod {from_rod} to {auxillary_rod} through {to_rod}")

        # Move (n-1) disks from "auxillary_rod" to "to_rod" using "from_rod"

        TowersOfHanoi(n-1, auxillary_rod, to_rod, from_rod)


def main():
    disks = int(input("Enter Number of disks to transfer: "))

    # Say, the names of the rods are A, B and C
    TowersOfHanoi(disks, "A", "B", "C")

if __name__ == "__main__":
    main()

