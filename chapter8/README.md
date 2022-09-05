## Rest

Representational State Transfer (REST) is an architectural style that is used to implement
web services. It was defined by Roy Fielding in his PhD dissertation in 2000.

REST aims to implement a standard for uniform and predefined operations between systems.

Facebook and Twitter use REST in their
application program interface, or API

REST provides the following guiding constraints:
- `Separation of concerns between the client and server:` The client and server
should be able to evolve or change independently as long as the API does not
change.
- `Stateless:` Any information that is necessary to handle requests is stored in the
request itself or by the client. An example of the server being stateless is
the session object in Flask. The session object does not store its information on
the server, but stores it on the client in a cookie. The cookie is sent along with
every request for the server to parse and determine whether the necessary data
for the requested resource is stored inside it, rather than the server storing
session information for every user.

- `Uniform interface:` There are many different parts to this constraint, which are as
follows:
    - The interface is based around resources, which in our case are
models.
    - Data sent by the server is not the actual data in the server, but a
representation. For example, a JSON abstraction of the data is sent
with each request, rather than the actual database.
    - The data sent by the server is enough to allow the client to modify
the data on the server. In the preceding example, the IDs that are
passed to the client fill this role.
    - Every resource provided by the API must be represented and
accessed in the same manner. For example, one resource cannot be
represented in XML and while another is represented in JSON.

- `Layered system:` Load balancers, proxies, caches, and other servers and services
can act between the client and the server, as long as the final result is the same as
if they were not there. This improves performance, scalability, and availability.
- `Cacheability:` Clients can cache responses, so a server must define whether a
response is cacheable or not. This improves performance.


## HTTP
The Hypertext Transfer Protocol (HTTP) is a request–response protocol that belongs to
layer 7 (the application layer)


http://someserver.com:5000/blog/user/user1?title=sometitle#1


    Scheme                  HTTP
    authority.host          someserver.com
    authority.port          5000
    path                    blog/user/user1
    query                   title=sometitle
    fragment                1

Accepted HTTP request methods are `GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE, and PATCH.`

## Status codes

    Informational: 1XX
    Successful: 2XX
    Redirection: 3XX
    Client error: 4XX
    Server error: 5XX


## Get requests
For some of our GET, PUT, and DELETE requests, our API will need the ID of the post that is
to be modified.

The data to be sent to the client must be a representation of the Post objects in JSON, so
how will our Post objects be translated? Flask Restful provides a way of translating any
object into JSON through the fields object and the marshal_with function decorator.
