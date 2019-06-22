#! /bin/python
import numpy as np
class SAC:
    """
    Seismology Analysis Code format, include head and data segments
    """
    def __init__(self):
        _sacRealNull = -12345.00
        _sacIntNull = -12345
        _sacStrNull = '-12345  '
        # real number
        self.delta, self.depmin, self.depmax, self.scale, self.odelta,self.b, self.e, self.o, self.a, self.internal1, self.t0, self.t1, self.t2, self.t3, self.t4, self.t5, self.t6, self.t7, self.t8, self.t9, self.f, self.resp0, self.resp1, self.resp2, self.resp3, self.resp4, self.resp5, self.resp6, self.resp7, self.resp8, self.resp9, self.stla, self.stlo, self.stel, self.stdp, self.evla, self.evlo, self.evel, self.evdp, self.mag, self.user0, self.user1, self.user2, self.user3, self.user4, self.user5, self.user6, self.user7, self.user8, self.user9, self.dist, self.az, self.baz, self.gcarc, self.internal2, self.internal3, self.depmen, self.cmpaz, self.cmpinc, self.xminimum, self.xmaximum, self.yminimum, self.ymaximum, self.unused1, self.unused2, self.unused3, self.unused4, self.unused5, self.unused6, self.unused7 = _sacRealNull * np.ones((70, ), dtype = float)
        self.nzyear, self.nzjday, self.nzhour, self.nzmin, self.nzsec, self.nzmsec, self.nvhdr, self.norid, self.nevid, self.npts, self.internal4, self.nwfid, self.nxsize, self.nysize, self.unused8, self.iftype, self.idep, self.iztype, self.unused9, self.iinst, self.istreg, self.ievreg, self.ievtyp, self.iqual, self.isynth, self.imagtyp, self.imagsrc, self.unused10, self.unused11, self.unused12, self.unused13, self.unused14, self.unused15, self.unused16, self.unused17, self.leven, self.lpspol, self.lovrok, self.lcalda, self.unused18 = _sacIntNull * np.ones((40, ), dtype = int)
        # characters
        strNull = list(range(23))
        for i in range(23):
            strNull[i] = _sacStrNull
        # attribute sacStrNull to string head variables
        self.kstnm, self.kevnm, self.khole, self.ko, self.ka, self.kt0, self.kt1, self.kt2, self.kt3, self.kt4, self.kt5, self.kt6, self.kt7, self.kt8, self.kt9, self.kf, self.kuser0, self.kuser1, self.kuser2, self.kcmpnm, self.knetwk, self.kdatrd, self.kinst = strNull
        
    def set_kevnm(self, evnm):
        if not isinstance(evnm, str):
            raise TypeError(evnm)
        self.kevnm = evnm
        
    def set_kstnm(self, stnm):
        self.kstnm = stnm
            
    def set_kinst(self, inst):
        # instrument
        self.kinst = inst
            
    def set_evla(self, evla):
        self.evla = evla
        
    def set_evlo(self, evlo):
        self.evlo = evlo
            
    def set_evdp(self, evdp):
        self.evdp = evdp
            
    def set_mag(self, mag):
        self.mag = mag

    def set_cmp(self, cmpaz, cmpinc):
        self.cmpaz = cmpaz
        self.cmpinc = cmpinc
    
    def set_stloc(self, stla, stlo):
        self.stla = float(stla); self.stlo = float(stlo)
    # set nessary head variables' values
    def set_iftype(self, iftype):
        self.iftype = int(iftype)
    
    def set_nvhdr(self):
        self.nvhdr = 6
    
    def set_npts(self, npts):
        self.npts = int(npts)

    def set_delta(self, delta):
        self.delta = float(delta)
    
    def set_be(self, b, e):
        self.b = float(b); self.e = float(e)
    
    def set_leven(self):
        self.leven = 1
    # end of set nessary head variables' values
    
    # write SAC objects to ascii files
    def writeOut(self, outFile, data):
        # write SAC object to outFile
        fo = open(outFile, 'w')
        fo.write(format(self.delta, ">15") +  format(self.depmin, ">15.2f") +  format(self.depmax, ">15.2f") +  format(self.scale, ">15.2f") +  format(self.odelta, ">15.2f") + '\n')
        fo.write(format(self.b, ">15") +  format(self.e, ">15") +  format(self.o, ">15.2f") +  format(self.a, ">15.2f") +  format(self.internal1, ">15.2f") + '\n')
        fo.write(format(self.t0, ">15.2f") +  format(self.t1, ">15.2f") +  format(self.t2, ">15.2f") +  format(self.t3, ">15.2f") +  format(self.t4, ">15.2f") + '\n')
        fo.write(format(self.t5, ">15.2f") +  format(self.t6, ">15.2f") +  format(self.t7, ">15.2f") +   format(self.t8, ">15.2f") +  format(self.t9, ">15.2f") + '\n') 
        fo.write(format(self.f, ">15.2f") +  format(self.resp0, ">15.2f") +  format(self.resp1, ">15.2f") +   format(self.resp2, ">15.2f") +  format(self.resp3, ">15.2f") + '\n') 
        fo.write(format(self.resp4, ">15.2f") +  format(self.resp5, ">15.2f") +  format(self.resp6, ">15.2f") +   format(self.resp7, ">15.2f") +  format(self.resp8, ">15.2f") + '\n') 
        fo.write(format(self.resp9, ">15.2f") +  format(self.stla, ">15") +  format(self.stlo, ">15") +   format(self.stel, ">15.2f") +  format(self.stdp, ">15.2f") + '\n') 
        fo.write(format(self.evla, ">15") +  format(self.evlo, ">15") +  format(self.evel, ">15.2f") +   format(self.evdp, ">15.2f") +  format(self.mag, ">15") + '\n') 
        fo.write(format(self.user0, ">15.2f") +  format(self.user1, ">15.2f") +  format(self.user2, ">15.2f") +   format(self.user3, ">15.2f") +  format(self.user4, ">15.2f") + '\n') 
        fo.write(format(self.user5, ">15.2f") +  format(self.user6, ">15.2f") +  format(self.user7, ">15.2f") +  format(self.user8, ">15.2f") +  format(self.user9, ">15.2f") + '\n' ) 
        fo.write(format(self.dist, ">15.2f") +  format(self.az, ">15.2f") +  format(self.baz, ">15.2f") +  format(self.gcarc, ">15.2f") +  format(self.internal2, ">15.2f") + '\n' ) 
        fo.write(format(self.internal3, ">15.2f") +  format(self.depmen, ">15.2f") +  format(self.cmpaz, ">15") +  format(self.cmpinc, ">15") +  format(self.xminimum, ">15.2f") + '\n' ) 
        fo.write(format(self.xmaximum, ">15.2f") +  format(self.yminimum, ">15.2f") +  format(self.ymaximum, ">15.2f") +  format(self.unused1, ">15.2f") +  format(self.unused2, ">15.2f") + '\n' ) 
        fo.write(format(self.unused3, ">15.2f") +  format(self.unused4, ">15.2f") +  format(self.unused5, ">15.2f") +  format(self.unused6, ">15.2f") +  format(self.unused7, ">15.2f") + '\n' ) 
        fo.write(format(self.nzyear, ">10") +  format(self.nzjday, ">10") +  format(self.nzhour, ">10") +  format(self.nzmin, ">10") +  format(self.nzsec, ">10") + '\n' ) 
        fo.write(format(self.nzmsec, ">10") +  format(self.nvhdr, ">10") +  format(self.norid, ">10") +  format(self.nevid, ">10") +  format(self.npts, ">10") + '\n' ) 
        fo.write(format(self.internal4, ">10") +  format(self.nwfid, ">10") +  format(self.nxsize, ">10") +  format(self.nysize, ">10") +  format(self.unused8, ">10") + '\n' ) 
        fo.write(format(self.iftype, ">10") +  format(self.idep, ">10") +  format(self.iztype, ">10") +  format(self.unused9, ">10") +  format(self.iinst, ">10") + '\n' ) 
        fo.write(format(self.istreg, ">10") +  format(self.ievreg, ">10") +  format(self.ievtyp, ">10") +  format(self.iqual, ">10") +  format(self.isynth, ">10") + '\n' ) 
        fo.write(format(self.imagtyp, ">10") +  format(self.imagsrc, ">10") +  format(self.unused10, ">10") +  format(self.unused11, ">10") +  format(self.unused12, ">10") + '\n' ) 
        fo.write(format(self.unused13, ">10") +  format(self.unused14, ">10") +  format(self.unused15, ">10") +  format(self.unused16, ">10") + format(self.unused17, ">10") + '\n' ) 
        fo.write(format(self.leven, ">10") +  format(self.lpspol, ">10") +  format(self.lovrok, ">10") +  format(self.lcalda, ">10") +  format(self.unused18, ">10") + '\n' )
        fo.write(format(self.kstnm, "<8") + format(self.kevnm, "<8")+ '\n')
        fo.write(format(self.khole, "<8") + format(self.ko, "<8") +  format(self.ka, "<8") + '\n')
        fo.write(format(self.kt0, "<8") + format(self.kt1, "<8") + format(self.kt2, "<8") + '\n')
        fo.write(format(self.kt3, "<8") + format(self.kt4, "<8") + format(self.kt5, "<8") + '\n' )
        fo.write(format(self.kt6, "<8") + format(self.kt7, "<8") + format(self.kt8, "<8") + '\n' )
        fo.write(format(self.kt9, "<8") + format(self.kf, "<8") + format(self.kuser0, "<8") + '\n' )
        fo.write(format(self.kuser1, "<8") + format(self.kuser2, "<8") + format(self.kcmpnm, "<8") + '\n')
        fo.write(format(self.knetwk, "<8") + format(self.kdatrd, "<8") + format(self.kinst, "<8") + '\n')
        # write data segment
        rem = self.npts % 5
        loop = int((self.npts - rem) / 5)
        for i in range(loop):
            fo.write(str(format(data[i * 5], ">15")) + str(format(data[i * 5 + 1], ">15")) + \
                     str(format(data[i * 5 + 2], ">15")) + str(format(data[i * 5 + 3], ">15")) + \
                     str(format(data[i * 5 + 4], ">15")) + '\n')
        if (rem != 0):
            for j in range(rem):
                fo.write(str(format(data[5 * loop + j], ">15")))
        
               
        fo.close()
