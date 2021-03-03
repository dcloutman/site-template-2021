from .. import db

class EmailList(db.Model):
    """
    Represents the email_list_subscription_sources table in the MySQL database. 
    Identifies site features containing forms that add emails to lists.
    """

    __tablename__ = "email_list_subscription_sources"

    subscription_source_id = db.Column(db., primary_key = True)
    # A short string for easy programmatic access. Must be unique.
    string_identifier = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db., nullable=False)
    time_added = db.Column(db.DateTime, nullable=True)
    time_updated = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<EmailList %r>' % self.name

