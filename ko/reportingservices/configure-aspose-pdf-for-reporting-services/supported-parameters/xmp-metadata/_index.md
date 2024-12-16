---
title: XMP 메타데이터
type: docs
weight: 80
url: /ko/reportingservices/xmp-metadata/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services 보고서 디자이너는 문서에 XMP 메타데이터를 포함하는 것을 지원하지 않습니다. Aspose.Pdf for Reporting Services는 해당 XMP 메타데이터를 설정하기 위해 네 가지 매개변수를 제공합니다. 그것들은:

{{% /alert %}}

{{% alert color="primary" %}}
**매개변수 이름**: CreationDate  
**데이터 유형**: 문자열  
**지원되는 값**: 날짜 형식 중 하나의 날짜

**매개변수 이름**: ModifyDate  
**데이터 유형**: 문자열  
**지원되는 값**: 날짜 형식 중 하나의 날짜

**매개변수 이름**: MetaDataDate  
**데이터 유형**: 문자열  
**지원되는 값**: 날짜 형식 중 하나의 날짜

**매개변수 이름**: CreatorTool  
**데이터 유형**: 문자열  
**지원되는 값**: 일반 텍스트  

**예시**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>

    <CreationDate>2017-12-10</CreationDate>
```

<ModifyDate>2018-1-12</ModifyDate>
<MetaDataDate>2018-3-7</MetaDataDate>
<CreatorTool>Aspose.Pdf for Reporting Services</CreatorTool>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```