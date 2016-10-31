from flask_restful import Resource
from flask import request
from  app.exceptions.exceptions import AppError
from app.account.functions import *


class Provision(Resource):
    def get(self, provision_id):
        """
        get Provision Account
        :param provision_id:
        :return:
        """
        try:
            return get_provision_data(provision_id)
        except AppError as e:
            return {"error": e.as_dict()}

    def post(self):
        """
        Save Provision Account
        :return:
        """
        try:
            data = request.get_json(force=True)
            if not data:
                return {"error": "Bad request data."}
            name = data.get("name")
            if not name:
                return {"error": 'Name of employee is missing in request data.'}
            designation = data.get("designation")
            if not designation:
                return {"error": "Designation of employee is missing in request data."}
            contact_no = data.get("contact_no")
            if not contact_no:
                return {"error": "Contact number of employee is missing in request data."}
            save_provision_data(name, designation, contact_no)
            return {"success": "Provision account Save successfully"}
        except AppError as e:
            return {"error": e.as_dict()}

    def put(self, provision_id):
        """
        Update Provision Account
        :return:
        """
        try:
            data = request.get_json(force=True)
            update_provison_data(provision_id, data)
            return {"success": "Notification account Update successfully"}
        except AppError as e:
            return {"error": e.as_dict()}

    def delete(self, provision_id):
        """
        Delete Provision Account
        :param provision_id:
        :return:
        """
        try:
            return delete_provision_data(provision_id)
        except AppError as e:
            return {"error": e.as_dict()}
