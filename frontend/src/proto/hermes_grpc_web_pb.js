/* eslint-disable */
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

const proto = require('./hermes_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.GatewayClient =
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
proto.GatewayPromiseClient =
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
 *   !proto.Login,
 *   !proto.Player>}
 */
const methodDescriptor_Gateway_GetPlayer = new grpc.web.MethodDescriptor(
  '/Gateway/GetPlayer',
  grpc.web.MethodType.UNARY,
  proto.Login,
  proto.Player,
  /**
   * @param {!proto.Login} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.Player.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.Login,
 *   !proto.Player>}
 */
const methodInfo_Gateway_GetPlayer = new grpc.web.AbstractClientBase.MethodInfo(
  proto.Player,
  /**
   * @param {!proto.Login} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.Player.deserializeBinary
);


/**
 * @param {!proto.Login} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.Player)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.Player>|undefined}
 *     The XHR Node Readable Stream
 */
proto.GatewayClient.prototype.getPlayer =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/Gateway/GetPlayer',
      request,
      metadata || {},
      methodDescriptor_Gateway_GetPlayer,
      callback);
};


/**
 * @param {!proto.Login} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.Player>}
 *     A native promise that resolves to the response
 */
proto.GatewayPromiseClient.prototype.getPlayer =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/Gateway/GetPlayer',
      request,
      metadata || {},
      methodDescriptor_Gateway_GetPlayer);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.Login,
 *   !proto.Timeranges>}
 */
const methodDescriptor_Gateway_GetTimeranges = new grpc.web.MethodDescriptor(
  '/Gateway/GetTimeranges',
  grpc.web.MethodType.UNARY,
  proto.Login,
  proto.Timeranges,
  /**
   * @param {!proto.Login} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.Timeranges.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.Login,
 *   !proto.Timeranges>}
 */
const methodInfo_Gateway_GetTimeranges = new grpc.web.AbstractClientBase.MethodInfo(
  proto.Timeranges,
  /**
   * @param {!proto.Login} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.Timeranges.deserializeBinary
);


/**
 * @param {!proto.Login} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.Timeranges)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.Timeranges>|undefined}
 *     The XHR Node Readable Stream
 */
proto.GatewayClient.prototype.getTimeranges =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/Gateway/GetTimeranges',
      request,
      metadata || {},
      methodDescriptor_Gateway_GetTimeranges,
      callback);
};


/**
 * @param {!proto.Login} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.Timeranges>}
 *     A native promise that resolves to the response
 */
proto.GatewayPromiseClient.prototype.getTimeranges =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/Gateway/GetTimeranges',
      request,
      metadata || {},
      methodDescriptor_Gateway_GetTimeranges);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.Timeranges,
 *   !proto.Empty>}
 */
const methodDescriptor_Gateway_SetTimeranges = new grpc.web.MethodDescriptor(
  '/Gateway/SetTimeranges',
  grpc.web.MethodType.UNARY,
  proto.Timeranges,
  proto.Empty,
  /**
   * @param {!proto.Timeranges} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.Empty.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.Timeranges,
 *   !proto.Empty>}
 */
const methodInfo_Gateway_SetTimeranges = new grpc.web.AbstractClientBase.MethodInfo(
  proto.Empty,
  /**
   * @param {!proto.Timeranges} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.Empty.deserializeBinary
);


/**
 * @param {!proto.Timeranges} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.Empty)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.Empty>|undefined}
 *     The XHR Node Readable Stream
 */
proto.GatewayClient.prototype.setTimeranges =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/Gateway/SetTimeranges',
      request,
      metadata || {},
      methodDescriptor_Gateway_SetTimeranges,
      callback);
};


/**
 * @param {!proto.Timeranges} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.Empty>}
 *     A native promise that resolves to the response
 */
proto.GatewayPromiseClient.prototype.setTimeranges =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/Gateway/SetTimeranges',
      request,
      metadata || {},
      methodDescriptor_Gateway_SetTimeranges);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.Timeranges,
 *   !proto.Empty>}
 */
const methodDescriptor_Gateway_DeleteTimeranges = new grpc.web.MethodDescriptor(
  '/Gateway/DeleteTimeranges',
  grpc.web.MethodType.UNARY,
  proto.Timeranges,
  proto.Empty,
  /**
   * @param {!proto.Timeranges} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.Empty.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.Timeranges,
 *   !proto.Empty>}
 */
const methodInfo_Gateway_DeleteTimeranges = new grpc.web.AbstractClientBase.MethodInfo(
  proto.Empty,
  /**
   * @param {!proto.Timeranges} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.Empty.deserializeBinary
);


/**
 * @param {!proto.Timeranges} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.Empty)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.Empty>|undefined}
 *     The XHR Node Readable Stream
 */
proto.GatewayClient.prototype.deleteTimeranges =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/Gateway/DeleteTimeranges',
      request,
      metadata || {},
      methodDescriptor_Gateway_DeleteTimeranges,
      callback);
};


/**
 * @param {!proto.Timeranges} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.Empty>}
 *     A native promise that resolves to the response
 */
proto.GatewayPromiseClient.prototype.deleteTimeranges =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/Gateway/DeleteTimeranges',
      request,
      metadata || {},
      methodDescriptor_Gateway_DeleteTimeranges);
};


module.exports = proto;
