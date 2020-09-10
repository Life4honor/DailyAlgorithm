// https://www.hackerrank.com/challenges/birthday-cake-candles/problem

func birthdayCakeCandles(candles []int32) int32 {
    count := int32(0)
    tallest := int32(-1)
    for _, candle := range(candles) {
        if candle > tallest {
            tallest = candle
            count = 1
        } else if tallest == candle {
            count += 1
        }
        fmt.Println(candle, tallest, count)
    }
    return count
}
