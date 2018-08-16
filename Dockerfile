FROM python

LABEL maintainer="TravixInternational"

RUN pip install google-auth google-auth-oauthlib

COPY generate-gcp-token.py /app/

WORKDIR /app/

ENTRYPOINT ["python", "generate-gcp-token.py", "svc-account.json"]
