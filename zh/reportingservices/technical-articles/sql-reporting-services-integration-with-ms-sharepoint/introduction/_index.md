---
title: Introduction
type: docs
weight: 10
url: zh/reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

多年来，Aspose.PDF for Reporting Services 在通过 SQL Reporting Services 生成 PDF 方面表现非常出色，并提供多种配置和参数化选项，这些选项在 SQL Reporting Services 中默认不支持。最近，我们收到了一些关于 Aspose.PDF for Reporting Services 与 SharePoint 集成的请求。对于本文，我们将重点关注 MS SharePoint 2010。在继续之前，我们假设您已经设置了 SharePoint Farm。在此示例中，我们将使用完整的 SharePoint Cloud。然而，对于 SharePoint Foundation Server，步骤是相似的。

{{% /alert %}}

{{% alert color="primary" %}}

在继续之前，让我们看看我们在准备本文过程中咨询的参考主题。

- [Reporting Services 和 SharePoint 技术集成概述](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Deployment Topologies for Reporting Services in SharePoint Integrated Mode](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configuring Reporting Services for SharePoint 2010 Integration](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## 环境设置

我们的设置由 4 台服务器组成。它包括一个域控制器、一台 SQL 服务器、一台 SharePoint 服务器和一台用于 Reporting Services 的服务器。您可以选择将 SharePoint 和 Reporting Services 安装在同一台机器上，这会使其稍微简化一些，我将指出其中的一些差异。

## 安装先决条件

{{% alert color="primary" %}}

SharePoint 的 Reporting Services 插件是使集成正常工作的关键组件之一。 The Add-In 需要安装在您的 SharePoint 场中的任何 Web 前端（WFE）上以及 Central Admin 服务器上。SQL 2008 R2 & SharePoint 2010 的一个新变化是 2008 R2 Add-In 现在是 SharePoint 安装的前提条件。这意味着，当您安装 SharePoint 时，RS Add-In 将被安装。它在下图中已显示并突出显示。这实际上避免了我们在安装 Add-In 时在 SP 2007 和 RS 2008 中看到的许多问题。

![todo:image_alt_text](introduction_1.png)

**Image1 :- Reporting Services Add-in for Share Point**
{{% /alert %}}

## SharePoint 身份验证

**在我们跳入 RS 集成部分之前，我想指出的关于 SharePoint 场的一件事是您如何设置网站。 更具体地说，您如何为站点配置身份验证。无论是经典模式还是声明模式，这一选择在开始时很重要。我认为一旦完成，您就无法更改此选项。如果可以更改，也不会是一个简单的过程。

注意：***Reporting Services 2008 R2 不支持声明***

即使您选择让 SharePoint 站点使用声明，报表服务本身也不支持声明。也就是说，它确实会影响报表服务的身份验证方式。那么，从报表服务的角度来看有什么区别？这取决于您是否希望将用户凭据转发到数据源。经典模式：- 可以使用 Kerberos 并将用户的凭据转发到您的后台数据源（需要为此使用 Kerberos）。声明模式：- 使用声明令牌而不是 Windows 令牌。在这种情况下，RS 将始终使用受信任的身份验证，并且只会访问 SPUser 令牌。您需要在数据源中存储您的凭据。

经典模式：- 可以使用 Kerberos 并将用户的凭据转发到您的后台数据源（需要为此使用 Kerberos）。
Claims :- 使用声明令牌而不是 Windows 令牌。在这种情况下，RS 将始终使用受信任的身份验证，并且只能访问 SPUser 令牌。您需要在数据源中存储您的凭据。

现在，我们只想专注于 RS 的设置。此时，我的 SharePoint 已安装在 SharePoint 服务器上，并在端口 80 上设置了经典身份验证站点。在 RS 服务器上，我刚刚安装了 Reporting Services，仅此而已。