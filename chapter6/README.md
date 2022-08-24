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

    # https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/
    
    http {
        server {
            listen 192.168.1.23:8080;
            root   /usr/share/nginx/html;

            location /api {
                api;
                satisfy all;

                deny  192.168.1.2;
                allow 192.168.1.1/24;
                allow 127.0.0.1;
                deny  all;

                auth_basic           "Administrator’s Area";
                auth_basic_user_file /etc/apache2/.htpasswd; 
            }
        }
    }

<br>

## Remote-user authentication

In blog application, we could just check whether the user exists on the database, so no
password database field is needed. 

This authentication method can be considered secure if
it is properly set up on the server, and can be very convenient on intranet setups since the
user, if already authenticated on the domain will no longer
need to fill login password again (using Kerberos GSSAPI..)

Kerberos is a computer network security protocol that authenticates service requests between two or more trusted hosts across an untrusted network, like the internet. It uses secret-key cryptography and a trusted third party for authenticating client-server applications and verifying users' identities.

<br>

## LDAP authentication

Frequent Reads / Rare Writes in LDAP SERVER 

The two most commonly used LDAP services nowadays are OpenLDAP (open and free)
and Microsoft Active Directory (commercial).

Example view of [LDAP auth](https://www.youtube.com/watch?v=TAhA7daZCb4)

<br>

## Database user model authentication

Database authentication is widely used for internet-faced applications. If properly
implemented, it can be considered a secure method. It has the advantages of being simple
to add new users, and having no dependency on any external services. Security roles,
groups, fine-grained access permissions, and extra user attributes are also all kept on the
database. These can be easily changed without any external dependencies, and maintained
within the scope change of the application.

but before saving password into database it passes through hash function.
