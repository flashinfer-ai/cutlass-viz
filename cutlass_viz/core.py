import subprocess

cutlass_include_path = [
    "/Users/zihaoy/cutlass-layout-visualizer/3rdparty/cutlass/include"
]


def visualize_atom():
    code = r"""
#include <cute/layout.hpp>
#include <cute/tensor.hpp>

int main() {
  Layout s2xh4 = make_layout(make_shape (2,make_shape (2,2)),
                             make_stride(4,make_stride(2,1)));

  print_layout(s2xh4);
  return 0;
}
"""
    with open("print_atom_latex.cc", "w") as f:
        f.write(code)
    compile_cmd = ["g++", "print_atom_latex.cc", "-std=c++17", "-o", "print_atom_latex"]
    for path in cutlass_include_path:
        compile_cmd.append("-I")
        compile_cmd.append(path)
    subprocess.run(compile_cmd)
    subprocess.run(["./print_atom_latex"])
    
if __name__ == "__main__":
    visualize_atom()
