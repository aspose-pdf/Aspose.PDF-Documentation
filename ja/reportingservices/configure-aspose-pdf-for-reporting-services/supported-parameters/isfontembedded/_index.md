---
title: フォントが埋め込まれています
linktitle: フォントが埋め込まれています
type: docs
weight: 50
url: /reportingservices/isfontembedded/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RS デザイナーはテキストの埋め込みフォントをサポートしていません。 Aspose.PDF for Reporting Services を使用すると、PDF ドキュメントにフォント情報を簡単に埋め込むことができます。

{{% /alert %}}

```txt
Parameter Name: IsFontEmbedded  
Date Type: Boolean  
Values supported: True, False (default)  
```

## 例

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
