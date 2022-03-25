with cleaned_data as
(select 
	ParentLocationCode AS RegionCode,
	ParentLocation AS Region,
	SpatialDimValueCode AS CountryCode,
	Location AS Country,
	Period AS Year,
	Dim1 AS Gender,
	Dim2 AS AgeRange,
	ROUND(FactValueNumeric, 2) AS SuicideRate
from dbo.suicide_mortality_by_age_group_and_country)

select
	CountryCode,
	Country,
	Year,
	Gender,
	AgeRange,
	SuicideRate
from cleaned_data
where Gender = 'Both sexes'
order by SuicideRate desc, RegionCode asc, AgeRange asc