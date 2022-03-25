select
	YEAR AS Year,
	STATE AS State,
	DEATHS AS DeathCount,
	lag(DEATHS, 1, 0) over(partition by state order by Year asc) AS PrevYearDeathCount
from dbo.suicide_mortality_by_state
where Year >= 2010
order by Year desc, State asc