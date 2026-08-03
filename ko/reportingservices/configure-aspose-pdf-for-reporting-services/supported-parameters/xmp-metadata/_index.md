---
title: XMP 메타데이터
linktitle: XMP 메타데이터
type: docs
weight: 80
url: /reportingservices/xmp-metadata/
description: Reporting Services용 Aspose.PDF를 사용하여 PDF 보고서의 XMP 메타데이터를 관리하는 방법을 알아보세요. 문서 메타데이터 처리를 강화합니다.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services 보고서 디자이너는 문서에 XMP 메타데이터를 포함하는 것을 지원하지 않습니다. Reporting Services용 Aspose.PDF는 해당 XMP 메타데이터를 설정하는 네 가지 매개 변수를 제공합니다.

{{% /alert %}}

```text
**Parameter Name: CreationDate  
**Date Type: String  
**Values supported: Date in one of the date formats
```

```text
**Parameter Name: ModifyDate  
**Date Type: String  
**Values supported: Date in one of the date formats 
```

```text
**Parameter Name: MetaDataDate  
**Date Type: String  
**Values supported: Date in one of the date formats 
```

```text
**Parameter Name: CreatorTool  
**Date Type: String  
**Values supported: Any plain text  
```

## 예

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>
    <CreationDate>2017-12-10</CreationDate>
    <ModifyDate>2018-1-12</ModifyDate>
    <MetaDataDate>2018-3-7</MetaDataDate>
    <CreatorTool>Aspose.PDF for Reporting Services</CreatorTool>
    </Configuration>
    </Extension>
</Render>
```


