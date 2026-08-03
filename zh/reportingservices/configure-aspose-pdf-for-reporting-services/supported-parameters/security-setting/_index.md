---
title: 安全设置
linktitle: 安全设置
type: docs
weight: 30
url: /reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

安全一直是各个领域最重要的问题，无论是网络还是 PDF 文档的保护。确保文档安全的原因有很多：文档的作者可能希望保证文档内容的安全并且不希望允许其他人更改它，等等。

Aspose.PDF for Reporting Services 非常重视此类安全方面的问题，为开发人员提供了这些功能，这些功能可帮助他们保护 PDF 文档。因此，它包含许多参数，允许开发人员对 PDF 文档应用不同的安全措施。

其中一项措施是在加密过程中使用密码保护 PDF 文档。您还可以限制或允许内容修改、复制内容、文档打印或允许/禁用表单填写。默认的 SQL Reporting Services PDF 导出器目前不支持这些功能，但您可以使用 Aspose.PDF for Reporting Services 来实现这些功能。只需将相应的安全参数添加到报表或报表服务器配置文件中，您就可以使用有限的权限创建安全的 PDF 文档。

目前，Aspose.PDF for Reporting Services 渲染器支持以下安全属性：

{{% /alert %}}

```text
Parameter Name: User Password  
Date Type: String  
Values supported: Any plain text
```

```text
Parameter Name: Master Password  
Date Type: String  
Values supported: Any plain text 
```

```text
Parameter Name: IsCopyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsPrintingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

```text
Parameter Name: IsContentsModifyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsFormFillingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

## 例子

```xml
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
```

