#!/bin/sh
P="BEAM:GONI:"
fullpath="/home/a2cb/EPICS/CountingRoom_CSS/Goni"

#source the epics env to get the path to caget etc.
. /opt/epics/thisEPICS.sh

usage()
{
    echo 
    echo "$0 All        Initialises all goniometer axes"
    echo "$0 <axis>     Initialises given axis (X,Y,ROLL,PITCH,YAW)"
    echo "$0 -h         print this message"
    echo
    echo "The goniometer and radiators are controlled by EPICS - see the Slow Controls page on the A2 wiki at"
    echo "http://wwwa2.kph.uni-mainz.de/intern/daqwiki/epics/goniometer"
    echo
    echo "If there were errors check that the GONI EPICS ioc is running".
    
}

wait_stop()
{
    moving="1"
    axis="${1}.MOVN"
    rbv="${1}.RBV"
    
    while [ ${moving} -gt 0 ]
    do
#	echo $moving
	sleep 1
	moving=`caget -t ${axis}`
	pos=`caget -t ${rbv}`
	echo "$rbv = $pos"
    done
    
}

if [ $# -lt "1" ]; then
   usage
   exit
else
    if [ $1 = "-h" ]; then
	usage
	exit
    fi
fi


if [ "$1" != "All" ]; then
  #Pop up a warning dialogue to check that the beam is off.
    if ! zenity --title="Warning: The Beam must be off to initialise ${P}${1} axis." --question --text "Is the beam off?" --width 650; then
	exit
    fi
    
    fullaxis="${P}${1}"
    home="${fullaxis}.HOMR"
    caput ${home} 1
    wait_stop ${fullaxis}
    exit    

fi

#or doing the whole thing

if ! zenity --title="Warning: Initialising THE WHOLE GONIOMETER." --question --text "Is the beam off?" --width 650; then
    exit
fi

for axis in X Y ROLL PITCH YAW
do
    fullaxis="${P}${axis}"
    home="${fullaxis}.HOMR"
    caput ${home} 1
    wait_stop ${fullaxis}
done
    
exit
