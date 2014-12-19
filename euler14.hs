{- Run with:
let lst = map (etup) [eseq x | x<-[1..1000000]]
foldl (emax) (head lst) (tail lst)
-}
eseq :: Int -> [Int]
eseq n
    | n == 1 = [1]
    | n `mod` 2 == 0 = n:(eseq (n `div` 2))
    | otherwise = n:(eseq (3*n + 1))

etup :: [Int]->(Int,Int)
etup l
    = (length l, head l)
emax :: (Int,Int)-> (Int,Int) -> (Int,Int)
emax a b
    | fst a > fst b = a
    | otherwise = b