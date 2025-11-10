# slinkerr

filters garbage from cl linker errors

turns test/err.txt (~7kb) into:

```
main.cpp.obj : error LNK2019: unresolved external symbol "class std::unordered_map> __cdecl DataParser::FileUsage::Concat(class std::unordered_map>,class std::unordered_map> const &)" ) referenced in function "class std::unordered_map> __cdecl ParseFileUsage(void)" )
```