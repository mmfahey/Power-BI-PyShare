from matplotlib.pyplot import table, title
from sklearn.utils import column_or_1d
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db


Base = declarative_base()


class Filter(Base):
    __tablename__ = "Reports"
    id = db.Column(db.Integer, primary_key=True)
    report_title = db.Column(db.String(100))
    parent_url = db.Column(db.String(100))
    table_name = db.Column(db.String(100))
    column_name = db.Column(db.String(100))
    filter_value = db.Column(db.String(100))

    def __repr__(self):
        return f"<{self.column_name} Filter with value {self.filter_value} for {self.report_title}>"
