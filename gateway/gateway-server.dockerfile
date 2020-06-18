FROM golang as build

WORKDIR /app

COPY go.* ./
RUN go mod download

COPY proto/*.go ./proto/
COPY *.go ./

RUN go build

FROM gcr.io/distroless/base
COPY --from=build /app/gateway /gateway

ENTRYPOINT ["/gateway"]
