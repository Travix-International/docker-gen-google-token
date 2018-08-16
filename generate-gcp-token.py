import argparse
import google.auth.crypt
from google.oauth2 import service_account
import json, time

def get_jwt_header_value(service_account_file, host):
    credentials = service_account.Credentials.from_service_account_file(service_account_file)
    svc_acc_email = credentials.service_account_email
    now = int(time.time())
    expires = now + 3600  # One hour in seconds

    payload = {
        'iat': now,
        'exp': expires,
        'iss': svc_acc_email,
        'sub': svc_acc_email,
        'email': svc_acc_email,
        'aud': host
    }
    jwt = google.auth.jwt.encode(credentials.signer, payload)

    return 'Bearer {}'.format(jwt.decode('utf-8'))

def main(service_account_file, host):
    signed_jwt = get_jwt_header_value(service_account_file, host)
    print(signed_jwt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'service_account_file',
        help='The path to your service account json file.')
    parser.add_argument(
        'host', help='Your API host, e.g. https://your-project.appspot.com.')

    args = parser.parse_args()

    main(args.service_account_file, args.host)
