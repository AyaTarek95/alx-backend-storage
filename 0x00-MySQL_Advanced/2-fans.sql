-- comment: group by origin and order by rank
SELECT origin, SUM(fans) AS nb_fans
from metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
