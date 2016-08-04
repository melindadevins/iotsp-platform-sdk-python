# coding: utf-8

"""
    API Documentation


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
from .models.page_thing import PageThing
from .models.scroll_id import ScrollId
from .models.scroll_page_thing import ScrollPageThing
from .models.section_schema_pair import SectionSchemaPair
from .models.sort_criteria import SortCriteria
from .models.thing import Thing
from .models.thing_create_request import ThingCreateRequest
from .models.thing_filter import ThingFilter
from .models.thing_identifier import ThingIdentifier
from .models.thing_scroll_filter import ThingScrollFilter
from .models.thing_update_request import ThingUpdateRequest

# import apis into sdk package
from .apis.things_api import ThingsApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
configuration.verify_ssl = False
