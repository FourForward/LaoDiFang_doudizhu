"""
数据库服务端
"""
import pymysql


class Database:
    def __init__(self, database: str, password: str):
        """
        建立数据库连接，并生成游标
        :param database: 数据库名
        """
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password=password,
            database=database,
            charset='utf8'
        )
        self.cur = self.db.cursor()

    def initialize_databese(self):
        """
        数据库初始化第一步，创建三个表（玩家表，场次表，对局表）
        """
        sql1 = 'create table user (' \
               'u_id tinyint unsigned primary key auto_increment,' \
               'u_name varchar(22) not null ,' \
               'all_earnings smallint,' \
               'all_bout smallint unsigned)'
        sql2 = 'create table session(' \
               's_id smallint unsigned primary key auto_increment,' \
               's_name varchar(100),' \
               'begin_time datetime default now(),' \
               'finish_time datetime,' \
               'u1_id tinyint unsigned not null ,' \
               'u2_id tinyint unsigned not null ,' \
               'u3_id tinyint unsigned not null ,' \
               'u4_id tinyint unsigned,' \
               'b_id tinyint unsigned not null )'
        sql3 = 'create table bout1(' \
               'b_id smallint unsigned primary key auto_increment,' \
               's_id smallint not null ,' \
               'u1_earnings tinyint not null ,' \
               'u2_earnings tinyint not null ,' \
               'u3_earnings tinyint not null ,' \
               'u4_earnings tinyint,' \
               'time datetime default now())'
        for i in range(1, 4):
            try:
                self.cur.execute(eval(f"sql{i}"))
                self.db.commit()
                print("数据库创建成功")
            except:
                self.db.rollback()
                print("数据库已经存在")
        self.initialize2()

    def initialize2(self):
        """
        初始化第二步，检查是否存在空的场次表，如果有，就删除
        """
        sql1 = 'select max(s_id) from laodifang_doudizhu.session'
        sql2 = 'select b_id from laodifang_doudizhu.bout1 where s_id = %s limit 1'
        sql3 = 'delete from laodifang_doudizhu.session where s_id = %s'
        self.cur.execute(sql1)
        number = self.cur.fetchone()
        if not number:
            for i in range(1,number+1):
                self.cur.executemany(sql2,(i,))
                if  not self.cur.fetchone():
                    try:
                        self.cur.executemany(sql3, (i,))
                        self.db.commit()
                        print(f'删除空场次 s_id = {i}')
                    except:
                        self.db.rollback()
                        print(f'删除空场次 s_id = {i} 失败,失败')
        else:
            print('全新数据库，暂无场次数据')


if __name__ == '__main__':
    abc = Database('laodifang_doudizhu','mu7401889')
    abc.initialize_databese()


