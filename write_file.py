#  coding:utf-8
import os


def write_file(success_content, url, filename, type):
    target_file = "_" + filename + "_" + type + ".html"
    if type == "sqli":
        with open("result/" + url + target_file, "w") as fp:
            for i in success_content:
                fp.write("<a href=" + i + ">" + i + "</a>" + "<br/>")
    elif type == "web":
        with open("result/" + url + target_file, "w") as fp:
            for i in success_content:
                fp.write("<a href=" + i + ">" + i + "</a>" + "<br/>")
    elif type == "cms":
        with open("result/" + url + target_file, "w") as fp:
            for i in success_content:
                fp.write("<a href=" + i + ">" + i + "</a>" + "<br/>")
    elif type == "admin":
        with open("result/" + url + target_file, "w") as fp:
            for i in success_content:
                fp.write("<a href=" + i + ">" + i + "</a>" + "<br/>")
    else:
        pass


if __name__ == '__main__':
    write_file("http", "localhost", "struts2", "admin")
