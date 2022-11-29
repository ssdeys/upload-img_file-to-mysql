import os,pymysql
path = r''#路径自己填
conn=pymysql.connect()#里面自己填

course = conn.cursor()

#sql语句自己xie


def insert_img(path):
    '''
    查询数据，path必须有，必须是个文件夹
    :param path:
    :return:
    '''

    files = os.listdir(path)
    end = len(files)
    start = 0
    prefix = '程序进度：'
    for filename in files:
        f = open(os.path.join(path, filename),'rb')
        f_read = f.read()# 把图片转为二进制才能进行插入操作，不然插入的就是一坨屎
        #print(filename)
        sql = "insert into ？values (%s,%s); "
        args = (filename,str(f_read))
        course.execute(sql,args)
        print('\r' + prefix + '[ %.2f%% ]' % (start / end * 100), end='')
        conn.commit()

    print("执行完毕")
    conn.close()
def w_img():
    """
    从数据库中把图把图片拿出来
    :return:
    """
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM ？ LIMIT 1")
    fout = open('test_new.jpg', 'wb')
    fout.write(cursor.fetchone()[0])
    fout.close()
    cursor.close()
    conn.close()

def select_img():
    '''
    查询数据库中有那些图片
    :return:
    '''
    sql="select * from ？"
    course.execute(sql)
    data = course.fetchall()
    print(data)


if __name__ == '__main__':
   insert_img(path)
