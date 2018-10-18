class BassConfig:
    TESTING = False
    DEBUG = False


class DevelopmentConfig(BassConfig):
    DEBUG = True


class TestingConfig(BassConfig):
    TESTING = True


class DeploymentConfig(BassConfig):
    TESTING = False
    DEBUG = False


config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'deployment': DevelopmentConfig
}
