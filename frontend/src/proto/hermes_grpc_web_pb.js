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
 *   !proto.Timeranges>}
 */
const methodDescriptor_Gateway_PutTimeranges = new grpc.web.MethodDescriptor(
  '/Gateway/PutTimeranges',
  grpc.web.MethodType.UNARY,
  proto.Timeranges,
  proto.Timeranges,
  /**
   * @param {!proto.Timeranges} request
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
 *   !proto.Timeranges,
 *   !proto.Timeranges>}
 */
const methodInfo_Gateway_PutTimeranges = new grpc.web.AbstractClientBase.MethodInfo(
  proto.Timeranges,
  /**
   * @param {!proto.Timeranges} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.Timeranges.deserializeBinary
);


/**
 * @param {!proto.Timeranges} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.Timeranges)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.Timeranges>|undefined}
 *     The XHR Node Readable Stream
 */
proto.GatewayClient.prototype.putTimeranges =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/Gateway/PutTimeranges',
      request,
      metadata || {},
      methodDescriptor_Gateway_PutTimeranges,
      callback);
};


/**
 * @param {!proto.Timeranges} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.Timeranges>}
 *     A native promise that resolves to the response
 */
proto.GatewayPromiseClient.prototype.putTimeranges =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/Gateway/PutTimeranges',
      request,
      metadata || {},
      methodDescriptor_Gateway_PutTimeranges);
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


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.SchedulerClient =
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
proto.SchedulerPromiseClient =
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
 *   !proto.Event,
 *   !proto.Empty>}
 */
const methodDescriptor_Scheduler_NotifyUpdated = new grpc.web.MethodDescriptor(
  '/Scheduler/NotifyUpdated',
  grpc.web.MethodType.UNARY,
  proto.Event,
  proto.Empty,
  /**
   * @param {!proto.Event} request
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
 *   !proto.Event,
 *   !proto.Empty>}
 */
const methodInfo_Scheduler_NotifyUpdated = new grpc.web.AbstractClientBase.MethodInfo(
  proto.Empty,
  /**
   * @param {!proto.Event} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.Empty.deserializeBinary
);


/**
 * @param {!proto.Event} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.Empty)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.Empty>|undefined}
 *     The XHR Node Readable Stream
 */
proto.SchedulerClient.prototype.notifyUpdated =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/Scheduler/NotifyUpdated',
      request,
      metadata || {},
      methodDescriptor_Scheduler_NotifyUpdated,
      callback);
};


/**
 * @param {!proto.Event} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.Empty>}
 *     A native promise that resolves to the response
 */
proto.SchedulerPromiseClient.prototype.notifyUpdated =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/Scheduler/NotifyUpdated',
      request,
      metadata || {},
      methodDescriptor_Scheduler_NotifyUpdated);
};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.EventDbClient =
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
proto.EventDbPromiseClient =
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
 *   !proto.GetMagicTokenRequest,
 *   !proto.GetMagicTokenResponse>}
 */
const methodDescriptor_EventDb_GetMagicToken = new grpc.web.MethodDescriptor(
  '/EventDb/GetMagicToken',
  grpc.web.MethodType.UNARY,
  proto.GetMagicTokenRequest,
  proto.GetMagicTokenResponse,
  /**
   * @param {!proto.GetMagicTokenRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.GetMagicTokenResponse.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.GetMagicTokenRequest,
 *   !proto.GetMagicTokenResponse>}
 */
const methodInfo_EventDb_GetMagicToken = new grpc.web.AbstractClientBase.MethodInfo(
  proto.GetMagicTokenResponse,
  /**
   * @param {!proto.GetMagicTokenRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.GetMagicTokenResponse.deserializeBinary
);


/**
 * @param {!proto.GetMagicTokenRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.GetMagicTokenResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.GetMagicTokenResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.EventDbClient.prototype.getMagicToken =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/EventDb/GetMagicToken',
      request,
      metadata || {},
      methodDescriptor_EventDb_GetMagicToken,
      callback);
};


/**
 * @param {!proto.GetMagicTokenRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.GetMagicTokenResponse>}
 *     A native promise that resolves to the response
 */
proto.EventDbPromiseClient.prototype.getMagicToken =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/EventDb/GetMagicToken',
      request,
      metadata || {},
      methodDescriptor_EventDb_GetMagicToken);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.Empty,
 *   !proto.GetEventsResponse>}
 */
const methodDescriptor_EventDb_GetEvents = new grpc.web.MethodDescriptor(
  '/EventDb/GetEvents',
  grpc.web.MethodType.UNARY,
  proto.Empty,
  proto.GetEventsResponse,
  /**
   * @param {!proto.Empty} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.GetEventsResponse.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.Empty,
 *   !proto.GetEventsResponse>}
 */
const methodInfo_EventDb_GetEvents = new grpc.web.AbstractClientBase.MethodInfo(
  proto.GetEventsResponse,
  /**
   * @param {!proto.Empty} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.GetEventsResponse.deserializeBinary
);


/**
 * @param {!proto.Empty} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.GetEventsResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.GetEventsResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.EventDbClient.prototype.getEvents =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/EventDb/GetEvents',
      request,
      metadata || {},
      methodDescriptor_EventDb_GetEvents,
      callback);
};


/**
 * @param {!proto.Empty} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.GetEventsResponse>}
 *     A native promise that resolves to the response
 */
proto.EventDbPromiseClient.prototype.getEvents =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/EventDb/GetEvents',
      request,
      metadata || {},
      methodDescriptor_EventDb_GetEvents);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.GetEventPlayersRequest,
 *   !proto.GetEventPlayersResponse>}
 */
const methodDescriptor_EventDb_GetEventPlayers = new grpc.web.MethodDescriptor(
  '/EventDb/GetEventPlayers',
  grpc.web.MethodType.UNARY,
  proto.GetEventPlayersRequest,
  proto.GetEventPlayersResponse,
  /**
   * @param {!proto.GetEventPlayersRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.GetEventPlayersResponse.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.GetEventPlayersRequest,
 *   !proto.GetEventPlayersResponse>}
 */
const methodInfo_EventDb_GetEventPlayers = new grpc.web.AbstractClientBase.MethodInfo(
  proto.GetEventPlayersResponse,
  /**
   * @param {!proto.GetEventPlayersRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.GetEventPlayersResponse.deserializeBinary
);


/**
 * @param {!proto.GetEventPlayersRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.GetEventPlayersResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.GetEventPlayersResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.EventDbClient.prototype.getEventPlayers =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/EventDb/GetEventPlayers',
      request,
      metadata || {},
      methodDescriptor_EventDb_GetEventPlayers,
      callback);
};


/**
 * @param {!proto.GetEventPlayersRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.GetEventPlayersResponse>}
 *     A native promise that resolves to the response
 */
proto.EventDbPromiseClient.prototype.getEventPlayers =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/EventDb/GetEventPlayers',
      request,
      metadata || {},
      methodDescriptor_EventDb_GetEventPlayers);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.SyncEventPlayerRequest,
 *   !proto.Empty>}
 */
const methodDescriptor_EventDb_SyncEventPlayers = new grpc.web.MethodDescriptor(
  '/EventDb/SyncEventPlayers',
  grpc.web.MethodType.UNARY,
  proto.SyncEventPlayerRequest,
  proto.Empty,
  /**
   * @param {!proto.SyncEventPlayerRequest} request
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
 *   !proto.SyncEventPlayerRequest,
 *   !proto.Empty>}
 */
const methodInfo_EventDb_SyncEventPlayers = new grpc.web.AbstractClientBase.MethodInfo(
  proto.Empty,
  /**
   * @param {!proto.SyncEventPlayerRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.Empty.deserializeBinary
);


/**
 * @param {!proto.SyncEventPlayerRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.Empty)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.Empty>|undefined}
 *     The XHR Node Readable Stream
 */
proto.EventDbClient.prototype.syncEventPlayers =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/EventDb/SyncEventPlayers',
      request,
      metadata || {},
      methodDescriptor_EventDb_SyncEventPlayers,
      callback);
};


/**
 * @param {!proto.SyncEventPlayerRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.Empty>}
 *     A native promise that resolves to the response
 */
proto.EventDbPromiseClient.prototype.syncEventPlayers =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/EventDb/SyncEventPlayers',
      request,
      metadata || {},
      methodDescriptor_EventDb_SyncEventPlayers);
};


module.exports = proto;

