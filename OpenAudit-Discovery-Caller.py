import requests

#region constants
DiscoveryPage = '/open-audit/index.php/discoveries'
LogonPage = '/open-audit/index.php/logon'
OpenAuditUsername = 'admin'
OpenAuditPassword = 'password'
#endregion

def main(argv):
    ServerName = argv.server
    DiscoveryID = argv.id

    #logon
    url = f'{ServerName}{LogonPage}'
    session = requests.session()
    response = session.post(url, data={'username':OpenAuditUsername, 'password':OpenAuditPassword})
    CheckHTTPError(response)

    #call discovery
    url = f'{ServerName}{DiscoveryPage}/{DiscoveryID}'
    payload = {'action':'execute'}
    response = session.get(url, params=payload)
    CheckHTTPError(response)
    print(f'[INFO] Successfully called OpenAudit discovery {DiscoveryID}')

#region Function definitions
def CheckHTTPError(response: requests.Response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        raise
    return response
#endregion

#region argparse section
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Trigger \'OpenAudit Community\' discovery. Built and tested against OpenAudit version 3.4.0')

    parser.add_argument('server',
                        metavar='server',
                        type=str,
                        help='Protocol and FQDN of OpenAudit server. Requires port to use if different from default.\r\nexample: http://oa-server.com:3051')
    parser.add_argument('-i', '--id',
                        metavar='id',
                        type=int,
                        help='The ID of the discovery task to call. Obtain this via OpenAudit\'s discovery page. Default to 1 if omitted',
                        default=1)


    args = parser.parse_args()
    main(args)
#endregion