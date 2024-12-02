# Advent of Code 2024
# Day 01 - https://adventofcode.com/2024/day/1
# Jeff Tillinghast

from collections import Counter

def sort_input():
    left, right = [], []
    with open("input.txt") as f:
        for line in f:
            values = line.split("   ");
            left.append(int(values[0]))
            right.append(int(values[1]))

    left.sort()
    right.sort()
    return left, right

def distance(left, right):
    distance_total = 0
    for i in range(len(left)):
        distance_total += abs(left[i] - right [i])

    return distance_total

def similarity(left, right):
    similarity_score = 0
    for i in range(len(left)):
        similarity_score += (left[i] * right.count(left[i]))
    return similarity_score

left, right = sort_input();

print("Distance: ",str(distance(left,right)))
print("Similarity: ",str(similarity(left,right)))