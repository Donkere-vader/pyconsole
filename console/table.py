class Table:
    def __init__(self, values: list, column_names=[], row_names=[], borders=None, max_column_width=100, max_row_height=100):
        """ Values should be provided in a array in array format: [[row1 item1, row1 item2], [row2 item1, row2 item 2]]"""
        self.values = values
        self.borders = borders
        self.row_names = row_names
        self.column_names = column_names

    def update_values(self, values):
        self.values = values

    def __repr__(self):
        output = ""

        row_heights = {}
        column_widths = {}

        for i, row_name in enumerate(self.row_names):
            row_name = str(row_name)
            for j, column_name in enumerate(self.column_names):
                column_name = str(column_name)
                if row_name in row_heights:
                    if str(self.values[i][j]).count('\n') > row_heights[row_name]:
                        row_heights[row_name] = str(self.values[i][j]).count('\n')  + 1
                else:
                    row_heights[row_name] = str(self.values[i][j]).count('\n')  + 1
                if column_name in column_widths:
                    if len(str(self.values[i][j])) > column_widths[column_name]:
                        column_widths[column_name] = len(str(self.values[i][j]))  + 1
                else:
                    column_widths[column_name] = len(str(self.values[i][j])) + 1
        
        for column_name in column_widths:
            if column_widths[column_name] < len(str(column_name)):
                column_widths[column_name] = len(str(column_name)) + 1
        
        row_titles_column_width = 0
        for name in self.row_names:
            if len(str(name)) > row_titles_column_width:
                row_titles_column_width = len(str(name)) + 1

        row_seperator = "\n" + "-" * row_titles_column_width + "-"
        for column_name in column_widths:
            row_seperator += "-"*column_widths[column_name] + "-"

        print(" " * row_titles_column_width, end="|")
        for column_name in self.column_names:
            print(column_name.ljust(column_widths[column_name]), end="|")
        print(row_seperator)


        for i, row_name in enumerate(self.row_names):
            row_name = str(row_name)
            print(row_name.ljust(row_titles_column_width), end="|")
            for j, column_name in enumerate(self.column_names):
                print(str(self.values[i][j]).ljust(column_widths[column_name]), end="|")
            
            if i != len(self.row_names) -1:
                print(row_seperator)

        
        return output[:-1]  # remove trailing enter