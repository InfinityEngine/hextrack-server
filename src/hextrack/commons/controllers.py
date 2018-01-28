from api_commons.common import BaseController
from hextrack.commons import permissions


class HextrackController(BaseController):
    permission_classes = [permissions.HextrackCommonPermission]
