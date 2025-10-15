def main():
    string = [val for val in input()]
    if string[0] != string[-1]:
        if string[0] == "a" :
            string[-1] = "a"
        else:
            string[-1] = "b"
    print("".join(string))
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()