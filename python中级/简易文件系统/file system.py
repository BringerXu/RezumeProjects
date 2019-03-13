#zhengyix 68996560 zengao 24272871
#C:/Users/ZhengyiXu/Desktop/ICS32 file system
from pathlib import Path
import shutil

def scan(root:dir,result:list)->list:
    '''
    return a list including all files in given root;scan root directory thoroughly 
    '''
    for item in root.iterdir():
        if item.is_file():
            result.append(item)
        elif item.is_dir:
            scan(item,result)
    return result

def sndo(List:list)->None:
    '''
    process print path of files, print firstline of files, duplicate files, touch files from given path filesList
    '''
    o=input()
    if o=='P':
        for path in List:
            print(str(path))
    elif o=='F':
        for path in List:
            file=open(str(path),'r')
            print('{}\n{}'.format(str(path),file.readline()))
            file.close()
    elif o=='D':
        for path in List:
            print(str(path))
            shutil.copyfile(path.name,path.name+".dup")
    elif o=='T':
        for path in List:
            print(str(path)+'\n'+str(path.stat().st_mtime))
            path.touch()
            print(str(path.stat().st_mtime))
    else:
        sndo(List)

def main()->None:
    '''
    using recursion to control structure
    '''
    try:
        r=input()
        root=Path(r)
    except:
        print('Error')
    else:
        if root.exists():
            container=[]
            container2=[]
            container=scan(root,container)
            o=input()
            command=o.split()[0]
            trigger=o.split()[1]	
            if command=='N':
                for item in container:
                    if item.name==trigger:
                        container2.append(item)
                sndo(container2)
            elif command=='E':
                for item in container:
                    if item.suffix==trigger or item.suffix=='.'+trigger:
                        container2.append(item)
                sndo(container2)
            elif command=='S':
                for item in container:
                    if item.stat().st_size>int(trigger):
                        container2.append(item)
                sndo(container2)
            else:
                print('Error')
        else:
            print('Error')
    finally:
        main()

if __name__ == '__main__':
    main()