import subprocess
import tempfile
import os
import pathlib

_package_root = pathlib.Path(__file__).resolve().parents[0]
CUDA_PATH = pathlib.Path(os.environ.get("CUDA_PATH", "/usr/local/cuda"))
CUDA_INCLUDE_PATH = CUDA_PATH / "include"

INCLUDE_PATHS = [
    _package_root / "data" / "cutlass" / "include",
    _package_root / "data" / "cutlass" / "tools" / "util" / "include",
    CUDA_INCLUDE_PATH,
]

header_str = r"""
#include <cute/layout.hpp>
#include <cute/tensor.hpp>
#include <cute/atom/mma_atom.hpp>
#include <cute/atom/copy_atom.hpp>
#define CUTE_ARCH_MMA_SM90_ENABLED
#define CUTE_SM90_EXTENDED_MMA_SHAPES_ENABLED

using namespace cute;
using namespace cute::SM90;
using namespace cute::SM90::GMMA;

"""


def visualize_atom(code: str, output_name: str):
    # Create temporary files with appropriate extensions
    cc_file = tempfile.NamedTemporaryFile(suffix=".cc", delete=False)
    cc_file.write(
        header_str.encode()
        + f"""
                  int main() {{
                  {code}
                  }}""".encode()
    )
    cc_file.close()

    executable_file = tempfile.NamedTemporaryFile(delete=False)
    executable_file.close()
    os.chmod(executable_file.name, 0o755)  # Make executable

    tex_file = tempfile.NamedTemporaryFile(suffix=".tex", delete=False)
    tex_file.close()

    try:
        compile_cmd = [
            "g++",
            cc_file.name,
            "-std=c++17",
            "-o",
            executable_file.name,
            "-DNDEBUG",
        ]
        for path in INCLUDE_PATHS:
            compile_cmd.append("-I")
            compile_cmd.append(str(path))
        subprocess.run(
            compile_cmd, check=True, 
        )

        with open(tex_file.name, "w") as f:
            subprocess.run(
                [executable_file.name], stdout=f, check=True, 
            )

        # Use output_name for the PDF file
        output_pdf = f"{output_name}.pdf"

        # Create a temporary directory for LaTeX intermediate files
        with tempfile.TemporaryDirectory() as temp_dir:
            # Run pdflatex in the temporary directory
            latex_command = [
                "pdflatex",
                "-jobname=" + output_name,
                "-output-directory=" + temp_dir,
                tex_file.name,
            ]
            result = subprocess.run(
                latex_command,
                check=True,
                stdout=subprocess.PIPE,
            )

            # Move the final PDF to the current directory
            temp_pdf_path = os.path.join(temp_dir, output_pdf)
            if os.path.exists(temp_pdf_path):
                subprocess.run(
                    ["mv", temp_pdf_path, "."],
                    check=True,
                    stdout=subprocess.PIPE,
                )
            else:
                print(f"Error: PDF was not generated in {temp_dir}")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # format error message
        print(f"Error: {e.stderr.decode('utf-8')}")
    finally:
        # Clean up temporary files
        for file_path in [cc_file.name, executable_file.name, tex_file.name]:
            try:
                os.unlink(file_path)
            except:
                pass
