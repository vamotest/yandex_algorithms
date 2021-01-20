
def main(string):
    temp_str = []
    result = 0
    
    for _, letter in enumerate(string, start=1):
        
        if letter not in temp_str:
            temp_str.append(letter)
        
        else:
            index = temp_str.index(letter)
            temp_str = temp_str[index + 1:] + list(letter)
        
        if len(temp_str) > result:
            result = len(temp_str)
    
    return result
    

if __name__ == '__main__':
    print(main(str(input())))
