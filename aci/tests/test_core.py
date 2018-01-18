from aci.core import login_into_aci
from aci.core import show_tenants


def test_login_into_aci():
    username = 'mock_username'
    password = 'mock_password'
    url = 'https://myauthserver.com'

    was_successful = login_into_aci(username, password, url)

    assert was_successful is not None
    assert was_successful is True


def test_show_tenants():
    print('show_tenants')

    # test inputs
    tenant1 = {}
    tenant1['type'] = 'tenant1'
    tenant1['name'] = 'tenant_name1'
    tenant1['description'] = 'The is the main tenant'
    tenant1['vlan'] = 'tenant_vlan1'
    tenant1['contracts'] = ['contract1', 'contract2']

    tenant2 = {}
    tenant2['type'] = 'tenant'
    tenant2['name'] = 'tenant_name'
    tenant1['description'] = 'The is another tenant'
    tenant2['vlan'] = 'tenant_vlan'
    tenant2['contracts'] = ['contract1', 'contract2']

    object_tree = {}
    object_tree['name'] = 'my_object_tree'
    object_tree['objects'] = [tenant1, tenant2]

    # test code
    tenants = show_tenants(object_tree)

    assert isinstance(tenants, list)
    assert len(tenants)
    for t in tenants:
        assert isinstance(t, dict)
        assert 'type' in t
        assert t['type'] == 'tenant'
