An authentication method is a process of confirming an identity

## Basic authentication

Transport Layer Security needed to use Basics Auth

The basic authentication protocol goes through the following general steps:
1. The user requests a protected resource from the server.
2. The server responds with 401 (unauthorized) and the HTTP header `WWWAuthenticate: Basic realm="Login required"`.
3. The browser will display a basic authentication login window for the user to
send a username/password back to the server.
4. The username and password provided by the user will be sent to the server on
the HTTP header with the form `Authorization:
Basic <Username>:<Password>`. The username:password will be base64-
encoded.

        $ echo -n "admin:admin" | base64
        YWRtaW46YWRtaW4=

        $ echo -n "YWRtaW46YWRtaW4=" | base64 --decode
        admin:admin


This type of authentication is very simple, but not very secure. The username and password
will be sent to the server on every request, so make sure that you always use HTTPS to
properly encrypt their transmission over the wire. Additionally, as you may have already
noticed in the code flow of the preceding example, the authentication method will be
invoked on every request, so it is not very efficient. Yet this can be a good option for the
internal use of a very simple back-office application, or for rapidly protecting a proof-ofconcept application.

