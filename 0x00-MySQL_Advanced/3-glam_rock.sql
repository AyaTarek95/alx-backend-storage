-- comment: rank by lifesapn and band_name
SELECT band_name,
IF(split IS NOT NULL, split - formed, 2022 - formed) AS lifespan
FROM metal_bands
WHERE style like %Glam rock%
ORDER BY lifespan DESC, band_name DESC;
