
drop table if exists music_recommend;

create table music_recommend(
							id integer primary key,
							name text not null,
							singer text);


