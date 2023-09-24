SELECT FLAVOR 
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID

-- 여러개의 ORDER BY 조건 사용 시 앞에서부터 순차적으로 적용(먼저 쓴 정렬 적용, 만약 같은 조건일 경우 이후 쓴 정렬 적용)