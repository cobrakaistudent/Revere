### get Address res ENodeB|LTE
This MO shnould always have an MO, cannot be empty

Example of an extract of moshell



    M7WAS234A> get Address res ENodeB|LTE

    240424-14:30:11-0500 11.242.90.212 24.0c MSRBS_NODE_MODEL_23.Q4_643.28133.125_0bc9 stopfile=/tmp/3909212
    =================================================================================================================
    MO                                                      Attribute         Value
    =================================================================================================================
    Router=LTE,InterfaceIPv4=LTE,AddressIPv4=1              reservedBy        [3] = 
    >>> reservedBy = ENodeBFunction=1
    >>> reservedBy = ENodeBFunction=1
    >>> reservedBy = Transport=1,SctpEndpoint=LTE
    =================================================================================================================
    Total: 1 MOs



### Termpoints

    The following extract shows the termpoints(Table 1) and the colocated nodes(Table 2) and the complete st term table (Table 3).


### Table 1
    M7HCH119A> st termpointtognb=1

    240430-15:40:33-0500 11.135.248.170 24.0c MSRBS_NODE_MODEL_23.Q4_643.28133.125_0bc9 stopfile=/tmp/2309857
    ===================================================================================
    Proxy  Adm State     Op. State     MO
    ===================================================================================
    783  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,GUtraNetwork=1,ExternalGNodeBFunction=1316220,TermPointToGNB=1
    788  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,GUtraNetwork=1,ExternalGNodeBFunction=1344694,TermPointToGNB=1
    ===================================================================================
    Total: 2 MOs


### Table 2
    M7HCH119A> get FUnction=1 nbid$

    240430-15:40:34-0500 11.135.248.170 24.0c MSRBS_NODE_MODEL_23.Q4_643.28133.125_0bc9 stopfile=/tmp/2309857
    =================================================================================================================
    MO                                                      Attribute         Value
    =================================================================================================================
    ENodeBFunction=1                                        eNBId             142198
    ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=1 eNBId             51126
    GNBCUCPFunction=1                                       gNBId             1316220
    GNBCUUPFunction=1                                       gNBId             1316220
    GNBDUFunction=1                                         gNBId             1316220
    ExtGNBDUPartnerFunction=1344694                         gNBId             1344694
    ExtGNBDUPartnerFunction=1360094                         gNBId             1360094
    =================================================================================================================
    Total: 7 MOs


### Table 3 
    M7HCH119A> st term

    240430-15:40:35-0500 11.135.248.170 24.0c MSRBS_NODE_MODEL_23.Q4_643.28133.125_0bc9 stopfile=/tmp/2309857
    ===================================================================================
    Proxy  Adm State     Op. State     MO
    ===================================================================================
    484  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=1,TermPointToENB=310260-51126
    489  1 (UNLOCKED)  0 (DISABLED)  ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310120-1040652,TermPointToENB=310120-1040652
    497  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-141679,TermPointToENB=310260-141679
    500  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-141680,TermPointToENB=310260-141680
    503  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-141681,TermPointToENB=310260-141681
    507  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-141683,TermPointToENB=310260-141683
    510  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-141687,TermPointToENB=310260-141687
    513  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-141688,TermPointToENB=310260-141688
    516  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-141692,TermPointToENB=310260-141692
    519  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-142037,TermPointToENB=310260-142037
    522  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-142174,TermPointToENB=310260-142174
    525  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-142194,TermPointToENB=310260-142194
    531  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-142201,TermPointToENB=310260-142201
    534  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-142210,TermPointToENB=310260-142210
    537  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-142220,TermPointToENB=310260-142220
    541  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-146243,TermPointToENB=310260-146243
    545  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-146379,TermPointToENB=310260-146379
    548  1 (UNLOCKED)  0 (DISABLED)  ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-216018,TermPointToENB=310260-216018
    550  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-219858,TermPointToENB=310260-219858
    553  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-307025,TermPointToENB=310260-307025
    562  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-310044,TermPointToENB=310260-310044
    565  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-310241,TermPointToENB=310260-310241
    569  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-310396,TermPointToENB=310260-310396
    577  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-326120,TermPointToENB=310260-326120
    580  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-326492,TermPointToENB=310260-326492
    582  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-326981,TermPointToENB=310260-326981
    588  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-331643,TermPointToENB=310260-331643
    593  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-331655,TermPointToENB=310260-331655
    597  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-343026,TermPointToENB=310260-343026
    604  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-343668,TermPointToENB=310260-343668
    608  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-344086,TermPointToENB=310260-344086
    613  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-344092,TermPointToENB=310260-344092
    616  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-344500,TermPointToENB=310260-344500
    621  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-345553,TermPointToENB=310260-345553
    632  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-345982,TermPointToENB=310260-345982
    634  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-347203,TermPointToENB=310260-347203
    637  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-347274,TermPointToENB=310260-347274
    646  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-347336,TermPointToENB=310260-347336
    650  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-348187,TermPointToENB=310260-348187
    655  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-435101,TermPointToENB=310260-435101
    658  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-435351,TermPointToENB=310260-435351
    661  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-435652,TermPointToENB=310260-435652
    669  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-446421,TermPointToENB=310260-446421
    676  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-50500,TermPointToENB=310260-50500
    679                1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-51124,EranInterMeLink=1
    688  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-51124,TermPointToENB=310260-51124
    696  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-51127,TermPointToENB=310260-51127
    699  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-51211,TermPointToENB=310260-51211
    702  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-51214,TermPointToENB=310260-51214
    706  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-51668,TermPointToENB=310260-51668
    713  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-51724,TermPointToENB=310260-51724
    721  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-52172,TermPointToENB=310260-52172
    724  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-54377,TermPointToENB=310260-54377
    732  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-56852,TermPointToENB=310260-56852
    737  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=310260-880970,TermPointToENB=310260-880970
    783  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,GUtraNetwork=1,ExternalGNodeBFunction=1316220,TermPointToGNB=1
    788  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,GUtraNetwork=1,ExternalGNodeBFunction=1344694,TermPointToGNB=1
    851  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,GUtraNetwork=1,ExternalGNodeBFunction=310260-000000001348894,TermPointToGNB=310260-000000001348894
    860  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,GUtraNetwork=1,ExternalGNodeBFunction=310260-000000001352091,TermPointToGNB=310260-000000001352091
    887  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,GUtraNetwork=1,ExternalGNodeBFunction=310260-000000001366010,TermPointToGNB=310260-000000001366010
    899  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,GUtraNetwork=1,ExternalGNodeBFunction=310260-000000001366949,TermPointToGNB=310260-000000001366949
    1041  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,TermPointToMme=DC1vMME1
    1042  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,TermPointToMme=DC1vMME2
    1043  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,TermPointToMme=DC2vMME1
    1044  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,TermPointToMme=NE1CMM01
    1045  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,TermPointToMme=NE1vMME1
    1046  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,TermPointToMme=NE1vMME2
    1047  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,TermPointToMme=NE4vMME1
    1048  1 (UNLOCKED)  0 (DISABLED)  ENodeBFunction=1,TermPointToMme=PH2vMME1
    1049  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,TermPointToMme=PH3nMME1
    1050  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,TermPointToMme=PH3vMME1
    1051  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,TermPointToMme=UP1vMME1
    1052  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,TermPointToMme=UP2nMME1
    1053  1 (UNLOCKED)  1 (ENABLED)   ENodeBFunction=1,TermPointToMme=UP2vMME1
    1902  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_142198,TermPointToENodeB=auto1
    1907  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_307025,TermPointToENodeB=auto1
    1912  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_310044,TermPointToENodeB=auto1
    1914  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_310941,TermPointToENodeB=auto1
    1917  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_326981,TermPointToENodeB=auto1
    1919  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_331643,TermPointToENodeB=auto1
    1921  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_331655,TermPointToENodeB=auto1
    1923  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_343026,TermPointToENodeB=auto1
    1925  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_343656,TermPointToENodeB=auto1
    1927  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_343668,TermPointToENodeB=auto1
    1929  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_344086,TermPointToENodeB=auto1
    1931  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_344092,TermPointToENodeB=auto1
    1937  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_345982,TermPointToENodeB=auto1
    1939  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_347203,TermPointToENodeB=auto1
    1941  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_347274,TermPointToENodeB=auto1
    1943  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_347324,TermPointToENodeB=auto1
    1946  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_347336,TermPointToENodeB=auto1
    1949  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_435101,TermPointToENodeB=auto1
    1951  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_435652,TermPointToENodeB=auto1
    1953  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_435656,TermPointToENodeB=auto1
    1956  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_50988,TermPointToENodeB=auto1
    1963  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_51124,TermPointToENodeB=auto1
    1965  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_51127,TermPointToENodeB=auto1
    1967  1 (UNLOCKED)  0 (DISABLED)  GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_51211,TermPointToENodeB=auto1
    1969  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_51668,TermPointToENodeB=auto1
    1973  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_51724,TermPointToENodeB=auto1
    1975  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_51779,TermPointToENodeB=auto1
    1979  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_52172,TermPointToENodeB=auto1
    1982  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_54377,TermPointToENodeB=auto1
    1984  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_55765,TermPointToENodeB=auto1
    1988  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_56852,TermPointToENodeB=auto1
    1990  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,EUtraNetwork=1,ExternalENodeBFunction=auto310_260_3_58699,TermPointToENodeB=auto1
    2340  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1311899,TermPointToGNodeB=auto1
    2351  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1311900,TermPointToGNodeB=auto1
    2362  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1311901,TermPointToGNodeB=auto1
    2373  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1311908,TermPointToGNodeB=auto1
    2384  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1311913,TermPointToGNodeB=auto1
    2395  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1316126,TermPointToGNodeB=auto1
    2417  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1321240,TermPointToGNodeB=auto1
    2428  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1323799,TermPointToGNodeB=auto1
    2448  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1325374,TermPointToGNodeB=auto1
    2459  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1325486,TermPointToGNodeB=auto1
    2488  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1329857,TermPointToGNodeB=auto1
    2508  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1329869,TermPointToGNodeB=auto1
    2519  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1333165,TermPointToGNodeB=auto1
    2539  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1337035,TermPointToGNodeB=auto1
    2559  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1337036,TermPointToGNodeB=auto1
    2579  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1337788,TermPointToGNodeB=auto1
    2599  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1341245,TermPointToGNodeB=auto1
    2619  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1344694,TermPointToGNodeB=auto1
    2639  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1344817,TermPointToGNodeB=auto1
    2659  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1345412,TermPointToGNodeB=auto1
    2679  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1345545,TermPointToGNodeB=auto1
    2690  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1346444,TermPointToGNodeB=auto1
    2710  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1346445,TermPointToGNodeB=auto1
    2730  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1346976,TermPointToGNodeB=auto1
    2732  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1347369,TermPointToGNodeB=auto1
    2761  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1347949,TermPointToGNodeB=auto1
    2781  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1347950,TermPointToGNodeB=auto1
    2810  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1348894,TermPointToGNodeB=auto1
    2830  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1348895,TermPointToGNodeB=auto1
    2850  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1349669,TermPointToGNodeB=auto1
    2879  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1349767,TermPointToGNodeB=auto1
    2905  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1350284,TermPointToGNodeB=auto1
    2934  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1350905,TermPointToGNodeB=auto1
    2954  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1350988,TermPointToGNodeB=auto1
    2983  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1351443,TermPointToGNodeB=auto1
    3012  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1352078,TermPointToGNodeB=auto1
    3041  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1352091,TermPointToGNodeB=auto1
    3070  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1352107,TermPointToGNodeB=auto1
    3099  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1352483,TermPointToGNodeB=auto1
    3119  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1353063,TermPointToGNodeB=auto1
    3148  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1353072,TermPointToGNodeB=auto1
    3177  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1353084,TermPointToGNodeB=auto1
    3197  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1355254,TermPointToGNodeB=auto1
    3226  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1355266,TermPointToGNodeB=auto1
    3246  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1355267,TermPointToGNodeB=auto1
    3275  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1355272,TermPointToGNodeB=auto1
    3295  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1355273,TermPointToGNodeB=auto1
    3306  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1358539,TermPointToGNodeB=auto1
    3317  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1358541,TermPointToGNodeB=auto1
    3337  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1359064,TermPointToGNodeB=auto1
    3366  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1359071,TermPointToGNodeB=auto1
    3386  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1360085,TermPointToGNodeB=auto1
    3406  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1360088,TermPointToGNodeB=auto1
    3426  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1360089,TermPointToGNodeB=auto1
    3446  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1360092,TermPointToGNodeB=auto1
    3466  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1360094,TermPointToGNodeB=auto1
    3486  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1360101,TermPointToGNodeB=auto1
    3506  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1360107,TermPointToGNodeB=auto1
    3517  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1360108,TermPointToGNodeB=auto1
    3546  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1363670,TermPointToGNodeB=auto1
    3575  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1366010,TermPointToGNodeB=auto1
    3586  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1366027,TermPointToGNodeB=auto1
    3615  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1366815,TermPointToGNodeB=auto1
    3635  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1366816,TermPointToGNodeB=auto1
    3664  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1366887,TermPointToGNodeB=auto1
    3684  1 (UNLOCKED)  0 (DISABLED)  GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1366944,TermPointToGNodeB=auto1
    3713  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1366949,TermPointToGNodeB=auto1
    3733  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1366950,TermPointToGNodeB=auto1
    3753  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1367008,TermPointToGNodeB=auto1
    3770  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1368194,TermPointToGNodeB=auto1
    3784  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1368990,TermPointToGNodeB=auto1
    3813  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1369961,TermPointToGNodeB=auto1
    3833  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1369962,TermPointToGNodeB=auto1
    3862  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,NRNetwork=1,ExternalGNBCUCPFunction=auto310_260_3_1371749,TermPointToGNodeB=auto1
    3923  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=DC1AMF01
    3925  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=DC2AMF01
    3927  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=DC2AMF02
    3929  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=NE1CMM01
    3931  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=NE3AMF01
    3933  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=NE4AMF01
    3935  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=NE4AMF02
    3937  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=PH1AMF01
    3939  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=PH2AMF01
    3941  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=PH2AMF02
    3943  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=PH3AMF01
    3945  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=UP1AMF01
    3947  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=UP2AMF01
    3949  1 (UNLOCKED)  1 (ENABLED)   GNBCUCPFunction=1,TermPointToAmf=UP2AMF02
    3951                1 (ENABLED)   GNBCUCPFunction=1,TermPointToGNBDU=1
    4774                1 (ENABLED)   GNBDUFunction=1,ExtGNBDUPartnerFunction=1344694,InterMeLink=1
    4775                1 (ENABLED)   GNBDUFunction=1,ExtGNBDUPartnerFunction=1344694,InterMeLink=2
    4777                1 (ENABLED)   GNBDUFunction=1,ExtGNBDUPartnerFunction=1360094,InterMeLink=1
    4778                1 (ENABLED)   GNBDUFunction=1,ExtGNBDUPartnerFunction=1360094,InterMeLink=2
    4868  1 (UNLOCKED)  1 (ENABLED)   GNBDUFunction=1,TermPointToGNBCUCP=1
    ===================================================================================
    Total: 200 MOs
