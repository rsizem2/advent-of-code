# Monstrosity
import numpy as np
from itertools import combinations, permutations, product

def read_file(test = True):
    if test:
        filename = '../tests/day19.txt'
    else:
        filename = '../input/day19.txt'
    with open(filename) as file:
        scanners = list()
        for line in file:
            if '--' in line:
                temp = list()
            elif ',' in line:
                temp.append(np.array(list(map(int,line.split(',')))))
            else:
                scanners.append(temp)
        scanners.append(temp)
    return scanners

def orientations():
    for a,b,c in permutations([0,1,2]):
        for i,j,k in product([1,-1],repeat = 3):
            yield lambda x: np.array([x[a]*i, x[b]*j, x[c]*k])
            
def offset(triple1, triple2):
    return triple1 - triple2

def transformation(triple1, triple2, points):
    x,y,z = triple1
    found = False
    for orient in orientations():
        for (i,u),(j,v),(k,w) in permutations(enumerate(triple2)):
            u,v,w = map(orient, [u,v,w])
            if not np.array_equal(x-y, u-v):
                continue
            if not np.array_equal(y-z, v-w):
                continue
            if not np.array_equal(z-x, w-u):
                continue
            found = True
            break
        if found: break
        
    # transforming the remaining points
    dist = offset(x, u)
    new = list()
    
    for point in points:
        new.append(orient(point))
    for i in range(len(new)):
        new[i] += dist

    return new, dist

def puzzle1(test = True):
    scanners = read_file(test)
    
    # We use triples of beacons to identify overlaps
    triangles = dict()
    indices = dict()
    
    # data structures for storing scanners
    unseen = set()
    seen = set()
    
    # calculating triples of beacons for each 
    for num, scanner in enumerate(scanners):
        unseen.add(num)
        temp_triples = set()
        temp_indices = dict()
        # for each triangle of beacons with a scanners range, sort the "taxicab" length for each edge
        for (i,x),(j,y),(k,z) in combinations(enumerate(scanner),3):
            key = tuple(sorted(map(int,[np.sum(np.abs(x-y)),np.sum(np.abs(y-z)),np.sum(np.abs(z-x))])))
            temp_triples.add(key)
            temp_indices[key] = (i,j,k)
        triangles[num] = temp_triples
        indices[num] = temp_indices
        
    
    # choose arbitrary scanner as reference point
    reference = unseen.pop()
    seen.add(reference)
    
    # store coords relative to reference point
    beacons = {reference: scanners[reference]}
    
    # while there are scanners not converted to reference frame
    while unseen:
        found = False
        for i in seen:
            for j in unseen:
                overlap = triangles[i] & triangles[j]
                if len(overlap) > 200:
                    found = True
                if found: break
            if found: break
        #print(i,j, len(overlap))
        key = overlap.pop()
        # Use overlapping triangles to convert
        beacons[j] = transformation(
            [beacons[i][x] for x in indices[i][key]],
            [scanners[j][x] for x in indices[j][key]],
            scanners[j]
            )[0]
        seen.add(j)
        unseen.remove(j)
    unique_beacons = set()
    for num in seen:
        for point in map(tuple, beacons[num]):
            unique_beacons.add(point)
    print(len(unique_beacons))
                
                

def puzzle2(test = True):
    scanners = read_file(test)
    
    # We use triples of beacons to identify overlaps
    triangles = dict()
    indices = dict()
    
    # data structures for storing scanners
    unseen = set()
    seen = set()
    
    # calculating triples of beacons for each 
    for num, scanner in enumerate(scanners):
        unseen.add(num)
        temp_triples = set()
        temp_indices = dict()
        # for each triangle of beacons with a scanners range, sort the "taxicab" length for each edge
        for (i,x),(j,y),(k,z) in combinations(enumerate(scanner),3):
            key = tuple(sorted(map(int,[np.sum(np.abs(x-y)),np.sum(np.abs(y-z)),np.sum(np.abs(z-x))])))
            temp_triples.add(key)
            temp_indices[key] = (i,j,k)
        triangles[num] = temp_triples
        indices[num] = temp_indices
        
    
    # choose arbitrary scanner as reference point
    reference = unseen.pop()
    seen.add(reference)
    
    # store coords relative to reference point
    beacons = {reference: scanners[reference]}
    locations = {reference: np.array([0,0,0])}
    
    # while there are scanners not converted to reference frame
    while unseen:
        found = False
        for i in seen:
            for j in unseen:
                overlap = triangles[i] & triangles[j]
                if len(overlap) > 200:
                    found = True
                if found: break
            if found: break
        #print(i,j, len(overlap))
        key = overlap.pop()
        # Use overlapping triangles to convert
        beacons[j], dist = transformation(
            [beacons[i][x] for x in indices[i][key]],
            [scanners[j][x] for x in indices[j][key]],
            scanners[j]
            )
        #print(dist)
        locations[j] = dist
        #print(locations[j])
        seen.add(j)
        unseen.remove(j)
    unique_beacons = set()
    for num in seen:
        for point in map(tuple, beacons[num]):
            unique_beacons.add(point)
    for x,y in combinations(locations.values(),2):
        pass
        #print(x,y)
    print(max(np.sum(np.abs(x-y)) for x,y in combinations(locations.values(),2) ))


puzzle1(False)
puzzle2(False)
