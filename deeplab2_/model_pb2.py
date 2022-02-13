# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deeplab2/model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='deeplab2/model.proto',
  package='deeplab2',
  syntax='proto2',
  serialized_options=_b('P\001'),
  serialized_pb=_b('\n\x14\x64\x65\x65plab2/model.proto\x12\x08\x64\x65\x65plab2\"\xd7\x01\n\x0e\x44\x65\x63oderOptions\x12\x13\n\x0b\x66\x65\x61ture_key\x18\x01 \x01(\t\x12\x1d\n\x10\x64\x65\x63oder_channels\x18\x02 \x01(\x05:\x03\x32\x35\x36\x12\x33\n\x11\x64\x65\x63oder_conv_type\x18\x05 \x01(\t:\x18\x64\x65pthwise_separable_conv\x12\x1a\n\raspp_channels\x18\x03 \x01(\x05:\x03\x32\x35\x36\x12\x14\n\x0c\x61trous_rates\x18\x04 \x03(\x05\x12*\n\x1b\x61spp_use_only_1x1_proj_conv\x18\x06 \x01(\x08:\x05\x66\x61lse\"@\n\x0fLowLevelOptions\x12\x13\n\x0b\x66\x65\x61ture_key\x18\x01 \x01(\t\x12\x18\n\x10\x63hannels_project\x18\x02 \x01(\x05\"\xbd\x01\n\x0bHeadOptions\x12\x17\n\x0foutput_channels\x18\x01 \x01(\x05\x12\x15\n\rhead_channels\x18\x02 \x01(\x05\x12\x30\n\x0ehead_conv_type\x18\x03 \x01(\t:\x18\x64\x65pthwise_separable_conv\x12%\n\x1amax_value_after_activation\x18\x04 \x01(\x02:\x01\x30\x12%\n\x1amin_value_after_activation\x18\x05 \x01(\x02:\x01\x30\"\xac\x02\n\x0fInstanceOptions\x12\x14\n\x06\x65nable\x18\x01 \x01(\x08:\x04true\x12\x35\n\x12low_level_override\x18\x02 \x03(\x0b\x32\x19.deeplab2.LowLevelOptions\x12;\n\x19instance_decoder_override\x18\x03 \x01(\x0b\x32\x18.deeplab2.DecoderOptions\x12*\n\x0b\x63\x65nter_head\x18\x04 \x01(\x0b\x32\x15.deeplab2.HeadOptions\x12.\n\x0fregression_head\x18\x05 \x01(\x0b\x32\x15.deeplab2.HeadOptions\x12\x33\n\x14next_regression_head\x18\x06 \x01(\x0b\x32\x15.deeplab2.HeadOptions\"\x83\x0e\n\x0cModelOptions\x12\x38\n\x08\x62\x61\x63kbone\x18\x01 \x01(\x0b\x32&.deeplab2.ModelOptions.BackboneOptions\x12)\n\x07\x64\x65\x63oder\x18\x02 \x01(\x0b\x32\x18.deeplab2.DecoderOptions\x12=\n\ndeeplab_v3\x18\x03 \x01(\x0b\x32\'.deeplab2.ModelOptions.DeeplabV3OptionsH\x00\x12\x46\n\x0f\x64\x65\x65plab_v3_plus\x18\x04 \x01(\x0b\x32+.deeplab2.ModelOptions.DeeplabV3PlusOptionsH\x00\x12I\n\x10panoptic_deeplab\x18\x05 \x01(\x0b\x32-.deeplab2.ModelOptions.PanopticDeeplabOptionsH\x00\x12\x45\n\x0emotion_deeplab\x18\x07 \x01(\x0b\x32+.deeplab2.ModelOptions.MotionDeepLabOptionsH\x00\x12?\n\x0bmax_deeplab\x18\n \x01(\x0b\x32(.deeplab2.ModelOptions.MaXDeepLabOptionsH\x00\x12\x44\n\x0bvip_deeplab\x18\x0b \x01(\x0b\x32-.deeplab2.ModelOptions.PanopticDeeplabOptionsH\x00\x12\x1a\n\x12initial_checkpoint\x18\x06 \x01(\t\x12\x41\n3restore_semantic_last_layer_from_initial_checkpoint\x18\x08 \x01(\x08:\x04true\x12\x41\n3restore_instance_last_layer_from_initial_checkpoint\x18\t \x01(\x08:\x04true\x1a\xde\x02\n\x0f\x42\x61\x63kboneOptions\x12\x16\n\x04name\x18\x01 \x01(\t:\x08resnet50\x12\x19\n\routput_stride\x18\x02 \x01(\x05:\x02\x33\x32\x12\x1a\n\x12pretrained_weights\x18\x03 \x01(\t\x12%\n\x16use_squeeze_and_excite\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x13\x64rop_path_keep_prob\x18\x05 \x01(\x02:\x01\x31\x12$\n\x12\x64rop_path_schedule\x18\x06 \x01(\t:\x08\x63onstant\x12 \n\x15stem_width_multiplier\x18\x07 \x01(\x02:\x01\x31\x12$\n\x19\x62\x61\x63kbone_width_multiplier\x18\x08 \x01(\x02:\x01\x31\x12$\n\x19\x62\x61\x63kbone_layer_multiplier\x18\t \x01(\x02:\x01\x31\x12!\n\x15use_sac_beyond_stride\x18\n \x01(\x05:\x02-1\x1a\'\n\x10\x44\x65\x65plabV3Options\x12\x13\n\x0bnum_classes\x18\x01 \x01(\x05\x1aY\n\x14\x44\x65\x65plabV3PlusOptions\x12,\n\tlow_level\x18\x01 \x01(\x0b\x32\x19.deeplab2.LowLevelOptions\x12\x13\n\x0bnum_classes\x18\x02 \x01(\x05\x1a\xcc\x01\n\x16PanopticDeeplabOptions\x12,\n\tlow_level\x18\x01 \x03(\x0b\x32\x19.deeplab2.LowLevelOptions\x12+\n\x08instance\x18\x02 \x01(\x0b\x32\x19.deeplab2.InstanceOptions\x12,\n\rsemantic_head\x18\x03 \x01(\x0b\x32\x15.deeplab2.HeadOptions\x12)\n\ndepth_head\x18\x04 \x01(\x0b\x32\x15.deeplab2.HeadOptions\x1a\xcb\x01\n\x14MotionDeepLabOptions\x12,\n\tlow_level\x18\x01 \x03(\x0b\x32\x19.deeplab2.LowLevelOptions\x12+\n\x08instance\x18\x02 \x01(\x0b\x32\x19.deeplab2.InstanceOptions\x12,\n\rsemantic_head\x18\x03 \x01(\x0b\x32\x15.deeplab2.HeadOptions\x12*\n\x0bmotion_head\x18\x04 \x01(\x0b\x32\x15.deeplab2.HeadOptions\x1a\xb4\x01\n\x11MaXDeepLabOptions\x12/\n\x10pixel_space_head\x18\x01 \x01(\x0b\x32\x15.deeplab2.HeadOptions\x12\x36\n\x13\x61uxiliary_low_level\x18\x02 \x03(\x0b\x32\x19.deeplab2.LowLevelOptions\x12\x36\n\x17\x61uxiliary_semantic_head\x18\x03 \x01(\x0b\x32\x15.deeplab2.HeadOptionsB\x13\n\x11meta_architectureB\x02P\x01')
)




_DECODEROPTIONS = _descriptor.Descriptor(
  name='DecoderOptions',
  full_name='deeplab2.DecoderOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_key', full_name='deeplab2.DecoderOptions.feature_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decoder_channels', full_name='deeplab2.DecoderOptions.decoder_channels', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=256,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decoder_conv_type', full_name='deeplab2.DecoderOptions.decoder_conv_type', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("depthwise_separable_conv").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aspp_channels', full_name='deeplab2.DecoderOptions.aspp_channels', index=3,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=256,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='atrous_rates', full_name='deeplab2.DecoderOptions.atrous_rates', index=4,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aspp_use_only_1x1_proj_conv', full_name='deeplab2.DecoderOptions.aspp_use_only_1x1_proj_conv', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=250,
)


_LOWLEVELOPTIONS = _descriptor.Descriptor(
  name='LowLevelOptions',
  full_name='deeplab2.LowLevelOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_key', full_name='deeplab2.LowLevelOptions.feature_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channels_project', full_name='deeplab2.LowLevelOptions.channels_project', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=316,
)


_HEADOPTIONS = _descriptor.Descriptor(
  name='HeadOptions',
  full_name='deeplab2.HeadOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_channels', full_name='deeplab2.HeadOptions.output_channels', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='head_channels', full_name='deeplab2.HeadOptions.head_channels', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='head_conv_type', full_name='deeplab2.HeadOptions.head_conv_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("depthwise_separable_conv").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_value_after_activation', full_name='deeplab2.HeadOptions.max_value_after_activation', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_value_after_activation', full_name='deeplab2.HeadOptions.min_value_after_activation', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=508,
)


_INSTANCEOPTIONS = _descriptor.Descriptor(
  name='InstanceOptions',
  full_name='deeplab2.InstanceOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable', full_name='deeplab2.InstanceOptions.enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low_level_override', full_name='deeplab2.InstanceOptions.low_level_override', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_decoder_override', full_name='deeplab2.InstanceOptions.instance_decoder_override', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='center_head', full_name='deeplab2.InstanceOptions.center_head', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regression_head', full_name='deeplab2.InstanceOptions.regression_head', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_regression_head', full_name='deeplab2.InstanceOptions.next_regression_head', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=511,
  serialized_end=811,
)


_MODELOPTIONS_BACKBONEOPTIONS = _descriptor.Descriptor(
  name='BackboneOptions',
  full_name='deeplab2.ModelOptions.BackboneOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='deeplab2.ModelOptions.BackboneOptions.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("resnet50").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_stride', full_name='deeplab2.ModelOptions.BackboneOptions.output_stride', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=32,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pretrained_weights', full_name='deeplab2.ModelOptions.BackboneOptions.pretrained_weights', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_squeeze_and_excite', full_name='deeplab2.ModelOptions.BackboneOptions.use_squeeze_and_excite', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drop_path_keep_prob', full_name='deeplab2.ModelOptions.BackboneOptions.drop_path_keep_prob', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drop_path_schedule', full_name='deeplab2.ModelOptions.BackboneOptions.drop_path_schedule', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("constant").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stem_width_multiplier', full_name='deeplab2.ModelOptions.BackboneOptions.stem_width_multiplier', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backbone_width_multiplier', full_name='deeplab2.ModelOptions.BackboneOptions.backbone_width_multiplier', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backbone_layer_multiplier', full_name='deeplab2.ModelOptions.BackboneOptions.backbone_layer_multiplier', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_sac_beyond_stride', full_name='deeplab2.ModelOptions.BackboneOptions.use_sac_beyond_stride', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1510,
  serialized_end=1860,
)

_MODELOPTIONS_DEEPLABV3OPTIONS = _descriptor.Descriptor(
  name='DeeplabV3Options',
  full_name='deeplab2.ModelOptions.DeeplabV3Options',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_classes', full_name='deeplab2.ModelOptions.DeeplabV3Options.num_classes', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1862,
  serialized_end=1901,
)

_MODELOPTIONS_DEEPLABV3PLUSOPTIONS = _descriptor.Descriptor(
  name='DeeplabV3PlusOptions',
  full_name='deeplab2.ModelOptions.DeeplabV3PlusOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='low_level', full_name='deeplab2.ModelOptions.DeeplabV3PlusOptions.low_level', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_classes', full_name='deeplab2.ModelOptions.DeeplabV3PlusOptions.num_classes', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1903,
  serialized_end=1992,
)

_MODELOPTIONS_PANOPTICDEEPLABOPTIONS = _descriptor.Descriptor(
  name='PanopticDeeplabOptions',
  full_name='deeplab2.ModelOptions.PanopticDeeplabOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='low_level', full_name='deeplab2.ModelOptions.PanopticDeeplabOptions.low_level', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance', full_name='deeplab2.ModelOptions.PanopticDeeplabOptions.instance', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='semantic_head', full_name='deeplab2.ModelOptions.PanopticDeeplabOptions.semantic_head', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth_head', full_name='deeplab2.ModelOptions.PanopticDeeplabOptions.depth_head', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1995,
  serialized_end=2199,
)

_MODELOPTIONS_MOTIONDEEPLABOPTIONS = _descriptor.Descriptor(
  name='MotionDeepLabOptions',
  full_name='deeplab2.ModelOptions.MotionDeepLabOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='low_level', full_name='deeplab2.ModelOptions.MotionDeepLabOptions.low_level', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance', full_name='deeplab2.ModelOptions.MotionDeepLabOptions.instance', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='semantic_head', full_name='deeplab2.ModelOptions.MotionDeepLabOptions.semantic_head', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='motion_head', full_name='deeplab2.ModelOptions.MotionDeepLabOptions.motion_head', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2202,
  serialized_end=2405,
)

_MODELOPTIONS_MAXDEEPLABOPTIONS = _descriptor.Descriptor(
  name='MaXDeepLabOptions',
  full_name='deeplab2.ModelOptions.MaXDeepLabOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pixel_space_head', full_name='deeplab2.ModelOptions.MaXDeepLabOptions.pixel_space_head', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auxiliary_low_level', full_name='deeplab2.ModelOptions.MaXDeepLabOptions.auxiliary_low_level', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auxiliary_semantic_head', full_name='deeplab2.ModelOptions.MaXDeepLabOptions.auxiliary_semantic_head', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2408,
  serialized_end=2588,
)

_MODELOPTIONS = _descriptor.Descriptor(
  name='ModelOptions',
  full_name='deeplab2.ModelOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='backbone', full_name='deeplab2.ModelOptions.backbone', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decoder', full_name='deeplab2.ModelOptions.decoder', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deeplab_v3', full_name='deeplab2.ModelOptions.deeplab_v3', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deeplab_v3_plus', full_name='deeplab2.ModelOptions.deeplab_v3_plus', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='panoptic_deeplab', full_name='deeplab2.ModelOptions.panoptic_deeplab', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='motion_deeplab', full_name='deeplab2.ModelOptions.motion_deeplab', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_deeplab', full_name='deeplab2.ModelOptions.max_deeplab', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vip_deeplab', full_name='deeplab2.ModelOptions.vip_deeplab', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_checkpoint', full_name='deeplab2.ModelOptions.initial_checkpoint', index=8,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restore_semantic_last_layer_from_initial_checkpoint', full_name='deeplab2.ModelOptions.restore_semantic_last_layer_from_initial_checkpoint', index=9,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restore_instance_last_layer_from_initial_checkpoint', full_name='deeplab2.ModelOptions.restore_instance_last_layer_from_initial_checkpoint', index=10,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MODELOPTIONS_BACKBONEOPTIONS, _MODELOPTIONS_DEEPLABV3OPTIONS, _MODELOPTIONS_DEEPLABV3PLUSOPTIONS, _MODELOPTIONS_PANOPTICDEEPLABOPTIONS, _MODELOPTIONS_MOTIONDEEPLABOPTIONS, _MODELOPTIONS_MAXDEEPLABOPTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='meta_architecture', full_name='deeplab2.ModelOptions.meta_architecture',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=814,
  serialized_end=2609,
)

_INSTANCEOPTIONS.fields_by_name['low_level_override'].message_type = _LOWLEVELOPTIONS
_INSTANCEOPTIONS.fields_by_name['instance_decoder_override'].message_type = _DECODEROPTIONS
_INSTANCEOPTIONS.fields_by_name['center_head'].message_type = _HEADOPTIONS
_INSTANCEOPTIONS.fields_by_name['regression_head'].message_type = _HEADOPTIONS
_INSTANCEOPTIONS.fields_by_name['next_regression_head'].message_type = _HEADOPTIONS
_MODELOPTIONS_BACKBONEOPTIONS.containing_type = _MODELOPTIONS
_MODELOPTIONS_DEEPLABV3OPTIONS.containing_type = _MODELOPTIONS
_MODELOPTIONS_DEEPLABV3PLUSOPTIONS.fields_by_name['low_level'].message_type = _LOWLEVELOPTIONS
_MODELOPTIONS_DEEPLABV3PLUSOPTIONS.containing_type = _MODELOPTIONS
_MODELOPTIONS_PANOPTICDEEPLABOPTIONS.fields_by_name['low_level'].message_type = _LOWLEVELOPTIONS
_MODELOPTIONS_PANOPTICDEEPLABOPTIONS.fields_by_name['instance'].message_type = _INSTANCEOPTIONS
_MODELOPTIONS_PANOPTICDEEPLABOPTIONS.fields_by_name['semantic_head'].message_type = _HEADOPTIONS
_MODELOPTIONS_PANOPTICDEEPLABOPTIONS.fields_by_name['depth_head'].message_type = _HEADOPTIONS
_MODELOPTIONS_PANOPTICDEEPLABOPTIONS.containing_type = _MODELOPTIONS
_MODELOPTIONS_MOTIONDEEPLABOPTIONS.fields_by_name['low_level'].message_type = _LOWLEVELOPTIONS
_MODELOPTIONS_MOTIONDEEPLABOPTIONS.fields_by_name['instance'].message_type = _INSTANCEOPTIONS
_MODELOPTIONS_MOTIONDEEPLABOPTIONS.fields_by_name['semantic_head'].message_type = _HEADOPTIONS
_MODELOPTIONS_MOTIONDEEPLABOPTIONS.fields_by_name['motion_head'].message_type = _HEADOPTIONS
_MODELOPTIONS_MOTIONDEEPLABOPTIONS.containing_type = _MODELOPTIONS
_MODELOPTIONS_MAXDEEPLABOPTIONS.fields_by_name['pixel_space_head'].message_type = _HEADOPTIONS
_MODELOPTIONS_MAXDEEPLABOPTIONS.fields_by_name['auxiliary_low_level'].message_type = _LOWLEVELOPTIONS
_MODELOPTIONS_MAXDEEPLABOPTIONS.fields_by_name['auxiliary_semantic_head'].message_type = _HEADOPTIONS
_MODELOPTIONS_MAXDEEPLABOPTIONS.containing_type = _MODELOPTIONS
_MODELOPTIONS.fields_by_name['backbone'].message_type = _MODELOPTIONS_BACKBONEOPTIONS
_MODELOPTIONS.fields_by_name['decoder'].message_type = _DECODEROPTIONS
_MODELOPTIONS.fields_by_name['deeplab_v3'].message_type = _MODELOPTIONS_DEEPLABV3OPTIONS
_MODELOPTIONS.fields_by_name['deeplab_v3_plus'].message_type = _MODELOPTIONS_DEEPLABV3PLUSOPTIONS
_MODELOPTIONS.fields_by_name['panoptic_deeplab'].message_type = _MODELOPTIONS_PANOPTICDEEPLABOPTIONS
_MODELOPTIONS.fields_by_name['motion_deeplab'].message_type = _MODELOPTIONS_MOTIONDEEPLABOPTIONS
_MODELOPTIONS.fields_by_name['max_deeplab'].message_type = _MODELOPTIONS_MAXDEEPLABOPTIONS
_MODELOPTIONS.fields_by_name['vip_deeplab'].message_type = _MODELOPTIONS_PANOPTICDEEPLABOPTIONS
_MODELOPTIONS.oneofs_by_name['meta_architecture'].fields.append(
  _MODELOPTIONS.fields_by_name['deeplab_v3'])
_MODELOPTIONS.fields_by_name['deeplab_v3'].containing_oneof = _MODELOPTIONS.oneofs_by_name['meta_architecture']
_MODELOPTIONS.oneofs_by_name['meta_architecture'].fields.append(
  _MODELOPTIONS.fields_by_name['deeplab_v3_plus'])
_MODELOPTIONS.fields_by_name['deeplab_v3_plus'].containing_oneof = _MODELOPTIONS.oneofs_by_name['meta_architecture']
_MODELOPTIONS.oneofs_by_name['meta_architecture'].fields.append(
  _MODELOPTIONS.fields_by_name['panoptic_deeplab'])
_MODELOPTIONS.fields_by_name['panoptic_deeplab'].containing_oneof = _MODELOPTIONS.oneofs_by_name['meta_architecture']
_MODELOPTIONS.oneofs_by_name['meta_architecture'].fields.append(
  _MODELOPTIONS.fields_by_name['motion_deeplab'])
_MODELOPTIONS.fields_by_name['motion_deeplab'].containing_oneof = _MODELOPTIONS.oneofs_by_name['meta_architecture']
_MODELOPTIONS.oneofs_by_name['meta_architecture'].fields.append(
  _MODELOPTIONS.fields_by_name['max_deeplab'])
_MODELOPTIONS.fields_by_name['max_deeplab'].containing_oneof = _MODELOPTIONS.oneofs_by_name['meta_architecture']
_MODELOPTIONS.oneofs_by_name['meta_architecture'].fields.append(
  _MODELOPTIONS.fields_by_name['vip_deeplab'])
_MODELOPTIONS.fields_by_name['vip_deeplab'].containing_oneof = _MODELOPTIONS.oneofs_by_name['meta_architecture']
DESCRIPTOR.message_types_by_name['DecoderOptions'] = _DECODEROPTIONS
DESCRIPTOR.message_types_by_name['LowLevelOptions'] = _LOWLEVELOPTIONS
DESCRIPTOR.message_types_by_name['HeadOptions'] = _HEADOPTIONS
DESCRIPTOR.message_types_by_name['InstanceOptions'] = _INSTANCEOPTIONS
DESCRIPTOR.message_types_by_name['ModelOptions'] = _MODELOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DecoderOptions = _reflection.GeneratedProtocolMessageType('DecoderOptions', (_message.Message,), dict(
  DESCRIPTOR = _DECODEROPTIONS,
  __module__ = 'deeplab2.model_pb2'
  # @@protoc_insertion_point(class_scope:deeplab2.DecoderOptions)
  ))
_sym_db.RegisterMessage(DecoderOptions)

LowLevelOptions = _reflection.GeneratedProtocolMessageType('LowLevelOptions', (_message.Message,), dict(
  DESCRIPTOR = _LOWLEVELOPTIONS,
  __module__ = 'deeplab2.model_pb2'
  # @@protoc_insertion_point(class_scope:deeplab2.LowLevelOptions)
  ))
_sym_db.RegisterMessage(LowLevelOptions)

HeadOptions = _reflection.GeneratedProtocolMessageType('HeadOptions', (_message.Message,), dict(
  DESCRIPTOR = _HEADOPTIONS,
  __module__ = 'deeplab2.model_pb2'
  # @@protoc_insertion_point(class_scope:deeplab2.HeadOptions)
  ))
_sym_db.RegisterMessage(HeadOptions)

InstanceOptions = _reflection.GeneratedProtocolMessageType('InstanceOptions', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCEOPTIONS,
  __module__ = 'deeplab2.model_pb2'
  # @@protoc_insertion_point(class_scope:deeplab2.InstanceOptions)
  ))
_sym_db.RegisterMessage(InstanceOptions)

ModelOptions = _reflection.GeneratedProtocolMessageType('ModelOptions', (_message.Message,), dict(

  BackboneOptions = _reflection.GeneratedProtocolMessageType('BackboneOptions', (_message.Message,), dict(
    DESCRIPTOR = _MODELOPTIONS_BACKBONEOPTIONS,
    __module__ = 'deeplab2.model_pb2'
    # @@protoc_insertion_point(class_scope:deeplab2.ModelOptions.BackboneOptions)
    ))
  ,

  DeeplabV3Options = _reflection.GeneratedProtocolMessageType('DeeplabV3Options', (_message.Message,), dict(
    DESCRIPTOR = _MODELOPTIONS_DEEPLABV3OPTIONS,
    __module__ = 'deeplab2.model_pb2'
    # @@protoc_insertion_point(class_scope:deeplab2.ModelOptions.DeeplabV3Options)
    ))
  ,

  DeeplabV3PlusOptions = _reflection.GeneratedProtocolMessageType('DeeplabV3PlusOptions', (_message.Message,), dict(
    DESCRIPTOR = _MODELOPTIONS_DEEPLABV3PLUSOPTIONS,
    __module__ = 'deeplab2.model_pb2'
    # @@protoc_insertion_point(class_scope:deeplab2.ModelOptions.DeeplabV3PlusOptions)
    ))
  ,

  PanopticDeeplabOptions = _reflection.GeneratedProtocolMessageType('PanopticDeeplabOptions', (_message.Message,), dict(
    DESCRIPTOR = _MODELOPTIONS_PANOPTICDEEPLABOPTIONS,
    __module__ = 'deeplab2.model_pb2'
    # @@protoc_insertion_point(class_scope:deeplab2.ModelOptions.PanopticDeeplabOptions)
    ))
  ,

  MotionDeepLabOptions = _reflection.GeneratedProtocolMessageType('MotionDeepLabOptions', (_message.Message,), dict(
    DESCRIPTOR = _MODELOPTIONS_MOTIONDEEPLABOPTIONS,
    __module__ = 'deeplab2.model_pb2'
    # @@protoc_insertion_point(class_scope:deeplab2.ModelOptions.MotionDeepLabOptions)
    ))
  ,

  MaXDeepLabOptions = _reflection.GeneratedProtocolMessageType('MaXDeepLabOptions', (_message.Message,), dict(
    DESCRIPTOR = _MODELOPTIONS_MAXDEEPLABOPTIONS,
    __module__ = 'deeplab2.model_pb2'
    # @@protoc_insertion_point(class_scope:deeplab2.ModelOptions.MaXDeepLabOptions)
    ))
  ,
  DESCRIPTOR = _MODELOPTIONS,
  __module__ = 'deeplab2.model_pb2'
  # @@protoc_insertion_point(class_scope:deeplab2.ModelOptions)
  ))
_sym_db.RegisterMessage(ModelOptions)
_sym_db.RegisterMessage(ModelOptions.BackboneOptions)
_sym_db.RegisterMessage(ModelOptions.DeeplabV3Options)
_sym_db.RegisterMessage(ModelOptions.DeeplabV3PlusOptions)
_sym_db.RegisterMessage(ModelOptions.PanopticDeeplabOptions)
_sym_db.RegisterMessage(ModelOptions.MotionDeepLabOptions)
_sym_db.RegisterMessage(ModelOptions.MaXDeepLabOptions)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
