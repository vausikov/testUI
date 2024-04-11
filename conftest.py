import pytest
import subprocess
@pytest.fixture(autouse=True, scope='session')
def record_adb_logcat():
    """
    Эта фикстура неявно записывает логкат во время всей тестовой сессии.
    """
    subprocess.run('adb logcat -c', shell=True)
    logcat_process = subprocess.Popen('adb logcat > logs.txt', shell=True)
    yield
    logcat_process.kill()