extracted_lines = []
isEstimote = False

f = open('hcidump_read.txt')
lines = f.readlines()
for line in lines:
    if line.startswith('      bdaddr ') and state == 1:
        extracted_lines.append(line.replace('      bdaddr ',''))
        state = 2
    elif 'estimote' in line and state == 2:
        extracted_lines.pop()
        isEstimote = False
        state = 3
    elif line.startswith('      RSSI: ') and isEstimote and state == 3:
        extracted_lines.append(line.replace('      RSSI: ',''))
        state = 1
        

f.close()