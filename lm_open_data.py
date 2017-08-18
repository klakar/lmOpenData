# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LmOpenData
                                 A QGIS plugin
 Swedish National Land Survey Open WMTS layers
                              -------------------
        begin                : 2016-07-01
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Klas Karlsson
        email                : klaskarlsson@hotmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon, QMessageBox

#My Imports
from qgis.core import QgsRasterLayer, QgsMapLayerRegistry

# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from lm_open_data_dialog import LmOpenDataDialog
import os.path


class LmOpenData:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            '{}.qm'.format(locale))
        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = LmOpenDataDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&LM Open Data WMTS')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'LmOpenData')
        self.toolbar.setObjectName(u'LmOpenData')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('LmOpenData', message)
        
    # Add a WMTS layer from a QGIS layer source string and give it a layer name
    def add_layer(
        self,
        layer_source,
        layer_name):
        layer = QgsRasterLayer(layer_source,self.tr(layer_name),"wms")
        if not layer.isValid(): # Test if string is valid
        	 QMessageBox.information(self.iface.mainWindow(),self.tr(u"Error!"), self.tr(u"Layer has no valid token... Try again!"))
        	 QSettings().setValue('lmopendata/token', '') # if layer is incorrect clear token key
        QgsMapLayerRegistry.instance().addMapLayer(layer)

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToWebMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/LmOpenData/lm.png'
        self.add_action(
            icon_path,
            text=self.tr('Topographic Map'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginWebMenu(
                self.tr(u'&LM Open Data WMTS'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def run(self):
        """Run method that performs all the real work"""
        lm_token = QSettings().value('lmopendata/token') # Get any value from the stored value key
        if lm_token == '': # if key is empty show dialog
          #self.dlg.tokentext.setText(lm_token)
          self.dlg.show()
          result = self.dlg.exec_()
          # See if OK was pressed
          if result:
            #iface.messageBar().pushMessage("Debug:", self.dlg.token.getText(), level=QgsMessageBar.INFO)
            lm_token = str(self.dlg.tokentext.text())
            QSettings().setValue( 'lmopendata/token', lm_token )
          else:
          	return # If dialog is aborted, do nothing!
        layer_string = "contextualWMSLegend=0&crs=EPSG:3006&dpiMode=7&featureCount=10&format=image/png&layers=topowebb&styles=default&tileMatrixSet=3006&url=https://api.lantmateriet.se/open/topowebb-ccby/v1/wmts/token/" + str(lm_token) + "/?SERVICE%3DWMTS%26REQUEST%3DGetCapabilities"
        self.add_layer(
          layer_string,
          self.tr(u"LM Topographic CC-0"))
        #QSettings().setValue( 'lmopendata/token', '')  # Debug code. Activate to clear token every time.
                
                
                
