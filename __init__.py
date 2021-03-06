# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LmOpenData
                                 A QGIS plugin
 Swedish National Land Survey Open WMTS layers
                             -------------------
        begin                : 2016-07-01
        copyright            : (C) 2016 by Klas Karlsson
        email                : klaskarlsson@hotmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LmOpenData class from file LmOpenData.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .lm_open_data import LmOpenData
    return LmOpenData(iface)
