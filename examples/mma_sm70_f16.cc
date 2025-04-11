TiledMMA mma = make_tiled_mma(SM70_8x8x4_F32F16F16F32_NT{},
                              Layout<Shape <_2,_2>,
                                     Stride<_2,_1>>{});
print_latex(mma);
