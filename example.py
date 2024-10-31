import base
from loguru import logger
baseurl = 'http://192.168.0.9'
port1 = 6000
port2 = 5000


def example_test_idcard_recog_server():
    test_url = r"\\192.168.0.9\share\测试使用\卡证相关\身份证识别\1-248\1-149\10)Hong Kong\testa.jpg"
    image_json = {
        "country": "EH",
        "type": "id",
        "language": "zh",
        "label": [
            {"coordinate": [162, 100, 224, 113], "name": "name"},
            {"coordinate": [59, 266, 130, 279], "name": "idcard"}
        ],
        "imageSize": [450, 300]
    }
    base_api = base.BaseApi()
    logger.info(base_api.idcard_recog_server(test_url, baseurl, port2, image_json))


if __name__ == '__main__':
    example_test_idcard_recog_server()
