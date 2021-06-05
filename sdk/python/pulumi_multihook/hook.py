# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['HookArgs', 'Hook']

@pulumi.input_type
class HookArgs:
    def __init__(__self__):
        """
        The set of arguments for constructing a Hook resource.
        """
        pass


class Hook(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        """
        Create a Hook resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[HookArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Hook resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param HookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HookArgs.__new__(HookArgs)

            __props__.__dict__["readonly_url"] = None
        super(Hook, __self__).__init__(
            'multihook:index:Hook',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="readonlyUrl")
    def readonly_url(self) -> pulumi.Output[Optional[str]]:
        """
        The hook URL.
        """
        return pulumi.get(self, "readonly_url")

