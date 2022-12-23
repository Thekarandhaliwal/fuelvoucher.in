

class SaiHiTech:
    def __init__(self, name=None, mobile=None, vehicle=None):
        self.name = name
        self.mobile = mobile
        self.vehicle = vehicle

    def insert_sql_command(self):
        sql = "insert into customer values( '{name}', '{mobile}', '{vehicle}')".format_map(vars(self))
        return sql

    # .format_map(vars(self))



