# -*- coding: utf-8 -*-

"""
***************************************************************************
    taudemProvider.py
    ---------------------
    Date                 : May 2012
    Copyright            : (C) 2012-2018 by Alexander Bruy
    Email                : alexander dot bruy at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Alexander Bruy'
__date__ = 'May 2012'
__copyright__ = '(C) 2012-2018, Alexander Bruy'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import QCoreApplication

from qgis.core import QgsProcessingProvider, QgsMessageLog

from processing.core.ProcessingConfig import ProcessingConfig, Setting

from taudem.pitremove import PitRemove
from taudem.aread8 import AreaD8
from taudem.d8flowdir import D8FlowDir
from taudem.areadinf import AreaDinf
from taudem.dinfflowdir import DinfFlowDir
from taudem.gridnet import GridNet

from taudem.peukerdouglas import PeukerDouglas
from taudem.threshold import Threshold
from taudem.d8flowpathextremeup import D8FlowPathExtremeUp
from taudem.slopearea import SlopeArea
from taudem.lengtharea import LengthArea
from taudem.dropanalysis import DropAnalysis
from taudem.streamnet import StreamNet
from taudem.moveoutletstostreams import MoveOutletsToStreams
from taudem.gagewatershed import GageWatershed
from taudem.connectdown import ConnectDown

from taudem.slopearearatio import SlopeAreaRatio
from taudem.d8hdisttostrm import D8HDistToStrm
from taudem.dinfupdependence import DinfUpDependence
from taudem.dinfdecayaccum import DinfDecayAccum
from taudem.dinfconclimaccum import DinfConcLimAccum
from taudem.dinftranslimaccum import DinfTransLimAccum
from taudem.dinfrevaccum import DinfRevAccum
from taudem.dinfdistdown import DinfDistDown
from taudem.dinfdistup import DinfDistUp
from taudem.dinfavalanche import DinfAvalanche
from taudem.slopeavedown import SlopeAveDown
from taudem.twi import Twi

from taudem import taudemUtils

pluginPath = os.path.dirname(__file__)


class TauDemProvider(QgsProcessingProvider):

    def __init__(self):
        super().__init__()
        self.algs = []

    def id(self):
        return "taudem"

    def name(self):
        return "TauDEM"

    def icon(self):
        return QIcon(os.path.join(pluginPath, "icons", "taudem.svg"))

    def load(self):
        ProcessingConfig.settingIcons[self.name()] = self.icon()
        ProcessingConfig.addSetting(Setting(self.name(),
                                            taudemUtils.TAUDEM_ACTIVE,
                                            self.tr("Activate"),
                                            False))
        ProcessingConfig.addSetting(Setting(self.name(),
                                            taudemUtils.TAUDEM_DIRECTORY,
                                            self.tr("TauDEM directory"),
                                            taudemUtils.taudemDirectory(),
                                            valuetype=Setting.FOLDER))
        ProcessingConfig.addSetting(Setting(self.name(),
                                            taudemUtils.TAUDEM_MPICH,
                                            self.tr("MPICH2/OpenMPI bin directory"),
                                            taudemUtils.mpichDirectory(),
                                            valuetype=Setting.FOLDER))
        ProcessingConfig.addSetting(Setting(self.name(),
                                            taudemUtils.TAUDEM_PROCESSES,
                                            self.tr("MPI processes to use"),
                                            2,
                                            valuetype=Setting.INT))
        ProcessingConfig.addSetting(Setting(self.name(),
                                            taudemUtils.TAUDEM_VERBOSE,
                                            self.tr("Log commands output"),
                                            False))
        ProcessingConfig.readSettings()
        self.refreshAlgorithms()
        return True

    def unload(self):
        ProcessingConfig.removeSetting(taudemUtils.TAUDEM_ACTIVE)
        ProcessingConfig.removeSetting(taudemUtils.TAUDEM_DIRECTORY)
        ProcessingConfig.removeSetting(taudemUtils.TAUDEM_MPICH)
        ProcessingConfig.removeSetting(taudemUtils.TAUDEM_PROCESSES)
        ProcessingConfig.removeSetting(taudemUtils.TAUDEM_VERBOSE)

    def isActive(self):
        return ProcessingConfig.getSetting(taudemUtils.TAUDEM_ACTIVE)

    def setActive(self, active):
        ProcessingConfig.setSettingValue(taudemUtils.TAUDEM_ACTIVE, active)

    def supportsNonFileBasedOutput(self):
        return False

    def getAlgs(self):
        algs = [PitRemove(),
                AreaD8(),
                D8FlowDir(),
                AreaDinf(),
                DinfFlowDir(),
                GridNet(),

                PeukerDouglas(),
                Threshold(),
                D8FlowPathExtremeUp(),
                SlopeArea(),
                LengthArea(),
                DropAnalysis(),
                StreamNet(),
                MoveOutletsToStreams(),
                GageWatershed(),
                ConnectDown(),

                SlopeAreaRatio(),
                D8HDistToStrm(),
                DinfUpDependence(),
                DinfDecayAccum(),
                DinfConcLimAccum(),
                DinfTransLimAccum(),
                DinfRevAccum(),
                DinfDistDown(),
                DinfDistUp(),
                DinfAvalanche(),
                SlopeAveDown(),
                Twi()
               ]

        return algs

    def loadAlgorithms(self):
        self.algs = self.getAlgs()
        for a in self.algs:
            self.addAlgorithm(a)

    def tr(self, string, context=''):
        if context == "":
            context = "TauDemProvider"
        return QCoreApplication.translate(context, string)
