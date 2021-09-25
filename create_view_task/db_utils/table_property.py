class TableProperty:
    table_prop = [{
    "table_name":"energy",
    "endpoint_id":"int",
    "event_time":"date",
    "kwh":"float"
    },
    {
    "table_name":"operators",
    "endpoint_id":"int",
    "login_time":"date",
    "logout_time":"date",
    "operator_name":"text"
    },
    {
    "table_name":"periods",
    "endpoint_id":"int",
    "mode_start":"date",
    "mode_duration":"int",
    "label":"text"
    },
    {
    "table_name":"reasons",
    "endpoint_id":"int",
    "event_time":"date",
    "reason":"text"
    }
    ]
    copy_table = (('energy', r'\csv_file\energy.csv'), ('operators', r'\csv_file\operators.csv'), 
                   ('periods', r'\csv_file\periods.csv'), ('reasons', r'\csv_file\reasons.csv'))
                  