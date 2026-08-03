---
title: 介绍
linktitle: 介绍
type: docs
weight: 10
url: /reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

多年来，Aspose.PDF for Reporting Services 在通过 SQL Reporting Services 生成 PDF 方面表现非常出色，它提供了 SQL Reporting Services 默认情况下不支持的各种配置和参数化选项。最近，我们收到了一些有关 Aspose.PDF 与 SharePoint 集成 Reporting Services 的请求。在本文中，我们将重点关注 MS SharePoint 2010。在继续之前，我们假设您已经设置了 SharePoint 场。在此示例中，我们将使用完整的 SharePoint Cloud。不过，SharePoint Foundation Server 的步骤类似。

{{% /alert %}}

{{% alert color="primary" %}}

在继续之前，让我们先看一下在准备本文期间参考过的参考主题。

- [Reporting Services 和 SharePoint 技术集成概述](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [SharePoint 集成模式下 Reporting Services 的部署拓扑](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [为 SharePoint 2010 集成配置 Reporting Services](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## 环境设置

输出设置由 4 台服务器组成。它包括域控制器、SQL Server、SharePoint Server 和 Reporting Services 服务器。您可以选择将 SharePoint 和 Reporting Services 放在同一个盒子上，这会稍微简化这一点，我将指出一些差异。

## 安装先决条件

{{% alert color="primary" %}}

SharePoint 的 Reporting Services 外接程序是使集成正常工作的关键组件之一。该加载项需要与中央管理服务器一起安装在 SharePoint 场中的任何 Web 前端 (WFE) 上。 SQL 2008 R2 和 SharePoint 2010 的新变化之一是 2008 R2 加载项现在是 SharePoint 安装的先决条件。这意味着当您安装 SharePoint 时，将安装 RS 加载项。它已在下图中显示并突出显示。这实际上避免了我们在安装插件时在 SP 2007 和 RS 2008 中看到的许多问题。

![Introduction](introduction_1.png)

**图片 1：- Share Point 的报告服务插件**
{{% /alert %}}

## SharePoint 身份验证

**在我们开始讨论 RS 集成部分之前，我想指出有关 SharePoint 场的一件事是如何设置站点。更具体地说，如何配置站点的身份验证。无论是经典还是索赔。这个选择在一开始就很重要。我不认为完成后您可以更改此选项。如果你能改变它，这将不是一个简单的过程。

注意：***Reporting Services 2008 R2 不支持声明***

即使您选择 SharePoint 网站使用声明，Reporting Services 本身也无法识别声明。也就是说，它确实会影响身份验证与 Reporting Services 的配合方式。那么，从 Reporting Services 的角度来看有什么区别呢？这取决于您是否要将用户凭据转发到数据源。经典：- 可以使用 Kerberos 并将用户的凭据转发到后端数据源（为此需要使用 Kerberos）。声明：- 使用声明令牌而不是 Windows 令牌。在这种情况下，RS 将始终使用受信任的身份验证，并且只能访问 SPUser 令牌。您需要将您的凭据存储在数据源中。

经典：- 可以使用 Kerberos 并将用户的凭据转发到后端数据源（为此需要使用 Kerberos。

声明：- 使用声明令牌而不是 Windows 令牌。在这种情况下，RS 将始终使用受信任的身份验证，并且只能访问 SPUser 令牌。您需要将您的凭据存储在数据源中。

现在我们只想关注 RS 的设置。此时，SharePoint 已安装在我的 SharePoint Box 上，并在端口 80 上设置了经典身份验证站点。在 RS 服务器上，我刚刚安装了 Reporting Services，仅此而已。
