select 
	case 
		when "State / [Region]" like '%]' 
		then LEFT("State / [Region]", CHARINDEX('[',"State / [Region]") - 1) 
		else "State / [Region]" 
	end AS State,
	ROUND([2010], 2) AS '2010',
	ROUND([2011], 2) AS '2011',
	ROUND([2012], 2) AS '2012',
	ROUND([2013], 2) AS '2013',
	ROUND([2014], 2) AS '2014',
	ROUND([2015], 2) AS '2015',
	ROUND([2016], 2) AS '2016',
	ROUND([2017], 2) AS '2017',
	ROUND([2018], 2) AS '2018',
	ROUND([2019], 2) AS '2019',
	ROUND([2020], 2) AS '2020'
from [dbo].[suicide_mortality_by_state_yearly]
where "State / [Region]" not like 'Compiled%'