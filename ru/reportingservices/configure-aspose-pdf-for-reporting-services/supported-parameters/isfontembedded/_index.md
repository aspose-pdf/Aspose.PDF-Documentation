---
title: IsFontEmbedded
linktitle: IsFontEmbedded
type: docs
weight: 50
url: /reportingservices/isfontembedded/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RS Designer не поддерживает встроенный шрифт для текста; с помощью Aspose.PDF for Reporting Services вы можете легко вставлять информацию о шрифтах в свой PDF-документ.

{{% /alert %}}

```txt
Parameter Name: IsFontEmbedded  
Date Type: Boolean  
Values supported: True, False (default)  
```

## Пример

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
