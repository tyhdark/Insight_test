import os
from loguru import logger
import json


class Tools:
    @staticmethod
    def write_folder(folder_path, mode="w"):
        """
        获取文件夹下所有文件全路径
        :param folder_path:
        :param mode:
        :return:
        """
        images_path = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # 构建完整的文件路径
                file_path = os.path.join(root, file)
                # 打印文件路径
                # print(file_path)
                images_path.append(file_path)
        return images_path

    @staticmethod
    def get_path_all_path(folder_path):
        """
        递归查询文件夹下所有文件夹的绝对路径+名称
        :param folder_path:
        :return:
        """
        files_path = []
        for root, dirs, files in os.walk(folder_path):
            # 打印当前目录路径
            # print(f"Directory: {root}")
            # 打印当前目录下的所有文件夹
            for dir_name in dirs:
                # print(f"Subdirectory: {os.path.join(root, dir_name)}")
                files_path.append(os.path.join(root, dir_name))
        return files_path

    @staticmethod
    def image_file(file_path, mode="rb"):
        """
        读取文件内容,并返回
        :param file_path:
        :param mode:
        :return:
        """
        return open(file_path, mode)

    @staticmethod
    def get_image_json_by_file(file_path):
        """
        读取json文件获得身份证识别需要用到的json
        :param file_path:
        :return:
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            # logger.info(f"json_path={json_path}")
            try:
                image_json = json.load(file)
                return image_json
            except:
                logger.info(f"json_path={file_path},json文件异常")
                return None


if __name__ == '__main__':
    1
