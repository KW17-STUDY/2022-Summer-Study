SELECT A.ID, A.NAME, B.HOST_ID
FROM PLACES A JOIN (SELECT HOST_ID
                    FROM PLACES
                    GROUP BY HOST_ID
                    HAVING COUNT(HOST_ID) >= 2
                    ) B
on A.HOST_ID = B.HOST_ID

'''
ID	NAME	HOST_ID
4431977	BOUTIQUE STAYS - Somerset Terrace, Pet Friendly	760849
5194998	BOUTIQUE STAYS - Elwood Beaches 3, Pet Friendly	760849
16045624	Urban Jungle in the Heart of Melbourne	30900122
17810814	Stylish Bayside Retreat with a Luscious Garden	760849
22740286	FREE PARKING - The Velvet Lux in Melbourne CBD	30900122
'''

SELECT *
FROM PLACES
GROUP BY HOST_ID
HAVING COUNT(HOST_ID) >= 2


'''
ID	NAME	HOST_ID
4431977	BOUTIQUE STAYS - Somerset Terrace, Pet Friendly	760849
16045624	Urban Jungle in the Heart of Melbourne	30900122

GROUP BY 사용하면 묶은 그룹에 대해서 HAVING절을 만족하는 데이터 중 맨위의 하나의 데이터만 나온다.
'''