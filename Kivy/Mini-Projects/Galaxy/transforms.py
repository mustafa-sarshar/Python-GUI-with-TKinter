def transform(self, x, y):
    # return self._transform_2D(x, y)
    # return self._transform_perspective(x, y)
    return self.transform_perspective_attraction_based(x, y)

def transform_2D(self, x, y):
    return int(x), int(y)

def transform_perspective(self, x, y):
    trans_y = y * self.perspective_point_y / self.height
    if trans_y > self.perspective_point_y:
        trans_y = self.perspective_point_y

    diff_x = x - self.perspective_point_x
    diff_y = self.perspective_point_y - trans_y
    proportion_y = diff_y/self.perspective_point_y # is 1 when diff_y == self.perspective_point_y OR is 0 when y == 0

    trans_x = self.perspective_point_x + diff_x * proportion_y
    return int(trans_x), int(trans_y)

def transform_perspective_attraction_based(self, x, y):
    linear_y = y * self.perspective_point_y / self.height
    if linear_y > self.perspective_point_y:
        linear_y = self.perspective_point_y

    diff_x = x - self.perspective_point_x
    diff_y = self.perspective_point_y - linear_y
    factor_y = diff_y/self.perspective_point_y # is 1 when diff_y == self.perspective_point_y OR is 0 when y == 0
    factor_y = factor_y * factor_y

    trans_x = self.perspective_point_x + diff_x * factor_y
    trans_y = self.perspective_point_y - factor_y * self.perspective_point_y # equal to -> trans_y = (1-factor_y) * self.perspective_point_y)
    return int(trans_x), int(trans_y)
