#j5 - tandem bicycle (2016)

question = int(input())
how_many_pairs = int(input())

raw_dmojistan_speeds = input().split(" ")
raw_pegland_speeds = input().split(" ")

dmojistan_speeds = [int(x) for x in raw_dmojistan_speeds]
pegland_speeds = [int(x) for x in raw_pegland_speeds]

if question == 1:
    dmojistan_speeds.sort()
    pegland_speeds.sort()
    
    total_speed = 0
    for counter in range(how_many_pairs):
        total_speed += max(dmojistan_speeds[counter], pegland_speeds[counter])
    print(total_speed)


elif question == 2:
    dmojistan_speeds.sort()
    pegland_speeds.sort(reverse = True)
    
    total_speed = 0
    for counter in range(how_many_pairs):
        total_speed += max(dmojistan_speeds[counter], pegland_speeds[counter])
    print(total_speed)