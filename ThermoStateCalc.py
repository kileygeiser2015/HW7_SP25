-*- coding: utf-8 -*-

# This updated UI version includes:
# - Separate group boxes for State 1 and State 2 property inputs
# - A group box for State 1, State 2, and Delta property outputs

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui__frm_2StateCalculator(object):
    def setupUi(self, _frm_2StateCalculator):
        _frm_2StateCalculator.setObjectName("_frm_2StateCalculator")
        _frm_2StateCalculator.resize(800, 600) #set width & hight of pixels
        self.verticalLayout = QtWidgets.QVBoxLayout(_frm_2StateCalculator)

        # Unit selection group
        self._grp_Units = QtWidgets.QGroupBox("System of Units")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self._grp_Units)
        self._rdo_SI = QtWidgets.QRadioButton("SI")
        self._rdo_SI.setChecked(True)
        self._rdo_English = QtWidgets.QRadioButton("English")
        self.horizontalLayout_2.addWidget(self._rdo_SI)
        self.horizontalLayout_2.addWidget(self._rdo_English)
        self.verticalLayout.addWidget(self._grp_Units)

        # Specified Properties group box with State 1 and State 2
        self._grp_SpecifiedProperties = QtWidgets.QGroupBox("Specified Properties")
        self.gridLayout = QtWidgets.QGridLayout(self._grp_SpecifiedProperties)
        #State 1
        self._grp_State1 = QtWidgets.QGroupBox("State 1")
        self.gridLayout_S1 = QtWidgets.QGridLayout(self._grp_State1)
        self._cmb_Property1_S1 = QtWidgets.QComboBox()
        self._le_Property1_S1 = QtWidgets.QLineEdit("1.0")
        self._lbl_Units1_S1 = QtWidgets.QLabel("Bar")
        self._cmb_Property2_S1 = QtWidgets.QComboBox()
        self._le_Property2_S1 = QtWidgets.QLineEdit("100.0")
        self._lbl_Units2_S1 = QtWidgets.QLabel("C")

        for cmb in [self._cmb_Property1_S1, self._cmb_Property2_S1]:
            cmb.addItems(["Pressure (p)",
                          "Temperature (T)",
                          "Quality (x)",
                          "Specific Internal Energy (u)",
                          "Specific Enthalpy (h)",
                          "Specific Volume (v)",
                          "Specific Entropy (s)"])

        self.gridLayout_S1.addWidget(QtWidgets.QLabel("Property 1"), 0, 0)
        self.gridLayout_S1.addWidget(self._cmb_Property1_S1, 1, 0)
        self.gridLayout_S1.addWidget(self._le_Property1_S1, 1, 1)
        self.gridLayout_S1.addWidget(self._lbl_Units1_S1, 1, 2)
        self.gridLayout_S1.addWidget(QtWidgets.QLabel("Property 2"), 2, 0)
        self.gridLayout_S1.addWidget(self._cmb_Property2_S1, 3, 0)
        self.gridLayout_S1.addWidget(self._le_Property2_S1, 3, 1)
        self.gridLayout_S1.addWidget(self._lbl_Units2_S1, 3, 2)
        #State 2
        self._grp_State2 = QtWidgets.QGroupBox("State 2")
        self.gridLayout_S2 = QtWidgets.QGridLayout(self._grp_State2)
        self._cmb_Property1_S2 = QtWidgets.QComboBox()
        self._le_Property1_S2 = QtWidgets.QLineEdit("1.0")
        self._lbl_Units1_S2 = QtWidgets.QLabel("Bar")
        self._cmb_Property2_S2 = QtWidgets.QComboBox()
        self._le_Property2_S2 = QtWidgets.QLineEdit("200.0")
        self._lbl_Units2_S2 = QtWidgets.QLabel("C")

        for cmb in [self._cmb_Property1_S2, self._cmb_Property2_S2]:
            cmb.addItems(["Pressure (p)",
                          "Temperature (T)",
                          "Quality (x)",
                          "Specific Internal Energy (u)",
                          "Specific Enthalpy (h)",
                          "Specific Volume (v)",
                          "Specific Entropy (s)"])

        self.gridLayout_S2.addWidget(QtWidgets.QLabel("Property 1"), 0, 0)
        self.gridLayout_S2.addWidget(self._cmb_Property1_S2, 1, 0)
        self.gridLayout_S2.addWidget(self._le_Property1_S2, 1, 1)
        self.gridLayout_S2.addWidget(self._lbl_Units1_S2, 1, 2)
        self.gridLayout_S2.addWidget(QtWidgets.QLabel("Property 2"), 2, 0)
        self.gridLayout_S2.addWidget(self._cmb_Property2_S2, 3, 0)
        self.gridLayout_S2.addWidget(self._le_Property2_S2, 3, 1)
        self.gridLayout_S2.addWidget(self._lbl_Units2_S2, 3, 2)

        self.gridLayout.addWidget(self._grp_State1, 0, 0)
        self.gridLayout.addWidget(self._grp_State2, 0, 1)
        #calculate
        self._pb_Calculate = QtWidgets.QPushButton("Calculate")
        self.gridLayout.addWidget(self._pb_Calculate, 1, 0, 1, 2)
        #warnings
        self._lbl_Warning = QtWidgets.QLabel()
        self._lbl_Warning.setText("Warning: Make sure properties are valid and not duplicated across states.")
        self._lbl_Warning.setStyleSheet("color: red; font-weight: bold")
        self.gridLayout.addWidget(self._lbl_Warning, 2, 0, 1, 2)
        self.verticalLayout.addWidget(self._grp_SpecifiedProperties)

        # Group box to show calculated state properties and changes
        self._grp_StateProperties = QtWidgets.QGroupBox("State Properties")
        self.hLayoutStates = QtWidgets.QHBoxLayout(self._grp_StateProperties)

        self._lbl_State1Props = QtWidgets.QLabel("State 1 Properties")
        self._lbl_State2Props = QtWidgets.QLabel("State 2 Properties")
        self._lbl_StateDelta = QtWidgets.QLabel("State Change")

        for lbl in [self._lbl_State1Props, self._lbl_State2Props, self._lbl_StateDelta]:
            lbl.setMinimumWidth(220)
            lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.hLayoutStates.addWidget(lbl)

        self.verticalLayout.addWidget(self._grp_StateProperties)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        QtCore.QMetaObject.connectSlotsByName(_frm_2StateCalculator)
