class ConversionDecisionEngine:
    """
    Decision layer translating model probability into product action segments.

    This layer represents policy logic — not model logic.
    """

    def __init__(self, high_threshold: float = 0.7, medium_threshold: float = 0.4):
        self.high_threshold = high_threshold
        self.medium_threshold = medium_threshold

    def decide(self, probability: float) -> str:
        if probability >= self.high_threshold:
            return "high_intent"
        elif probability >= self.medium_threshold:
            return "medium_intent"
        return "low_intent"
