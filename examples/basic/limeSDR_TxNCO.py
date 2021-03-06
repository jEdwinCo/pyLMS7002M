from __future__ import print_function
from pyLMS7002M import *
import sys

def logTxt(text, end="\n"):
    print(text, end=end)
    sys.stdout.flush()
    
logTxt("Searching for LimeSDR... ",end="")
try:
    limeSDR = LimeSDR()
except:
    logTxt("\nLimeSDR not found")
    exit(1)
logTxt("FOUND")

limeSDR.LMS7002_Reset()                             # reset the LMS7002M
lms7002 = limeSDR.getLMS7002()                      # get the LMS7002M object
lms7002.MIMO = 'MIMO'

# Initial configuration
logTxt("Tuning CGEN... ", end="")
lms7002.CGEN.setCLK(300e6)
logTxt("OK")

logTxt("Tuning SXT... ", end="")
lms7002.SX['T'].setFREQ(1.2e9)
logTxt("OK")

logTxt("Configuring TxTSP... ",end="")
TxTSP = lms7002.TxTSP['A']
TxTSP.TSGMODE = 'DC'
TxTSP.INSEL = 'TEST'
TxTSP.CMIX_BYP = 'USE'  # Use the complex mixer
TxTSP.GFIR1_BYP = 'BYP'
TxTSP.GFIR2_BYP = 'BYP'
TxTSP.GFIR3_BYP = 'BYP'
TxTSP.GC_BYP = 'BYP'
TxTSP.DC_BYP = 'BYP'
TxTSP.PH_BYP = 'BYP'
I = 0x7FFF
Q = 0x8000
TxTSP.loadDCIQ(I, Q)
logTxt("OK")

logTxt("Configuring TRF... ",end="")
TRF = lms7002.TRF['A']
TRF.LOSS_MAIN_TXPAD_TRF = 10 
TRF.EN_LOOPB_TXPAD_TRF = 0
TRF.L_LOOPB_TXPAD_TRF = 0    
TRF.PD_TLOBUF_TRF = 0
logTxt("OK")

logTxt("Configuring NCO... ",end="")
TXNCO = lms7002.NCO["TXA"]
TXNCO.MODE = 0
TXNCO.setNCOFrequency(0, 1e6)
TXNCO.SEL = 0
logTxt("OK")

