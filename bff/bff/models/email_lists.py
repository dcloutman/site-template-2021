
class EmailList(db.Model):
    """
    Represents the email_lists table in the MySQL database. 
    Stores metadata about email lists.
    """

    __table_name__ = "email_lists"

    email_list_id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(1023), nullable=False)
    list_description = db.Column(db.Text, nullable=False)
    time_added = db.Column(db.DateTime, nullable=True)
    time_updated = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<EmailAddress %r>' % self.list_name
