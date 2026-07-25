class FogProcessor:
    def calculate_score(self, payload):

        score = 0
        # CPU
        if payload["cpu"] > 90:
            score += 20

        # Memory
        if payload["memory"] > 90:
            score += 20

        # Temperature
        if payload["temperature"] > 80:
            score += 25

        # Network
        if payload["network"] > 1500:
            score += 20

        # Power
        if payload["power"] > 500:
            score += 15

        return score


    def severity(self, score):

        if score >= 60:
            return "HIGH"

        elif score >= 30:
            return "MEDIUM"

        else:
            return "LOW"


    def recommendation(self, severity):

        if severity == "HIGH":
            return "Immediate inspection required."

        elif severity == "MEDIUM":
            return "Monitor machine closely."

        else:
            return "No action required."