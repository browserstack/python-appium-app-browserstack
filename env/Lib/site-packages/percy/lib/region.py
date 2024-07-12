class Region:
    def __init__(self, top, bottom, left, right):
        if top < 0 or bottom < 0 or left < 0 or right < 0:
            raise ValueError('Only Positive integer is allowed!')

        if top >= bottom or left >= right:
            raise ValueError('Invalid ignore region parameters!')

        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    def is_valid(self, screen_height, screen_width):
        if self.top >= screen_height or self.bottom > screen_height or self.left >= screen_width or self.right > screen_width:
            return False

        return True
