class EmailAddress(db.Model):
    """
    Represents the email_addresses table in the MySQL database.
    """

    __table_name__ = "email_addresses"

    email_address_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(320), nullable=False)
    time_added = db.Column(db.DateTime, nullable=True)
    time_updated = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<EmailAddress %r>' % self.email_address
