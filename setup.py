from setuptools import setup, find_packages

setup(
    name="tryonai",
    version="0.1.0",
    packages=find_packages(),
    description="TryOn AI Python SDK - Use this SDK to interact with TryOn AI API. Integrate virtual try-on, model swap, outfit generation and captioning in your application.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="TryOn AI",
    author_email="contact@tryonlabs.ai",
    url="https://www.tryonlabs.ai",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        "requests",
        "python-dotenv"
    ]
)
