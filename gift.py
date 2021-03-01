def taumBday(b, w, bc, wc, z):
    if z>=bc and z>=wc or bc==wc:
        x=(bc*b)+(wc*w)
        print(x)
    else:
        if bc>z and bc>wc:
            val=wc+z
            if(bc>=val):
                x=(b*val)+(w*wc)
                print(x)
            else:
                x=(bc*b)+(wc*w)
                print(x)
        elif wc>z and wc>bc:
            val=bc+z
            if(wc>=val):
                x=(b*bc)+(w*val)
                print(x)
            else:
                x=(bc*b)+(wc*w)
                print(x)


t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    b = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    bc = int(second_multiple_input[0])

    wc = int(second_multiple_input[1])

    z = int(second_multiple_input[2])
    result = taumBday(b, w, bc, wc, z)
