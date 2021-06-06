from distutils.core import setup
setup(
  name = 'opencv-handtracking',
  packages = ['opencv-handtracking'],
  version = '0.1',
  license='MIT',
  description = 'OpenCV Hand Tracking Modules. Skip right to the real deal without dealing with hand tracking.',
  author = 'Al Rifat',
  author_email = 'alrifat088@gmail.com',
  url = 'https://github.com/AlDevStuff/opencvhandtracking',
  download_url = 'https://github.com/AlDevStuff/opencvhandtracking/archive/refs/tags/v_0.1.tar.gz',
  keywords = ['opencv', 'computer vision', 'handtracking', 'cv2', 'mediapipe'],
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
