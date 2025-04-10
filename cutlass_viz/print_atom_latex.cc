
#include <cute/layout.hpp>
#include <cute/tensor.hpp>

int main() {
  Layout s2xh4 = make_layout(make_shape (2,make_shape (2,2)),
                             make_stride(4,make_stride(2,1)));

  print_layout(s2xh4);
  return 0;
}
