class Config:
    DEBUG = False
    TESTING = False

    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False

    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 Mb limit
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True


class DebugConfig(Config):
    DEBUG = True
    TESTING = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    EXPLAIN_TEMPLATE_LOADING = True
    TRAP_HTTP_EXCEPTIONS = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

config = {
    'debug': DebugConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': ProductionConfig
}
