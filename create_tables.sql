CREATE TABLE category (
	category_id	VARCHAR(50),
	category_title	VARCHAR(50),
	assignable	BOOLEAN,
	country_region_code VARCHAR(50)
);

CREATE TABLE all_countries_regions (
	video_id VARCHAR(50),
	trending_date DATE,
	title VARCHAR(250),
	channel_title VARCHAR(250),
	publish_date DATE,
	category_id VARCHAR(50),
	publish_time DATE,
	tags VARCHAR(250),
	views INT,
	likes INT,
	dislikes INT,
	comment_count INT,
	thumbnail_link VARCHAR(50),
	comments_disabled BOOLEAN,
	ratings_disabled BOOLEAN,
	video_error_or_removed BOOLEAN,
	description VARCHAR(2500),
	country_region_code VARCHAR(50),
	check_twitter BOOLEAN,
	twitter_profile VARCHAR(50)
)


