__author__ = 'Richard L. Sweat Jr.'


class CodeHandler:
    def __init__(self):
        self.in_comment = False
        self.comment_open = '('
        self.comment_close = ')'

    def process_line(self, line, index):
        for c in line:
            if c == self.comment_open:
                if self.in_comment:
                    raise ValueError('You have nested Comments: Line: {}:{}'.format(index, line))
                else:
                    self.in_comment = True
                    continue
            elif c == self.comment_close:
                if self.in_comment:
                    self.in_comment = False
                    continue
                else:
                    raise ValueError('You tried to close an un-opened comment: Line: {}:{}'.format(index, line))
            else:
                continue
