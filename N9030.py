# -*- coding: utf-8 -*-
"""
Created on Fri May 11 19:50:53 2018

@author: Administrador
"""

'''
Created on 1 nov. 2017

@author: frank
'''
from instruments import spectrum_analyzer


class AgilentN9030(spectrum_analyzer.SpectrumAnalyzer):
    '''
    classdocs
    '''
    COMMAND_SET_RBW = "BAND {}"
    COMMAND_GET_RBW = "BAND?"
    COMMAND_SET_SPAN = "FREQ:SPAN {}"
    COMMAND_GET_SPAN = "FREQ:SPAN?"
    COMMAND_SET_CENTER_FREQ = "FREQ:CENT {}"
    COMMAND_GET_CENTER_FREQ = "FREQ:CENT?"
    COMMAND_SET_SWEEP_TIME = "SWE:TIME {}"
    COMMAND_GET_SWEEP_TIME = "SWE:TIME?"
    COMMAND_SET_VBW = "BAND:VID {}"
    COMMAND_GET_VBW = "BAND:VID?"
    COMMAND_SET_REF_LEVEL = "DISP:WIND:TRAC:Y:RLEV {}"
    COMMAND_GET_REF_LEVEL = "DISP:WIND:TRAC:Y:RLEV?"
    COMMAND_ZERO_SPAN = "FREQ:SPAN 0 Hz"
    COMMAND_TITLE = "DISP:ANN:TITL:DATA {}"  ## NO FUNCIONA!!!!!!
    COMMAND_SET_ATT = "POW:ATT {}"
    COMMAND_GET_ATT = "POW:ATT?"
    COMMAND_TAKE_SWEEP = ":INIT:CONT OFF; *WAI; :INIT:IMM; *WAI"
    COMMAND_SINGLE_SWEEP = "INIT:CONT OFF"  # NO FUNCIONA
    COMMAND_PEAK_SEARCH = "CALC:MARK1:MAX"
    COMMAND_NEXT_PEAK = "CALC:MARK1:MAX:NEXT"
    COMMAND_NEXT_PEAK_RIGHT = "CALC:MARK1:MAX:RIGH"
    COMMAND_NEXT_PEAK_LEFT = "CALC:MARK1:MAX:LEFT"
    COMMAND_GET_MARKER_AMPLITUDE = "CALC:MARK1:Y?"
    COMMAND_GET_MARKER_FREQ = "CALC:MARK1:X?"
    COMMAND_SET_DET_POSITIVE = "DET:TRAC POS"
    COMMAND_SET_DET_QPEAK = "DET:TRAC QPE"
    COMMAND_SET_DET_AVERAGE = "DET:TRAC AVER"
    COMMAND_SET_DET_RMS = "DET:TRAC RAV"
    COMMAND_SET_DET_SAMPLE = "DET:TRAC SAMP"
    COMMAND_SET_DET_NEGATIVE = "DET:TRAC NEG"
    COMMAND_GET_DET_TYPE = "DET:TRAC?"
    COMMAND_SET_LOG_SCALE = "DISP:WIND:TRAC:Y:PDIV {}"
    COMMAND_GET_LOG_SCALE = "DISP:WIND:TRAC:Y:PDIV?"
    COMMAND_SET_START_FREQ = "FREQ:STAR {}"
    COMMAND_SET_STOP_FREQ = "FREQ:STOP {}"
    COMMAND_SET_RBW_AUTO = "BWID:AUTO ON"
    COMMAND_SET_VBW_AUTO = "BWID:VID:AUTO ON"
    COMMAND_SET_SWEEP_AUTO = "SWE:TIME:AUTO ON"
    COMMAND_SET_CENTER_FREQ_MARKER = "CALC:MARK1:CENT"
    COMMAND_SET_AMP_UNIT = ":UNIT:POWer {}"
    
    def __init__(self, instrument_handler):
        '''
        Constructor
        '''
        super().__init__(instrument_handler)