from setuptools import setup, find_packages

import os
import shutil

# Create the package data directory
package_data_dir = os.path.join("cutlass_viz", "data")
os.makedirs(package_data_dir, exist_ok=True)

# Copy the cutlass directory to the package data directory
cutlass_data_dir = os.path.join(package_data_dir, "cutlass")
if os.path.exists(cutlass_data_dir):
    shutil.rmtree(cutlass_data_dir)

# Ensure cutlass is included in the package
cutlass_src_dir = "3rdparty/cutlass"
if os.path.exists(cutlass_src_dir):
    shutil.copytree(cutlass_src_dir, cutlass_data_dir)
else:
    raise FileNotFoundError(f"Cutlass directory not found at {cutlass_src_dir}")

setup(
    name="cutlass-viz",
    version="0.0.1",
    description="Visualization tool for CUTLASS tensor operations",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cutlass-viz=cutlass_viz.__main__:main",
        ],
    },
    package_data={
        "cutlass_viz": ["data/cutlass/**/*"],  # Correct package name
    },
    include_package_data=True,
    install_requires=[
        "nvidia-cutlass",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
