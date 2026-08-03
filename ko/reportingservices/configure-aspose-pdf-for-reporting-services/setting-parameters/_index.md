---
title: 매개변수 설정
linktitle: 매개변수 설정
type: docs
weight: 10
url: /reportingservices/setting-parameters/
description: Reporting Services용 Aspose.PDF에서 PDF 렌더링을 위한 매개변수를 설정하는 방법을 알아보세요. 출력을 정밀하게 제어할 수 있습니다.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services용 Aspose.PDF가 문서를 생성하는 방법에 영향을 미치는 특정 구성 매개 변수를 지정할 수 있습니다. 이 섹션에서는 이 프로세스에 대해 설명합니다.

{{% /alert %}}

Reporting Services에 대해 Aspose.Pdf를 구성하려면 `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config` 파일을 편집해야 합니다. 이것은 XML 파일이며 렌더러 구성은 Aspose.PDF 렌더러에 해당하는 `<Extension>` 요소 내부에 있습니다.

## 예

```xml
<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insert configuration elements for exporting to PDF here. The following is an example
For PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>
```

{{% alert color="primary" %}}

서버의 모든 보고서가 아닌 특정 보고서 파일에 대한 매개변수를 설정하려는 경우 다음 단계에 따라 보고서 작성기에서 특정 보고서에 대한 보고서 매개변수를 추가할 수 있습니다(예를 들어 앞서 표시된 'IsLandscape' 매개변수를 추가합니다).

1. 보고서 디자이너에서 보고서를 열고 '보고서 데이터' 창에서 '매개변수' 폴더를 마우스 오른쪽 버튼으로 클릭한 다음 '매개변수 추가…'를 선택합니다(또는 '새' 목록을 풀다운하고 '매개변수…' 선택).

![Parameters set up. Step 1](setting-parameters_1.png)

1. '보고서 매개변수 속성' 대화 상자에서 데이터 유형이 부울인 'IsLandscape'라는 매개변수를 생성하고 '기본값' 탭에 True 값을 추가합니다.

![Parameters set up. Step 2](setting-parameters_2.png)

{{% /alert %}}
