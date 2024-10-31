import json

import requests
from loguru import logger
import os
import tools


class BaseApi(object):
    def face_detect_server(self, path, baseurl, port):
        # 人脸检测
        files_detect = {"image": tools.Tools.image_file(path)}
        response = requests.post(f"{baseurl}:{port}/api/face_detect", files=files_detect).json()
        return response

    def face_compare_server(self, path1, path2, baseurl, port):
        # 2. 接口名称:  1:1人脸比对
        # 接口说明：人脸比对，上传两种带人脸的图片，返回人脸相似度、人脸切图、人脸坐标框等
        files_detect = {"image1": tools.Tools.image_file(path1), "image2": tools.Tools.image_file(path2)}
        response = requests.post(f"{baseurl}:{port}/api/face_compare", files=files_detect).json()
        return response

    def face_search_server(self, path, baseurl, port):
        # 3. 接口名称：1:N人脸检索
        # 接口说明：人脸检索，上传带人脸的图片及待检索的库信息（过滤字段），返回相似度最大的五个人脸
        files_detect = {"image": tools.Tools.image_file(path)}
        data = {
            'data': '{"appid":["appid_0"],"faceid":["faceid_0"],"gender":["0"]}'
        }
        response = requests.post(f"{baseurl}:{port}/api/face_search", files=files_detect, data=data).json()
        return response

    def face_insert_server(self, baseurl, port):
        # 4. 接口名称：人脸特征向量入库
        # 接口说明：人脸特征向量入库，提供待入库的人脸信息（id、特征向量、性别等），在向量搜索库中进行插入，mysql是否插入相关信息由后端决定
        data = {
            "id": [0],
            "appid": ["appid_0"],
            "faceid": ["faceid_0"],
            "vector": ["0.0361639895", "-0.0185372047", "-0.0114454078", "-0.06028888", "0.0089296941"],
            "gender": ["0"]
        }
        response = requests.post(f"{baseurl}:{port}/api/face_insert", json=data).json()
        return response

    def face_delete_server(self, baseurl, port):
        # 5. 接口名称：人脸特征向量删除
        # 接口说明：人脸特征向量删除，提供待删除的人脸id，在对应向量搜索库中进行删除，mysql是否删除由后端决定
        data = {
            "id": [100000000000]
        }
        response = requests.post(f"{baseurl}:{port}/api/face_delete", json=data).json()
        return response

    def edge_detect_server(self, path, baseurl, port):
        # 101. 接口名称:卡证轮廓检测
        files_detect = {"image": tools.Tools.image_file(path)}
        response = requests.post(f"{baseurl}:{port}/api/edge_detect_server", files=files_detect).json()
        return response

    def idcard_recog_server(self, path, baseurl, port, image_json):
        """
        :param path: 需要验证的身份证图片路径
        :param baseurl: 请求接口的地址
        :param port: 请求接口的端口
        :param image_json: 需要验证身份证图片对应的json
        :return:
        """
        # 102. 接口名称:身份证识别(json配置版)
        files_detect = {"image": tools.Tools.image_file(path)}

        response = requests.post(f"{baseurl}:{port}/api/idcard_recog_server", files=files_detect,
                                 data={'image_json': str(image_json)})
        str_json = response.json()
        return str_json

    def security_detect_server(self, path, baseurl, port):
        # 103. 接口名称:证件真伪识别
        files_detect = {"image": tools.Tools.image_file(path)}
        headers = {
            'Content-Type': 'image/jpeg'
        }
        response = requests.post(f"{baseurl}:{port}/api/security_detect_server", files=files_detect,
                                 headers=headers).json()
        return response

    def ocr_all_server(self, path, baseurl, port):
        # 104. 接口名称:多语种图片识别基础版(通用识别)
        files_detect = {"image": tools.Tools.image_file(path)}
        data = {'language': 'ch'}
        response = requests.post(f"{baseurl}:{port}/api/ocr_all_server", files=files_detect, data=data).json()
        return response

    def pp_edge_detect_server(self, path, baseurl, port):
        # 105. 接口名称:护照轮廓检测
        files_detect = {"image": tools.Tools.image_file(path)}
        data = {'language': 'ch'}
        response = requests.post(f"{baseurl}:{port}/api/pp_edge_detect_server", files=files_detect, data=data).json()
        return response

    def passport_recog_server(self, path, baseurl, port):
        # 106. 接口名称:护照识别基础版进阶版
        files_detect = {"image": tools.Tools.image_file(path)}
        data = {'pp_type': 'base'}
        response = requests.post(f"{baseurl}:{port}/api/passport_recog_server", files=files_detect, data=data).json()
        return response

