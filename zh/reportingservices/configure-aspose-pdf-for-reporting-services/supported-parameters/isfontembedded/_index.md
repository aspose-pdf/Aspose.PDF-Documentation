---
title: 是否嵌入字体
linktitle: 是否嵌入字体
type: docs
weight: 50
url: /reportingservices/isfontembedded/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RS Designer 不支持文本的嵌入字体；使用 Aspose.PDF for Reporting Services，您可以轻松地将字体信息嵌入到 PDF 文档中。

{{% /alert %}}

```txt
Parameter Name: IsFontEmbedded  
Date Type: Boolean  
Values supported: True, False (default)  
```

## 例子

```xml
<Render>
...
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsFontEmbedded>True</IsFontEmbedded>
    </Configuration>
    </Extension>
</Render>
```
