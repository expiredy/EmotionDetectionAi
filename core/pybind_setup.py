import pybind11
from distutils.core import setup, Extension

ext_modules = [
    Extension(
        'library', # название нашей либы
        ['library.cpp', 'main.cpp'], # файлики которые компилируем
        include_dirs=[pybind11.get_include()],  # не забываем добавить инклюды pybind11
        language='c++',
        extra_compile_args=['-std=c++11'],  # используем с++11
    ),
]

setup(
    name='library',
    version='0.0.1',
    author='user',
    author_email='user@user.ru',
    description='pybind11 extension',
    ext_modules=ext_modules,
    requires=['pybind11']  # не забываем указать зависимость от pybind11
)