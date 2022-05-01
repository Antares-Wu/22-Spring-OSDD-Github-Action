import os
import os.path as path

code_dir = './build.md'
output_dir = './assets/build.md'



if __name__ == '__main__':


    os.system("xcopy ./build.md ./assets/build.md")


