# -*- coding: utf-8 -*-
import json
import requests
import base64
import hashlib

# 获取上传文件的media_id
#media_url 获取mediaid的url
#path_file_name 完整文件路径（包含文件名）
def get_media_ID(media_url, path_file_name):
    files = {'file': open(path_file_name, 'rb')}
    print(files)
    r = requests.post(media_url, files=files)
    print(r.json())
    re = r.json()['media_id']
    return re

# 发送文件到企业微信群
#send_url  企业微信机器人url
#file_name  文件名
def send_file(send_url, media_url, file_name):
    media_id = get_media_ID(media_url, file_name)
    print(media_id)
    post_data = {
        "msgtype": "file",
        "file": {
            "media_id": media_id
        },
        "safe": 0
    }
    json_post_data = json.dumps(post_data, ensure_ascii=False).encode('utf-8')
    r = requests.post(send_url, data=json_post_data, headers={"Content-Type": "application/json; charset=utf-8"})
    print(r.text)

#发送图片至企业微信
def send_image(send_url, image):
    with open(image, 'rb') as file:  # 转换图片成base64格式
        data = file.read()
        encodestr = base64.b64encode(data)
        image_data = str(encodestr, 'utf-8')

    with open(image, 'rb') as file:  # 图片的MD5值
        md = hashlib.md5()
        md.update(file.read())
        image_md5 = md.hexdigest()

    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "image",
        "image": {
            "base64": image_data,
            "md5": image_md5
        }
    }
    result = requests.post(send_url, headers=headers, json=data)
    print(result.text)
    return result


if __name__ == '__main__':

    media_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=eb3b75a8-edf2-4219-91bf-5b1c8026e093&type=file'
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=eb3b75a8-edf2-4219-91bf-5b1c8026e093'
    path_file_name="E:\\datax_json\\test.xlsx"
    send_file(send_url,media_url,path_file_name)