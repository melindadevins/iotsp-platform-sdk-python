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

from pprint import pformat
from six import iteritems
import re


class ThingClaimFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, page_info=None, sort_criteria=None, filter_criteria=None, filter_operator_enum=None):
        """
        ThingClaimFilter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'page_info': 'PageInfo',
            'sort_criteria': 'SortCriteria',
            'filter_criteria': 'list[FilterCriteria]',
            'filter_operator_enum': 'str'
        }

        self.attribute_map = {
            'page_info': 'pageInfo',
            'sort_criteria': 'sortCriteria',
            'filter_criteria': 'filterCriteria',
            'filter_operator_enum': 'filterOperatorEnum'
        }

        self._page_info = page_info
        self._sort_criteria = sort_criteria
        self._filter_criteria = filter_criteria
        self._filter_operator_enum = filter_operator_enum

    @property
    def page_info(self):
        """
        Gets the page_info of this ThingClaimFilter.


        :return: The page_info of this ThingClaimFilter.
        :rtype: PageInfo
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """
        Sets the page_info of this ThingClaimFilter.


        :param page_info: The page_info of this ThingClaimFilter.
        :type: PageInfo
        """

        self._page_info = page_info

    @property
    def sort_criteria(self):
        """
        Gets the sort_criteria of this ThingClaimFilter.


        :return: The sort_criteria of this ThingClaimFilter.
        :rtype: SortCriteria
        """
        return self._sort_criteria

    @sort_criteria.setter
    def sort_criteria(self, sort_criteria):
        """
        Sets the sort_criteria of this ThingClaimFilter.


        :param sort_criteria: The sort_criteria of this ThingClaimFilter.
        :type: SortCriteria
        """

        self._sort_criteria = sort_criteria

    @property
    def filter_criteria(self):
        """
        Gets the filter_criteria of this ThingClaimFilter.


        :return: The filter_criteria of this ThingClaimFilter.
        :rtype: list[FilterCriteria]
        """
        return self._filter_criteria

    @filter_criteria.setter
    def filter_criteria(self, filter_criteria):
        """
        Sets the filter_criteria of this ThingClaimFilter.


        :param filter_criteria: The filter_criteria of this ThingClaimFilter.
        :type: list[FilterCriteria]
        """

        self._filter_criteria = filter_criteria

    @property
    def filter_operator_enum(self):
        """
        Gets the filter_operator_enum of this ThingClaimFilter.


        :return: The filter_operator_enum of this ThingClaimFilter.
        :rtype: str
        """
        return self._filter_operator_enum

    @filter_operator_enum.setter
    def filter_operator_enum(self, filter_operator_enum):
        """
        Sets the filter_operator_enum of this ThingClaimFilter.


        :param filter_operator_enum: The filter_operator_enum of this ThingClaimFilter.
        :type: str
        """
        allowed_values = ["MATCH_ALL", "MATCH_ANY", "MATCH_NONE"]
        if filter_operator_enum not in allowed_values:
            raise ValueError(
                "Invalid value for `filter_operator_enum`, must be one of {0}"
                .format(allowed_values)
            )

        self._filter_operator_enum = filter_operator_enum

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other