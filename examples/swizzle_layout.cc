using Swizzle_128B = Swizzle<3, 0, 3>;
auto layout = composition(make_layout(Shape<_8, _8>{}, LayoutLeft{}), Swizzle_128B{});
print_latex(layout);
