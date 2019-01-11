class BaseConfig:
    DEBUG = False
    TEST = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TEST = True


class ProductionConfig(BaseConfig):
    TEST = False
    DEBUG = False


config = {
    'Testing': TestingConfig,
    'development': ProductionConfig,
    'production': ProductionConfig
}