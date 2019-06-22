def readCSMNC(fileName):
    # open files
    fn = open(fileName, 'r')
    # magic number, ns, number of splited string
    # counted of the *.dat file download from CSMNC
    ns = 59
    tmp1 = fn.read()
    tmp2 = tmp1.split(maxsplit=59)
    tmpData = tmp2[59]
    # output the longitude and latitude of station to stationList.dat
    tmpLat = tmp2[18]
    tmpLong = tmp2[19]
    lat = tmpLat[0:6]
    lon = tmpLong[0:7]
    # magic number, td, duration time in seconds
    # pay attention to the type of variables!!!
    # td and step are floats
    # nps is an integer
    td = float(tmp2[52])
    # time intervals, = 0.005 SEC
    step = float(tmp2[43])
    # nps, number of data points
    nps = int(float(tmp2[38]))
    
    # start to distribute SAC head variables
    # component direction
    tmp2[30]
    # time interval
    delta = float(tmp2[43])
    # number of points
    npts = nps
    # station name
    stnm = tmp2[17]
    # instrument
    inst = tmp2[25]
    # compant name
    cmpNm = tmp2[30]
    # cmpaz, 方位角; cmpinc，倾角
    if (cmpNm == 'UD'):
        cmpaz = 0.0; cmpinc = 0.0
    elif (cmpNm == 'EW'):
        cmpaz = 90.0; cmpinc = 90.0
    elif (cmpNm == 'NS'):
        cmpaz = 0.0; cmpinc = 90.0
    else:
        raise ValueError('wrong component direction', cmpNm)
    # event name
    evnm = tmp2[5]
    # event latitude
    evla = float(tmp2[9][0:6])
    # event longitude
    evlo = float(tmp2[10][0:7])
    # event depth
    evdp = float(tmp2[12])
    # magnitude
    mag = float(tmp2[15][0:2])
    # latitude and longitude
    stla = lat
    stlo = lon
    iftype = 1
    # linspace default include start and stop
    # np.linspace(start, stop, number of samples)
    times = np.linspace(step, td, npts)
    tmp3 = tmpData.split(maxsplit=npts)
    tmp4 = np.asfarray(tmp3)
    # create null SAC object
    head = SAC()
    # set head variables
    head.set_cmp(cmpaz, cmpinc)
    head.set_evdp(evdp)
    head.set_evla(evla)
    head.set_evlo(evlo)
    head.set_kevnm(evnm)
    head.set_mag(mag)
    head.set_kinst(inst)
    head.set_kstnm(stnm)
    head.set_stloc(stla, stlo)
    # set nessary head variables' values
    head.set_iftype(iftype)
    head.set_npts(npts)
    head.set_delta(delta)
    head.set_leven()
    head.set_be(step, td)
    head.set_nvhdr()
    # close all files
    fn.close()
    return head, tmp4