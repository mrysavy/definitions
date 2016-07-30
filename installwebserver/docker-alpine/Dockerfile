FROM alpine:3.4

RUN apk --no-cache add lighttpd curl
ADD lighttpd.conf /etc/lighttpd/lighttpd.conf

EXPOSE 80
VOLUME ["/srv"]
ENTRYPOINT ["/usr/sbin/lighttpd.conf", "-f", "/etc/lighttpd/lighttpd.conf", "-D"]

