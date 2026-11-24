#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: PRJ-MCOM GATE-2: Baseband Audio Link
# Author: Nguyen Huynh Van Phuong
# Description: Baseband Audio Streaming with PCM Framing (PRJ-MCOM GATE-2)
# GNU Radio version: 3.10.12.0

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import baseband_audio_link_epy_block_depacketizer as epy_block_depacketizer  # embedded python block
import baseband_audio_link_epy_block_packetizer as epy_block_packetizer  # embedded python block
import threading




class baseband_audio_link(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "PRJ-MCOM GATE-2: Baseband Audio Link", catch_exceptions=True)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000

        ##################################################
        # Blocks
        ##################################################

        self.epy_block_packetizer = epy_block_packetizer.blk(frame_samples=48)
        self.epy_block_depacketizer = epy_block_depacketizer.blk(frame_samples=48)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('test_audio_48k.wav', False)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(
            'rx_audio_48k.wav',
            1,
            samp_rate,
            blocks.FORMAT_WAV,
            blocks.FORMAT_PCM_16,
            False
            )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_wavfile_source_0, 0), (self.epy_block_packetizer, 0))
        self.connect((self.epy_block_depacketizer, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.epy_block_packetizer, 0), (self.epy_block_depacketizer, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate




def main(top_block_cls=baseband_audio_link, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()
    tb.flowgraph_started.set()

    tb.wait()


if __name__ == '__main__':
    main()
