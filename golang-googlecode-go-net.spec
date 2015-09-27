Name     : golang-googlecode-go-net 
Version  : 0
Release  : 1
URL      : https://github.com/golang/net/archive/03affa02f16950ea3188823456766ed60bfed9bb.tar.gz
Source0  : https://github.com/golang/net/archive/03affa02f16950ea3188823456766ed60bfed9bb.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : go
BuildRequires : golang-googlecode-go-text

%description
This repository holds supplementary Go networking libraries.
To submit changes to this repository, see http://golang.org/doc/contribute.html.

%prep
%setup -q -n net-03affa02f16950ea3188823456766ed60bfed9bb

%build

%install
%global gopath /usr/lib/golang
%global library_path golang.org/x/net
rm -rf %{buildroot}
# Copy all *.go and *.s files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in s go xml html; do
    for file in $(find . -iname "*.$ext") ; do
         install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
         cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
    done
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}/context
go test %{library_path}/context/ctxhttp
go test %{library_path}/html
go test %{library_path}/html/atom
go test %{library_path}/html/charset
go test %{library_path}/http2
go test %{library_path}/http2/hpack
go test %{library_path}/icmp ||:
go test %{library_path}/idna
go test %{library_path}/internal/timeseries
go test %{library_path}/ipv4
go test %{library_path}/ipv6
go test %{library_path}/netutil
go test %{library_path}/proxy
go test %{library_path}/publicsuffix
go test %{library_path}/trace
go test %{library_path}/webdav
go test %{library_path}/websocket

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/golang.org/x/net/context/context.go
/usr/lib/golang/src/golang.org/x/net/context/context_test.go
/usr/lib/golang/src/golang.org/x/net/context/ctxhttp/cancelreq.go
/usr/lib/golang/src/golang.org/x/net/context/ctxhttp/cancelreq_go14.go
/usr/lib/golang/src/golang.org/x/net/context/ctxhttp/ctxhttp.go
/usr/lib/golang/src/golang.org/x/net/context/ctxhttp/ctxhttp_test.go
/usr/lib/golang/src/golang.org/x/net/context/withtimeout_test.go
/usr/lib/golang/src/golang.org/x/net/dict/dict.go
/usr/lib/golang/src/golang.org/x/net/html/atom/atom.go
/usr/lib/golang/src/golang.org/x/net/html/atom/atom_test.go
/usr/lib/golang/src/golang.org/x/net/html/atom/gen.go
/usr/lib/golang/src/golang.org/x/net/html/atom/table.go
/usr/lib/golang/src/golang.org/x/net/html/atom/table_test.go
/usr/lib/golang/src/golang.org/x/net/html/charset/charset.go
/usr/lib/golang/src/golang.org/x/net/html/charset/charset_test.go
/usr/lib/golang/src/golang.org/x/net/html/charset/gen.go
/usr/lib/golang/src/golang.org/x/net/html/charset/table.go
/usr/lib/golang/src/golang.org/x/net/html/charset/testdata/HTTP-charset.html
/usr/lib/golang/src/golang.org/x/net/html/charset/testdata/HTTP-vs-UTF-8-BOM.html
/usr/lib/golang/src/golang.org/x/net/html/charset/testdata/HTTP-vs-meta-charset.html
/usr/lib/golang/src/golang.org/x/net/html/charset/testdata/HTTP-vs-meta-content.html
/usr/lib/golang/src/golang.org/x/net/html/charset/testdata/No-encoding-declaration.html
/usr/lib/golang/src/golang.org/x/net/html/charset/testdata/UTF-16BE-BOM.html
/usr/lib/golang/src/golang.org/x/net/html/charset/testdata/UTF-16LE-BOM.html
/usr/lib/golang/src/golang.org/x/net/html/charset/testdata/UTF-8-BOM-vs-meta-charset.html
/usr/lib/golang/src/golang.org/x/net/html/charset/testdata/UTF-8-BOM-vs-meta-content.html
/usr/lib/golang/src/golang.org/x/net/html/charset/testdata/meta-charset-attribute.html
/usr/lib/golang/src/golang.org/x/net/html/charset/testdata/meta-content-attribute.html
/usr/lib/golang/src/golang.org/x/net/html/const.go
/usr/lib/golang/src/golang.org/x/net/html/doc.go
/usr/lib/golang/src/golang.org/x/net/html/doctype.go
/usr/lib/golang/src/golang.org/x/net/html/entity.go
/usr/lib/golang/src/golang.org/x/net/html/entity_test.go
/usr/lib/golang/src/golang.org/x/net/html/escape.go
/usr/lib/golang/src/golang.org/x/net/html/escape_test.go
/usr/lib/golang/src/golang.org/x/net/html/example_test.go
/usr/lib/golang/src/golang.org/x/net/html/foreign.go
/usr/lib/golang/src/golang.org/x/net/html/node.go
/usr/lib/golang/src/golang.org/x/net/html/node_test.go
/usr/lib/golang/src/golang.org/x/net/html/parse.go
/usr/lib/golang/src/golang.org/x/net/html/parse_test.go
/usr/lib/golang/src/golang.org/x/net/html/render.go
/usr/lib/golang/src/golang.org/x/net/html/render_test.go
/usr/lib/golang/src/golang.org/x/net/html/testdata/go1.html
/usr/lib/golang/src/golang.org/x/net/html/token.go
/usr/lib/golang/src/golang.org/x/net/html/token_test.go
/usr/lib/golang/src/golang.org/x/net/http2/buffer.go
/usr/lib/golang/src/golang.org/x/net/http2/buffer_test.go
/usr/lib/golang/src/golang.org/x/net/http2/errors.go
/usr/lib/golang/src/golang.org/x/net/http2/errors_test.go
/usr/lib/golang/src/golang.org/x/net/http2/flow.go
/usr/lib/golang/src/golang.org/x/net/http2/flow_test.go
/usr/lib/golang/src/golang.org/x/net/http2/frame.go
/usr/lib/golang/src/golang.org/x/net/http2/frame_test.go
/usr/lib/golang/src/golang.org/x/net/http2/gotrack.go
/usr/lib/golang/src/golang.org/x/net/http2/gotrack_test.go
/usr/lib/golang/src/golang.org/x/net/http2/h2demo/h2demo.go
/usr/lib/golang/src/golang.org/x/net/http2/h2demo/launch.go
/usr/lib/golang/src/golang.org/x/net/http2/h2i/h2i.go
/usr/lib/golang/src/golang.org/x/net/http2/headermap.go
/usr/lib/golang/src/golang.org/x/net/http2/hpack/encode.go
/usr/lib/golang/src/golang.org/x/net/http2/hpack/encode_test.go
/usr/lib/golang/src/golang.org/x/net/http2/hpack/hpack.go
/usr/lib/golang/src/golang.org/x/net/http2/hpack/hpack_test.go
/usr/lib/golang/src/golang.org/x/net/http2/hpack/huffman.go
/usr/lib/golang/src/golang.org/x/net/http2/hpack/tables.go
/usr/lib/golang/src/golang.org/x/net/http2/http2.go
/usr/lib/golang/src/golang.org/x/net/http2/http2_test.go
/usr/lib/golang/src/golang.org/x/net/http2/pipe.go
/usr/lib/golang/src/golang.org/x/net/http2/pipe_test.go
/usr/lib/golang/src/golang.org/x/net/http2/priority_test.go
/usr/lib/golang/src/golang.org/x/net/http2/server.go
/usr/lib/golang/src/golang.org/x/net/http2/server_test.go
/usr/lib/golang/src/golang.org/x/net/http2/testdata/draft-ietf-httpbis-http2.xml
/usr/lib/golang/src/golang.org/x/net/http2/transport.go
/usr/lib/golang/src/golang.org/x/net/http2/transport_test.go
/usr/lib/golang/src/golang.org/x/net/http2/write.go
/usr/lib/golang/src/golang.org/x/net/http2/writesched.go
/usr/lib/golang/src/golang.org/x/net/http2/z_spec_test.go
/usr/lib/golang/src/golang.org/x/net/icmp/dstunreach.go
/usr/lib/golang/src/golang.org/x/net/icmp/echo.go
/usr/lib/golang/src/golang.org/x/net/icmp/endpoint.go
/usr/lib/golang/src/golang.org/x/net/icmp/example_test.go
/usr/lib/golang/src/golang.org/x/net/icmp/extension.go
/usr/lib/golang/src/golang.org/x/net/icmp/extension_test.go
/usr/lib/golang/src/golang.org/x/net/icmp/helper_posix.go
/usr/lib/golang/src/golang.org/x/net/icmp/interface.go
/usr/lib/golang/src/golang.org/x/net/icmp/ipv4.go
/usr/lib/golang/src/golang.org/x/net/icmp/ipv4_test.go
/usr/lib/golang/src/golang.org/x/net/icmp/ipv6.go
/usr/lib/golang/src/golang.org/x/net/icmp/listen_posix.go
/usr/lib/golang/src/golang.org/x/net/icmp/listen_stub.go
/usr/lib/golang/src/golang.org/x/net/icmp/message.go
/usr/lib/golang/src/golang.org/x/net/icmp/message_test.go
/usr/lib/golang/src/golang.org/x/net/icmp/messagebody.go
/usr/lib/golang/src/golang.org/x/net/icmp/mpls.go
/usr/lib/golang/src/golang.org/x/net/icmp/multipart.go
/usr/lib/golang/src/golang.org/x/net/icmp/multipart_test.go
/usr/lib/golang/src/golang.org/x/net/icmp/packettoobig.go
/usr/lib/golang/src/golang.org/x/net/icmp/paramprob.go
/usr/lib/golang/src/golang.org/x/net/icmp/ping_test.go
/usr/lib/golang/src/golang.org/x/net/icmp/sys_freebsd.go
/usr/lib/golang/src/golang.org/x/net/icmp/timeexceeded.go
/usr/lib/golang/src/golang.org/x/net/idna/idna.go
/usr/lib/golang/src/golang.org/x/net/idna/idna_test.go
/usr/lib/golang/src/golang.org/x/net/idna/punycode.go
/usr/lib/golang/src/golang.org/x/net/idna/punycode_test.go
/usr/lib/golang/src/golang.org/x/net/internal/iana/const.go
/usr/lib/golang/src/golang.org/x/net/internal/iana/gen.go
/usr/lib/golang/src/golang.org/x/net/internal/nettest/error_posix.go
/usr/lib/golang/src/golang.org/x/net/internal/nettest/error_stub.go
/usr/lib/golang/src/golang.org/x/net/internal/nettest/interface.go
/usr/lib/golang/src/golang.org/x/net/internal/nettest/rlimit.go
/usr/lib/golang/src/golang.org/x/net/internal/nettest/rlimit_stub.go
/usr/lib/golang/src/golang.org/x/net/internal/nettest/rlimit_unix.go
/usr/lib/golang/src/golang.org/x/net/internal/nettest/rlimit_windows.go
/usr/lib/golang/src/golang.org/x/net/internal/nettest/stack.go
/usr/lib/golang/src/golang.org/x/net/internal/nettest/stack_stub.go
/usr/lib/golang/src/golang.org/x/net/internal/nettest/stack_unix.go
/usr/lib/golang/src/golang.org/x/net/internal/nettest/stack_windows.go
/usr/lib/golang/src/golang.org/x/net/internal/timeseries/timeseries.go
/usr/lib/golang/src/golang.org/x/net/internal/timeseries/timeseries_test.go
/usr/lib/golang/src/golang.org/x/net/ipv4/control.go
/usr/lib/golang/src/golang.org/x/net/ipv4/control_bsd.go
/usr/lib/golang/src/golang.org/x/net/ipv4/control_pktinfo.go
/usr/lib/golang/src/golang.org/x/net/ipv4/control_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv4/control_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv4/control_windows.go
/usr/lib/golang/src/golang.org/x/net/ipv4/defs_darwin.go
/usr/lib/golang/src/golang.org/x/net/ipv4/defs_dragonfly.go
/usr/lib/golang/src/golang.org/x/net/ipv4/defs_freebsd.go
/usr/lib/golang/src/golang.org/x/net/ipv4/defs_linux.go
/usr/lib/golang/src/golang.org/x/net/ipv4/defs_netbsd.go
/usr/lib/golang/src/golang.org/x/net/ipv4/defs_openbsd.go
/usr/lib/golang/src/golang.org/x/net/ipv4/defs_solaris.go
/usr/lib/golang/src/golang.org/x/net/ipv4/dgramopt_posix.go
/usr/lib/golang/src/golang.org/x/net/ipv4/dgramopt_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv4/doc.go
/usr/lib/golang/src/golang.org/x/net/ipv4/endpoint.go
/usr/lib/golang/src/golang.org/x/net/ipv4/example_test.go
/usr/lib/golang/src/golang.org/x/net/ipv4/gen.go
/usr/lib/golang/src/golang.org/x/net/ipv4/genericopt_posix.go
/usr/lib/golang/src/golang.org/x/net/ipv4/genericopt_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv4/header.go
/usr/lib/golang/src/golang.org/x/net/ipv4/header_test.go
/usr/lib/golang/src/golang.org/x/net/ipv4/helper.go
/usr/lib/golang/src/golang.org/x/net/ipv4/helper_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv4/helper_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv4/helper_windows.go
/usr/lib/golang/src/golang.org/x/net/ipv4/iana.go
/usr/lib/golang/src/golang.org/x/net/ipv4/icmp.go
/usr/lib/golang/src/golang.org/x/net/ipv4/icmp_linux.go
/usr/lib/golang/src/golang.org/x/net/ipv4/icmp_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv4/icmp_test.go
/usr/lib/golang/src/golang.org/x/net/ipv4/mocktransponder_test.go
/usr/lib/golang/src/golang.org/x/net/ipv4/multicast_test.go
/usr/lib/golang/src/golang.org/x/net/ipv4/multicastlistener_test.go
/usr/lib/golang/src/golang.org/x/net/ipv4/multicastsockopt_test.go
/usr/lib/golang/src/golang.org/x/net/ipv4/packet.go
/usr/lib/golang/src/golang.org/x/net/ipv4/payload.go
/usr/lib/golang/src/golang.org/x/net/ipv4/payload_cmsg.go
/usr/lib/golang/src/golang.org/x/net/ipv4/payload_nocmsg.go
/usr/lib/golang/src/golang.org/x/net/ipv4/readwrite_test.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sockopt.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sockopt_asmreq.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sockopt_asmreq_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sockopt_asmreq_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sockopt_asmreq_windows.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sockopt_asmreqn_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sockopt_asmreqn_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sockopt_ssmreq_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sockopt_ssmreq_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sockopt_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sockopt_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sockopt_windows.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sys_bsd.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sys_darwin.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sys_freebsd.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sys_linux.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sys_openbsd.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sys_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv4/sys_windows.go
/usr/lib/golang/src/golang.org/x/net/ipv4/syscall_linux_386.go
/usr/lib/golang/src/golang.org/x/net/ipv4/syscall_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv4/thunk_linux_386.s
/usr/lib/golang/src/golang.org/x/net/ipv4/unicast_test.go
/usr/lib/golang/src/golang.org/x/net/ipv4/unicastsockopt_test.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_darwin.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_dragonfly.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_freebsd_386.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_freebsd_amd64.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_freebsd_arm.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_linux_386.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_linux_amd64.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_linux_arm.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_linux_arm64.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_linux_ppc64.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_linux_ppc64le.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_netbsd.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_openbsd.go
/usr/lib/golang/src/golang.org/x/net/ipv4/zsys_solaris.go
/usr/lib/golang/src/golang.org/x/net/ipv6/control.go
/usr/lib/golang/src/golang.org/x/net/ipv6/control_rfc2292_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv6/control_rfc3542_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv6/control_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv6/control_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv6/control_windows.go
/usr/lib/golang/src/golang.org/x/net/ipv6/defs_darwin.go
/usr/lib/golang/src/golang.org/x/net/ipv6/defs_dragonfly.go
/usr/lib/golang/src/golang.org/x/net/ipv6/defs_freebsd.go
/usr/lib/golang/src/golang.org/x/net/ipv6/defs_linux.go
/usr/lib/golang/src/golang.org/x/net/ipv6/defs_netbsd.go
/usr/lib/golang/src/golang.org/x/net/ipv6/defs_openbsd.go
/usr/lib/golang/src/golang.org/x/net/ipv6/defs_solaris.go
/usr/lib/golang/src/golang.org/x/net/ipv6/dgramopt_posix.go
/usr/lib/golang/src/golang.org/x/net/ipv6/dgramopt_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv6/doc.go
/usr/lib/golang/src/golang.org/x/net/ipv6/endpoint.go
/usr/lib/golang/src/golang.org/x/net/ipv6/example_test.go
/usr/lib/golang/src/golang.org/x/net/ipv6/gen.go
/usr/lib/golang/src/golang.org/x/net/ipv6/genericopt_posix.go
/usr/lib/golang/src/golang.org/x/net/ipv6/genericopt_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv6/header.go
/usr/lib/golang/src/golang.org/x/net/ipv6/header_test.go
/usr/lib/golang/src/golang.org/x/net/ipv6/helper.go
/usr/lib/golang/src/golang.org/x/net/ipv6/helper_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv6/helper_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv6/helper_windows.go
/usr/lib/golang/src/golang.org/x/net/ipv6/iana.go
/usr/lib/golang/src/golang.org/x/net/ipv6/icmp.go
/usr/lib/golang/src/golang.org/x/net/ipv6/icmp_bsd.go
/usr/lib/golang/src/golang.org/x/net/ipv6/icmp_linux.go
/usr/lib/golang/src/golang.org/x/net/ipv6/icmp_solaris.go
/usr/lib/golang/src/golang.org/x/net/ipv6/icmp_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv6/icmp_test.go
/usr/lib/golang/src/golang.org/x/net/ipv6/icmp_windows.go
/usr/lib/golang/src/golang.org/x/net/ipv6/mocktransponder_test.go
/usr/lib/golang/src/golang.org/x/net/ipv6/multicast_test.go
/usr/lib/golang/src/golang.org/x/net/ipv6/multicastlistener_test.go
/usr/lib/golang/src/golang.org/x/net/ipv6/multicastsockopt_test.go
/usr/lib/golang/src/golang.org/x/net/ipv6/payload.go
/usr/lib/golang/src/golang.org/x/net/ipv6/payload_cmsg.go
/usr/lib/golang/src/golang.org/x/net/ipv6/payload_nocmsg.go
/usr/lib/golang/src/golang.org/x/net/ipv6/readwrite_test.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sockopt.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sockopt_asmreq_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sockopt_asmreq_windows.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sockopt_ssmreq_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sockopt_ssmreq_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sockopt_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sockopt_test.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sockopt_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sockopt_windows.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sys_bsd.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sys_darwin.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sys_freebsd.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sys_linux.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sys_stub.go
/usr/lib/golang/src/golang.org/x/net/ipv6/sys_windows.go
/usr/lib/golang/src/golang.org/x/net/ipv6/syscall_linux_386.go
/usr/lib/golang/src/golang.org/x/net/ipv6/syscall_unix.go
/usr/lib/golang/src/golang.org/x/net/ipv6/thunk_linux_386.s
/usr/lib/golang/src/golang.org/x/net/ipv6/unicast_test.go
/usr/lib/golang/src/golang.org/x/net/ipv6/unicastsockopt_test.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_darwin.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_dragonfly.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_freebsd_386.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_freebsd_amd64.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_freebsd_arm.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_linux_386.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_linux_amd64.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_linux_arm.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_linux_arm64.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_linux_ppc64.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_linux_ppc64le.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_netbsd.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_openbsd.go
/usr/lib/golang/src/golang.org/x/net/ipv6/zsys_solaris.go
/usr/lib/golang/src/golang.org/x/net/netutil/listen.go
/usr/lib/golang/src/golang.org/x/net/netutil/listen_test.go
/usr/lib/golang/src/golang.org/x/net/proxy/direct.go
/usr/lib/golang/src/golang.org/x/net/proxy/per_host.go
/usr/lib/golang/src/golang.org/x/net/proxy/per_host_test.go
/usr/lib/golang/src/golang.org/x/net/proxy/proxy.go
/usr/lib/golang/src/golang.org/x/net/proxy/proxy_test.go
/usr/lib/golang/src/golang.org/x/net/proxy/socks5.go
/usr/lib/golang/src/golang.org/x/net/publicsuffix/gen.go
/usr/lib/golang/src/golang.org/x/net/publicsuffix/list.go
/usr/lib/golang/src/golang.org/x/net/publicsuffix/list_test.go
/usr/lib/golang/src/golang.org/x/net/publicsuffix/table.go
/usr/lib/golang/src/golang.org/x/net/publicsuffix/table_test.go
/usr/lib/golang/src/golang.org/x/net/trace/events.go
/usr/lib/golang/src/golang.org/x/net/trace/histogram.go
/usr/lib/golang/src/golang.org/x/net/trace/histogram_test.go
/usr/lib/golang/src/golang.org/x/net/trace/trace.go
/usr/lib/golang/src/golang.org/x/net/trace/trace_test.go
/usr/lib/golang/src/golang.org/x/net/webdav/file.go
/usr/lib/golang/src/golang.org/x/net/webdav/file_test.go
/usr/lib/golang/src/golang.org/x/net/webdav/if.go
/usr/lib/golang/src/golang.org/x/net/webdav/if_test.go
/usr/lib/golang/src/golang.org/x/net/webdav/internal/xml/atom_test.go
/usr/lib/golang/src/golang.org/x/net/webdav/internal/xml/example_test.go
/usr/lib/golang/src/golang.org/x/net/webdav/internal/xml/marshal.go
/usr/lib/golang/src/golang.org/x/net/webdav/internal/xml/marshal_test.go
/usr/lib/golang/src/golang.org/x/net/webdav/internal/xml/read.go
/usr/lib/golang/src/golang.org/x/net/webdav/internal/xml/read_test.go
/usr/lib/golang/src/golang.org/x/net/webdav/internal/xml/typeinfo.go
/usr/lib/golang/src/golang.org/x/net/webdav/internal/xml/xml.go
/usr/lib/golang/src/golang.org/x/net/webdav/internal/xml/xml_test.go
/usr/lib/golang/src/golang.org/x/net/webdav/litmus_test_server.go
/usr/lib/golang/src/golang.org/x/net/webdav/lock.go
/usr/lib/golang/src/golang.org/x/net/webdav/lock_test.go
/usr/lib/golang/src/golang.org/x/net/webdav/prop.go
/usr/lib/golang/src/golang.org/x/net/webdav/prop_test.go
/usr/lib/golang/src/golang.org/x/net/webdav/webdav.go
/usr/lib/golang/src/golang.org/x/net/webdav/webdav_test.go
/usr/lib/golang/src/golang.org/x/net/webdav/xml.go
/usr/lib/golang/src/golang.org/x/net/webdav/xml_test.go
/usr/lib/golang/src/golang.org/x/net/websocket/client.go
/usr/lib/golang/src/golang.org/x/net/websocket/exampledial_test.go
/usr/lib/golang/src/golang.org/x/net/websocket/examplehandler_test.go
/usr/lib/golang/src/golang.org/x/net/websocket/hybi.go
/usr/lib/golang/src/golang.org/x/net/websocket/hybi_test.go
/usr/lib/golang/src/golang.org/x/net/websocket/server.go
/usr/lib/golang/src/golang.org/x/net/websocket/websocket.go
/usr/lib/golang/src/golang.org/x/net/websocket/websocket_test.go
