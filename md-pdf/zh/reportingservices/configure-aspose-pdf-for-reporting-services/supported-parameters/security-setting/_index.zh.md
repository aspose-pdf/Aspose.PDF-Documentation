---
title: Security Setting
type: docs
weight: 30
url: /reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

安全性一直是每个领域中最重要的问题，无论是网络保护还是 PDF 文档的保护。出于多种可能的原因，文档需要安全保护：文档的作者可能希望保持文档内容的安全，并且不希望允许其他人更改它，等等。

Aspose.Pdf for Reporting Services 在安全性方面非常注重，提供了这些功能供开发人员使用，这对他们保护 PDF 文档非常有用。因此，它包含许多参数，允许开发人员对 PDF 文档应用不同的安全措施。

其中一项措施是在加密过程中为 PDF 文档设置密码保护。 你还可以限制或允许内容修改、复制内容、文档打印或允许/禁用表单填写。这些功能目前不受默认的 SQL Reporting Services PDF 导出器支持，但您可以使用 Aspose.Pdf for Reporting Services 实现这些功能。只需将相应的安全参数添加到报告或报告服务器配置文件中，您就可以创建具有有限权限的安全 PDF 文档。

目前，Aspose.Pdf for Reporting Services 渲染器支持以下安全属性：

{{% /alert %}}

{{% alert color="primary" %}}

**Parameter Name**: User Password  
**Date Type**: String  
**Values supported**: Any plain text

**Parameter Name**: Master Password  
**Date Type**: String  
**Values supported**: Any plain text 

**Parameter Name**: IsCopyingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (default)  

**Parameter Name**: IsPrintingAllowed  
**Date Type**: Boolean  

**Values supported**: True, False (default)  
**Parameter Name**: IsContentsModifyingAllowed  
**Date Type**: 布尔值  
**Values supported**: True, False (默认)  

**Parameter Name**: IsFormFillingAllowed  
**Date Type**: 布尔值  
**Values supported**: True, False (默认)  

**Example**

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