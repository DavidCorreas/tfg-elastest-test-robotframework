import xmlrpc.client

with xmlrpc.client.ServerProxy("http://127.0.0.1:8270") as proxy:
    print(proxy.system.listMethods())
    library_info = proxy.get_keyword_names
    library_info2 = proxy.get_library_information
    info = library_info()
    info2 = library_info2()
    pass
    # print("3 is even: %s" % str(proxy.get_library_information))

