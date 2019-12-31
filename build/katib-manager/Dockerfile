FROM cargo.caicloud.xyz/library/golang:1.12.12-stretch as build-env
# The GOPATH in the image is /go.
ADD . /go/src/github.com/kubeflow/katib
WORKDIR /go/src/github.com/kubeflow/katib/cmd/manager
RUN if [ "$(uname -m)" = "ppc64le" ] || [ "$(uname -m)" = "aarch64" ]; then \
        apk --update add git gcc musl-dev && \
        go build -o katib-manager ./v1alpha3; \
    else \
        go build -o katib-manager ./v1alpha3; \
    fi

RUN GRPC_HEALTH_PROBE_VERSION=v0.3.1 && \
    if [ "$(uname -m)" = "ppc64le" ]; then \
	wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-ppc64le; \
    else \
	wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64; \
    fi
    
RUN chmod +x /bin/grpc_health_probe

FROM cargo.caicloud.xyz/library/debian:stretch
WORKDIR /app
COPY --from=build-env /bin/grpc_health_probe /bin/
COPY --from=build-env /go/src/github.com/kubeflow/katib/cmd/manager/katib-manager /app/
ENTRYPOINT ["./katib-manager"]
CMD ["-w", "kubernetes"]
