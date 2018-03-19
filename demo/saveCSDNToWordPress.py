# coding:utf-8
import mysql.connector


def saveWordPress(title, content, seq):
    conn = mysql.connector.connect(host='**', port='3306', user='knhzigws_wp710', password='gp123456!@#$%^',
                                   database='knhzigws_wp710', \
                                   use_unicode=True)
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO `wp5x_posts` (`ID`, `post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_excerpt`, `post_status`, `comment_status`, `ping_status`, `post_password`, `post_name`, `to_ping`, `pinged`, `post_modified`, `post_modified_gmt`, `post_content_filtered`, `post_parent`, `guid`, `menu_order`, `post_type`, `post_mime_type`, `comment_count`)"
        sql = sql + " VALUES (" + seq + ", " \
                                        "1, " \
                                        "now(), " \
                                        "now(), '" + content + "', " \
                                        "'" + title + "', " \
                                        "'', " \
                                        "'publish', " \
                                        "'open', " \
                                        "'open', " \
                                        "'', " \
                                        "'" + seq + "', " \
                                        "'', '', " \
                                        "now(), " \
                                        "now(), " \
                                        "'" + content + "', " \
                                        "0, " \
                                        "'http://www.woailjw.com/?p=" + seq + "', " \
                                        "0, " \
                                        "'post'," \
                                        " '', 0)"

        cursor.execute(sql)

    finally:
        cursor.close()
        conn.close()
