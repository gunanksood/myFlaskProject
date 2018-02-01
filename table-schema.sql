-- sqlite3 content_table.db < table-schema.sql

drop table if exists content_table;
create table content_table (
  id integer primary key autoincrement,
  title text not null,
  content_text text not null
);