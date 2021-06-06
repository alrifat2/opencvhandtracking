from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='opencv-handtracking',
    packages=['opencv-handtracking'],
    version='0.2',
    license='MIT',
    description='OpenCV Hand Tracking Modules. Skip right to the real deal without dealing with hand tracking.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Al Rifat',
    author_email='alrifat088@gmail.com',
    url='https://github.com/AlDevStuff/opencvhandtracking',
    download_url='https://github.com/AlDevStuff/opencvhandtracking/archive/refs/tags/v_0.2.tar.gz',
    keywords=['opencv', 'computer vision', 'handtracking', 'cv2', 'mediapipe'],
    install_requires=[
        'opencv-python',
        'mediapipe',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
