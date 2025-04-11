from setuptools import setup, find_packages

setup(
    name="cutlass-viz",
    version="0.0.1",
    description="Visualization tool for CUTLASS tensor operations",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cutlass-viz=cutlass_viz.__main__:main',
        ],
    },
    install_requires=[
        "nvidia-cutlass",
        # No specific Python dependencies beyond standard library
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
)
