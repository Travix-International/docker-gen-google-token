# docker-gen-google-token

This is a docker image built to generate a google token based on the service account json file.

## Usage

```
docker run -it --rm -v your-svc-account-file.json:/app/svc-account.json gen-google-token https://the-host-you-are-trying-to-connect.com
```

## Response

The response will be something like this:

```
Bearer eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJSUzI1NiIsICJraWQiOiAiZDhiMDk4OTdhOTBlMjdkMDJlMDE4NDE4NzJiMTg2Yjc6ICJwbGF0Zm9ybS1kb3RuZXQtZ29jZEB2ZXJkYW50LWN1cnJlbnQtMTA0MjEwLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwgInN1YiI6ICJwbGF0Zm9ybS1kb3RuZXQtZ29jZEB2ZXJkYW50LWN1cnJlbnQtMTA0MjEwLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwgImVtYWlsIjogInBsYX0OV0ekcJt-sqYREbABSMHLoynmS6jG2fgsfYIYt_WIH_lajLrAsBWpsRbmbOUjwpTLln8YJjE6_650YelHVUPns9YZbacY_agozT6g22hPuJD4SCik0mpGvaM4zppuNdW-2Uf41UeaeEK0iutaYXx710tvwo9fsI6t1THM0SRjVSJKcPPE5_hYF2ZtjpPOsQIWOgqgCojyy5hJoJEYB8u9cVA==
```

### Response Usage

With this you can connect to your endpoint authenticated:
```
curl --header "Authorization: ${PREVIOUS_RESPONSE_TOKEN} https://the-host-you-are-trying-to-connect.com/path-you-need"
```
