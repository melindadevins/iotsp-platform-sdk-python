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

from pprint import pformat
from six import iteritems
import re


class ThingScrollFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, scroll_page_size=None, filter_criteria=None, filter_operator=None):
        """
        ThingScrollFilter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'scroll_page_size': 'int',
            'filter_criteria': 'list[FilterCriteria]',
            'filter_operator': 'str'
        }

        self.attribute_map = {
            'scroll_page_size': 'scrollPageSize',
            'filter_criteria': 'filterCriteria',
            'filter_operator': 'filterOperator'
        }

        self._scroll_page_size = scroll_page_size
        self._filter_criteria = filter_criteria
        self._filter_operator = filter_operator

    @property
    def scroll_page_size(self):
        """
        Gets the scroll_page_size of this ThingScrollFilter.


        :return: The scroll_page_size of this ThingScrollFilter.
        :rtype: int
        """
        return self._scroll_page_size

    @scroll_page_size.setter
    def scroll_page_size(self, scroll_page_size):
        """
        Sets the scroll_page_size of this ThingScrollFilter.


        :param scroll_page_size: The scroll_page_size of this ThingScrollFilter.
        :type: int
        """

        self._scroll_page_size = scroll_page_size

    @property
    def filter_criteria(self):
        """
        Gets the filter_criteria of this ThingScrollFilter.


        :return: The filter_criteria of this ThingScrollFilter.
        :rtype: list[FilterCriteria]
        """
        return self._filter_criteria

    @filter_criteria.setter
    def filter_criteria(self, filter_criteria):
        """
        Sets the filter_criteria of this ThingScrollFilter.


        :param filter_criteria: The filter_criteria of this ThingScrollFilter.
        :type: list[FilterCriteria]
        """

        self._filter_criteria = filter_criteria

    @property
    def filter_operator(self):
        """
        Gets the filter_operator of this ThingScrollFilter.


        :return: The filter_operator of this ThingScrollFilter.
        :rtype: str
        """
        return self._filter_operator

    @filter_operator.setter
    def filter_operator(self, filter_operator):
        """
        Sets the filter_operator of this ThingScrollFilter.


        :param filter_operator: The filter_operator of this ThingScrollFilter.
        :type: str
        """
        allowed_values = ["MATCH_ALL", "MATCH_ANY", "MATCH_NONE"]
        if filter_operator not in allowed_values:
            raise ValueError(
                "Invalid value for `filter_operator`, must be one of {0}"
                .format(allowed_values)
            )

        self._filter_operator = filter_operator

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