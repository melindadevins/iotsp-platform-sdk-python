#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
# coding: utf-8

"""
    API documentation for Claims

    APIs for operations on Claims

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

# import models into sdk package
from .models.filter_criteria import FilterCriteria
from .models.io_t_exception_model import IoTExceptionModel
from .models.page_info import PageInfo
from .models.page_thing_claim import PageThingClaim
from .models.sort_criteria import SortCriteria
from .models.thing_claim import ThingClaim
from .models.thing_claim_filter import ThingClaimFilter
from .models.thing_claim_request import ThingClaimRequest
from .models.thing_claim_update_request import ThingClaimUpdateRequest
from .models.thing_claimed_detail import ThingClaimedDetail
from .models.thing_descriptor import ThingDescriptor
from .models.unique_identifier import UniqueIdentifier

# import apis into sdk package
from .apis.claims_api import ClaimsApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
configuration.verify_ssl = False

