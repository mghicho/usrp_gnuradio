#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Oct  7 16:45:52 2015
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from ofdm_radio import ofdm_radio  # grc-generated hier_block
from optparse import OptionParser
import time


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, ampl=0.7, args='', mtu=255, port="12345", rate=1e6, rx_antenna="TX/RX", rx_freq=420e6, rx_gain=0, rx_lo_offset=0, samps_per_sym=4, tx_freq=440e6, tx_gain=20, tx_lo_offset=0):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.ampl = ampl
        self.args = args
        self.mtu = mtu
        self.port = port
        self.rate = rate
        self.rx_antenna = rx_antenna
        self.rx_freq = rx_freq
        self.rx_gain = rx_gain
        self.rx_lo_offset = rx_lo_offset
        self.samps_per_sym = samps_per_sym
        self.tx_freq = tx_freq
        self.tx_gain = tx_gain
        self.tx_lo_offset = tx_lo_offset

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 500000

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", args)),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(rx_freq, 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0.set_bandwidth(2*samp_rate, 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", args)),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(tx_freq, 0)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_bandwidth(2*samp_rate, 0)
        self.ofdm_radio_0 = ofdm_radio(
            rate=1e6,
        )
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1, "127.0.0.1", 12346, 1470, True)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_SERVER", "", port, mtu, False)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, "length")
        self.blocks_message_debug_0_0_1 = blocks.message_debug()

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0, 'pdus'), (self.ofdm_radio_0, 'msg_in'))    
        self.msg_connect((self.ofdm_radio_0, 'msg_out'), (self.blocks_message_debug_0_0_1, 'print_pdu'))    
        self.msg_connect((self.ofdm_radio_0, 'msg_out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))    
        self.msg_connect((self.ofdm_radio_0, 'msg_out'), (self.blocks_socket_pdu_0, 'pdus'))    
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_udp_sink_0, 0))    
        self.connect((self.ofdm_radio_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.ofdm_radio_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_ampl(self):
        return self.ampl

    def set_ampl(self, ampl):
        self.ampl = ampl

    def get_args(self):
        return self.args

    def set_args(self, args):
        self.args = args

    def get_mtu(self):
        return self.mtu

    def set_mtu(self, mtu):
        self.mtu = mtu
        #self.blocks_udp_sink_0.Template error: set_mtu($self.mtu)
        #    cannot find 'mtu'

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_rx_antenna(self):
        return self.rx_antenna

    def set_rx_antenna(self, rx_antenna):
        self.rx_antenna = rx_antenna

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.uhd_usrp_source_0.set_center_freq(self.rx_freq, 0)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)
        	

    def get_rx_lo_offset(self):
        return self.rx_lo_offset

    def set_rx_lo_offset(self, rx_lo_offset):
        self.rx_lo_offset = rx_lo_offset

    def get_samps_per_sym(self):
        return self.samps_per_sym

    def set_samps_per_sym(self, samps_per_sym):
        self.samps_per_sym = samps_per_sym

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq
        self.uhd_usrp_sink_0.set_center_freq(self.tx_freq, 0)

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)
        	

    def get_tx_lo_offset(self):
        return self.tx_lo_offset

    def set_tx_lo_offset(self, tx_lo_offset):
        self.tx_lo_offset = tx_lo_offset

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_bandwidth(2*self.samp_rate, 0)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_bandwidth(2*self.samp_rate, 0)


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "", "--ampl", dest="ampl", type="eng_float", default=eng_notation.num_to_str(0.7),
        help="Set TX BB amp [default=%default]")
    parser.add_option(
        "-a", "--args", dest="args", type="string", default='',
        help="Set USRP device args [default=%default]")
    parser.add_option(
        "", "--mtu", dest="mtu", type="intx", default=255,
        help="Set TCP Socket MTU [default=%default]")
    parser.add_option(
        "", "--port", dest="port", type="string", default="12345",
        help="Set TCP port [default=%default]")
    parser.add_option(
        "-r", "--rate", dest="rate", type="eng_float", default=eng_notation.num_to_str(1e6),
        help="Set Sample rate [default=%default]")
    parser.add_option(
        "-A", "--rx-antenna", dest="rx_antenna", type="string", default="TX/RX",
        help="Set RX antenna [default=%default]")
    parser.add_option(
        "", "--rx-freq", dest="rx_freq", type="eng_float", default=eng_notation.num_to_str(420e6),
        help="Set RX freq [default=%default]")
    parser.add_option(
        "", "--rx-gain", dest="rx_gain", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set RX gain [default=%default]")
    parser.add_option(
        "", "--rx-lo-offset", dest="rx_lo_offset", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set RX LO offset [default=%default]")
    parser.add_option(
        "", "--samps-per-sym", dest="samps_per_sym", type="intx", default=4,
        help="Set Samples/symbol [default=%default]")
    parser.add_option(
        "", "--tx-freq", dest="tx_freq", type="eng_float", default=eng_notation.num_to_str(440e6),
        help="Set TX freq [default=%default]")
    parser.add_option(
        "", "--tx-gain", dest="tx_gain", type="eng_float", default=eng_notation.num_to_str(20),
        help="Set TX gain [default=%default]")
    parser.add_option(
        "", "--tx-lo-offset", dest="tx_lo_offset", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set TX LO offset [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(ampl=options.ampl, args=options.args, mtu=options.mtu, port=options.port, rate=options.rate, rx_antenna=options.rx_antenna, rx_freq=options.rx_freq, rx_gain=options.rx_gain, rx_lo_offset=options.rx_lo_offset, samps_per_sym=options.samps_per_sym, tx_freq=options.tx_freq, tx_gain=options.tx_gain, tx_lo_offset=options.tx_lo_offset)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
