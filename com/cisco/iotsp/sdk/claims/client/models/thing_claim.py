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


class ThingClaim(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, uid=None, created_on=None, make=None, model=None, unique_identifiers=None, claimed=False, claimed_details=None, thing_details=None, tags=None):
        """
        ThingClaim - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'uid': 'str',
            'created_on': 'str',
            'make': 'str',
            'model': 'str',
            'unique_identifiers': 'UniqueIdentifier',
            'claimed': 'bool',
            'claimed_details': 'ThingClaimedDetail',
            'thing_details': 'ThingDescriptor',
            'tags': 'list[str]'
        }

        self.attribute_map = {
            'uid': 'uid',
            'created_on': 'createdOn',
            'make': 'make',
            'model': 'model',
            'unique_identifiers': 'uniqueIdentifiers',
            'claimed': 'claimed',
            'claimed_details': 'claimedDetails',
            'thing_details': 'thingDetails',
            'tags': 'tags'
        }

        self._uid = uid
        self._created_on = created_on
        self._make = make
        self._model = model
        self._unique_identifiers = unique_identifiers
        self._claimed = claimed
        self._claimed_details = claimed_details
        self._thing_details = thing_details
        self._tags = tags

    @property
    def uid(self):
        """
        Gets the uid of this ThingClaim.


        :return: The uid of this ThingClaim.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this ThingClaim.


        :param uid: The uid of this ThingClaim.
        :type: str
        """

        self._uid = uid

    @property
    def created_on(self):
        """
        Gets the created_on of this ThingClaim.


        :return: The created_on of this ThingClaim.
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """
        Sets the created_on of this ThingClaim.


        :param created_on: The created_on of this ThingClaim.
        :type: str
        """

        self._created_on = created_on

    @property
    def make(self):
        """
        Gets the make of this ThingClaim.


        :return: The make of this ThingClaim.
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make):
        """
        Sets the make of this ThingClaim.


        :param make: The make of this ThingClaim.
        :type: str
        """

        self._make = make

    @property
    def model(self):
        """
        Gets the model of this ThingClaim.


        :return: The model of this ThingClaim.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this ThingClaim.


        :param model: The model of this ThingClaim.
        :type: str
        """

        self._model = model

    @property
    def unique_identifiers(self):
        """
        Gets the unique_identifiers of this ThingClaim.


        :return: The unique_identifiers of this ThingClaim.
        :rtype: UniqueIdentifier
        """
        return self._unique_identifiers

    @unique_identifiers.setter
    def unique_identifiers(self, unique_identifiers):
        """
        Sets the unique_identifiers of this ThingClaim.


        :param unique_identifiers: The unique_identifiers of this ThingClaim.
        :type: UniqueIdentifier
        """

        self._unique_identifiers = unique_identifiers

    @property
    def claimed(self):
        """
        Gets the claimed of this ThingClaim.


        :return: The claimed of this ThingClaim.
        :rtype: bool
        """
        return self._claimed

    @claimed.setter
    def claimed(self, claimed):
        """
        Sets the claimed of this ThingClaim.


        :param claimed: The claimed of this ThingClaim.
        :type: bool
        """

        self._claimed = claimed

    @property
    def claimed_details(self):
        """
        Gets the claimed_details of this ThingClaim.


        :return: The claimed_details of this ThingClaim.
        :rtype: ThingClaimedDetail
        """
        return self._claimed_details

    @claimed_details.setter
    def claimed_details(self, claimed_details):
        """
        Sets the claimed_details of this ThingClaim.


        :param claimed_details: The claimed_details of this ThingClaim.
        :type: ThingClaimedDetail
        """

        self._claimed_details = claimed_details

    @property
    def thing_details(self):
        """
        Gets the thing_details of this ThingClaim.


        :return: The thing_details of this ThingClaim.
        :rtype: ThingDescriptor
        """
        return self._thing_details

    @thing_details.setter
    def thing_details(self, thing_details):
        """
        Sets the thing_details of this ThingClaim.


        :param thing_details: The thing_details of this ThingClaim.
        :type: ThingDescriptor
        """

        self._thing_details = thing_details

    @property
    def tags(self):
        """
        Gets the tags of this ThingClaim.


        :return: The tags of this ThingClaim.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ThingClaim.


        :param tags: The tags of this ThingClaim.
        :type: list[str]
        """

        self._tags = tags

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