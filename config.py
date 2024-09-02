import os
DB_DETAILS = {
    'dev' : {

        'SOURCE_DB' :{
            'DB_TYPE': 'postgres',
            'DB_HOST': 'localhost',
            'DB_PORT': 5432,
            'DB_USER': 'admin_gopi',
            'DB_PASS': 'admin',
            'DB_NAME': 'data_pipeline_dev',
        }
        'TARGET_DB' : {
            'DB_TYPE': 'postgres',
            'DB_HOST': 'localhost',
            'DB_PORT': 5432,
            'DB_USER': 'admin_gopi',
            'DB_PASS': 'admin',
            'DB_NAME': 'data_pipeline_dev',
        }
    }
}