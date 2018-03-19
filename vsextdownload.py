import argparse
import os
import requests


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

ext_url="https://{0}.gallery.vsassets.io/_apis/public/gallery/publisher/{1}/extension/{2}/{3}/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage"

def download_ext(publisher,name,ver):
    url=ext_url.format(publisher,publisher,name,ver)
    print(url)
    res=requests.get(url,headers=HEADERS)
    res.raise_for_status()  
    playFile = open(publisher+'.'+name+'.vsix', 'wb')  
    for chunk in res.iter_content(1024):  
        playFile.write(chunk)  
    playFile.close()


def arg_parse():
    parse=argparse.ArgumentParser(description='VSCode Extension Download  CLI Tools')
    parse.add_argument("-i",'--identifier',type=str,help='extension unique identifier')
    parse.add_argument('-v','--version',type=str,help='extension version')
    return parse

def command_parse():
    parse=arg_parse()
    args=vars(parse.parse_args())
    print(args)

    key=args["identifier"]

    index=key.find('.')
    publisher=key[:index]
    name=key[index+1:]
    download_ext(publisher,name,args['version'])
   

if __name__ == "__main__":
    command_parse()
           