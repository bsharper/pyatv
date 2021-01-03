# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/ProtocolMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/ProtocolMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n(pyatv/mrp/protobuf/ProtocolMessage.proto\"\xe1\x14\n\tErrorCode\"\xd3\x14\n\x04\x45num\x12\x0b\n\x07NoError\x10\x00\x12\x10\n\x0cUnknownError\x10\x01\x12\x14\n\x10InvalidOperation\x10\x02\x12\x19\n\x15OperationNotPermitted\x10\x03\x12\x16\n\x12\x43lientDoesNotExist\x10\x04\x12\x16\n\x12OriginDoesNotExist\x10\x05\x12\x18\n\x14UnsupportedOperation\x10\x06\x12\x1a\n\x16\x46\x61iledToSetPickedRoute\x10\x07\x12 \n\x1c\x46\x61iledToRegisterCustomOrigin\x10\x08\x12\x1e\n\x1a\x46\x61iledToRemoveCustomOrigin\x10\t\x12&\n\"TheApplicationActivityDoesNotExist\x10\n\x12.\n*TheAppHasNotSetupABrowsableContentEndpoint\x10\x0b\x12\x41\n=TheRequestedBrowsableContentApiIsNotSupportedByTheApplication\x10\x0c\x12\x32\n.TheNotficationHasNotBeenWhitelistedByTheServer\x10\r\x12\x38\n4OperationRequiresAClientCallbackToHaveBeenRegistered\x10\x0e\x12:\n6OperationRequiresAClientDataSourceToHaveBeenRegistered\x10\x0f\x12\x35\n1RequestedDataIsOutOfDateAndShouldBeRequestedAgain\x10\x10\x12\x30\n,TheDevicesEnforcedVolumeLimitHasBeenExceeded\x10\x11\x12\x1b\n\x17VolumeValueIsOutOfRange\x10\x12\x12$\n VolumeIsAlreadyAtTheMaximumValue\x10\x13\x12\x18\n\x14VolumeIsAlreadyMuted\x10\x14\x12\"\n\x1eVoiceInputEndpointDoesNotExist\x10\x15\x12\x34\n0TheVoiceInputDeviceIsNotRegisteredOrDoesNotExist\x10\x16\x12\x15\n\x11\x45ncryptionFailure\x10\x17\x12\x18\n\x14\x45ndpointDoesNotExist\x10\x18\x12.\n*TheClientsApplicationCancelledTheOperation\x10\x19\x12\x18\n\x14TheOperationTimedOut\x10\x1a\x12*\n&TheSpecifiedPlayerPathObjectWasInvalid\x10\x1b\x12:\n6AddingOrRemovingDevicesFromTheAvOutputContextHasFailed\x10\x1c\x12,\n(CouldNotFindTheSpecifiedNowPlayingPlayer\x10\x1d\x12\'\n#TheSpecifiedContentItemDoesNotExist\x10\x1e\x12\x1f\n\x1bTheSpecifiedOffsetIsInvalid\x10\x1f\x12&\n\"TheSpecifiedOutputContextIsInvalid\x10 \x12\x32\n.OneOrMoreSpecifiedOutputDevicesAreNotGroupable\x10!\x12H\nDTheSpecifiedOutputContextDoesNotSupportAddingMoreThanOneOutputDevice\x10\"\x12,\n(CouldNotFindTheSpecifiedNowPlayingClient\x10#\x12P\nLEndpointVolumeControlIsOnlyPossibleIfTheEndpointIsPickedOrRemoteControllable\x10$\x12T\nPOutputDeviceVolumeControlIsOnlyPossibleIfTheEndpointIsPickedOrRemoteControllable\x10%\x12\"\n\x1e\x43oderMustSupportKeyValueCoding\x10&\x12$\n CouldNotFindTheGivenOutputdevice\x10\'\x12!\n\x1d\x46\x61iledToConnectToRemoteDevice\x10\x64\x12 \n\x1c\x41uthenticationTokenIsInvalid\x10\x65\x12\x33\n/RecordingSessionIsAlreadyInProgressOnThisDevice\x10\x66\x12$\n TheDeviceIsNotCurrentlyRecording\x10g\x12\x1c\n\x18TheClientHasDisconnected\x10h\x12\x1c\n\x18TheServerHasDisconnected\x10i\x12,\n(TheConnectionHasBeenCancelledByTheClient\x10j\x12\x34\n0PairingFunctionalityIsLockedDueToSecurityReasons\x10k\x12,\n(TheClientsOperatingSystemVersionIsTooOld\x10l\x12(\n$TheClientsApplicationVersionIsTooOld\x10m\x12\x18\n\x14TheDeviceIsNotPaired\x10n\x12?\n;ThePinPairingDialogWasRemovedByTheUserBeforePairingOccoured\x10o\x12@\n<ThePinPairingDialogWasRemovedByATimeoutBeforePairingOccoured\x10p\x12\x19\n\x15TheConnectionTimedout\x10q\x12\"\n\x1ePairingWithThisDeviceIsBlocked\x10r\x12\x1b\n\x17TheDeviceIsGoingToSleep\x10s\x12\x1d\n\x19\x43onnectionBlockedByServer\x10t\x12<\n8MravendpointWasDeallocatedWhileWaitingForDeviceToConnect\x10u\x12H\nCOutputContextModificationCausedADeviceToNoLongerBeAProxyGroupPlayer\x10\xc8\x01\x12\x44\n?OutputContextModificationCausedADeviceToBecomeAProxyGroupPlayer\x10\xc9\x01\x12\x37\n2OutputContextModificationRequestedNoTopologyChange\x10\xca\x01\x12\x16\n\x11OtherUnknownError\x10\xab\x02\"\x8b\x11\n\x0fProtocolMessage\x12#\n\x04type\x18\x01 \x01(\x0e\x32\x15.ProtocolMessage.Type\x12\x12\n\nidentifier\x18\x02 \x01(\t\x12\x1b\n\x13\x61uthenticationToken\x18\x03 \x01(\t\x12\"\n\terrorCode\x18\x04 \x01(\x0e\x32\x0f.ErrorCode.Enum\x12\x11\n\ttimestamp\x18\x05 \x01(\x04\x12\x18\n\x10\x65rrorDescription\x18N \x01(\t\x12\x18\n\x10uniqueIdentifier\x18U \x01(\t\"\xa0\x0f\n\x04Type\x12\x13\n\x0fUNKNOWN_MESSAGE\x10\x00\x12\x18\n\x14SEND_COMMAND_MESSAGE\x10\x01\x12\x1f\n\x1bSEND_COMMAND_RESULT_MESSAGE\x10\x02\x12\x15\n\x11GET_STATE_MESSAGE\x10\x03\x12\x15\n\x11SET_STATE_MESSAGE\x10\x04\x12\x17\n\x13SET_ARTWORK_MESSAGE\x10\x05\x12\x1f\n\x1bREGISTER_HID_DEVICE_MESSAGE\x10\x06\x12&\n\"REGISTER_HID_DEVICE_RESULT_MESSAGE\x10\x07\x12\x1a\n\x16SEND_HID_EVENT_MESSAGE\x10\x08\x12\x1b\n\x17SEND_HID_REPORT_MESSAGE\x10\t\x12$\n SEND_VIRTUAL_TOUCH_EVENT_MESSAGE\x10\n\x12\x18\n\x14NOTIFICATION_MESSAGE\x10\x0b\x12.\n*CONTENT_ITEMS_CHANGED_NOTIFICATION_MESSAGE\x10\x0c\x12\x17\n\x13\x44\x45VICE_INFO_MESSAGE\x10\x0f\x12!\n\x1d\x43LIENT_UPDATES_CONFIG_MESSAGE\x10\x10\x12\'\n#VOLUME_CONTROL_AVAILABILITY_MESSAGE\x10\x11\x12\x1b\n\x17GAME_CONTROLLER_MESSAGE\x10\x12\x12$\n REGISTER_GAME_CONTROLLER_MESSAGE\x10\x13\x12-\n)REGISTER_GAME_CONTROLLER_RESPONSE_MESSAGE\x10\x14\x12&\n\"UNREGISTER_GAME_CONTROLLER_MESSAGE\x10\x15\x12/\n+REGISTER_FOR_GAME_CONTROLLER_EVENTS_MESSAGE\x10\x16\x12\x14\n\x10KEYBOARD_MESSAGE\x10\x17\x12 \n\x1cGET_KEYBOARD_SESSION_MESSAGE\x10\x18\x12\x16\n\x12TEXT_INPUT_MESSAGE\x10\x19\x12#\n\x1fGET_VOICE_INPUT_DEVICES_MESSAGE\x10\x1a\x12,\n(GET_VOICE_INPUT_DEVICES_RESPONSE_MESSAGE\x10\x1b\x12\'\n#REGISTER_VOICE_INPUT_DEVICE_MESSAGE\x10\x1c\x12\x30\n,REGISTER_VOICE_INPUT_DEVICE_RESPONSE_MESSAGE\x10\x1d\x12\x1f\n\x1bSET_RECORDING_STATE_MESSAGE\x10\x1e\x12\x1c\n\x18SEND_VOICE_INPUT_MESSAGE\x10\x1f\x12\"\n\x1ePLAYBACK_QUEUE_REQUEST_MESSAGE\x10 \x12\x17\n\x13TRANSACTION_MESSAGE\x10!\x12\x1a\n\x16\x43RYPTO_PAIRING_MESSAGE\x10\"\x12&\n\"GAME_CONTROLLER_PROPERTIES_MESSAGE\x10#\x12\x1b\n\x17SET_READY_STATE_MESSAGE\x10$\x12\x1e\n\x1a\x44\x45VICE_INFO_UPDATE_MESSAGE\x10%\x12 \n\x1cSET_CONNECTION_STATE_MESSAGE\x10&\x12\x15\n\x11SEND_BUTTON_EVENT\x10\'\x12\x1b\n\x17SET_HILITE_MODE_MESSAGE\x10(\x12\x17\n\x13WAKE_DEVICE_MESSAGE\x10)\x12\x13\n\x0fGENERIC_MESSAGE\x10*\x12+\n\'SEND_PACKED_VIRTUAL_TOUCH_EVENT_MESSAGE\x10+\x12\x15\n\x11SEND_LYRICS_EVENT\x10,\x12\"\n\x1eSET_NOW_PLAYING_CLIENT_MESSAGE\x10.\x12\"\n\x1eSET_NOW_PLAYING_PLAYER_MESSAGE\x10/\x12\x19\n\x15REMOVE_CLIENT_MESSAGE\x10\x35\x12\x19\n\x15REMOVE_PLAYER_MESSAGE\x10\x36\x12\x19\n\x15UPDATE_CLIENT_MESSAGE\x10\x37\x12\x1f\n\x1bUPDATE_CONTENT_ITEM_MESSAGE\x10\x38\x12\x32\n.VOLUME_CONTROL_CAPABILITIES_DID_CHANGE_MESSAGE\x10@\x12 \n\x1cUPDATE_OUTPUT_DEVICE_MESSAGE\x10\x41\x12*\n&SET_DEFAULT_SUPPORTED_COMMANDS_MESSAGE\x10H\x12\x1e\n\x1aSET_DISCOVERY_MODE_MESSAGE\x10\x65\x12\x1d\n\x19UPDATE_END_POINTS_MESSAGE\x10\x66\x12\x1c\n\x18REMOVE_ENDPOINTS_MESSAGE\x10g\x12$\n PLAYER_CLIENT_PROPERTIES_MESSAGE\x10h\x12$\n ORIGIN_CLIENT_PROPERTIES_MESSAGE\x10i\x12\x16\n\x12\x41UDIO_FADE_MESSAGE\x10j\x12\x1f\n\x1b\x41UDIO_FADE_RESPONSE_MESSAGE\x10k*\x04\x08\x06\x10N*\x04\x08O\x10U*\x08\x08V\x10\x80\x80\x80\x80\x02'
)



_ERRORCODE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='ErrorCode.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoError', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnknownError', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InvalidOperation', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OperationNotPermitted', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ClientDoesNotExist', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OriginDoesNotExist', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnsupportedOperation', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailedToSetPickedRoute', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailedToRegisterCustomOrigin', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailedToRemoveCustomOrigin', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheApplicationActivityDoesNotExist', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheAppHasNotSetupABrowsableContentEndpoint', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheRequestedBrowsableContentApiIsNotSupportedByTheApplication', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheNotficationHasNotBeenWhitelistedByTheServer', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OperationRequiresAClientCallbackToHaveBeenRegistered', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OperationRequiresAClientDataSourceToHaveBeenRegistered', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RequestedDataIsOutOfDateAndShouldBeRequestedAgain', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheDevicesEnforcedVolumeLimitHasBeenExceeded', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VolumeValueIsOutOfRange', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VolumeIsAlreadyAtTheMaximumValue', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VolumeIsAlreadyMuted', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VoiceInputEndpointDoesNotExist', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheVoiceInputDeviceIsNotRegisteredOrDoesNotExist', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EncryptionFailure', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EndpointDoesNotExist', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheClientsApplicationCancelledTheOperation', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheOperationTimedOut', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheSpecifiedPlayerPathObjectWasInvalid', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AddingOrRemovingDevicesFromTheAvOutputContextHasFailed', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CouldNotFindTheSpecifiedNowPlayingPlayer', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheSpecifiedContentItemDoesNotExist', index=30, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheSpecifiedOffsetIsInvalid', index=31, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheSpecifiedOutputContextIsInvalid', index=32, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneOrMoreSpecifiedOutputDevicesAreNotGroupable', index=33, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheSpecifiedOutputContextDoesNotSupportAddingMoreThanOneOutputDevice', index=34, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CouldNotFindTheSpecifiedNowPlayingClient', index=35, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EndpointVolumeControlIsOnlyPossibleIfTheEndpointIsPickedOrRemoteControllable', index=36, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OutputDeviceVolumeControlIsOnlyPossibleIfTheEndpointIsPickedOrRemoteControllable', index=37, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CoderMustSupportKeyValueCoding', index=38, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CouldNotFindTheGivenOutputdevice', index=39, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailedToConnectToRemoteDevice', index=40, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AuthenticationTokenIsInvalid', index=41, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RecordingSessionIsAlreadyInProgressOnThisDevice', index=42, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheDeviceIsNotCurrentlyRecording', index=43, number=103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheClientHasDisconnected', index=44, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheServerHasDisconnected', index=45, number=105,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheConnectionHasBeenCancelledByTheClient', index=46, number=106,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PairingFunctionalityIsLockedDueToSecurityReasons', index=47, number=107,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheClientsOperatingSystemVersionIsTooOld', index=48, number=108,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheClientsApplicationVersionIsTooOld', index=49, number=109,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheDeviceIsNotPaired', index=50, number=110,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ThePinPairingDialogWasRemovedByTheUserBeforePairingOccoured', index=51, number=111,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ThePinPairingDialogWasRemovedByATimeoutBeforePairingOccoured', index=52, number=112,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheConnectionTimedout', index=53, number=113,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PairingWithThisDeviceIsBlocked', index=54, number=114,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TheDeviceIsGoingToSleep', index=55, number=115,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ConnectionBlockedByServer', index=56, number=116,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MravendpointWasDeallocatedWhileWaitingForDeviceToConnect', index=57, number=117,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OutputContextModificationCausedADeviceToNoLongerBeAProxyGroupPlayer', index=58, number=200,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OutputContextModificationCausedADeviceToBecomeAProxyGroupPlayer', index=59, number=201,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OutputContextModificationRequestedNoTopologyChange', index=60, number=202,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OtherUnknownError', index=61, number=299,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=59,
  serialized_end=2702,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE_ENUM)

_PROTOCOLMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='ProtocolMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_MESSAGE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_COMMAND_MESSAGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_COMMAND_RESULT_MESSAGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_STATE_MESSAGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_STATE_MESSAGE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_ARTWORK_MESSAGE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_HID_DEVICE_MESSAGE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_HID_DEVICE_RESULT_MESSAGE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_HID_EVENT_MESSAGE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_HID_REPORT_MESSAGE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_VIRTUAL_TOUCH_EVENT_MESSAGE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOTIFICATION_MESSAGE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTENT_ITEMS_CHANGED_NOTIFICATION_MESSAGE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_INFO_MESSAGE', index=13, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_UPDATES_CONFIG_MESSAGE', index=14, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME_CONTROL_AVAILABILITY_MESSAGE', index=15, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_CONTROLLER_MESSAGE', index=16, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_GAME_CONTROLLER_MESSAGE', index=17, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_GAME_CONTROLLER_RESPONSE_MESSAGE', index=18, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREGISTER_GAME_CONTROLLER_MESSAGE', index=19, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_FOR_GAME_CONTROLLER_EVENTS_MESSAGE', index=20, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYBOARD_MESSAGE', index=21, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_KEYBOARD_SESSION_MESSAGE', index=22, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_INPUT_MESSAGE', index=23, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_VOICE_INPUT_DEVICES_MESSAGE', index=24, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_VOICE_INPUT_DEVICES_RESPONSE_MESSAGE', index=25, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_VOICE_INPUT_DEVICE_MESSAGE', index=26, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_VOICE_INPUT_DEVICE_RESPONSE_MESSAGE', index=27, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_RECORDING_STATE_MESSAGE', index=28, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_VOICE_INPUT_MESSAGE', index=29, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYBACK_QUEUE_REQUEST_MESSAGE', index=30, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSACTION_MESSAGE', index=31, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRYPTO_PAIRING_MESSAGE', index=32, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_CONTROLLER_PROPERTIES_MESSAGE', index=33, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_READY_STATE_MESSAGE', index=34, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_INFO_UPDATE_MESSAGE', index=35, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_CONNECTION_STATE_MESSAGE', index=36, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_BUTTON_EVENT', index=37, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_HILITE_MODE_MESSAGE', index=38, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAKE_DEVICE_MESSAGE', index=39, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENERIC_MESSAGE', index=40, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_PACKED_VIRTUAL_TOUCH_EVENT_MESSAGE', index=41, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_LYRICS_EVENT', index=42, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_NOW_PLAYING_CLIENT_MESSAGE', index=43, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_NOW_PLAYING_PLAYER_MESSAGE', index=44, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_CLIENT_MESSAGE', index=45, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_PLAYER_MESSAGE', index=46, number=54,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_CLIENT_MESSAGE', index=47, number=55,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_CONTENT_ITEM_MESSAGE', index=48, number=56,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME_CONTROL_CAPABILITIES_DID_CHANGE_MESSAGE', index=49, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_OUTPUT_DEVICE_MESSAGE', index=50, number=65,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_DEFAULT_SUPPORTED_COMMANDS_MESSAGE', index=51, number=72,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_DISCOVERY_MODE_MESSAGE', index=52, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_END_POINTS_MESSAGE', index=53, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_ENDPOINTS_MESSAGE', index=54, number=103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_CLIENT_PROPERTIES_MESSAGE', index=55, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORIGIN_CLIENT_PROPERTIES_MESSAGE', index=56, number=105,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO_FADE_MESSAGE', index=57, number=106,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO_FADE_RESPONSE_MESSAGE', index=58, number=107,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2918,
  serialized_end=4870,
)
_sym_db.RegisterEnumDescriptor(_PROTOCOLMESSAGE_TYPE)


_ERRORCODE = _descriptor.Descriptor(
  name='ErrorCode',
  full_name='ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ERRORCODE_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=2702,
)


_PROTOCOLMESSAGE = _descriptor.Descriptor(
  name='ProtocolMessage',
  full_name='ProtocolMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ProtocolMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='ProtocolMessage.identifier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authenticationToken', full_name='ProtocolMessage.authenticationToken', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorCode', full_name='ProtocolMessage.errorCode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ProtocolMessage.timestamp', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorDescription', full_name='ProtocolMessage.errorDescription', index=5,
      number=78, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uniqueIdentifier', full_name='ProtocolMessage.uniqueIdentifier', index=6,
      number=85, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROTOCOLMESSAGE_TYPE,
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(6, 78), (79, 85), (86, 536870912), ],
  oneofs=[
  ],
  serialized_start=2705,
  serialized_end=4892,
)

_ERRORCODE_ENUM.containing_type = _ERRORCODE
_PROTOCOLMESSAGE.fields_by_name['type'].enum_type = _PROTOCOLMESSAGE_TYPE
_PROTOCOLMESSAGE.fields_by_name['errorCode'].enum_type = _ERRORCODE_ENUM
_PROTOCOLMESSAGE_TYPE.containing_type = _PROTOCOLMESSAGE
DESCRIPTOR.message_types_by_name['ErrorCode'] = _ERRORCODE
DESCRIPTOR.message_types_by_name['ProtocolMessage'] = _PROTOCOLMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ErrorCode = _reflection.GeneratedProtocolMessageType('ErrorCode', (_message.Message,), {
  'DESCRIPTOR' : _ERRORCODE,
  '__module__' : 'pyatv.mrp.protobuf.ProtocolMessage_pb2'
  # @@protoc_insertion_point(class_scope:ErrorCode)
  })
_sym_db.RegisterMessage(ErrorCode)

ProtocolMessage = _reflection.GeneratedProtocolMessageType('ProtocolMessage', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOLMESSAGE,
  '__module__' : 'pyatv.mrp.protobuf.ProtocolMessage_pb2'
  # @@protoc_insertion_point(class_scope:ProtocolMessage)
  })
_sym_db.RegisterMessage(ProtocolMessage)


# @@protoc_insertion_point(module_scope)
