#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
    # Some general metadata. By convention, a plugin is named:
    # opensesame-plugin-[plugin name]
    name='opensesame-plugin-Pulse_EVT2',
    version='1.0.0',
    description='Send markers through an EVT2 (RUG USB interface)',
    author='Mark Span',
    author_email='m.m.span@rug.nl',
    url='https://github.com/markspan/EVT2',
    # Classifiers used by PyPi if you upload the plugin there
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Environment :: Win32 (MS Windows)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    data_files=[
        (
            'share/opensesame_plugins/Pulse_EVT2',
            [
                'opensesame_plugins/Pulse_EVT2/Pulse_EVT2.md',
                'opensesame_plugins/Pulse_EVT2/Pulse_EVT2.png',
                'opensesame_plugins/Pulse_EVT2/Pulse_EVT2_large.png',
                'opensesame_plugins/Pulse_EVT2/Pulse_EVT2.py',
                'opensesame_plugins/Pulse_EVT2/libevt.py',
                'opensesame_plugins/Pulse_EVT2/info.yaml',
                'opensesame_plugins/Pulse_EVT2/dll/EventExchanger.dll',
                'opensesame_plugins/Pulse_EVT2/dll/HidSharp.dll',
                'opensesame_plugins/Pulse_EVT2/dll/HidSharp.DeviceHelpers.dll',
                'Example.osexp',
                'License.HidSharp',
            ]
        )
    ]
)
