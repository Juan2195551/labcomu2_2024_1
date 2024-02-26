#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: practica2
# Author: bradlee_castro
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import bloques_epy_block_2 as epy_block_2  # embedded python block
import sip



class bloques(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "practica2", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("practica2")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "bloques")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################

        self.media = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.media.set_update_time(0.10)
        self.media.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.media.set_min(i, -1)
            self.media.set_max(i, 1)
            self.media.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.media.set_label(i, "Data {0}".format(i))
            else:
                self.media.set_label(i, labels[i])
            self.media.set_unit(i, units[i])
            self.media.set_factor(i, factor[i])

        self.media.enable_autoscale(False)
        self._media_win = sip.wrapinstance(self.media.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._media_win)
        self.epy_block_2 = epy_block_2.blk()
        self.blocks_vector_source_x_0 = blocks.vector_source_f((1, 2, -1), True, 1, [])
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 3, 0)
        self.RMS = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.RMS.set_update_time(0.10)
        self.RMS.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.RMS.set_min(i, -1)
            self.RMS.set_max(i, 1)
            self.RMS.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.RMS.set_label(i, "Data {0}".format(i))
            else:
                self.RMS.set_label(i, labels[i])
            self.RMS.set_unit(i, units[i])
            self.RMS.set_factor(i, factor[i])

        self.RMS.enable_autoscale(False)
        self._RMS_win = sip.wrapinstance(self.RMS.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._RMS_win)
        self.POT_PROMEDIO = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.POT_PROMEDIO.set_update_time(0.10)
        self.POT_PROMEDIO.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.POT_PROMEDIO.set_min(i, -1)
            self.POT_PROMEDIO.set_max(i, 1)
            self.POT_PROMEDIO.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.POT_PROMEDIO.set_label(i, "Data {0}".format(i))
            else:
                self.POT_PROMEDIO.set_label(i, labels[i])
            self.POT_PROMEDIO.set_unit(i, units[i])
            self.POT_PROMEDIO.set_factor(i, factor[i])

        self.POT_PROMEDIO.enable_autoscale(False)
        self._POT_PROMEDIO_win = sip.wrapinstance(self.POT_PROMEDIO.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._POT_PROMEDIO_win)
        self.M_cuadratica = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.M_cuadratica.set_update_time(0.10)
        self.M_cuadratica.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.M_cuadratica.set_min(i, -1)
            self.M_cuadratica.set_max(i, 1)
            self.M_cuadratica.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.M_cuadratica.set_label(i, "Data {0}".format(i))
            else:
                self.M_cuadratica.set_label(i, labels[i])
            self.M_cuadratica.set_unit(i, units[i])
            self.M_cuadratica.set_factor(i, factor[i])

        self.M_cuadratica.enable_autoscale(False)
        self._M_cuadratica_win = sip.wrapinstance(self.M_cuadratica.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._M_cuadratica_win)
        self.DES_ESTANDAR = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.DES_ESTANDAR.set_update_time(0.10)
        self.DES_ESTANDAR.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.DES_ESTANDAR.set_min(i, -1)
            self.DES_ESTANDAR.set_max(i, 1)
            self.DES_ESTANDAR.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.DES_ESTANDAR.set_label(i, "Data {0}".format(i))
            else:
                self.DES_ESTANDAR.set_label(i, labels[i])
            self.DES_ESTANDAR.set_unit(i, units[i])
            self.DES_ESTANDAR.set_factor(i, factor[i])

        self.DES_ESTANDAR.enable_autoscale(False)
        self._DES_ESTANDAR_win = sip.wrapinstance(self.DES_ESTANDAR.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._DES_ESTANDAR_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.epy_block_2, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.epy_block_2, 4), (self.DES_ESTANDAR, 0))
        self.connect((self.epy_block_2, 1), (self.M_cuadratica, 0))
        self.connect((self.epy_block_2, 3), (self.POT_PROMEDIO, 0))
        self.connect((self.epy_block_2, 2), (self.RMS, 0))
        self.connect((self.epy_block_2, 0), (self.media, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "bloques")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate




def main(top_block_cls=bloques, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
