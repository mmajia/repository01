from a创建连接数据库 import cursor,db


#使用execute方法执行SQL，如果表存在则删除
cursor.execute("drop table if exists books")
#使用预处理语句创建表
sql = """
create table books(
    id int(8) not null auto_increment,
    name varchar(50) not null,
    category varchar(50) not null,
    price decimal(10,2) default null,
    publish_time date default null,
    primary key (id)
) engine = myisam auto_increment=1 default charset=utf8
"""
#执行sql语句
cursor.execute(sql)

db.close()