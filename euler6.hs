{- Run with:
esqr (sum [1..100]) - sum (map (esqr) [1..100])
-}
esqr :: Int -> Int
esqr n
    = n * n