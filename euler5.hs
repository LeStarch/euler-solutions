{-
Run with:
foldl elcm 1 [1..20]
for the solution.
-}

egcd :: Int -> Int -> Int
egcd x y
    | y == 0 = x
    | otherwise = gcd y (x `mod` y) 
elcm :: Int -> Int -> Int
elcm x y
    = x * y `div` (egcd x y) 