# CreateNestedPythonDicts
This little function is ment to create nested Python dictionaries from a stack of keys.

```
target_dict = {}

for key1 in keyGroup1:
    for key2 in keyGroup3:
        for key3 in keyGroup2:
            create_nested_dict(target_dict, key1,key2,key3 )
            target_dict[key1][key2][key3] = SomethingToStore
```

