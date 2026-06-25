def get_signal(price, ema50, ema200, rsi, structure):

    score = 0
    reasons = []

    # EMA Trend
    if ema50 > ema200:
        score += 30
        reasons.append("EMA 50 above EMA 200")
    else:
        score -= 30
        reasons.append("EMA 50 below EMA 200")

    # Price Position
    if price > ema50:
        score += 20
        reasons.append("Price above EMA 50")
    else:
        score -= 20
        reasons.append("Price below EMA 50")

    # Market Structure
    if structure == "BULLISH":
        score += 30
        reasons.append("Bullish market structure")
    elif structure == "BEARISH":
        score -= 30
        reasons.append("Bearish market structure")

    # RSI
    if rsi < 30:
        score += 20
        reasons.append("RSI oversold")
    elif rsi > 70:
        score -= 20
        reasons.append("RSI overbought")
    else:
        reasons.append("RSI neutral")

    confidence = min(abs(score), 100)

    if score >= 40:
        signal = "BUY"
    elif score <= -40:
        signal = "SELL"
    else:
        signal = "WAIT"

    return signal, confidence, reasons