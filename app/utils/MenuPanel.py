class MenuPanel:
    def draw(self, width, height, lines):
        border = '='
        rows_to_draw = height - 2
        columns_to_draw = width - 2

        first_line = [ border * width ]
        last_line = [ border * width ]

        middle_lines = [
            border + l.center(columns_to_draw, ' ') + border
            for l in lines[:rows_to_draw]
        ]
        num_lines = len(middle_lines)

        if num_lines < rows_to_draw:
            remainder = rows_to_draw - num_lines
            padding_amount = remainder // 2
            padding_remainder = remainder - 2 * padding_amount
            padding_line = [ border + ' ' * columns_to_draw + border ]
            top_padding = padding_line * padding_amount
            bottom_padding = padding_line * (padding_amount + padding_remainder)
            middle_lines = top_padding + middle_lines + bottom_padding

        return first_line + middle_lines + last_line
