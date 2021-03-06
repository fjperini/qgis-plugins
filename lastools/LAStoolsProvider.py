# -*- coding: utf-8 -*-

"""
/***************************************************************************
    LAStoolsProvider.py
    ---------------------
    This script initializes the valid providers, depending on Wine and OS.
    ---------------------
    Date                 : January 2017, August 2018
    Copyright            : (C) 2017 Boundless, http://boundlessgeo.com
                           (C) 2018 rapidlasso GmbH, http://rapidlasso.com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Victor Olaya'
__date__ = 'January 2017'
__copyright__ = '(C) 2017, Boundless, http://boundlessgeo.com'

__author__ = 'Martin Isenburg'
__date__ = 'August 2018'
__copyright__ = '(C) 2018, rapidlasso GmbH, http://rapidlasso.com'

import os
from PyQt5.QtGui import QIcon
from qgis.core import QgsProcessingProvider
from processing.core.ProcessingConfig import Setting, ProcessingConfig

from .LAStoolsUtils import LAStoolsUtils

from .LAStools.blast2dem import blast2dem
from .LAStools.blast2iso import blast2iso
from .LAStools.las2dem import las2dem
from .LAStools.las2iso import las2iso
from .LAStools.las2las_filter import las2las_filter
from .LAStools.las2las_project import las2las_project
from .LAStools.las2las_transform import las2las_transform
from .LAStools.las2shp import las2shp
from .LAStools.las2tin import las2tin
from .LAStools.las2txt import las2txt
from .LAStools.lasboundary import lasboundary
from .LAStools.lascanopy import lascanopy
from .LAStools.lasclassify import lasclassify
from .LAStools.lasclip import lasclip
from .LAStools.lascolor import lascolor
from .LAStools.lascontrol import lascontrol
from .LAStools.lasdiff import lasdiff
from .LAStools.lasduplicate import lasduplicate
from .LAStools.lasgrid import lasgrid
from .LAStools.lasground import lasground
from .LAStools.lasground_new import lasground_new
from .LAStools.lasheight import lasheight
from .LAStools.lasheight_classify import lasheight_classify
from .LAStools.lasindex import lasindex
from .LAStools.lasinfo import lasinfo
from .LAStools.lasmerge import lasmerge
from .LAStools.lasnoise import lasnoise
from .LAStools.lasoverage import lasoverage
from .LAStools.lasoverlap import lasoverlap
from .LAStools.lasprecision import lasprecision
from .LAStools.laspublish import laspublish
from .LAStools.lassort import lassort
from .LAStools.lassplit import lassplit
from .LAStools.lastile import lastile
from .LAStools.lasthin import lasthin
from .LAStools.lasvalidate import lasvalidate
from .LAStools.lasview import lasview
from .LAStools.laszip import laszip
from .LAStools.shp2las import shp2las
from .LAStools.txt2las import txt2las

from .LAStoolsProduction.blast2demPro import blast2demPro
from .LAStoolsProduction.blast2isoPro import blast2isoPro
from .LAStoolsProduction.las2demPro import las2demPro
from .LAStoolsProduction.las2lasPro_filter import las2lasPro_filter
from .LAStoolsProduction.las2lasPro_project import las2lasPro_project
from .LAStoolsProduction.las2lasPro_transform import las2lasPro_transform
from .LAStoolsProduction.las2txtPro import las2txtPro
from .LAStoolsProduction.lasboundaryPro import lasboundaryPro
from .LAStoolsProduction.lascanopyPro import lascanopyPro
from .LAStoolsProduction.lasclassifyPro import lasclassifyPro
from .LAStoolsProduction.lasduplicatePro import lasduplicatePro
from .LAStoolsProduction.lasindexPro import lasindexPro
from .LAStoolsProduction.lasinfoPro import lasinfoPro
from .LAStoolsProduction.lasgridPro import lasgridPro
from .LAStoolsProduction.lasgroundPro import lasgroundPro
from .LAStoolsProduction.lasgroundPro_new import lasgroundPro_new
from .LAStoolsProduction.lasheightPro import lasheightPro
from .LAStoolsProduction.lasheightPro_classify import lasheightPro_classify
from .LAStoolsProduction.lasmergePro import lasmergePro
from .LAStoolsProduction.lasnoisePro import lasnoisePro
from .LAStoolsProduction.lasoveragePro import lasoveragePro
from .LAStoolsProduction.lasoverlapPro import lasoverlapPro
from .LAStoolsProduction.laspublishPro import laspublishPro
from .LAStoolsProduction.lassortPro import lassortPro
from .LAStoolsProduction.lastilePro import lastilePro
from .LAStoolsProduction.lasthinPro import lasthinPro
from .LAStoolsProduction.lasviewPro import lasviewPro
from .LAStoolsProduction.laszipPro import laszipPro
from .LAStoolsProduction.lasvalidatePro import lasvalidatePro
from .LAStoolsProduction.txt2lasPro import txt2lasPro

from .LAStoolsPipelines.hugeFileClassify import hugeFileClassify
from .LAStoolsPipelines.hugeFileGroundClassify import hugeFileGroundClassify
from .LAStoolsPipelines.hugeFileNormalize import hugeFileNormalize
from .LAStoolsPipelines.flightlinesToCHM_FirstReturn import flightlinesToCHM_FirstReturn
from .LAStoolsPipelines.flightlinesToCHM_HighestReturn import flightlinesToCHM_HighestReturn
from .LAStoolsPipelines.flightlinesToCHM_SpikeFree import flightlinesToCHM_SpikeFree
from .LAStoolsPipelines.flightlinesToDTMandDSM_FirstReturn import flightlinesToDTMandDSM_FirstReturn
from .LAStoolsPipelines.flightlinesToDTMandDSM_SpikeFree import flightlinesToDTMandDSM_SpikeFree
from .LAStoolsPipelines.flightlinesToMergedCHM_FirstReturn import flightlinesToMergedCHM_FirstReturn
from .LAStoolsPipelines.flightlinesToMergedCHM_HighestReturn import flightlinesToMergedCHM_HighestReturn
from .LAStoolsPipelines.flightlinesToMergedCHM_PitFree import flightlinesToMergedCHM_PitFree
from .LAStoolsPipelines.flightlinesToMergedCHM_SpikeFree import flightlinesToMergedCHM_SpikeFree

from .LAStoolsPipelinesOthers.flightlinesToDTMandDSM import flightlinesToDTMandDSM
from .LAStoolsPipelinesOthers.flightlinesToCHM import flightlinesToCHM
from .LAStoolsPipelinesOthers.flightlinesToSingleCHMpitFree import flightlinesToSingleCHMpitFree

from . import resources

class LAStoolsProvider(QgsProcessingProvider):

    def __init__(self):
        QgsProcessingProvider.__init__(self)

    def load(self):
        """In this method we add settings needed to configure our
        provider.
        """
        ProcessingConfig.settingIcons[self.name()] = self.icon()
        ProcessingConfig.addSetting(Setting(self.name(), 'LASTOOLS_ACTIVATED', 'Activate', True))
        ProcessingConfig.addSetting(Setting(self.name(), 'LASTOOLS_FOLDER', 'LAStools folder', "/usr/local/opt/lastools", valuetype=Setting.FOLDER))
        ProcessingConfig.addSetting(Setting(self.name(), 'WINE_FOLDER', 'Wine folder', "", valuetype=Setting.FOLDER))
        # una vez que se eestablece WINE_FOLDER, habilitará todos las funciones
        # por ej: Wine folder /usr/local/opt/lastools
        ProcessingConfig.readSettings()
        self.refreshAlgorithms()
        return True

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        ProcessingConfig.removeSetting('LASTOOLS_ACTIVATED')
        ProcessingConfig.removeSetting('LASTOOLS_FOLDER')
        ProcessingConfig.removeSetting('WINE_FOLDER')
        pass

    def isActive(self):
        """Return True if the provider is activated and ready to run algorithms"""
        return ProcessingConfig.getSetting('LASTOOLS_ACTIVATED')

    def setActive(self, active):
        ProcessingConfig.setSettingValue('LASTOOLS_ACTIVATED', active)

    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """

        # available on MacOS and GNU Linux
        # las2las las2txt lasdiff lasindex lasinfo lasmerge lasprecision laszip txt2las

        # LAStools for processing single files

        if (os.name == 'nt' or LAStoolsUtils.hasWine()):
            lastools = [
                lasground(), lasheight(), lasclassify(), lasclip(), lastile(),
                lascolor(), lasgrid(), las2dem(), blast2dem(), las2iso(), blast2iso(),
                lasview(), lasboundary(), lasinfo(), lasprecision(), las2tin(),
                lasvalidate(), lasduplicate(), las2txt(), txt2las(), laszip(),
                lasindex(), lasthin(), lassort(), lascanopy(), lasmerge(),
                las2shp(), shp2las(), lasnoise(), lassplit(), las2las_filter(),
                las2las_project(), las2las_transform(), lasoverage(), lasoverlap(),
                laspublish(), lasground_new(), lascontrol(), lasdiff(),
                lasheight_classify()
            ]
        else:
            lastools = [
                lasinfo(), lasprecision(), las2txt(), txt2las(),
                laszip(), lasindex(), lasmerge(), las2las_filter(), las2las_project(),
                las2las_transform(), lasdiff()
            ]
        for alg in lastools:
            self.addAlgorithm( alg )

        # LAStools Production for processing folders of files

        if (os.name == 'nt' or LAStoolsUtils.hasWine()):
            lastoolsPro = [
                lastilePro(), lasgroundPro(), las2demPro(), lasheightPro(), laszipPro(),
                lasduplicatePro(), lasgridPro(), lassortPro(), lasclassifyPro(), lasthinPro(),
                lasnoisePro(), lasindexPro(), lascanopyPro(), blast2demPro(), lasboundaryPro(),
                lasinfoPro(), las2lasPro_filter(), las2lasPro_project(), las2lasPro_transform(),
                lasoveragePro(), txt2lasPro(), las2txtPro(), blast2isoPro(), lasvalidatePro(),
                lasmergePro(), lasviewPro(), lasoverlapPro(), laspublishPro(), lasgroundPro_new(),
                lasheightPro_classify()
            ]
        else:
            lastoolsPro = [
                laszipPro(), lasindexPro(), lasinfoPro(), las2lasPro_filter(), las2lasPro_project(),
                las2lasPro_transform(), txt2lasPro(), las2txtPro(), lasmergePro()
            ]
        for alg in lastoolsPro:
            self.addAlgorithm( alg )

        # LAStools pipelines
        if (os.name == 'nt' or LAStoolsUtils.hasWine()):
            lastoolsPipe = [
                hugeFileClassify(), hugeFileGroundClassify(), hugeFileNormalize(), flightlinesToCHM_FirstReturn(),
                flightlinesToCHM_HighestReturn(), flightlinesToCHM_SpikeFree(), flightlinesToDTMandDSM_FirstReturn(),
                flightlinesToDTMandDSM_SpikeFree(), flightlinesToMergedCHM_FirstReturn(), flightlinesToMergedCHM_HighestReturn(),
                flightlinesToMergedCHM_PitFree(), flightlinesToMergedCHM_SpikeFree()
            ]
        else:
            lastoolsPipe = []
        for alg in lastoolsPipe:
            self.addAlgorithm( alg )

        # Other LAStools Pipelines

        if (os.name == 'nt' or LAStoolsUtils.hasWine()):
            lastoolsPipeOther = [
                flightlinesToDTMandDSM(), flightlinesToCHM(), flightlinesToSingleCHMpitFree(),
            ]
        else:
            lastoolsPipeOther = []
        for alg in lastoolsPipeOther:
            self.addAlgorithm( alg )

    def icon(self):
        return QIcon(":/plugins/LAStools/LAStools.png")

    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return 'LAStools'

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.

        This string should be short (e.g. "LAStools") and localised.
        """
        return 'LAStools'

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "LAStools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return 'LAStools LiDAR and point cloud processing'
