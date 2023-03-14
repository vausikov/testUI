import subprocess

class ADBCommands:

    # TODO
    #  1: Разобраться в subprocess
    #  2: Почитать про статические методы класса

    @staticmethod
    def get_build_number():
        build_number = subprocess.run('adb shell getprop ro.build.id', shell=True, stdout=subprocess.PIPE, text=True)\
            .stdout
        build_number_clear = build_number[:-1]
        return build_number_clear



