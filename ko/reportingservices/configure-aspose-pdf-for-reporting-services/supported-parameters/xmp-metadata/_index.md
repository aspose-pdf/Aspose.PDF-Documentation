---
title: XMP 메타데이터
linktitle: XMP 메타데이터
type: docs
weight: 80
url: /ko/reportingservices/xmp-metadata/
description: Aspose.PDF for Reporting Services를 사용하여 PDF 보고서에서 XMP 메타데이터를 관리하는 방법을 배우세요. 문서 메타데이터 처리를 향상시킵니다.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Reporting Services 보고서 디자이너는 문서에 XMP 메타데이터를 삽입하는 것을 지원하지 않습니다. Aspose.Pdf for Reporting Services는 해당 XMP 메타데이터를 설정하기 위한 네 가지 매개변수를 제공하며, 이들은 다음과 같습니다:

{{% /alert %}}

{{% alert color="primary" %}}
**매개변수 이름**: CreationDate  
**Date Type**: 문자열  
**Values supported**: 날짜 형식 중 하나에 해당하는 날짜

**매개변수 이름**: ModifyDate  
**Date Type**: 문자열  
**Values supported**: 날짜 형식 중 하나에 해당하는 날짜 

**매개변수 이름**: MetaDataDate  
**Date Type**: 문자열  
**Values supported**: 날짜 형식 중 하나에 해당하는 날짜 

**매개변수 이름**: CreatorTool  
**Date Type**: 문자열  
**Values supported**: 어떤 일반 텍스트든  

**예시**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>
    <CreationDate>2017-12-10</CreationDate>
    <ModifyDate>2018-1-12</ModifyDate>
    <MetaDataDate>2018-3-7</MetaDataDate>
    <CreatorTool>Aspose.Pdf for Reporting Services</CreatorTool>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}



