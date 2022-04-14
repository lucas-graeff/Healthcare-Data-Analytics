with precleaned_data as (
	select
		State,
		Year,
		Ten_Year_Age_Groups,
		Crude_Rate AS SuicideRate,
		lag(Crude_Rate, 1, 0) over(partition by State order by Year asc) AS PrevYearRate
	from dbo.suicide_by_agegroup_by_state
	where Notes is null
	and Crude_Rate != 'Unreliable'
	and year in ('2019', '2020')
),

cleaned_data as (
	select
		State,
		Year,
		Ten_Year_Age_Groups as age_group,
		cast(PrevYearRate as float) as nineteen_rate,
		cast(SuicideRate as float) as twenty_rate
	from precleaned_data
	where Year = 2020
),

state_rankings as (
	select 
	* 
	from dbo.covid_lockdown_severity_rankings_states
),

joined_tables as (
		select
		c.*,
		round(100.0 * (twenty_rate - nineteen_rate) / nineteen_rate, 2) AS percent_change,
		s.rank
		from cleaned_data as c
	join state_rankings as s on c.State = s.State
)

select
	State,
	Year,
	age_group,
	nineteen_rate,
	twenty_rate,
	percent_change,
	rank as severity_rank,
	round(avg(percent_change) over (partition by age_group), 2) as avg_change_for_agegroup
from joined_tables
order by rank asc, percent_change desc;