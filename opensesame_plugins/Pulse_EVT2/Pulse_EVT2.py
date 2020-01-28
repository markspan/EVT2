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

from libopensesame import item
from libopensesame.oslogging import oslogger
from libqtopensesame.items.qtautoplugin import qtautoplugin


class Pulse_EVT2(item.item):

    """
    A plugin to send triggers to the EventExchanger2 device.
    """
    
    description = u"Allows setting pins on the EventExchanger-2 (USB) Port"
    
    def reset(self):
        
        self.var.dummy = 'no'
        self.var._value = 0
        self.var._duration = 500
        self.var._serialNumber = u'autodetect'
          
    def prepare(self):

        item.item.prepare(self)
        if self.var.dummy == 'yes':
            return
        dev = self.var._serialNumber
        if dev == u"autodetect":
            dev = None
        if not hasattr(self.experiment, "EventExchanger"):
            import libevt
            self.experiment.EventExchanger = libevt.libevt(
                self.experiment,
                dev
            )
            self.python_workspace[u'EventExchanger'] = \
                self.experiment.EventExchanger

    def run(self):

        if self.var.dummy == 'yes':
            oslogger.info(
                'dummy trigger (value={}, duration={})'.format(
                    self.var._value,
                    self.var._duration
                )
            )
            return
        self.experiment.EventExchanger.PulseLines(
            self.var._value,
            self.var._duration
        )


class qtPulse_EVT2(Pulse_EVT2, qtautoplugin):

    def __init__(self, name, experiment, string=None):

        Pulse_EVT2.__init__(self, name, experiment, string)
        qtautoplugin.__init__(self, __file__)
