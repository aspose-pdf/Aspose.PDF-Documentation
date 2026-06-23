---
title: 페이지 방향
linktitle: 페이지 방향
type: docs
weight: 10
url: /ko/reportingservices/page-orientation/
description: Aspose.PDF for Reporting Services의 PDF 보고서에 대한 페이지 방향을 구성합니다. 더욱 나은 표시를 위해 레이아웃을 사용자 지정합니다.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Definition Language는 보고서에서 페이지 방향을 명시적으로 지정하는 것을 허용하지 않습니다. Aspose.Pdf for Reporting Services를 사용하면 내보내기 프로그램에 가로 페이지 방향의 PDF 문서를 생성하도록 쉽게 지시할 수 있습니다. 기본 방향은 세로입니다.

{{% /alert %}}

{{% alert color="primary" %}}

기본 방향은 세로입니다.
**매개변수 이름**: IsLandscape
**데이터 유형**: Boolean
**지원되는 값**: True, False (default)

**예시**
{{< highlight csharp >}}
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}


