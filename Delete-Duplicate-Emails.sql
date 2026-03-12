1# Write your MySQL query statement below
2
3DELETE P1 FROM person P1, person P2 WHERE P1.email = P2.email AND P1.id > P2.id;