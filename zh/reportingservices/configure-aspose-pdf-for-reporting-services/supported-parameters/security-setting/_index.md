---
title: 安全设置
linktitle: 安全设置
type: docs
weight: 30
url: /zh/reportingservices/security-setting/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

安全一直是各个领域中最重要的问题，无论是网络保护还是 PDF 文档的保护。文档出于许多可能的原因需要被加密：文档的编写者可能希望保持文档内容的安全，并且不希望其他人对其进行更改，等等。

Aspose.Pdf for Reporting Services 在这些安全方面下了很大功夫，向开发人员提供了可用于保护 PDF 文档的功能。因此，它包含了许多参数，允许开发人员对 PDF 文档应用不同的安全措施。

其中一种措施是在加密过程中对 PDF 文档进行密码保护。您还可以限制或允许内容修改、复制内容、文档打印或启用/禁用表单填写。这些功能目前默认的 SQL Reporting Services PDF Exporter 并不支持，但您可以使用 Aspose.Pdf for Reporting Services 实现这些功能。只需向报表或报表服务器配置文件添加相应的安全参数，即可创建具有受限权限的安全 PDF 文档。

当前，Aspose.Pdf for Reporting Services 渲染器支持以下安全属性：

{{% /alert %}}

{{% alert color="primary" %}}

**参数名称**: 用户密码  
**日期类型**: 字符串  
**支持的值**: 任意纯文本

**参数名称**: 主密码  
**日期类型**: 字符串  
**支持的值**: 任意纯文本 

**参数名称**: IsCopyingAllowed  
**数据类型**: 布尔  
**支持的值**: True, False (default)  

**参数名称**: IsPrintingAllowed  
**数据类型**: 布尔  
**支持的值**: True, False (default)  

**参数名称**: IsContentsModifyingAllowed  
**数据类型**: 布尔  
**支持的值**: True, False (default)  

**参数名称**: IsFormFillingAllowed  
**数据类型**: 布尔  
**支持的值**: True, False (default)  

**示例**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>False</IsCopyingAllowed>
    <IsPrintingAllowed>False</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

