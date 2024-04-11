import subprocess

class ADBCommands:
    @staticmethod
    def get_build_number():
        build_number = subprocess.run('adb shell getprop ro.build.id', shell=True, stdout=subprocess.PIPE, text=True)\
            .stdout
        build_number_clear = build_number[:-1]
        return build_number_clear



