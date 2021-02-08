# Current-Voltage-instantaneous-power-
The file rawdata.txt contains voltage and current data in binary format, which are obtained from an electric power system with a digital device. The left-most digit of each binary values indicated the sign. If this digit is 0, the values is positive (+); if the digit is 1, the value is negative (-).
This code:
* loads the data to the program
* converts the binary values to their decimal equivalents with their signs,
* calculates the average and effective (rms) values of the both voltage and current data,
* determines the absolute peak value of the both voltage and current data,
* plots the voltage, current and instantaneous power as a function of time, separately, but in the same plot window .
* writes the decimal values with their signs in another file named powdata.txt with a similar table format.
