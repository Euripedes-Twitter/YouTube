CREATE VIEW vw_youtube as

SELECT 
	video_id, 
	trending_date, 
	channel_title, 
	publish_date, 
	views, 
	likes, 
	dislikes, 
	comment_count, 
	cr.country_region_code, 
	split_part(twitter_profile,'\n',1) as twitter_profile,
	category_title
	FROM public.all_countries_regions cr
	LEFT JOIN public.category ct ON cr.category_id = ct.category_id;