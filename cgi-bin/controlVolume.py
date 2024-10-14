from flask import Flask, request, jsonify
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL



def get_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        ISimpleAudioVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(ISimpleAudioVolume))
    return volume.GetMasterVolume()

def set_volume(value):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        ISimpleAudioVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(ISimpleAudioVolume))
    volume.SetMasterVolume(value, None)


def get_volume_endpoint():
    volume = get_volume()
    return jsonify({'volume': volume})


def set_volume_endpoint():
    value = request.json.get('volume')
    if 0 <= value <= 1:
        set_volume(value)
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'Volume must be between 0 and 1'})


get_volume()
