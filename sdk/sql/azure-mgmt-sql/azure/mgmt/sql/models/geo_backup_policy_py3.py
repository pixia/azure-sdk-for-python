# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_resource_py3 import ProxyResource


class GeoBackupPolicy(ProxyResource):
    """A database geo backup policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param state: Required. The state of the geo backup policy. Possible
     values include: 'Disabled', 'Enabled'
    :type state: str or ~azure.mgmt.sql.models.GeoBackupPolicyState
    :ivar storage_type: The storage type of the geo backup policy.
    :vartype storage_type: str
    :ivar kind: Kind of geo backup policy.  This is metadata used for the
     Azure portal experience.
    :vartype kind: str
    :ivar location: Backup policy location.
    :vartype location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'state': {'required': True},
        'storage_type': {'readonly': True},
        'kind': {'readonly': True},
        'location': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'GeoBackupPolicyState'},
        'storage_type': {'key': 'properties.storageType', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, *, state, **kwargs) -> None:
        super(GeoBackupPolicy, self).__init__(**kwargs)
        self.state = state
        self.storage_type = None
        self.kind = None
        self.location = None