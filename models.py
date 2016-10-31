from app import db
from datetime import datetime

class Provision(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    designation = db.Column(db.String(50))
    contact_no = db.Column(db.String(10))
    created_at = db.Column(db.DateTime)

    def __init__(self, name, designation, contact_no):
        self.name = name
        self.designation = designation
        self.contact_no = contact_no
        self.created_at = datetime.utcnow()

    def set_name(self, name):
        """
        Update Name
        :param name:
        :return:
        """
        self.name = name

    def set_designation(self, designation):
        """
        Update designation
        :param designation:
        :return:
        """
        self.designation = designation

    def set_contact_no(self, contact_no):
        """
        Update Contact Number
        :param contact_no:
        :return:
        """
        self.contact_no = contact_no

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    def __repr__(self):
        return '<Provision %r>' % self.id
