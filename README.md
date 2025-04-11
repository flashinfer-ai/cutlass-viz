# Cutlass visualization tool

This tool is a simple wrapper around CUTLASS's `print_latex` function to visualize the layouts, tiled copy, and MMA operations.

## Installation

```bash
git clone git@github.com:flashinfer-ai/cutlass-viz.git --recursive
pip install -e . -v
```

## Usage

```
cutlass-viz --layout "(4,(4,2)):(4,(1,16))"  # visualize a single layout
cutlass-viz --source examples/tiled_copy.cc -o tiled_copy  # visualize a tiled copy
cutlass-viz --source examples/mma.cc -o mma  # visualize a MMA operation
python examples/layout_algebra.py | xargs -I {} cutlass-viz --layout "{}"
```
