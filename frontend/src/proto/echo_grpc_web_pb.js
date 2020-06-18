/**
 * @fileoverview gRPC-Web generated client stub for
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = require('./echo_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.EchoServiceClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.EchoServicePromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.EchoRequestList,
 *   !proto.EchoResponse>}
 */
const methodDescriptor_EchoService_Echo = new grpc.web.MethodDescriptor(
  '/EchoService/Echo',
  grpc.web.MethodType.UNARY,
  proto.EchoRequestList,
  proto.EchoResponse,
  /**
   * @param {!proto.EchoRequestList} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.EchoResponse.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.EchoRequestList,
 *   !proto.EchoResponse>}
 */
const methodInfo_EchoService_Echo = new grpc.web.AbstractClientBase.MethodInfo(
  proto.EchoResponse,
  /**
   * @param {!proto.EchoRequestList} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.EchoResponse.deserializeBinary
);


/**
 * @param {!proto.EchoRequestList} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.EchoResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.EchoResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.EchoServiceClient.prototype.echo =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/EchoService/Echo',
      request,
      metadata || {},
      methodDescriptor_EchoService_Echo,
      callback);
};


/**
 * @param {!proto.EchoRequestList} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.EchoResponse>}
 *     A native promise that resolves to the response
 */
proto.EchoServicePromiseClient.prototype.echo =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/EchoService/Echo',
      request,
      metadata || {},
      methodDescriptor_EchoService_Echo);
};


module.exports = proto;
