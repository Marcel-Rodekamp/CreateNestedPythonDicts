def create_nested_dict(target, *keys):
    r"""
        params:
            - target: dict
            - *keys: keys

        Create a dictionary which has nested keys s.t. for every key in keys:
        target[keys[0]][keys[1]][...][keys[N]] = None

        usage:
        ```
        target_dict = {}

        for key1 in keyGroup1:
            for key2 in keyGroup3:
                for key3 in keyGroup2:
                    create_nested_dict(target_dict, key1,key2,key3 )
                    target_dict[key1][key2][key3] = SomethingToStore
        ```
    """

    def recursion(sub_target, level):
        # stop recursion at the end of 
        if level == len(keys)-1:
            sub_target[keys[level]] = None
        else:
            try:
                # try if key is already inserted
                sub_target[ keys[level] ]
            except:
                # otherwise create next level dict at this key
                sub_target[ keys[level] ] = {}

            # restart recursion for next level
            recursion(sub_target[keys[level]],level+1)

    recursion(target, level=0)
