from models import *
from sqlalchemy.orm import sessionmaker
import re

engine = db.create_engine("sqlite:///IUHreports.sqlite")
connection = engine.connect()
Base.metadata.create_all(engine)  # Similarly, Base.metadata.drop_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
# Stating my thoughts
# Automated python program that allows for creation of automated sharing jobs for PowerBI app pages.
# Will do what I think the subscription button should do.

# Subscription consists of:
# Name of subscription
# App/Report Page parent link being subscriped to
# SOMEHOW the filters that should be applied in the subscription
# Best case - somehow entirely automated pull from the app
# Next best - Can link this program to the report page and pull the filter options
# Worst case - Manual entry of filters needed
# FORMAT <Table>/<Filter Column> eq(uals) '<Filter Value>' with specified rules
# Who it goes to, name and email
# Parameters of share: Screenshot, message, ...

# Program takes input and generates the filter embedded url that will be shared with the subscribers and the screenshot of the filtered report.

# Get inputs from User (name, parent link)

# Get filters from XXX???

# Create url from filters listed
def createURLfromFilter(filterIDlist):
    # if only single filter, single int id passed
    if isinstance(filterIDlist, int):
        # fetch filter data
        filter = connection.execute(
            f"select * from Reports where id = {filterIDlist}"
        ).fetchone()
        # concatenate data to create filtered report page url
        url = (
            filter[2]
            + "?filter="
            # Regex to deal with special characters
            + re.sub(r"\s", "_x0020_", filter[3])
            + "/"
            + re.sub(r"\s", "_x0020_", filter[4])
            + " eq "
            + f"'{filter[5]}'"
        )
        print(url)

    else:
        # fetch filters data
        filters = connection.execute(
            f"select * from Reports where id IN {filterIDlist}"
        ).fetchall()
        url = filters[0][2] + "?filter="
        for i in range(len(filters)):
            assert filters[0][1] == filters[i - 1][1], "Filters from different Reports!"
            url += (
                # Regex to deal with special characters
                re.sub(r"\s", "_x0020_", filters[i - 1][3])
                + "/"
                + re.sub(r"\s", "_x0020_", filters[i - 1][4])
                + " eq "
                + f"'{filters[i - 1][5]}'"
            )
            if i != len(filters) - 1:
                url += " and "
        print(url)


# Use selenium to get screenshot of formatted report using link previously generated.

# Email subscribers link and screenshot along with any message.
if __name__ == "__main__":
    createURLfromFilter(1)
    createURLfromFilter((1, 2))
