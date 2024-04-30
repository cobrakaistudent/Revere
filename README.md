### Checks get Address res ENodeB|LTE
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
