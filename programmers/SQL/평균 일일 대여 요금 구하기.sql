SELECT ROUND(AVG(DAILY_FEE),0) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
GROUP BY CAR_TYPE
HAVING CAR_TYPE = 'SUV'
-- 그룹핑하면 자동으로 daily_fee합쳐짐, round함수(,*) *값 + 1 반올림할 자리