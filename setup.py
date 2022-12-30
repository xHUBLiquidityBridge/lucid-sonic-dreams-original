import setuptools

with open("./content/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
#with open('requirements.txt') as f:
#    required = f.read().splitlines()

setuptools.setup(
    name="lucidsonicdreams v2", 
    version="0.01",
    author="BigZaddy",
    author_email="@gmail.com",
    description="Syncs GAN-generated visuals to music",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.7',
    url="https://github.com/xHUBLiquidityBridge/lucid-sonic-dreams-original.git",
   # download_url="https://github.com/DeFi-Coder-News-Letter/lucid-sonic-dreams/lucid-sonic-dreams.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['tensorflow==1.15.0',
                      'librosa',
                      'numpy',
                      'moviepy',
                      'Pillow',
                      'tqdm',
                      'scipy',
                      'scikit-image',
                      'pygit2',
                      'gdown', 
                      'mega.py',
                      'requests',
                      'pandas',
                      'SoundFile']
)
