# coding=utf-8

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame.py3compat import *
import os
from libopensesame.exceptions import osexception
from libopensesame.oslogging import oslogger


class libevt:

    """
    desc: |
        If you insert the EVT2 plugin at the start of your experiment, an
        instance of `EventExchanger` automatically becomes part of the
        experiment object and can be accessed within an inline_script item as
        `EventExchanger`.

        __Important note 1:__

        If you do not specify a device, the plug-in will try to autodetect the
        EVT2. The first device will be used if multiple devices are attached,
        so it is better to explicitly specify a device.
    """

    def __init__(self, experiment, dev=None):

        self.experiment = experiment
        import clr
        clr.AddReference("System.Reflection")
        from System.Reflection import Assembly
        directory = os.path.join(os.path.dirname(__file__), 'dll')
        Assembly.UnsafeLoadFrom(os.path.join(directory, 'HidSharp.dll'))
        Assembly.UnsafeLoadFrom(
            os.path.join(directory, 'HidSharp.DeviceHelpers.dll')
        )
        Assembly.UnsafeLoadFrom(
            os.path.join(directory, 'EventExchanger.dll')
        )
        self._EVT2 = clr.ID.EventExchanger()
        oslogger.info(self._EVT2.Attached())
        self._nEVT2 = self._EVT2.Attached().count('/') + 1
        self.devnr = self._EVT2.Attached().partition('/')[0]
        # If a device has not been specified, autodetect
        if dev in (None, "", "autodetect"):
            try:
                if self._nEVT2 == 1:
                    print("Starting the only attached EVT")
                    self._EVT2.Start()
                else:
                    print("Starting device %s" % self.devnr)
                self._EVT2.Start(self.devnr)
            except Exception as e:
                oslogger.warning(e.Message)
                raise osexception(
                    "libEVT2 does not know how to auto-detect the EVT on your "
                    "platform. Please specify a device."
                )
        else:
            try:
                self._EVT2.Start(str(dev))
            except Exception as e:
                raise osexception(
                    "Failed to open device port '%s' in libEVT2: '%s'"
                    % (dev, e)
                )
        if self._EVT2 is None:
            raise osexception(
                "libEVT2 failed to auto-detect a unique instance of the EVT. "
                "Please specify a device."
            )
        oslogger.info("using device %s" % dev)

    def PulseLines(self, code, ms):
        """
        desc:
            Pulse the outport with value 'code' for 'ms' millis
        """
        self._EVT2.PulseLines(code, ms)
