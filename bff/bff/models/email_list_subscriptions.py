class EmailListSubscription(db.Model):
    __tablename__ = "email_list_subscriptions"
    email_list_id = db.column(db.Integer, primary_key=True, nullable=True)
    email_address_id = db.column(db.Integer, nullable=False, db.ForeignKey("email_addresses.email_address_id"))
    subscription_source_id = db.column(db.Integer, nullable=False, db.ForeignKey("email_list_subscription_sources.subscription_source_id"))
    time_added = db.Column(db.DateTime, nullable=True)
    time_updated = db.Column(db.DateTime, nullable=True)

