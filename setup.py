from setuptools import setup, find_packages

setup(
    name='LLoghelper',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'colorlog>=6.8.2',  # 如果有依赖项，请列出
    ],
    author='atgczcl',
    author_email='atgzcl@163.com',
    description='A helper module for logging.',
    long_description_content_type='text/markdown',
    long_description=open('README.md', encoding='utf-8').read(),
    url='https://github.com/atgczcl/LLoghelper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)