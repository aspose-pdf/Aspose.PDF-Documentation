---
title: 简介
linktitle: 简介
type: docs
weight: 10
url: /zh/reportingservices/introduction/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services 多年来在通过 SQL Reporting Services 生成 PDF 方面表现卓越，并且提供了多种配置和参数化选项，这些选项在 SQL Reporting Services 中默认不受支持。最近我们收到了一些关于 Aspose.PDF for Reporting Services 与 SharePoint 集成的需求。本文将重点关注 MS SharePoint 2010。在继续之前，假设您已经搭建好了 SharePoint Farm。本文示例使用完整的 SharePoint Cloud，但对于 SharePoint Foundation Server，步骤类似。

{{% /alert %}}

{{% alert color="primary" %}}

在继续之前，让我们先看看在准备本文时参考的主题。

- [Reporting Services 与 SharePoint 技术集成概述](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Reporting Services 在 SharePoint 集成模式下的部署拓扑](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [为 SharePoint 2010 集成配置 Reporting Services](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## 环境设置

我们的设置包括 4 台服务器。它包括域控制器、SQL Server、SharePoint Server 和一台用于 Reporting Services 的服务器。您可以选择将 SharePoint 与 Reporting Services 部署在同一台机器上，这样可以简化一些，我将指出其中的一些差异。

## 安装前提条件

{{% alert color="primary" %}}

Reporting Services 的 SharePoint Add‑In 是实现集成正常工作的重要组件之一。该 Add‑In 需要安装在 SharePoint 农场中的任何 Web 前端 (WFE) 上，以及 Central Admin 服务器。SQL 2008 R2 与 SharePoint 2010 的一个新变化是，2008 R2 Add‑In 现在是 SharePoint 安装的前提条件。这意味着在安装 SharePoint 时会自动部署 RS Add‑In。下图已展示并突出显示了这一点。这实际上避免了我们在使用 SP 2007 和 RS 2008 安装 Add‑In 时遇到的许多问题。

![todo:image_alt_text](introduction_1.png)

**Image1 :- Reporting Services Share Point 加载项**
{{% /alert %}}

## SharePoint 身份验证

**在我们进入 RS 集成部分之前，我想指出关于 SharePoint 农场的一个关键点，即您如何设置站点。更具体地说，您如何为站点配置身份验证。是使用经典模式还是 Claims 模式。这个选择在起始阶段非常重要。我认为一旦完成后无法更改此选项。如果可以更改，也不是一个简单的过程。

NOTE: ***Reporting Services 2008 R2 不支持 Claims***

即使您选择将 SharePoint 站点使用 Claims，Reporting Services 本身并未实现对 Claims 的感知。话虽如此，这确实会影响 Reporting Services 的身份验证方式。那么，从 Reporting Services 的角度来看，有何区别？关键在于您是否希望将用户凭据转发到数据源。Classic:- 可以使用 Kerberos 并将用户的凭据转发到后端数据源（需要使用 Kerberos）。Claims:- 使用 Claims 令牌而非 Windows 令牌。RS 在此情形下会始终使用受信任身份验证，并且只能访问 SPUser 令牌。您需要在数据源中存储您的凭据。

Classic :- 可以使用 Kerberos 并将用户的凭据转发到后端数据源（需要使用 Kerberos）。

Claims :- 使用 Claims 令牌而非 Windows 令牌。RS 在此情形下会始终使用受信任身份验证，并且只能访问 SPUser 令牌。您需要在数据源中存储您的凭据。

目前我们只想专注于 RS 的设置。此时 SharePoint 已经安装在我的 SharePoint Box 上，并使用 Classic Auth 站点在端口 80 上进行设置。在 RS 服务器上，我刚刚安装了 Reporting Services，仅此而已。
