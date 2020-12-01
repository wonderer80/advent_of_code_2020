class Day1:
    def __init__(self, input_file_file_name):
        self.input_file_name = input_file_file_name
        self.input_data = self.read_input_data()

    def read_input_data(self):
        with open(self.input_file_name) as f:
            data = list(map(int, f.read().splitlines()))

        return data

    def expense_report(self, sum_value):
        for idx, current_value in enumerate(self.input_data):
            if current_value >= sum_value:
                continue
            delta = sum_value - current_value

            if delta in self.input_data:
                return current_value * delta

        print('not found!')

    def expense_report2(self, sum_value):
        for idx, current_value in enumerate(self.input_data):
            if current_value >= sum_value:
                continue
            delta = sum_value - current_value

            for idx2, current_value2 in enumerate(self.input_data[idx+1:]):
                if current_value2 >= delta:
                    continue
                delta2 = delta - current_value2

                if delta2 in self.input_data:
                    return current_value * current_value2 * delta2

        print('not found!')
