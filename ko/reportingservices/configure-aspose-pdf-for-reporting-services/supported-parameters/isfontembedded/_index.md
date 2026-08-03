---
title: IsFont임베디드
linktitle: IsFont임베디드
type: docs
weight: 50
url: /reportingservices/isfontembedded/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RS 디자이너는 텍스트에 포함된 글꼴을 지원하지 않습니다. Reporting Services용 Aspose.PDF를 사용하면 PDF 문서에 글꼴 정보를 쉽게 포함할 수 있습니다.

{{% /alert %}}

```txt
Parameter Name: IsFontEmbedded  
Date Type: Boolean  
Values supported: True, False (default)  
```

## 예

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
