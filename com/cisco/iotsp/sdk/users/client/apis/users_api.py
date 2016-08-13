#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
# coding: utf-8

"""
    API documentation for User Service

    These are all the APIs for the User Service

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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UsersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_user(self, user_create_request, **kwargs):
        """
        Create new user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_user(user_create_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserCreateObject user_create_request: The user to be created (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_user_with_http_info(user_create_request, **kwargs)
        else:
            (data) = self.create_user_with_http_info(user_create_request, **kwargs)
            return data

    def create_user_with_http_info(self, user_create_request, **kwargs):
        """
        Create new user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_user_with_http_info(user_create_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserCreateObject user_create_request: The user to be created (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_create_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_create_request' is set
        if ('user_create_request' not in params) or (params['user_create_request'] is None):
            raise ValueError("Missing the required parameter `user_create_request` when calling `create_user`")

        resource_path = '/v1/user-services/users'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_create_request' in params:
            body_params = params['user_create_request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuthScheme']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='User',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def delete_user(self, user_uid, **kwargs):
        """
        Delete user by userUid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user(user_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_uid: Uid of user (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_user_with_http_info(user_uid, **kwargs)
        else:
            (data) = self.delete_user_with_http_info(user_uid, **kwargs)
            return data

    def delete_user_with_http_info(self, user_uid, **kwargs):
        """
        Delete user by userUid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user_with_http_info(user_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_uid: Uid of user (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_uid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_uid' is set
        if ('user_uid' not in params) or (params['user_uid'] is None):
            raise ValueError("Missing the required parameter `user_uid` when calling `delete_user`")

        resource_path = '/v1/user-services/users/{userUid}'.replace('{format}', 'json')
        path_params = {}
        if 'user_uid' in params:
            path_params['userUid'] = params['user_uid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['tokenAuthScheme']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='User',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_user(self, user_uid, **kwargs):
        """
        Get user by userUid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user(user_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_uid: Uid of user (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_user_with_http_info(user_uid, **kwargs)
        else:
            (data) = self.get_user_with_http_info(user_uid, **kwargs)
            return data

    def get_user_with_http_info(self, user_uid, **kwargs):
        """
        Get user by userUid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_with_http_info(user_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_uid: Uid of user (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_uid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_uid' is set
        if ('user_uid' not in params) or (params['user_uid'] is None):
            raise ValueError("Missing the required parameter `user_uid` when calling `get_user`")

        resource_path = '/v1/user-services/users/{userUid}'.replace('{format}', 'json')
        path_params = {}
        if 'user_uid' in params:
            path_params['userUid'] = params['user_uid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['tokenAuthScheme']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='User',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_users(self, **kwargs):
        """
        Get a page of users by filter
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_users(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email_address: search by emailAddress of the user
        :param str sort_key: sort by a key in user. Nested fields can be . delimited
        :param str sort_order: sort in ascending or descending order
        :param int limit: maximum number of users to return
        :param int offset: starting index of users in return payload
        :return: PageUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_users_with_http_info(**kwargs)
        else:
            (data) = self.get_users_with_http_info(**kwargs)
            return data

    def get_users_with_http_info(self, **kwargs):
        """
        Get a page of users by filter
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_users_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email_address: search by emailAddress of the user
        :param str sort_key: sort by a key in user. Nested fields can be . delimited
        :param str sort_order: sort in ascending or descending order
        :param int limit: maximum number of users to return
        :param int offset: starting index of users in return payload
        :return: PageUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email_address', 'sort_key', 'sort_order', 'limit', 'offset']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/user-services/users'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'email_address' in params:
            query_params['emailAddress'] = params['email_address']
        if 'sort_key' in params:
            query_params['sortKey'] = params['sort_key']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['tokenAuthScheme']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageUser',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_user(self, user_uid, user_update_request, **kwargs):
        """
        Update user by userUid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_user(user_uid, user_update_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_uid: Uid of user (required)
        :param UserUpdateObject user_update_request: The complete list of field and their values to be updated (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_user_with_http_info(user_uid, user_update_request, **kwargs)
        else:
            (data) = self.update_user_with_http_info(user_uid, user_update_request, **kwargs)
            return data

    def update_user_with_http_info(self, user_uid, user_update_request, **kwargs):
        """
        Update user by userUid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_user_with_http_info(user_uid, user_update_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_uid: Uid of user (required)
        :param UserUpdateObject user_update_request: The complete list of field and their values to be updated (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_uid', 'user_update_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_uid' is set
        if ('user_uid' not in params) or (params['user_uid'] is None):
            raise ValueError("Missing the required parameter `user_uid` when calling `update_user`")
        # verify the required parameter 'user_update_request' is set
        if ('user_update_request' not in params) or (params['user_update_request'] is None):
            raise ValueError("Missing the required parameter `user_update_request` when calling `update_user`")

        resource_path = '/v1/user-services/users/{userUid}'.replace('{format}', 'json')
        path_params = {}
        if 'user_uid' in params:
            path_params['userUid'] = params['user_uid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_update_request' in params:
            body_params = params['user_update_request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuthScheme']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='User',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
