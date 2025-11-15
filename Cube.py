# this the cube emulation biatch

class Piece:
    def __init__(self, pos, ori):
        self.pos = pos  # position - where the piece is
        self.ori = ori  # orientation - how the piece is rotated

    def move(self, pos, ori):
        self.pos = pos # new pos
        self.ori = ori # new ori

# cube is held with green in front and white on top
# piece number starts at 0 with wbo corner and goes across from l to r when solved

# position is equal to the pieces number when solved, otherwise correlating to where the piece is on the cube

# corner orientation is 0 when the w or y face of the piece is on the w or y face of the cube
    # from there orientation is the number of clockwise rotations from 0

# edge orientation is 0 when one or more of the faces of the piece is on the same or opposite face of the cube
    # otherwise orientation is 1

class Cube:
    def __init__(self):
        self.pieces = [Piece(n, 0) for n in range(20)]
        # creates a list of pieces with three values: the piece number, position, and orientation
        print("cube formed")

    # find what piece is in a certain position
    def find_piece(self, pos):
        for i in self.pieces:
            if i.pos == pos:
                return i
        return None

    def flip_check(self, piece, axis):
        if axis == "X": # R/L
            if piece == self.pieces[1] or piece == self.pieces[6] or piece == self.pieces[13] or piece == self.pieces[18]:
                if piece.ori == 1:
                    return 0
                else:
                    return 1
            else:
                return piece.ori
        elif axis == "Y": # U/D
            if piece == self.pieces[8] or piece == self.pieces[9] or piece == self.pieces[10] or piece == self.pieces[11]:
                if piece.ori == 1:
                    return 0
                else:
                    return 1
            else:
                return piece.ori
        elif axis == "Z": # F/B
            if piece == self.pieces[3] or piece == self.pieces[4] or piece == self.pieces[15] or piece == self.pieces[16]:
                if piece.ori == 1:
                    return 0
                else:
                    return 1
            else:
                return piece.ori
        return None

    def run_slice(self, string):
        for i in string.split(" "):
            self.turn(i)

    def turn(self, side):
        match side:
            # Right side
            case "R": # moving pos {2c 4e 7c 9e 11e 14c 16e 19c} -> {14c 9e 2c 16e 4e 19c 11e 7c}
                moving = [self.find_piece(n) for n in [2, 4, 7, 9, 11, 14, 16, 19]]
                to = [14, 9, 2, 16, 4, 19, 11, 7]
                axis = "X"

                moving[0].move(to[0], moving[0].ori - 1) # 2 -> 10
                moving[1].move(to[1], self.flip_check(moving[1], axis)) # 5 -> 9
                moving[2].move(to[2], moving[2].ori + 1) # 7 -> 2
                moving[3].move(to[3], self.flip_check(moving[3], axis)) # 9 -> 16
                moving[4].move(to[4], self.flip_check(moving[4], axis)) # 11 -> 5
                moving[5].move(to[5], moving[5].ori + 1) # 14 -> 19
                moving[6].move(to[6], self.flip_check(moving[6], axis)) # 16 -> 11
                moving[7].move(to[7], moving[7].ori - 1) # 19 -> 7

            case "R'":  # moving pos {2c 5e 8c 11e 16e 19c 22e 25c} -> {8c 16e 25c 5e 22e 2c 11e 19c}
                moving = list(self.find_piece(n) for n in [2, 4, 7, 9, 11, 14, 16, 19])
                to = [7, 11, 19, 4, 16, 2, 9, 14]
                axis = "X"

                moving[0].move(to[0], moving[0].ori - 1)  # 2 -> 7
                moving[1].move(to[1], self.flip_check(moving[1], axis))  # 5 -> 11
                moving[2].move(to[2], moving[2].ori + 1)  # 7 -> 19
                moving[3].move(to[3], self.flip_check(moving[3], axis))  # 9 -> 5
                moving[4].move(to[4], self.flip_check(moving[4], axis))  # 11 -> 16
                moving[5].move(to[5], moving[5].ori + 1)  # 14 -> 2
                moving[6].move(to[6], self.flip_check(moving[6], axis))  # 16 -> 9
                moving[7].move(to[7], moving[7].ori - 1)  # 19 -> 14

            case "R2":  # moving pos {2c 5e 8c 11e 16e 19c 22e 25c} -> {25c 22e 19c 16e 11e 8c 5e 2c}
                moving = list(self.find_piece(n) for n in [2, 4, 7, 9, 11, 14, 16, 19])
                to = [19, 16, 14, 11, 9, 7, 4, 2]

                moving[0].move(to[0], moving[0].ori)  # 2 -> 19
                moving[1].move(to[1], moving[1].ori)  # 5 -> 16
                moving[2].move(to[2], moving[2].ori)  # 7 -> 14
                moving[3].move(to[3], moving[3].ori)  # 9 -> 11
                moving[4].move(to[4], moving[4].ori)  # 11 -> 9
                moving[5].move(to[5], moving[5].ori)  # 14 -> 7
                moving[6].move(to[6], moving[6].ori)  # 16 -> 5
                moving[7].move(to[7], moving[7].ori)  # 19 -> 2

            # Left Side
            case "L":
                moving = list(self.find_piece(n) for n in [0, 3, 5, 8, 10, 12, 15, 17])
                to = [5, 10, 17, 3, 15, 0, 8, 12]
                axis = "X"

                moving[0].move(to[0], moving[0].ori + 1)
                moving[1].move(to[1], self.flip_check(moving[1], axis))
                moving[2].move(to[2], moving[2].ori - 1)
                moving[3].move(to[3], self.flip_check(moving[3], axis))
                moving[4].move(to[4], self.flip_check(moving[4], axis))
                moving[5].move(to[5], moving[5].ori - 1)
                moving[6].move(to[6], self.flip_check(moving[6], axis))
                moving[7].move(to[7], moving[7].ori + 1)

            case "L'":
                moving = list(self.find_piece(n) for n in [0, 3, 5, 8, 10, 12, 15, 17])
                to = [12, 8, 0, 15, 3, 17, 10, 5]
                axis = "X"

                moving[0].move(to[0], moving[0].ori + 1)
                moving[1].move(to[1], self.flip_check(moving[1], axis))
                moving[2].move(to[2], moving[2].ori - 1)
                moving[3].move(to[3], self.flip_check(moving[3], axis))
                moving[4].move(to[4], self.flip_check(moving[4], axis))
                moving[5].move(to[5], moving[5].ori - 1)
                moving[6].move(to[6], self.flip_check(moving[6], axis))
                moving[7].move(to[7], moving[7].ori + 1)

            case "L2":
                moving = list(self.find_piece(n) for n in [0, 3, 5, 8, 10, 12, 15, 17])
                to = [17, 15, 12, 10, 8, 5, 3, 0]

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], moving[1].ori)
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], moving[3].ori)
                moving[4].move(to[4], moving[4].ori)
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], moving[6].ori)
                moving[7].move(to[7], moving[7].ori)

            # Front Side
            case "F":
                moving = list(self.find_piece(n) for n in [5, 6, 7, 10, 11, 17, 18, 19])
                to = [7, 11, 19, 6, 18, 5, 10, 17]
                axis = "Z"

                moving[0].move(to[0], moving[0].ori + 1)
                moving[1].move(to[1], self.flip_check(moving[1], axis))
                moving[2].move(to[2], moving[2].ori - 1)
                moving[3].move(to[3], self.flip_check(moving[3], axis))
                moving[4].move(to[4], self.flip_check(moving[4], axis))
                moving[5].move(to[5], moving[5].ori - 1)
                moving[6].move(to[6], self.flip_check(moving[6], axis))
                moving[7].move(to[7], moving[7].ori + 1)

            case "F'":
                moving = list(self.find_piece(n) for n in [5, 6, 7, 10, 11, 17, 18, 19])
                to = [17, 10, 5, 18, 6, 19, 11, 7]
                axis = "Z"

                moving[0].move(to[0], moving[0].ori + 1)
                moving[1].move(to[1], self.flip_check(moving[1], axis))
                moving[2].move(to[2], moving[2].ori - 1)
                moving[3].move(to[3], self.flip_check(moving[3], axis))
                moving[4].move(to[4], self.flip_check(moving[4], axis))
                moving[5].move(to[5], moving[5].ori - 1)
                moving[6].move(to[6], self.flip_check(moving[6], axis))
                moving[7].move(to[7], moving[7].ori + 1)

            case "F2":
                moving = list(self.find_piece(n) for n in [5, 6, 7, 10, 11, 17, 18, 19])
                to = [19, 18, 17, 11, 10, 7, 6, 5]

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], moving[1].ori)
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], moving[3].ori)
                moving[4].move(to[4], moving[4].ori)
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], moving[6].ori)
                moving[7].move(to[7], moving[7].ori)

            # Back Side
            case "B":
                moving = list(self.find_piece(n) for n in [0, 1, 2, 8, 9, 12, 13, 14])
                to = [12, 8, 0, 13, 1, 14, 9, 2]
                axis = "Z"

                moving[0].move(to[0], moving[0].ori - 1)
                moving[1].move(to[1], self.flip_check(moving[1], axis))
                moving[2].move(to[2], moving[2].ori + 1)
                moving[3].move(to[3], self.flip_check(moving[3], axis))
                moving[4].move(to[4], self.flip_check(moving[4], axis))
                moving[5].move(to[5], moving[5].ori + 1)
                moving[6].move(to[6], self.flip_check(moving[6], axis))
                moving[7].move(to[7], moving[7].ori - 1)

            case "B'":
                moving = list(self.find_piece(n) for n in [0, 1, 2, 8, 9, 12, 13, 14])
                to = [2, 9, 14, 1, 13, 0, 8, 12]
                axis = "Z"

                moving[0].move(to[0], moving[0].ori - 1)
                moving[1].move(to[1], self.flip_check(moving[1], axis))
                moving[2].move(to[2], moving[2].ori + 1)
                moving[3].move(to[3], self.flip_check(moving[3], axis))
                moving[4].move(to[4], self.flip_check(moving[4], axis))
                moving[5].move(to[5], moving[5].ori + 1)
                moving[6].move(to[6], self.flip_check(moving[6], axis))
                moving[7].move(to[7], moving[7].ori - 1)

            case "B2":
                moving = list(self.find_piece(n) for n in [0, 1, 2, 8, 9, 12, 13, 14])
                to = [14, 13, 12, 9, 8, 2, 1, 0]

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], moving[1].ori)
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], moving[3].ori)
                moving[4].move(to[4], moving[4].ori)
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], moving[6].ori)
                moving[7].move(to[7], moving[7].ori)

            # Up Side
            case "U":
                moving = list(self.find_piece(n) for n in [0, 1, 2,
                                                           3, 4,
                                                           5, 6, 7])
                to = [2, 4, 7, 1, 6, 0, 3, 5]
                axis = "Y"

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], self.flip_check(moving[1], axis))
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], self.flip_check(moving[3], axis))
                moving[4].move(to[4], self.flip_check(moving[4], axis))
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], self.flip_check(moving[6], axis))
                moving[7].move(to[7], moving[7].ori)

            case "U'":
                moving = list(self.find_piece(n) for n in [0, 1, 2, 3, 4, 5, 6, 7])
                to = [5, 3, 0, 6, 1, 7, 4, 2]
                axis = "Y"

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], self.flip_check(moving[1], axis))
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], self.flip_check(moving[3], axis))
                moving[4].move(to[4], self.flip_check(moving[4], axis))
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], self.flip_check(moving[6], axis))
                moving[7].move(to[7], moving[7].ori)

            case "U2":
                moving = list(self.find_piece(n) for n in [0, 1, 2, 3, 4, 5, 6, 7])
                to = [7, 6, 5, 4, 3, 2, 1, 0]

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], moving[1].ori)
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], moving[3].ori)
                moving[4].move(to[4], moving[4].ori)
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], moving[6].ori)
                moving[7].move(to[7], moving[7].ori)

            # Down Side
            case "D":
                moving = list(self.find_piece(n) for n in [12, 13, 14, 15, 16, 17, 18, 19])
                to = [17, 15, 12, 18, 13, 19, 16, 14]
                axis = "Y"

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], self.flip_check(moving[1], axis))
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], self.flip_check(moving[3], axis))
                moving[4].move(to[4], self.flip_check(moving[4], axis))
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], self.flip_check(moving[6], axis))
                moving[7].move(to[7], moving[7].ori)

            case "D'":
                moving = list(self.find_piece(n) for n in [12, 13, 14, 15, 16, 17, 18, 19])
                to = [14, 16, 19, 13, 18, 12, 15, 17]
                axis = "Y"

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], self.flip_check(moving[1], axis))
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], self.flip_check(moving[3], axis))
                moving[4].move(to[4], self.flip_check(moving[4], axis))
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], self.flip_check(moving[6], axis))
                moving[7].move(to[7], moving[7].ori)

            case "D2":
                moving = list(self.find_piece(n) for n in [12, 13, 14, 15, 16, 17, 18, 19])
                to = [19, 18, 17, 16, 15, 14, 13, 12]

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], moving[1].ori)
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], moving[3].ori)
                moving[4].move(to[4], moving[4].ori)
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], moving[6].ori)
                moving[7].move(to[7], moving[7].ori)
        for i in self.pieces:
            while i.ori < 0:
                i.ori += 3
            while i.ori > 2:
                i.ori -= 3
