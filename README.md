# sclerr

filters garbage from cl errors

turns test/link.txt (~7kb) into:

```
main.cpp.obj : error LNK2019: unresolved external symbol "class std::unordered_map<..> __cdecl DataParser::FileUsage::Concat(class std::unordered_map<..>,class std::unordered_map<..> const &)"  referenced in function "class std::unordered_map<..> __cdecl ParseFileUsage(void)"
```

install with `uv tool install git+https://github.com/camper0008/strip-cl-errors`

run with `ninja | sclerr`