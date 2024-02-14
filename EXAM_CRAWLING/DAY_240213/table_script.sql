create database scraping;

use scraping;

# pages 테이블이 존재하면 삭제함
drop table if exists pages;

create table pages (
	id bigint(7) not null auto_increment,
	title varchar(200),
	content varchar(10000),
	created timestamp default current_timestamp,	# 자동으로 현재 시간이 저장됨
	primary key(id)
);

# 테이블 구조 확인
describe pages;

# 데이터 추가
insert into pages(title, content)
values(
"Test page title",
"This is some test page content. It can be up to 10,000 characters long.");

insert into pages(title, content)
values(
	"Second page title",
	"This is the second test page content"
);

# pages 테이블에서 id값이 2인 모든 데이터 가져오기
select * from pages where id = 2;

# title 필드(컬럼)에 "test"를 포함하는 행 반환
select * from pages where title like "%test%";

# 조건에 맞는 id, title, created 필드만 가져오기
select id, title, created from pages where content like "%second%";

# id값이 1인 행 삭제
delete from pages where id=1;

# 전체 pages 테이블 데이터 가져오기
select * from pages;

# 자료 수정 : UPDATE 명령어
update pages 
set title='A new title',
	content='Some new content'
where id=2;
select * from pages;

