class DataAnalyzer:

    def __init__(self, good_posture_data):
        self.good_posture_data = good_posture_data

    def analyzeNewData(self, data):
        delta_y = data['top'] - self.good_posture_data['top']
        delta_x = data['left'] - self.good_posture_data['left']

        if abs(delta_x) > 10 or delta_y < 10:
            return True

        else:
            return False