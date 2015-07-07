# -*- coding: utf-8 -*-
"""
/***************************************************************************
 lantmateridata
                                 A QGIS plugin
 Open Data Lantmäteriet (SWE)
                             -------------------
        begin                : 2015-07-07
        copyright            : (C) 2015 by Geosupportsystem.wordpress.com
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
    """Load lantmateridata class from file lantmateridata.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .lmOpenData import lantmateridata
    return lantmateridata(iface)
