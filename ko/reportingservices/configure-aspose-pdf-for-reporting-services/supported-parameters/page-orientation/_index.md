---
title: 페이지 방향
linktitle: 페이지 방향
type: docs
weight: 10
url: /reportingservices/page-orientation/
description: Reporting Services용 Aspose.PDF에서 PDF 보고서의 페이지 방향을 구성합니다. 더 나은 프레젠테이션을 위해 레이아웃을 사용자 정의하세요.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

보고서 정의 언어에서는 보고서의 페이지 방향을 명시적으로 지정할 수 없습니다. Reporting Services용 Aspose.PDF를 사용하면 수출자에게 가로 페이지 방향의 PDF 문서를 생성하도록 쉽게 지시할 수 있습니다. 기본 방향은 세로입니다.

{{% /alert %}}

```text
The default orientation is portrait.
Parameter Name: IsLandscape
Date Type: Boolean
Values supported: True, False (default)
```

## 예

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>
```

