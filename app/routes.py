from app import api
from app.account import HealthCheck
from app.account.handler import Provision

api.add_resource(HealthCheck, "/v1/status")
api.add_resource(Provision, "/v1/provision/<provision_id>",
                 "/v1/provision")
