# Cutlass visualization tool

This tool is a simple wrapper around CUTLASS's `print_latex` function to visualize the layouts, tiled copy, and MMA operations.

## Installation

```bash
git clone git@github.com:flashinfer-ai/cutlass-viz.git --recursive
pip install -e . -v
```

## Usage

```bash
cutlass-viz --help
```

Example usage:

```
cutlass-viz --layout "(4,(4,2)):(4,(1,16))"  # visualize a single layout, output to tmp.pdf
cutlass-viz --source examples/tiled_copy.cc -o tiled_copy  # visualize a tiled copy, output to tiled_copy.pdf
cutlass-viz --source examples/mma_sm89_fp8.cc -o mma_sm89_fp8  # visualize a MMA operation with sm89 and fp8, output to mma_sm89_fp8.pdf
cutlass-viz --source examples/mma_sm90_fp8.cc -o mma_sm90_fp8  # visualize a MMA operation with sm90 and fp8, output to mma_sm90_fp8.pdf
python examples/layout_algebra.py | xargs -I {} cutlass-viz --layout "{}"  # visualize all layouts generated by layout algebra, output to tmp.pdf
```
