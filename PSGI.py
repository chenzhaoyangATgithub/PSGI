#!/usr/bin/env python
# coding:utf-8

# import——list


# End-import

DATABASE_CONFIG = {}
TRANSPORT_CONFIG = {}


# 数据二级适配,将传入的参数
def data_adapter_level_2(data_input, config=TRANSPORT_CONFIG):
    # TODO 参数1：data_input 配置项要往里传的，调用level_2的时候必须传进来
    # TODO 参数2：config 需要根据FTP、Email等不同的表单传进来的不同的配置JSON

    # TODO 2.提前配置好脚本库所在的根目录作为import的根（系统级配置）
    # 使得import module_name 可以直接import出来

    # TODO 3.获取到python文件的名称，作为模块名，赋值给module_name
    module_name = ""

    try:
        module = get_module(module_name)
        data = module.run(config=config,input=data_input)
        done_data = data_adapter_level_3(data)
        put_data_to_database(done_data)

    except Exception as es:
        # TODO 4.将import的错误信息扔进log
        pass


def get_module(module_name):
    if not module_name:
        return None
    else:
        return __import__(module_name)


# 数据三级适配，当前版本没有用，下个版本如果想去重再说
def data_adapter_level_3(data):
    return data


def put_data_to_database(data,config=DATABASE_CONFIG):
    # TODO 5.将最终处理好的数据写入数据库
    return data
