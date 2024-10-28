---
title: 페이지 방향
type: docs
weight: 10
url: /reportingservices/page-orientation/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

보고서 정의 언어는 보고서의 페이지 방향을 명시적으로 지정할 수 없습니다. Aspose.Pdf for Reporting Services를 사용하면 내보내기 프로그램에 가로 페이지 방향으로 PDF 문서를 생성하도록 쉽게 지시할 수 있습니다. 기본 방향은 세로입니다.

{{% /alert %}}

{{% alert color="primary" %}}

기본 방향은 세로입니다.
**매개변수 이름**: IsLandscape
**데이터 유형**: Boolean
**지원되는 값**: True, False (기본값)

**예제**
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