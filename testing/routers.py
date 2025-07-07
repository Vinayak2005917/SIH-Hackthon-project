class TestingRouter:
    def db_for_read(self, model, **hints):
        # Direct read operations for 'testing' models to the 'UserDB' database
        if model._meta.app_label == 'testing':
            return 'second_db'
        return 'default'

    def db_for_write(self, model, **hints):
        # Direct write operations for 'testing' models to the 'UserDB' database
        if model._meta.app_label == 'testing':
            return 'second_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations if both models are in 'testing'
        if obj1._meta.app_label == 'testing' or obj2._meta.app_label == 'testing':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Allow migrations for 'testing' models on the 'UserDB' database
        if app_label == 'testing':
            return db == 'second_db'
        return None