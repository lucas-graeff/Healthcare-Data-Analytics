with cleaned_data as (
	select 
		case 
		when "State / [Region]" like '%]' 
		then LEFT("State / [Region]", CHARINDEX('[',"State / [Region]") - 1) 
		else "State / [Region]" 
	end AS State,
	ROUND([2010], 2) AS ten_rate,
	ROUND([2011], 2) AS eleven_rate,
	ROUND([2012], 2) AS twelve_rate,
	ROUND([2013], 2) AS thirteen_rate,
	ROUND([2014], 2) AS fourteen_rate,
	ROUND([2015], 2) AS fifteen_rate,
	ROUND([2016], 2) AS sixteen_rate,
	ROUND([2017], 2) AS seventeen_rate,
	ROUND([2018], 2) AS eighteen_rate,
	ROUND([2019], 2) AS nineteen_rate,
	ROUND([2020], 2) AS twenty_rate
	from [dbo].[suicide_mortality_by_state_yearly]
	where "State / [Region]" not like 'Compiled%'
),

state_rankings as (
	select 
	* 
	from dbo.covid_lockdown_severity_rankings_states
)

select 
	c.State,
	cast(nineteen_rate as float) as nineteen_rate,
	cast(twenty_rate as float) as twenty_rate,
	cast(round(100.0 * (twenty_rate - nineteen_rate) / nineteen_rate, 2) as float) as percent_change,
	cast(s.rank as int) as rank,
	cast(s.rank as int) * -1 as pbi_rank
from cleaned_data as c
join state_rankings as s on c.State = s.state
order by rank asc, percent_change desc;