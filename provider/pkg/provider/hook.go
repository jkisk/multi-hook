// Copyright 2016-2021, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package provider

import (
	github "github.com/pulumi/pulumi-github/sdk/v4/go/github"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The set of arguments for creating a Githhub webhook component resource.
type HookArgs struct {
	Org   pulumi.stringInput `pulumi:"org"`
	Repo  pulumi.StringInput `pulumi:"repo"`
	Token pulumi.SecretInput `pulumi:"token"`
}

// The GHWebhook component resource.
type Hook struct {
	pulumi.ResourceState

	Hook        *github.Hook        `pulumi:"hook"`
	readOnlyUrl pulumi.StringOutput `pulumi:"readonlyUrl"`
}

// NewHook creates a new...
func NewHook(ctx *pulumi.Context,
	name string, args *HookArgs, opts ...pulumi.ResourceOption) (*Hook, error) {
	if args == nil {
		args = &HookArgs{}
	}

	component := &Hook{}
	err := ctx.RegisterComponentResource("multihook:index:Hook", name, component, opts...)
	if err != nil {
		return nil, err
	}

	return component, nil
}
