import zipfile
import os
import shutil

def process_data(data):
    data = data.split('\r\n')
    name_flag = False
    data_flag = False
    name = None
    write_data = []
    for line in data:
        if line.startswith('Comment:'):
            if name == None:
                name = line.strip().split('/')[-1].replace('tif', 'txt')
                continue
            with open(name, 'w') as f:
                for i in write_data[1:-1]:
                    f.write(i + '\r\n')
            name = line.strip().split('/')[-1].replace('tif', 'txt')

        if line.startswith('Tth'):
            write_data.clear()
        write_data.append(line)




def main():
    for z in os.listdir('raw_data'):
        if '.zip' not in z:
            continue
        zf = zipfile.ZipFile('raw_data/' + z)

        if z in os.listdir():
            shutil.rmtree(z)
        os.mkdir(z)
        os.chdir(z)
        for dat in zf.namelist():
            with zf.open(dat) as f:
                data = f.read().decode()
                process_data(data)
                #print(repr(data[:100]))
        os.chdir('..')
        

if __name__ == '__main__':
    main()
