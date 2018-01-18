
def login_into_aci(username, password, url):
    '''Logins into ACI server

    Parameters
    ----------
    username: string
    password: string
    url: authentication host

    Return
    ------
    success: boolean
      indicates if login was successful
    '''
    print('.login_into_aci')
    print(username)
    print(password)
    print(url)

    # return True if successful
    return True


def show_tenants(object_tree):
    print('.show_tenants')

    if not isinstance(object_tree, dict):
        msg = 'Please use an object tree dict'
        raise ValueError(msg)

    if not 'objects' in object_tree:
        msg = 'Object Tree must contain objects key'
        raise ValueError(msg)


    objects = object_tree['objects']
    tenants = []
    for obj in objects:

        # TODO: make sure that objects have `type` key
        if obj['type'] == 'tenant':
            tenants.append(obj)

    return tenants


def create_tenant():
    print('create_tenant')


def create_bridge_domain():
    print('create_bridge_domain')


def create_vrf():
    print('create_vrf')


def create_epg():
    print('create_epg')
