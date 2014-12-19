{- Run with:
sum (takeWhile (<4000000) [x | x <- [ fib(p) |p <- [0..]], x `mod` 2 == 0])
-}
fib :: Int -> Int
fib n
    | n == 0 = 0
    | n == 1 = 1
    | otherwise = fib(n-1) + fib(n-2)