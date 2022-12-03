from __future__ import annotations
from dataclasses import dataclass
from pprint import pprint
from operator import mul
from functools import reduce

with open("Day16.txt", "r") as file:
    data = file.read()


@dataclass
class Packet:
    version: int
    type_id: int


@dataclass
class Literal(Packet):
    value: int

    def eval(self):
        return self.value


@dataclass
class Operator(Packet):
    packets: list[Literal | Operator]

    def eval(self):
        sub_values = [i.eval() for i in self.packets]
        if self.type_id == 0:
            return sum(sub_values)
        elif self.type_id == 1:
            return reduce(mul, sub_values)
        elif self.type_id == 2:
            return min(sub_values)
        elif self.type_id == 3:
            return max(sub_values)
        elif self.type_id == 5:
            return int(sub_values[0] > sub_values[1])
        elif self.type_id == 6:
            return int(sub_values[0] < sub_values[1])
        elif self.type_id == 7:
            return int(sub_values[0] == sub_values[1])


def parse_packet(index: int, string: str) -> (int, Packet):
    version = int(string[index:index+3], 2)
    type_id = int(string[index+3:index+6], 2)
    index += 6
    if type_id == 4:
        num = 0
        more_data = True
        while more_data:
            more_data = string[index] == '1'
            index += 1
            num <<= 4
            num += int(string[index:index+4], 2)
            index += 4
        return index, Literal(version, type_id, num)
    else:
        length_type = string[index]
        index += 1
        if length_type == '0':
            length = int(string[index:index + 15], 2)
            index += 15
            final_index = index + length
            packets = []
            while index < final_index:
                index, packet = parse_packet(index, string)
                packets.append(packet)
            if index != final_index:
                print("fuck1")
            return index, Operator(version, type_id, packets)
        else:
            num_packets = int(string[index:index+11], 2)
            index += 11
            packets = []
            for _ in range(num_packets):
                index, packet = parse_packet(index, string)
                packets.append(packet)
            return index, Operator(version, type_id, packets)


def sum_versions(packet: Literal | Operator):
    if type(packet) == Literal:
        return packet.version
    elif type(packet) == Operator:
        return sum(map(sum_versions, packet.packets)) + packet.version


binary_string = ''.join(bin(int(i, 16))[2:].zfill(4) for i in data)
final_index, packet = parse_packet(0, binary_string)

print(sum_versions(packet))
print(packet.eval())