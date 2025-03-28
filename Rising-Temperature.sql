# Write your MySQL query statement below
-- select w1.id
-- from Weather w1
-- join Weather w2
-- on datediff(w1.recordDate, w2.recordDate) = 1
-- where w1.temperature > w2.temperature;


with weather_data as
(
    select id, recordDate, temperature,
    lag(temperature, 1) over (order by recordDate) as PrevTemp,
    lag(recordDate, 1) over (order by recordDate) as PrevDate
    from Weather
)

select id
from weather_data
where temperature > PrevTemp
and recordDate = DATE_ADD(PrevDate, interval 1 day);