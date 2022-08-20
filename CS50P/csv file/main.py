
def main():
    with open("data.csv") as file:
        for line in file:
           row = line.rstrip().split(",") 
           print(f"{row[0]} is the {row[1]} of {row[2]}.")


if __name__ == "__main__":
    main()