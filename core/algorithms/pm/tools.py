# -*- coding: UTF-8 -*-

def get_grade(value):
    if value <= 50 and value >= 0:
        return '健康'
    elif value <= 100:
        return '中等'
    elif value <= 150:
        return '对敏感人群不健康'
    elif value <= 200:
        return '不健康'
    elif value <= 300:
        return '非常不健康'
    elif value <= 500:
        return '危险'
    elif value > 500:
        return '非常危险'  # 爆表了
    else:
        return None  # 输入值无效
