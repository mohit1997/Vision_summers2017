import csv
print "'Accelerometer X',	'ACCELEROMETER Y' ,	'ACCELEROMETER Z' ,	'GRAVITY X',	'GRAVITY Y',	'GRAVITY Z',	'LINEAR ACCELERATION X',	'LINEAR ACCELERATION Y',	'LINEAR ACCELERATION Z',	'GYROSCOPE X',	'GYROSCOPE Y',	'GYROSCOPE Z',	'LIGHT',	'MAGNETIC FIELD X',	'MAGNETIC FIELD Y',	'MAGNETIC FIELD Z',	'ORIENTATION Z', 'ORIENTATION X', 'ORIENTATION Y',	'PROXIMITY' ,	'SOUND LEVEL' ,	'LOCATION Latitude' , 	'LOCATION Longitude', 	'LOCATION Altitude',	'LOCATION Altitude-google',	'LOCATION Speed',	'LOCATION Accuracy',	'LOCATION ORIENTATION',	'Satellites in range'	,'Time since start in ms' ,	'YYYY-MO-DD HH-MI-SS_SSS'"
#length = input('type values you want to print on video seperated by semicolon:')

##################################INPUT START Time
initHH = int(input("Initail HH:"))
initMM = int(input("Initial MM:"))
initSS = int(input("Initial SS:"))
initMS = int(input("Initial MS:"))

####################################33

print 'put the index of the values that we\'ll need on frames'
select = raw_input().split(",")
data = []
for ind in range(0,len(select)):
    data.append([])
print data
with open('readings.csv') as csvfile:
    reader = csv.reader(csvfile)
    index = 0
    for row in reader:
        if index==0:
            index = index+1
            continue
        else:
            temp = row[0].split(';')
            i = 0
            for val in select:
                data[i].append(temp[int(val)-1])
                i = i+1
print data
######################################################################################
timestamp = []
with open('readings.csv') as csvfile:
    reader = csv.reader(csvfile)
    index = 0
    for row in reader:
        if index==0:
            index = index+1
            continue
        else:
            temp = row[0].split(';')
            timestamp.append(temp[31-1])

print timestamp[1]
modstamp = []
index = 0
temp = len(timestamp[1])
for item in timestamp[2:]:
    modstamp.append(item[temp-12:])
    index = index+1

print modstamp[0]

HH=[]
MM=[]
SS=[]
MS=[]

for item in modstamp:
    HH.append(int(item[0:2]))
    MM.append(int(item[3:5]))
    SS.append(int(item[6:8]))
    MS.append(int(item[9:12]))
#print HH[0]

initailtimeelpased = (initHH*3600*1000+initMM*60*1000+initSS*1000+initMS)-(int(HH[0])*3600*1000+int(MM[0])*60*1000+int(SS[0])*1000+int(MS[0]))
##################### MODIFYING THE FINAL STAMPS
time_ms = []
with open('readings.csv') as csvfile:
    reader = csv.reader(csvfile)
    index = 0
    for row in reader:
        if index==0:
            index = index+1
            continue
        else:
            temp = row[0].split(';')
            time_ms.append((temp[30-1]))
time_ms = time_ms[1:]
print (time_ms[0])
time_ms = map(int, time_ms)
time_ms[:] = [x - initailtimeelpased for x in time_ms]
HH[:] = [x/3600/1000 for x in time_ms]
MM[:] = [(x/1000/60)%60  for x in time_ms]
SS[:] = [(x/1000)%60  for x in time_ms]
MS[:] = [(x)%1000 for x in time_ms]

print time_ms
#######################################################################################3
subtitle_object = open('clip.srt', 'w')
index = 1
metadata = data[1:]
a = 0
b = 0
for a in range(len(data[1])-1):
    if a ==0:
        continue
    if a>=2:
        if HH[a-2]<0 or MM[a-2]<0 or SS[a-2]<0 or MS[a-2]<0 :
            continue
        subtitle_object.write(str(index)+'\n')
        index = index+1
        subtitle_object.write(str(HH[a-2])+':'+str(MM[a-2])+':'+str(SS[a-2])+','+str(MS[a-2])+' --> '+str(HH[a-1])+':'+str(MM[a-1])+':'+str(SS[a-1])+','+str(MS[a-1])+'\n')
        for b in range(len(data)):
            subtitle_object.write(data[b][0]+":"+data[b][a])
            subtitle_object.write('\t')
    subtitle_object.write('\n\n')

subtitle_object.close
#Note: Time stamps are at no. 31. At 30 time is in milli seconds.
