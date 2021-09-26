import logging


# 设置日志输出样式
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(filename)s line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')
                    # filename='./log.log',
                    # filemode='a')

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("1111111111111")
    logger.warning("22222222222")