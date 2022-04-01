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

# append filter start and formatted filter tags to link

# Use selenium to get screenshot of formatted report using link previously generated.

# Email subscribers link and screenshot along with any message.
print("TEST")