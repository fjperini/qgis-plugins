# -*- coding: utf-8 -*-

"""
***************************************************************************
    las2lasPro_project.py
    ---------------------
    Date                 : October 2014, May 2016 and August 2018
    Copyright            : (C) 2014 by Martin Isenburg
    Email                : martin near rapidlasso point com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Martin Isenburg'
__date__ = 'October 2014'
__copyright__ = '(C) 2014, Martin Isenburg'

import os
from qgis.core import QgsProcessingParameterEnum
from qgis.core import QgsProcessingParameterNumber

from ..LAStoolsUtils import LAStoolsUtils
from ..LAStoolsAlgorithm import LAStoolsAlgorithm

class las2lasPro_project(LAStoolsAlgorithm):

    STATE_PLANES = ["---", "AK_10", "AK_2", "AK_3", "AK_4", "AK_5", "AK_6", "AK_7", "AK_8", "AK_9", "AL_E", "AL_W", "AR_N", "AR_S", "AZ_C", "AZ_E", "AZ_W", "CA_I", "CA_II", "CA_III", "CA_IV", "CA_V", "CA_VI", "CA_VII", "CO_C", "CO_N", "CO_S", "CT", "DE", "FL_E", "FL_N", "FL_W", "GA_E", "GA_W", "HI_1", "HI_2", "HI_3", "HI_4", "HI_5", "IA_N", "IA_S", "ID_C", "ID_E", "ID_W", "IL_E", "IL_W", "IN_E", "IN_W", "KS_N", "KS_S", "KY_N", "KY_S", "LA_N", "LA_S", "MA_I", "MA_M", "MD", "ME_E", "ME_W", "MI_C", "MI_N", "MI_S", "MN_C", "MN_N", "MN_S", "MO_C", "MO_E", "MO_W", "MS_E", "MS_W", "MT_C", "MT_N", "MT_S", "NC", "ND_N", "ND_S", "NE_N", "NE_S", "NH", "NJ", "NM_C", "NM_E", "NM_W", "NV_C", "NV_E", "NV_W", "NY_C", "NY_E", "NY_LI", "NY_W", "OH_N", "OH_S", "OK_N", "OK_S", "OR_N", "OR_S", "PA_N", "PA_S", "PR", "RI", "SC_N", "SC_S", "SD_N", "SD_S", "St.Croix", "TN", "TX_C", "TX_N", "TX_NC", "TX_S", "TX_SC", "UT_C", "UT_N", "UT_S", "VA_N", "VA_S", "VT", "WA_N", "WA_S", "WI_C", "WI_N", "WI_S", "WV_N", "WV_S", "WY_E", "WY_EC", "WY_W", "WY_WC"]

    UTM_ZONES = ["---", "1 (north)", "2 (north)", "3 (north)", "4 (north)", "5 (north)", "6 (north)", "7 (north)", "8 (north)", "9 (north)", "10 (north)", "11 (north)", "12 (north)", "13 (north)", "14 (north)", "15 (north)", "16 (north)", "17 (north)", "18 (north)", "19 (north)", "20 (north)", "21 (north)", "22 (north)", "23 (north)", "24 (north)", "25 (north)", "26 (north)", "27 (north)", "28 (north)", "29 (north)", "30 (north)", "31 (north)", "32 (north)", "33 (north)", "34 (north)", "35 (north)", "36 (north)", "37 (north)", "38 (north)", "39 (north)", "40 (north)", "41 (north)", "42 (north)", "43 (north)", "44 (north)", "45 (north)", "46 (north)", "47 (north)", "48 (north)", "49 (north)", "50 (north)", "51 (north)", "52 (north)", "53 (north)", "54 (north)", "55 (north)", "56 (north)", "57 (north)", "58 (north)", "59 (north)", "60 (north)", "1 (south)", "2 (south)", "3 (south)", "4 (south)", "5 (south)", "6 (south)", "7 (south)", "8 (south)", "9 (south)", "10 (south)", "11 (south)", "12 (south)", "13 (south)", "14 (south)", "15 (south)", "16 (south)", "17 (south)", "18 (south)", "19 (south)", "20 (south)", "21 (south)", "22 (south)", "23 (south)", "24 (south)", "25 (south)", "26 (south)", "27 (south)", "28 (south)", "29 (south)", "30 (south)", "31 (south)", "32 (south)", "33 (south)", "34 (south)", "35 (south)", "36 (south)", "37 (south)", "38 (south)", "39 (south)", "40 (south)", "41 (south)", "42 (south)", "43 (south)", "44 (south)", "45 (south)", "46 (south)", "47 (south)", "48 (south)", "49 (south)", "50 (south)", "51 (south)", "52 (south)", "53 (south)", "54 (south)", "55 (south)", "56 (south)", "57 (south)", "58 (south)", "59 (south)", "60 (south)"]

    PROJECTIONS = ["---", "epsg", "utm", "sp83", "sp27", "longlat", "latlong", "ecef"]

    SOURCE_PROJECTION = "SOURCE_PROJECTION"
    SOURCE_EPSG_CODE = "SOURCE_EPSG_CODE"
    SOURCE_UTM = "SOURCE_UTM"
    SOURCE_SP = "SOURCE_SP"

    TARGET_PROJECTION = "TARGET_PROJECTION"
    TARGET_EPSG_CODE = "TARGET_EPSG_CODE"
    TARGET_UTM = "TARGET_UTM"
    TARGET_SP = "TARGET_SP"

    def initAlgorithm(self, config):
        self.addParametersPointInputFolderGUI()
        self.addParameter(QgsProcessingParameterEnum(las2lasPro_project.SOURCE_PROJECTION, "source projection", las2lasPro_project.PROJECTIONS, False, 0))
        self.addParameter(QgsProcessingParameterNumber(las2lasPro_project.SOURCE_EPSG_CODE, "source EPSG code", QgsProcessingParameterNumber.Integer, 25832, False, 1, 65535))
        self.addParameter(QgsProcessingParameterEnum(las2lasPro_project.SOURCE_UTM, "source utm zone", las2lasPro_project.UTM_ZONES, False, 0))
        self.addParameter(QgsProcessingParameterEnum(las2lasPro_project.SOURCE_SP, "source state plane code", las2lasPro_project.STATE_PLANES, False, 0))
        self.addParameter(QgsProcessingParameterEnum(las2lasPro_project.TARGET_PROJECTION, "target projection", las2lasPro_project.PROJECTIONS, False, 0))
        self.addParameter(QgsProcessingParameterNumber(las2lasPro_project.TARGET_EPSG_CODE, "target EPSG code", QgsProcessingParameterNumber.Integer, 25832, False, 1, 65535))
        self.addParameter(QgsProcessingParameterEnum(las2lasPro_project.TARGET_UTM, "target utm zone", las2lasPro_project.UTM_ZONES, False, 0))
        self.addParameter(QgsProcessingParameterEnum(las2lasPro_project.TARGET_SP, "target state plane code", las2lasPro_project.STATE_PLANES, False, 0))
        self.addParametersOutputDirectoryGUI()
        self.addParametersOutputAppendixGUI()
        self.addParametersPointOutputFormatGUI()
        self.addParametersAdditionalGUI()
        self.addParametersCoresGUI()
        self.addParametersVerboseGUI64()

    def processAlgorithm(self, parameters, context, feedback):
        if (LAStoolsUtils.hasWine()):
            commands = [os.path.join(LAStoolsUtils.LAStoolsPath(), "bin", "las2las.exe")]
        else:
            commands = [os.path.join(LAStoolsUtils.LAStoolsPath(), "bin", "las2las")]
        self.addParametersVerboseCommands64(parameters, context, commands)
        self.addParametersPointInputFolderCommands(parameters, context, commands)
        source_projection = self.parameterAsInt(parameters, las2lasPro_project.SOURCE_PROJECTION, context)
        if (source_projection != 0):
            if (source_projection == 1):
                epsg_code = self.parameterAsInt(parameters, las2lasPro_project.SOURCE_EPSG_CODE, context)
                if (epsg_code != 0):
                    commands.append("-" + las2lasPro_project.PROJECTIONS[source_projection])
                    commands.append(unicode(epsg_code))
            elif (source_projection == 2):
                source_utm_zone = self.parameterAsInt(parameters, las2lasPro_project.SOURCE_UTM, context)
                if (source_utm_zone != 0):
                    commands.append("-" + las2lasPro_project.PROJECTIONS[source_projection])
                    if (source_utm_zone > 60):
                        commands.append(unicode(source_utm_zone - 60) + "south")
                    else:
                        commands.append(unicode(source_utm_zone) + "north")
            elif (source_projection < 5):
                source_sp_code = self.parameterAsInt(parameters, las2lasPro_project.SOURCE_SP, context)
                if (source_sp_code != 0):
                    commands.append("-" + las2lasPro_project.PROJECTIONS[source_projection])
                    commands.append(las2lasPro_project.STATE_PLANES[source_sp_code])
            else:
                commands.append("-" + las2lasPro_project.PROJECTIONS[source_projection])
        target_projection = self.parameterAsInt(parameters, las2lasPro_project.TARGET_PROJECTION, context)
        if (target_projection != 0):
            if (target_projection == 1):
                epsg_code = self.parameterAsInt(parameters, las2lasPro_project.TARGET_EPSG_CODE, context)
                if (epsg_code != 0):
                    commands.append("-target_" + las2lasPro_project.PROJECTIONS[source_projection])
                    commands.append(unicode(epsg_code))
            elif (target_projection == 2):
                target_utm_zone = self.parameterAsInt(parameters, las2lasPro_project.TARGET_UTM, context)
                if (target_utm_zone != 0):
                    commands.append("-target_" + las2lasPro_project.PROJECTIONS[target_projection])
                    if (target_utm_zone > 60):
                        commands.append(unicode(target_utm_zone - 60) + "south")
                    else:
                        commands.append(unicode(target_utm_zone) + "north")
            elif (target_projection < 5):
                target_sp_code = self.parameterAsInt(parameters, las2lasPro_project.TARGET_SP, context)
                if (target_sp_code != 0):
                    commands.append("-target_" + las2lasPro_project.PROJECTIONS[target_projection])
                    commands.append(las2lasPro_project.STATE_PLANES[target_sp_code])
            else:
                commands.append("-target_" + las2lasPro_project.PROJECTIONS[target_projection])
        self.addParametersOutputDirectoryCommands(parameters, context, commands)
        self.addParametersOutputAppendixCommands(parameters, context, commands)
        self.addParametersPointOutputFormatCommands(parameters, context, commands)
        self.addParametersAdditionalCommands(parameters, context, commands)
        self.addParametersCoresCommands(parameters, context, commands)

        LAStoolsUtils.runLAStools(commands, feedback)

        return {"": None}

    def name(self):
        return 'las2lasPro_project'

    def displayName(self):
        return 'las2lasPro_project'

    def group(self):
        return 'folder - processing points'

    def groupId(self):
        return 'folder - processing points'

    def createInstance(self):
        return las2lasPro_project()
