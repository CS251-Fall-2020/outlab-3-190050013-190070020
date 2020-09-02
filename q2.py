import argparse

def process(inputs):
    path = []

    for i in inputs:
            if (i == '.' or i == ''):
                continue
            elif (i == '..'):
                path = path[0:-1]
            else:
                path.append(i)
    return path

def print_path(path,output_file):
    with open(output_file,'w') as fout:
        for i in path:
            fout.write('/')
            fout.write(i)
        if (len(path) == 0):
            fout.write('/')


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-in","--infile")
    parser.add_argument("-out","--outfile")
    args = parser.parse_args()


    input_string = ''
    with open(args.infile) as fin:
        input_string = fin.readline()

    if input_string[-1] == '\n':
        input_string = input_string[0:-1]
    input_string = input_string.strip()
    
    
    input_string = '/' + input_string + '/'
    inputs = input_string.split('/')

    path = process(inputs)
    print_path(path,args.outfile)

    

if __name__ == "__main__":
    main()
    
