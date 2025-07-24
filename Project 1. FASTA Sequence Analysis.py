sequence = ""

with open ('sequence.fasta', 'r') as file:
    for line in file:
        if not line.startswith('>'): # 그 줄이 '>'로 시작하지 않는다면 실행
            sequence += line.strip().upper()
print(sequence)
g_count = sequence.count('G')
c_count = sequence.count('C')

total = len(sequence)
gc = g_count + c_count
gc_percent = (gc/total) * 100

print('Total number of bases:',total)
print('Number of G bases:',g_count)
print('Number of C bases:',c_count)
print('GC content:',round(gc_percent,2),'%')
