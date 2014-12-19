{- Run with:
let lst = [show (x*y) | x <- [100..999],y <- [100..999]]
maximum (conv ([g | g <- lst, g == reverse g]))
-}
conv :: [String] -> [Int]
conv = map read