from models import Provision
from app import db
from app.exceptions.exceptions import AppError
from sqlalchemy import exc


def get_provision_data(provision_id):
    try:
        provision_account = Provision.query.filter_by(id=provision_id).first()
        if provision_account:
            return {"success": provision_account.as_dict()}
        else:
            return {"error": "No Provision Account for given id"}
    except exc.SQLAlchemyError as e:
        raise AppError(error_code='', error_message='Sql alchemy error while showing provision data: ' + str(e.message))


def save_provision_data(name, designation, contact_no):
    try:
        session = db.session()
        init = Provision(name=name, designation=designation, contact_no=contact_no)
        session.add(init)
        session.commit()
    except exc.SQLAlchemyError as e:
        raise AppError(error_code='',
                       error_message='Sql alchemy error while saving provision data: ' + str(e.message))


def update_provison_data(provision_id, data):
    provision_account = Provision.query.filter_by(id=provision_id).first()
    if not provision_account:
        return {"error": "No Provision Account for given id"}
    name = data.get("name")
    if name and name != provision_account.name:
        provision_account.set_name(name)
    designation = data.get("designation")
    if designation and designation != provision_account.designation:
        provision_account.set_designation(designation)
    contact_no = data.get("contact_no")
    if contact_no and contact_no != provision_account.contact_no:
        provision_account.set_contact_no(contact_no)
    try:
        session = db.session()
        session.add(provision_account)
        session.commit()
    except exc.SQLAlchemyError as e:
        raise AppError(error_code='',
                       error_message='Sql alchemy error while updating provision data: ' + str(e.message))


def delete_provision_data(provision_id):
    try:
        provision_account = Provision.query.filter_by(id=provision_id).first()
        if provision_account:
            session = db.session()
            Provision.query.filter_by(id=provision_id).delete()
            session.commit()
            return {"success": "Provision data is deleted for {} id".format(provision_id)}
        else:
            return {"error": "No Provision Account for given id"}
    except exc.SQLAlchemyError as e:
        raise AppError(error_code='',
                           error_message='Sql alchemy error while deleting provision data: ' + str(e.message))
