---
title: 介绍
linktitle: 介绍
type: docs
weight: 10
url: /zh/reportingservices/introduction/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services 多年来在通过 SQL Reporting Services 生成 PDF 方面表现出色，并提供了多种配置和参数化选项，这些选项在 SQL Reporting Services 中默认不支持。最近我们收到了一些关于 Aspose.PDF for Reporting Services 与 SharePoint 集成的请求。本文将重点关注 MS SharePoint 2010。在继续之前，假设您已经搭建了 SharePoint Farm。在本例中我们将使用完整的 SharePoint Cloud。不过这些步骤在 SharePoint Foundation Server 上也类似。

{{% /alert %}}

{{% alert color="primary" %}}

在继续之前，让我们先看看在准备本文时参考的主题。

- [Reporting Services 与 SharePoint 技术集成概览](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [在 SharePoint 集成模式下的 Reporting Services 部署拓扑](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [为 SharePoint 2010 集成配置 Reporting Services](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## 环境设置

我们的设置包括 4 台服务器。它包括域控制器、SQL Server、SharePoint Server 和一台用于 Reporting Services 的服务器。您可以选择在同一台机器上同时运行 SharePoint 和 Reporting Services，这将稍微简化部署，我会指出其中的一些差异。

## 安装前提条件

{{% alert color="primary" %}}

Reporting Services 的 SharePoint 插件是实现集成正常运行的关键组件之一。该插件需安装在 SharePoint 农场中的任何 Web Front Ends (WFE) 上，同时也需要在 Central Admin 服务器上安装。SQL 2008 R2 与 SharePoint 2010 的一个新变化是，2008 R2 插件现在成为 SharePoint 安装的前提条件。这意味着在您安装 SharePoint 时会自动部署 RS 插件。下图已展示并突出显示了这一点。实际上，这避免了我们在安装插件时在 SP 2007 与 RS 2008 上遇到的许多问题。

![todo:image_alt_text](introduction_1.png)

**Image1 :- SharePoint 的 Reporting Services 加载项**
{{% /alert %}}

## SharePoint 身份验证

**在我们进入 RS 集成部分之前，我想指出关于 SharePoint 农场的一个问题，即您如何设置站点。更具体地说，您如何配置站点的身份验证。是使用经典模式还是声明模式。此选择在开始时非常重要。我认为一旦完成后就无法更改此选项。如果可以更改，也不是一个简单的过程。**

NOTE: ***Reporting Services 2008 R2 不支持声明模式***

即使您选择将 SharePoint 站点设置为使用 Claims，Reporting Services 本身并不具备 Claims 感知能力。不过，这会影响 Reporting Services 的身份验证方式。那么，从 Reporting Services 的角度来看有什么区别？关键在于您是否想将用户凭据转发到数据源。Classic:- 可以使用 Kerberos 并将用户的凭据转发到后端数据源（需要使用 Kerberos）。Claims:- 使用 Claims 令牌而不是 Windows 令牌。RS 将始终在此情形下使用受信任身份验证，并且只能访问 SPUser 令牌。您需要在数据源中存储您的凭据。

Classic :- 可以使用 Kerberos 并将用户的凭据转发到后端数据源（需要使用 Kerberos）。

Claims :- 使用 Claims 令牌而不是 Windows 令牌。RS 将始终在此情形下使用受信任身份验证，并且只能访问 SPUser 令牌。您需要在数据源中存储您的凭据。

目前我们只想专注于 RS 的设置。此时 SharePoint 已安装在我的 SharePoint 服务器上，并在端口 80 上设置了 Classic Auth 站点。在 RS 服务器上，我刚刚安装了 Reporting Services，仅此而已。

