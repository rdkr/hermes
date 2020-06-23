// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.24.0-devel
// 	protoc        v3.6.1
// source: hermes.proto

package proto

import (
	context "context"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

type Login struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Token string `protobuf:"bytes,1,opt,name=token,proto3" json:"token,omitempty"`
	Event string `protobuf:"bytes,2,opt,name=event,proto3" json:"event,omitempty"`
	Tz    string `protobuf:"bytes,3,opt,name=tz,proto3" json:"tz,omitempty"`
}

func (x *Login) Reset() {
	*x = Login{}
	if protoimpl.UnsafeEnabled {
		mi := &file_hermes_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Login) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Login) ProtoMessage() {}

func (x *Login) ProtoReflect() protoreflect.Message {
	mi := &file_hermes_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Login.ProtoReflect.Descriptor instead.
func (*Login) Descriptor() ([]byte, []int) {
	return file_hermes_proto_rawDescGZIP(), []int{0}
}

func (x *Login) GetToken() string {
	if x != nil {
		return x.Token
	}
	return ""
}

func (x *Login) GetEvent() string {
	if x != nil {
		return x.Event
	}
	return ""
}

func (x *Login) GetTz() string {
	if x != nil {
		return x.Tz
	}
	return ""
}

type Event struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id   int32  `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	Name string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
}

func (x *Event) Reset() {
	*x = Event{}
	if protoimpl.UnsafeEnabled {
		mi := &file_hermes_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Event) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Event) ProtoMessage() {}

func (x *Event) ProtoReflect() protoreflect.Message {
	mi := &file_hermes_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Event.ProtoReflect.Descriptor instead.
func (*Event) Descriptor() ([]byte, []int) {
	return file_hermes_proto_rawDescGZIP(), []int{1}
}

func (x *Event) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *Event) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

type Player struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name   string   `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Tz     string   `protobuf:"bytes,2,opt,name=tz,proto3" json:"tz,omitempty"`
	Events []*Event `protobuf:"bytes,3,rep,name=events,proto3" json:"events,omitempty"`
}

func (x *Player) Reset() {
	*x = Player{}
	if protoimpl.UnsafeEnabled {
		mi := &file_hermes_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Player) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Player) ProtoMessage() {}

func (x *Player) ProtoReflect() protoreflect.Message {
	mi := &file_hermes_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Player.ProtoReflect.Descriptor instead.
func (*Player) Descriptor() ([]byte, []int) {
	return file_hermes_proto_rawDescGZIP(), []int{2}
}

func (x *Player) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *Player) GetTz() string {
	if x != nil {
		return x.Tz
	}
	return ""
}

func (x *Player) GetEvents() []*Event {
	if x != nil {
		return x.Events
	}
	return nil
}

type Timerange struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id    int32  `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	Start int32  `protobuf:"varint,2,opt,name=start,proto3" json:"start,omitempty"`
	End   int32  `protobuf:"varint,3,opt,name=end,proto3" json:"end,omitempty"`
	Tz    string `protobuf:"bytes,4,opt,name=tz,proto3" json:"tz,omitempty"`
}

func (x *Timerange) Reset() {
	*x = Timerange{}
	if protoimpl.UnsafeEnabled {
		mi := &file_hermes_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Timerange) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Timerange) ProtoMessage() {}

func (x *Timerange) ProtoReflect() protoreflect.Message {
	mi := &file_hermes_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Timerange.ProtoReflect.Descriptor instead.
func (*Timerange) Descriptor() ([]byte, []int) {
	return file_hermes_proto_rawDescGZIP(), []int{3}
}

func (x *Timerange) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *Timerange) GetStart() int32 {
	if x != nil {
		return x.Start
	}
	return 0
}

func (x *Timerange) GetEnd() int32 {
	if x != nil {
		return x.End
	}
	return 0
}

func (x *Timerange) GetTz() string {
	if x != nil {
		return x.Tz
	}
	return ""
}

type Timeranges struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Timeranges []*Timerange `protobuf:"bytes,1,rep,name=timeranges,proto3" json:"timeranges,omitempty"`
	Token      string       `protobuf:"bytes,2,opt,name=token,proto3" json:"token,omitempty"`
	Event      string       `protobuf:"bytes,3,opt,name=event,proto3" json:"event,omitempty"`
}

func (x *Timeranges) Reset() {
	*x = Timeranges{}
	if protoimpl.UnsafeEnabled {
		mi := &file_hermes_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Timeranges) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Timeranges) ProtoMessage() {}

func (x *Timeranges) ProtoReflect() protoreflect.Message {
	mi := &file_hermes_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Timeranges.ProtoReflect.Descriptor instead.
func (*Timeranges) Descriptor() ([]byte, []int) {
	return file_hermes_proto_rawDescGZIP(), []int{4}
}

func (x *Timeranges) GetTimeranges() []*Timerange {
	if x != nil {
		return x.Timeranges
	}
	return nil
}

func (x *Timeranges) GetToken() string {
	if x != nil {
		return x.Token
	}
	return ""
}

func (x *Timeranges) GetEvent() string {
	if x != nil {
		return x.Event
	}
	return ""
}

type Empty struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *Empty) Reset() {
	*x = Empty{}
	if protoimpl.UnsafeEnabled {
		mi := &file_hermes_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Empty) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Empty) ProtoMessage() {}

func (x *Empty) ProtoReflect() protoreflect.Message {
	mi := &file_hermes_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Empty.ProtoReflect.Descriptor instead.
func (*Empty) Descriptor() ([]byte, []int) {
	return file_hermes_proto_rawDescGZIP(), []int{5}
}

var File_hermes_proto protoreflect.FileDescriptor

var file_hermes_proto_rawDesc = []byte{
	0x0a, 0x0c, 0x68, 0x65, 0x72, 0x6d, 0x65, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x43,
	0x0a, 0x05, 0x4c, 0x6f, 0x67, 0x69, 0x6e, 0x12, 0x14, 0x0a, 0x05, 0x74, 0x6f, 0x6b, 0x65, 0x6e,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x12, 0x14, 0x0a,
	0x05, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x65, 0x76,
	0x65, 0x6e, 0x74, 0x12, 0x0e, 0x0a, 0x02, 0x74, 0x7a, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x02, 0x74, 0x7a, 0x22, 0x2b, 0x0a, 0x05, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x0e, 0x0a, 0x02,
	0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x02, 0x69, 0x64, 0x12, 0x12, 0x0a, 0x04,
	0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65,
	0x22, 0x4c, 0x0a, 0x06, 0x50, 0x6c, 0x61, 0x79, 0x65, 0x72, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61,
	0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x0e,
	0x0a, 0x02, 0x74, 0x7a, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x02, 0x74, 0x7a, 0x12, 0x1e,
	0x0a, 0x06, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x18, 0x03, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x06,
	0x2e, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x52, 0x06, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x22, 0x53,
	0x0a, 0x09, 0x54, 0x69, 0x6d, 0x65, 0x72, 0x61, 0x6e, 0x67, 0x65, 0x12, 0x0e, 0x0a, 0x02, 0x69,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x02, 0x69, 0x64, 0x12, 0x14, 0x0a, 0x05, 0x73,
	0x74, 0x61, 0x72, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x05, 0x73, 0x74, 0x61, 0x72,
	0x74, 0x12, 0x10, 0x0a, 0x03, 0x65, 0x6e, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x05, 0x52, 0x03,
	0x65, 0x6e, 0x64, 0x12, 0x0e, 0x0a, 0x02, 0x74, 0x7a, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x02, 0x74, 0x7a, 0x22, 0x64, 0x0a, 0x0a, 0x54, 0x69, 0x6d, 0x65, 0x72, 0x61, 0x6e, 0x67, 0x65,
	0x73, 0x12, 0x2a, 0x0a, 0x0a, 0x74, 0x69, 0x6d, 0x65, 0x72, 0x61, 0x6e, 0x67, 0x65, 0x73, 0x18,
	0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x0a, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x72, 0x61, 0x6e, 0x67,
	0x65, 0x52, 0x0a, 0x74, 0x69, 0x6d, 0x65, 0x72, 0x61, 0x6e, 0x67, 0x65, 0x73, 0x12, 0x14, 0x0a,
	0x05, 0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x74, 0x6f,
	0x6b, 0x65, 0x6e, 0x12, 0x14, 0x0a, 0x05, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x18, 0x03, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x05, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x22, 0x07, 0x0a, 0x05, 0x45, 0x6d, 0x70,
	0x74, 0x79, 0x32, 0x9c, 0x01, 0x0a, 0x07, 0x47, 0x61, 0x74, 0x65, 0x77, 0x61, 0x79, 0x12, 0x1c,
	0x0a, 0x09, 0x47, 0x65, 0x74, 0x50, 0x6c, 0x61, 0x79, 0x65, 0x72, 0x12, 0x06, 0x2e, 0x4c, 0x6f,
	0x67, 0x69, 0x6e, 0x1a, 0x07, 0x2e, 0x50, 0x6c, 0x61, 0x79, 0x65, 0x72, 0x12, 0x24, 0x0a, 0x0d,
	0x47, 0x65, 0x74, 0x54, 0x69, 0x6d, 0x65, 0x72, 0x61, 0x6e, 0x67, 0x65, 0x73, 0x12, 0x06, 0x2e,
	0x4c, 0x6f, 0x67, 0x69, 0x6e, 0x1a, 0x0b, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x72, 0x61, 0x6e, 0x67,
	0x65, 0x73, 0x12, 0x24, 0x0a, 0x0d, 0x53, 0x65, 0x74, 0x54, 0x69, 0x6d, 0x65, 0x72, 0x61, 0x6e,
	0x67, 0x65, 0x73, 0x12, 0x0b, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x72, 0x61, 0x6e, 0x67, 0x65, 0x73,
	0x1a, 0x06, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x12, 0x27, 0x0a, 0x10, 0x44, 0x65, 0x6c, 0x65,
	0x74, 0x65, 0x54, 0x69, 0x6d, 0x65, 0x72, 0x61, 0x6e, 0x67, 0x65, 0x73, 0x12, 0x0b, 0x2e, 0x54,
	0x69, 0x6d, 0x65, 0x72, 0x61, 0x6e, 0x67, 0x65, 0x73, 0x1a, 0x06, 0x2e, 0x45, 0x6d, 0x70, 0x74,
	0x79, 0x42, 0x09, 0x5a, 0x07, 0x2e, 0x3b, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_hermes_proto_rawDescOnce sync.Once
	file_hermes_proto_rawDescData = file_hermes_proto_rawDesc
)

func file_hermes_proto_rawDescGZIP() []byte {
	file_hermes_proto_rawDescOnce.Do(func() {
		file_hermes_proto_rawDescData = protoimpl.X.CompressGZIP(file_hermes_proto_rawDescData)
	})
	return file_hermes_proto_rawDescData
}

var file_hermes_proto_msgTypes = make([]protoimpl.MessageInfo, 6)
var file_hermes_proto_goTypes = []interface{}{
	(*Login)(nil),      // 0: Login
	(*Event)(nil),      // 1: Event
	(*Player)(nil),     // 2: Player
	(*Timerange)(nil),  // 3: Timerange
	(*Timeranges)(nil), // 4: Timeranges
	(*Empty)(nil),      // 5: Empty
}
var file_hermes_proto_depIdxs = []int32{
	1, // 0: Player.events:type_name -> Event
	3, // 1: Timeranges.timeranges:type_name -> Timerange
	0, // 2: Gateway.GetPlayer:input_type -> Login
	0, // 3: Gateway.GetTimeranges:input_type -> Login
	4, // 4: Gateway.SetTimeranges:input_type -> Timeranges
	4, // 5: Gateway.DeleteTimeranges:input_type -> Timeranges
	2, // 6: Gateway.GetPlayer:output_type -> Player
	4, // 7: Gateway.GetTimeranges:output_type -> Timeranges
	5, // 8: Gateway.SetTimeranges:output_type -> Empty
	5, // 9: Gateway.DeleteTimeranges:output_type -> Empty
	6, // [6:10] is the sub-list for method output_type
	2, // [2:6] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_hermes_proto_init() }
func file_hermes_proto_init() {
	if File_hermes_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_hermes_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Login); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_hermes_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Event); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_hermes_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Player); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_hermes_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Timerange); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_hermes_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Timeranges); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_hermes_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Empty); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_hermes_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   6,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_hermes_proto_goTypes,
		DependencyIndexes: file_hermes_proto_depIdxs,
		MessageInfos:      file_hermes_proto_msgTypes,
	}.Build()
	File_hermes_proto = out.File
	file_hermes_proto_rawDesc = nil
	file_hermes_proto_goTypes = nil
	file_hermes_proto_depIdxs = nil
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// GatewayClient is the client API for Gateway service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type GatewayClient interface {
	GetPlayer(ctx context.Context, in *Login, opts ...grpc.CallOption) (*Player, error)
	GetTimeranges(ctx context.Context, in *Login, opts ...grpc.CallOption) (*Timeranges, error)
	SetTimeranges(ctx context.Context, in *Timeranges, opts ...grpc.CallOption) (*Empty, error)
	DeleteTimeranges(ctx context.Context, in *Timeranges, opts ...grpc.CallOption) (*Empty, error)
}

type gatewayClient struct {
	cc grpc.ClientConnInterface
}

func NewGatewayClient(cc grpc.ClientConnInterface) GatewayClient {
	return &gatewayClient{cc}
}

func (c *gatewayClient) GetPlayer(ctx context.Context, in *Login, opts ...grpc.CallOption) (*Player, error) {
	out := new(Player)
	err := c.cc.Invoke(ctx, "/Gateway/GetPlayer", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayClient) GetTimeranges(ctx context.Context, in *Login, opts ...grpc.CallOption) (*Timeranges, error) {
	out := new(Timeranges)
	err := c.cc.Invoke(ctx, "/Gateway/GetTimeranges", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayClient) SetTimeranges(ctx context.Context, in *Timeranges, opts ...grpc.CallOption) (*Empty, error) {
	out := new(Empty)
	err := c.cc.Invoke(ctx, "/Gateway/SetTimeranges", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayClient) DeleteTimeranges(ctx context.Context, in *Timeranges, opts ...grpc.CallOption) (*Empty, error) {
	out := new(Empty)
	err := c.cc.Invoke(ctx, "/Gateway/DeleteTimeranges", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// GatewayServer is the server API for Gateway service.
type GatewayServer interface {
	GetPlayer(context.Context, *Login) (*Player, error)
	GetTimeranges(context.Context, *Login) (*Timeranges, error)
	SetTimeranges(context.Context, *Timeranges) (*Empty, error)
	DeleteTimeranges(context.Context, *Timeranges) (*Empty, error)
}

// UnimplementedGatewayServer can be embedded to have forward compatible implementations.
type UnimplementedGatewayServer struct {
}

func (*UnimplementedGatewayServer) GetPlayer(context.Context, *Login) (*Player, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetPlayer not implemented")
}
func (*UnimplementedGatewayServer) GetTimeranges(context.Context, *Login) (*Timeranges, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetTimeranges not implemented")
}
func (*UnimplementedGatewayServer) SetTimeranges(context.Context, *Timeranges) (*Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SetTimeranges not implemented")
}
func (*UnimplementedGatewayServer) DeleteTimeranges(context.Context, *Timeranges) (*Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteTimeranges not implemented")
}

func RegisterGatewayServer(s *grpc.Server, srv GatewayServer) {
	s.RegisterService(&_Gateway_serviceDesc, srv)
}

func _Gateway_GetPlayer_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Login)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServer).GetPlayer(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Gateway/GetPlayer",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServer).GetPlayer(ctx, req.(*Login))
	}
	return interceptor(ctx, in, info, handler)
}

func _Gateway_GetTimeranges_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Login)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServer).GetTimeranges(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Gateway/GetTimeranges",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServer).GetTimeranges(ctx, req.(*Login))
	}
	return interceptor(ctx, in, info, handler)
}

func _Gateway_SetTimeranges_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Timeranges)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServer).SetTimeranges(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Gateway/SetTimeranges",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServer).SetTimeranges(ctx, req.(*Timeranges))
	}
	return interceptor(ctx, in, info, handler)
}

func _Gateway_DeleteTimeranges_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Timeranges)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServer).DeleteTimeranges(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Gateway/DeleteTimeranges",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServer).DeleteTimeranges(ctx, req.(*Timeranges))
	}
	return interceptor(ctx, in, info, handler)
}

var _Gateway_serviceDesc = grpc.ServiceDesc{
	ServiceName: "Gateway",
	HandlerType: (*GatewayServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetPlayer",
			Handler:    _Gateway_GetPlayer_Handler,
		},
		{
			MethodName: "GetTimeranges",
			Handler:    _Gateway_GetTimeranges_Handler,
		},
		{
			MethodName: "SetTimeranges",
			Handler:    _Gateway_SetTimeranges_Handler,
		},
		{
			MethodName: "DeleteTimeranges",
			Handler:    _Gateway_DeleteTimeranges_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "hermes.proto",
}
