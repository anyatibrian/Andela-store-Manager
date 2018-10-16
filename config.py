class BaseConfig:
    DEBUG = False
    TESTING = False


# Development configurations for our application
class DevelopmentConfig(BaseConfig):
    """ this is where the development  configuration goes """
    DEBUG = True


# Testing Configurations for our application
class TestingConfig(BaseConfig):
    """ this is were our testing configurations goes"""
    TESTING = True


# production config
class ProductionConfig(BaseConfig):
    """this is where our production configuration goes"""
    DEBUG = False
    TESTING = False


config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
