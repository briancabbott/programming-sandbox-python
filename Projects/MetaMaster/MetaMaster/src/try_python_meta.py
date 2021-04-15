


class AMetaBase:
    def __init__(self, type, *args, **kwargs) -> None:
        print("BCA-DBG: into => __init__()")
        print(type)
        print(args)
        print(kwargs)
        pass
        
class AMetaClass(AMetaBase):
    def __init__(self, *args, **kwargs) -> None:
        AMetaBase(self, AMetaClass.__class__, args, kwargs)
        pass

    # to_dict()
    # from_dict()
    # to_json()
    # from_json()
    # to_hcl()
    # from_hcl() 


if __name__ == "__main__":
    amc = AMetaClass("typename", "instancename", prop1 = "hello", prop2 = 5, prop3=False, prop4 = None)
    print("hello  world")