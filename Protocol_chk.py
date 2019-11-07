import pytest
from commandM import *

C = commands()

#check the data length recieved is correct

def test_checklength01():
    dataTx = [0x0A, 0x07, 0x0B, 0x06]
    dataRx  = [0x01, 0x04, 0x0B, 0x06]
    assert len(dataRx)==4
    assert dataRx == [0x01, 0x04, 0x0B, 0x06]

 





