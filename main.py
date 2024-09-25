import subprocess
import sys
import pkg_resources

from models.processor import main

def install_dependencies():
    required = {"pyyaml", "requests"}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        print("正在安装依赖...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install",
                *missing
            ])
        except subprocess.CalledProcessError as e:
            print("依赖安装失败")
            print(f"错误代码: {e.returncode}")
            print(f"命令输出: {e.output}")
            sys.exit(1)

if __name__ == "__main__":
    install_dependencies()
    main()