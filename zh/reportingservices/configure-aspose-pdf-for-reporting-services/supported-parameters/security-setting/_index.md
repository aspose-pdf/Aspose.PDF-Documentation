---
title: 安全设置
linktitle: 安全设置
type: docs
weight: 30
url: /zh/reportingservices/security-setting/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

安全始终是所有领域中最重要的问题，无论是网络保护还是 PDF 文档的保护。文档之所以被加密，可能有多种原因：文档作者可能希望保持文档内容的安全，并且不希望他人进行更改，等等。

Aspose.PDF for Reporting Services 通过向开发者提供这些可用于保护 PDF 文档的功能，对此类安全方面给予了充分关注。因此，它包含了许多参数，允许开发者对 PDF 文档实施不同的安全措施。

其中一项措施是在加密过程中对 PDF 文档进行密码保护。您还可以限制或允许内容修改、复制内容、文档打印或启用/禁用表单填写。当前默认的 SQL Reporting Services PDF 导出器不支持这些功能，但您可以使用 Aspose.PDF for Reporting Services 实现这些功能。只需在报告或报告服务器配置文件中添加相应的安全参数，即可创建具有受限权限的安全 PDF 文档。

当前，Aspose.PDF for Reporting Services 渲染器支持以下安全属性：

{{% /alert %}}

{{% alert color="primary" %}}

**参数名称**: User Password  
**日期类型**: String  
**支持的值**: Any plain text

**参数名称**: Master Password  
**日期类型**: String  
**支持的值**: Any plain text 

**参数名称**: IsCopyingAllowed  
**数据类型**: Boolean  
**支持的值**: True, False (默认)  

**参数名称**: IsPrintingAllowed  
**数据类型**: Boolean  
**支持的值**: True, False (默认)  

**参数名称**: IsContentsModifyingAllowed  
**数据类型**: Boolean  
**支持的值**: True, False (默认)  

**参数名称**: IsFormFillingAllowed  
**数据类型**: Boolean  
**支持的值**: True, False (默认)  

**示例**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>假</IsCopyingAllowed>
    <IsPrintingAllowed>假</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
