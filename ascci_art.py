def print_art(c_set, text, w, h):
    # st = (P-1)*O, en = st+O-1
    indx_list = [(ord(ch)-65)*w if ord(ch)>= 65 and ord(ch)<=90 else 26*w for ch in text]
    # print(indx_list)
    for i in range(h):
        for indx in indx_list:
            for j in range(w):
                print(c_set[i][indx+j], end='')
        print('')

w = int(input())
h = int(input())
char_set = [ input() for i in range(h)]
text = input()
print('---------------------')
print_art(char_set, text.upper(), w, h)
