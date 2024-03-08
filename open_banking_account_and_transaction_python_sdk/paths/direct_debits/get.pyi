# coding: utf-8

"""
    Account and Transaction API Specification

    Swagger for Account and Transaction API Specification

    The version of the OpenAPI document: 3.1.7
    Contact: ServiceDesk@openbanking.org.uk
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from open_banking_account_and_transaction_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from open_banking_account_and_transaction_python_sdk.api_response import AsyncGeneratorResponse
from open_banking_account_and_transaction_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from open_banking_account_and_transaction_python_sdk import schemas  # noqa: F401

from open_banking_account_and_transaction_python_sdk.model.ob_read_direct_debit2 import OBReadDirectDebit2 as OBReadDirectDebit2Schema
from open_banking_account_and_transaction_python_sdk.model.ob_error_response1 import OBErrorResponse1 as OBErrorResponse1Schema

from open_banking_account_and_transaction_python_sdk.type.ob_error_response1 import OBErrorResponse1
from open_banking_account_and_transaction_python_sdk.type.ob_read_direct_debit2 import OBReadDirectDebit2

from ...api_client import Dictionary
from open_banking_account_and_transaction_python_sdk.pydantic.ob_error_response1 import OBErrorResponse1 as OBErrorResponse1Pydantic
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_direct_debit2 import OBReadDirectDebit2 as OBReadDirectDebit2Pydantic

# Header params


class XFapiAuthDateSchema(
    schemas.StrSchema
):
    pass
XFapiCustomerIpAddressSchema = schemas.StrSchema
XFapiInteractionIdSchema = schemas.StrSchema
XCustomerUserAgentSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'x-fapi-auth-date': typing.Union[XFapiAuthDateSchema, str, ],
        'x-fapi-customer-ip-address': typing.Union[XFapiCustomerIpAddressSchema, str, ],
        'x-fapi-interaction-id': typing.Union[XFapiInteractionIdSchema, str, ],
        'x-customer-user-agent': typing.Union[XCustomerUserAgentSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_fapi_auth_date = api_client.HeaderParameter(
    name="x-fapi-auth-date",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XFapiAuthDateSchema,
)
request_header_x_fapi_customer_ip_address = api_client.HeaderParameter(
    name="x-fapi-customer-ip-address",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XFapiCustomerIpAddressSchema,
)
request_header_x_fapi_interaction_id = api_client.HeaderParameter(
    name="x-fapi-interaction-id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XFapiInteractionIdSchema,
)
request_header_x_customer_user_agent = api_client.HeaderParameter(
    name="x-customer-user-agent",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XCustomerUserAgentSchema,
)
XFapiInteractionIdSchema = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJson = OBReadDirectDebit2Schema
SchemaFor200ResponseBodyApplicationJosejwe = OBReadDirectDebit2Schema
SchemaFor200ResponseBodyApplicationJsonCharsetutf8 = OBReadDirectDebit2Schema
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'x-fapi-interaction-id': XFapiInteractionIdSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: OBReadDirectDebit2


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: OBReadDirectDebit2


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/jose+jwe': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJosejwe),
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonCharsetutf8),
    },
    headers=[
        x_fapi_interaction_id_parameter,
    ]
)
XFapiInteractionIdSchema = schemas.StrSchema
SchemaFor400ResponseBodyApplicationJson = OBErrorResponse1Schema
SchemaFor400ResponseBodyApplicationJosejwe = OBErrorResponse1Schema
SchemaFor400ResponseBodyApplicationJsonCharsetutf8 = OBErrorResponse1Schema
ResponseHeadersFor400 = typing_extensions.TypedDict(
    'ResponseHeadersFor400',
    {
        'x-fapi-interaction-id': XFapiInteractionIdSchema,
    }
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: OBErrorResponse1


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: OBErrorResponse1


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
        'application/jose+jwe': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJosejwe),
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonCharsetutf8),
    },
    headers=[
        x_fapi_interaction_id_parameter,
    ]
)
XFapiInteractionIdSchema = schemas.StrSchema
ResponseHeadersFor401 = typing_extensions.TypedDict(
    'ResponseHeadersFor401',
    {
        'x-fapi-interaction-id': XFapiInteractionIdSchema,
    }
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    headers: ResponseHeadersFor401
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    headers: ResponseHeadersFor401
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    headers=[
        x_fapi_interaction_id_parameter,
    ]
)
XFapiInteractionIdSchema = schemas.StrSchema
SchemaFor403ResponseBodyApplicationJson = OBErrorResponse1Schema
SchemaFor403ResponseBodyApplicationJosejwe = OBErrorResponse1Schema
SchemaFor403ResponseBodyApplicationJsonCharsetutf8 = OBErrorResponse1Schema
ResponseHeadersFor403 = typing_extensions.TypedDict(
    'ResponseHeadersFor403',
    {
        'x-fapi-interaction-id': XFapiInteractionIdSchema,
    }
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: OBErrorResponse1


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: OBErrorResponse1


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
        'application/jose+jwe': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJosejwe),
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJsonCharsetutf8),
    },
    headers=[
        x_fapi_interaction_id_parameter,
    ]
)
XFapiInteractionIdSchema = schemas.StrSchema
ResponseHeadersFor404 = typing_extensions.TypedDict(
    'ResponseHeadersFor404',
    {
        'x-fapi-interaction-id': XFapiInteractionIdSchema,
    }
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    headers: ResponseHeadersFor404
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    headers: ResponseHeadersFor404
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    headers=[
        x_fapi_interaction_id_parameter,
    ]
)
XFapiInteractionIdSchema = schemas.StrSchema
ResponseHeadersFor405 = typing_extensions.TypedDict(
    'ResponseHeadersFor405',
    {
        'x-fapi-interaction-id': XFapiInteractionIdSchema,
    }
)


@dataclass
class ApiResponseFor405(api_client.ApiResponse):
    headers: ResponseHeadersFor405
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor405Async(api_client.AsyncApiResponse):
    headers: ResponseHeadersFor405
    body: schemas.Unset = schemas.unset


_response_for_405 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor405,
    response_cls_async=ApiResponseFor405Async,
    headers=[
        x_fapi_interaction_id_parameter,
    ]
)
XFapiInteractionIdSchema = schemas.StrSchema
ResponseHeadersFor406 = typing_extensions.TypedDict(
    'ResponseHeadersFor406',
    {
        'x-fapi-interaction-id': XFapiInteractionIdSchema,
    }
)


@dataclass
class ApiResponseFor406(api_client.ApiResponse):
    headers: ResponseHeadersFor406
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor406Async(api_client.AsyncApiResponse):
    headers: ResponseHeadersFor406
    body: schemas.Unset = schemas.unset


_response_for_406 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor406,
    response_cls_async=ApiResponseFor406Async,
    headers=[
        x_fapi_interaction_id_parameter,
    ]
)
RetryAfterSchema = schemas.IntSchema
XFapiInteractionIdSchema = schemas.StrSchema
ResponseHeadersFor429 = typing_extensions.TypedDict(
    'ResponseHeadersFor429',
    {
        'Retry-After': RetryAfterSchema,
        'x-fapi-interaction-id': XFapiInteractionIdSchema,
    }
)


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    headers: ResponseHeadersFor429
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    headers: ResponseHeadersFor429
    body: schemas.Unset = schemas.unset


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    headers=[
        retry_after_parameter,
        x_fapi_interaction_id_parameter,
    ]
)
XFapiInteractionIdSchema = schemas.StrSchema
SchemaFor500ResponseBodyApplicationJson = OBErrorResponse1Schema
SchemaFor500ResponseBodyApplicationJosejwe = OBErrorResponse1Schema
SchemaFor500ResponseBodyApplicationJsonCharsetutf8 = OBErrorResponse1Schema
ResponseHeadersFor500 = typing_extensions.TypedDict(
    'ResponseHeadersFor500',
    {
        'x-fapi-interaction-id': XFapiInteractionIdSchema,
    }
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: OBErrorResponse1


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: OBErrorResponse1


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
        'application/jose+jwe': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJosejwe),
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJsonCharsetutf8),
    },
    headers=[
        x_fapi_interaction_id_parameter,
    ]
)
_all_accept_content_types = (
    'application/json',
    'application/jose+jwe',
    'application/json; charset=utf-8',
)


class BaseApi(api_client.Api):

    def _get_all_mapped_args(
        self,
        x_fapi_auth_date: typing.Optional[str] = None,
        x_fapi_customer_ip_address: typing.Optional[str] = None,
        x_fapi_interaction_id: typing.Optional[str] = None,
        x_customer_user_agent: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        if x_fapi_auth_date is not None:
            _header_params["x-fapi-auth-date"] = x_fapi_auth_date
        if x_fapi_customer_ip_address is not None:
            _header_params["x-fapi-customer-ip-address"] = x_fapi_customer_ip_address
        if x_fapi_interaction_id is not None:
            _header_params["x-fapi-interaction-id"] = x_fapi_interaction_id
        if x_customer_user_agent is not None:
            _header_params["x-customer-user-agent"] = x_customer_user_agent
        args.header = _header_params
        return args

    async def _aget_all_oapg(
        self,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Direct Debits
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_fapi_auth_date,
            request_header_x_fapi_customer_ip_address,
            request_header_x_fapi_interaction_id,
            request_header_x_customer_user_agent,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/direct-debits',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_all_oapg(
        self,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Direct Debits
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_fapi_auth_date,
            request_header_x_fapi_customer_ip_address,
            request_header_x_fapi_interaction_id,
            request_header_x_customer_user_agent,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/direct-debits',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetAllRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_all(
        self,
        x_fapi_auth_date: typing.Optional[str] = None,
        x_fapi_customer_ip_address: typing.Optional[str] = None,
        x_fapi_interaction_id: typing.Optional[str] = None,
        x_customer_user_agent: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_mapped_args(
            x_fapi_auth_date=x_fapi_auth_date,
            x_fapi_customer_ip_address=x_fapi_customer_ip_address,
            x_fapi_interaction_id=x_fapi_interaction_id,
            x_customer_user_agent=x_customer_user_agent,
        )
        return await self._aget_all_oapg(
            header_params=args.header,
            **kwargs,
        )
    
    def get_all(
        self,
        x_fapi_auth_date: typing.Optional[str] = None,
        x_fapi_customer_ip_address: typing.Optional[str] = None,
        x_fapi_interaction_id: typing.Optional[str] = None,
        x_customer_user_agent: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_mapped_args(
            x_fapi_auth_date=x_fapi_auth_date,
            x_fapi_customer_ip_address=x_fapi_customer_ip_address,
            x_fapi_interaction_id=x_fapi_interaction_id,
            x_customer_user_agent=x_customer_user_agent,
        )
        return self._get_all_oapg(
            header_params=args.header,
        )

class GetAll(BaseApi):

    async def aget_all(
        self,
        x_fapi_auth_date: typing.Optional[str] = None,
        x_fapi_customer_ip_address: typing.Optional[str] = None,
        x_fapi_interaction_id: typing.Optional[str] = None,
        x_customer_user_agent: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> OBReadDirectDebit2Pydantic:
        raw_response = await self.raw.aget_all(
            x_fapi_auth_date=x_fapi_auth_date,
            x_fapi_customer_ip_address=x_fapi_customer_ip_address,
            x_fapi_interaction_id=x_fapi_interaction_id,
            x_customer_user_agent=x_customer_user_agent,
            **kwargs,
        )
        if validate:
            return OBReadDirectDebit2Pydantic(**raw_response.body)
        return api_client.construct_model_instance(OBReadDirectDebit2Pydantic, raw_response.body)
    
    
    def get_all(
        self,
        x_fapi_auth_date: typing.Optional[str] = None,
        x_fapi_customer_ip_address: typing.Optional[str] = None,
        x_fapi_interaction_id: typing.Optional[str] = None,
        x_customer_user_agent: typing.Optional[str] = None,
        validate: bool = False,
    ) -> OBReadDirectDebit2Pydantic:
        raw_response = self.raw.get_all(
            x_fapi_auth_date=x_fapi_auth_date,
            x_fapi_customer_ip_address=x_fapi_customer_ip_address,
            x_fapi_interaction_id=x_fapi_interaction_id,
            x_customer_user_agent=x_customer_user_agent,
        )
        if validate:
            return OBReadDirectDebit2Pydantic(**raw_response.body)
        return api_client.construct_model_instance(OBReadDirectDebit2Pydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        x_fapi_auth_date: typing.Optional[str] = None,
        x_fapi_customer_ip_address: typing.Optional[str] = None,
        x_fapi_interaction_id: typing.Optional[str] = None,
        x_customer_user_agent: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_mapped_args(
            x_fapi_auth_date=x_fapi_auth_date,
            x_fapi_customer_ip_address=x_fapi_customer_ip_address,
            x_fapi_interaction_id=x_fapi_interaction_id,
            x_customer_user_agent=x_customer_user_agent,
        )
        return await self._aget_all_oapg(
            header_params=args.header,
            **kwargs,
        )
    
    def get(
        self,
        x_fapi_auth_date: typing.Optional[str] = None,
        x_fapi_customer_ip_address: typing.Optional[str] = None,
        x_fapi_interaction_id: typing.Optional[str] = None,
        x_customer_user_agent: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_mapped_args(
            x_fapi_auth_date=x_fapi_auth_date,
            x_fapi_customer_ip_address=x_fapi_customer_ip_address,
            x_fapi_interaction_id=x_fapi_interaction_id,
            x_customer_user_agent=x_customer_user_agent,
        )
        return self._get_all_oapg(
            header_params=args.header,
        )

