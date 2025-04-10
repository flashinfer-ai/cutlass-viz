import subprocess

cutlass_include_path = [
    "/home/zhye/cutlass-viz/3rdparty/cutlass/include"
]


def visualize_atom():
    code = r"""
#include <cute/layout.hpp>
#include <cute/tensor.hpp>
#include <cute/atom/copy_traits_sm75.hpp>

using namespace cute;

int main() {
  //Layout s2xh4 = make_layout(make_shape (2,make_shape (2,2)),
  //                           make_stride(4,make_stride(2,1)));
  using SrcLayout = Layout<Shape < _32,_128>,
                           Stride<_128,  _1>>;

  print_latex(SrcLayout{});
  return 0;
}
"""
    with open("print_atom_latex.cu", "w") as f:
        f.write(code)
    compile_cmd = ["nvcc", "print_atom_latex.cu", "-std=c++17", "-o", "print_atom_latex"]
    for path in cutlass_include_path:
        compile_cmd.append("-I")
        compile_cmd.append(path)
    subprocess.run(compile_cmd, check=True)
    with open("1.tex", "w") as f:
        subprocess.run(["./print_atom_latex"], stdout=f, check=True)
    latex_command = ["pdflatex", "1.tex"]
    subprocess.run(latex_command, check=True)
    
if __name__ == "__main__":
    visualize_atom()
