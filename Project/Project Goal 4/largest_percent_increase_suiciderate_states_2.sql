with cleaned_data AS (
	select
		YEAR AS Year,
		STATE AS State,
		DEATHS AS DeathCount,
		lag(DEATHS, 1, 0) over(partition by state order by Year asc) AS PrevYearDeathCount
	from dbo.suicide_mortality_by_state
	where Year >= 2010
)

select
	State,
	PrevYearDeathCount as nineteen_rate,
	DeathCount as twenty_rate,
	round(100.0 * (DeathCount - PrevYearDeathCount) / PrevYearDeathCount, 2) AS percent_change
from cleaned_data
where Year = 2020
order by percent_change desc;