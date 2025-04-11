from typing import Union, Tuple
from ast import literal_eval as make_tuple


def parse_layout(layout: str) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    r"""Layout format:

    SHAPE:STRIDE

    where SHAPE is a nested tuple of integers, and STRIDE is a nested tuple of integers.
    """
    shape, stride = layout.split(":")

    shape = make_tuple(shape)
    stride = make_tuple(stride)
    return shape, stride

def gen_make_shape_str(shape: Union[tuple, int]) -> str:
    if isinstance(shape, int):
        return f"{shape}"
    else:
        return f"make_shape({', '.join(gen_make_shape_str(item) for item in shape)})"


def gen_make_stride_str(stride: Union[tuple, int]) -> str:
    if isinstance(stride, int):
        return f"{stride}"
    else:
        return f"make_stride({', '.join(gen_make_stride_str(item) for item in stride)})"


def gen_viz_source(shape: Tuple[int, ...], stride: Tuple[int, ...]) -> str:
    r"""Generate source code for visualize the layout.

    Example:

    shape = (16, 16)
    stride = (1, 1)
    print(gen_viz_source(shape, stride))
    """
    make_shape_str = gen_make_shape_str(shape)
    make_stride_str = gen_make_stride_str(stride)
    return f"""
    auto layout = make_layout(
        {make_shape_str},
        {make_stride_str}
    );
    print_latex(layout);
"""
