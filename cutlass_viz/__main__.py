import argparse
from .core import visualize_atom
from .layout import parse_layout, gen_viz_source

def main():
    parser = argparse.ArgumentParser("Cutlass visualization tool")
    parser.add_argument("--output", "-o", type=str, default="tmp", help="Output file base name, default is tmp")
    parser.add_argument("--layout", type=str, help="Layout, format: SHAPE:STRIDE, where SHAPE and STRIDE are nested tuples of integers, e.g. (8,4):(4,1)")
    parser.add_argument("--source", type=str, help="Source code")
    args = parser.parse_args()

    if args.layout:
        visualize_atom(gen_viz_source(*parse_layout(args.layout)), args.output)
    elif args.source:
        with open(args.source, "r") as f:
            source = f.read()
        visualize_atom(source, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
