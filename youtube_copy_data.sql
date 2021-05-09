COPY category
FROM 'D:/Twitter/archive/all_countries_category.csv'
CSV HEADER DELIMITER ',';

COPY public.all_countries_regions
FROM 'D:/Twitter/archive/all_countries_data.csv'
CSV HEADER DELIMITER ',';