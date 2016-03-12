select count(*)
from tweets
where is_delete = 1;

select count(*)
from tweets
where reply_to <> 0;

select uid
from tweets
where is_delete = 0
group by uid
order by count(*) desc, uid
limit 5;