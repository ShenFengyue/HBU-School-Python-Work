# 第十六周 Python笔记

数据库

2023-6-4

- 数据的种类
	- 结构化数据（一张二维表可存储）（更容易处理）
	- 非结构化数据（逐渐成为主流）
- 管理数据
	- 关系数据库（管结构化数据）
	- 其它（管非结构化数据）

DBMS (Database Management System) 数据库管理系统：开发数据库应用软件
如：
Microsoft SQL Server  
Microsoft Access

DBS 数据库系统

- 常用的数据库模型
	- 层次模型
	- 网状模型
	- 关系模型 （一对一联系）
	- 面向对象的数据模型

主关键字：用于唯一确定一条记录
姓名不行，因为有重名，但学号可以


创建表及进行操作

建立游标
conn.cursor()

提交
conn.commit()

获取当前游标后的n行数据
ds=res.fetchmany(n)

获取所有数据
ds=res.fatchall()


SQL：结构化查询语言

数据定义语句：

CREATE TABLE 表名(
	列名1 数据类型
	列名2 数据类型
	...
	列名n 数据类型)

删除指定的表：
DROP TABLE 表名 

插入数据：
INSERT INTO (列1，列2...)  VALUES  (值1，值2，值3...)

数据查询
SELECT
FROM
WHERE

修改表中的数据记录
UPDATE 表名 SET 列名=新值.WHERE 条件

删除表中数据
DELETE FROM 表名 WHERE 条件

