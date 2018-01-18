from aci.core import login_into_aci

def test_login_into_aci():
    username = 'mock_username'
    password = 'mock_password'
    url = 'https://myauthserver.com'

    was_successful = login_into_aci(username, password, url)

    assert was_successful is not None
    assert was_successful is True
    
