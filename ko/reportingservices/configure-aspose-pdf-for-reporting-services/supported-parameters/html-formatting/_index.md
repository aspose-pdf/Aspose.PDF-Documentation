---
title: HTML 형식화
linktitle: HTML 형식화
type: docs
weight: 20
url: /reportingservices/html-formatting/
description: Reporting Services용 Aspose.PDF를 사용하여 PDF 보고서에서 HTML 형식을 활성화합니다. 스타일과 구조를 쉽게 추가하세요.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

때로는 서식을 적용하여 텍스트 상자의 텍스트를 내보내고 싶을 수도 있습니다. 안타깝게도 Reporting Services는 이를 지원하지 않습니다. 그러나 Reporting Services용 Aspose.PDF를 사용하여 구현할 수 있습니다. 텍스트 상자의 모든 텍스트가 HTML로 처리되는 특수 모드를 활성화하고 필요한 HTML 태그를 넣어 출력 문서의 텍스트 형식을 지정하기만 하면 됩니다. 예를 들어, 동일한 텍스트 상자에 일반, 굵게 및 기울임꼴 텍스트를 포함하려면 다음 텍스트 상자 값을 입력하십시오.

이 텍스트 중 일부는 `<b>bold</b>`이고 다른 텍스트는 `<i>italic</i>`입니다.

내보내면 텍스트 중 일부는 **굵게**, 다른 텍스트는 *기울임꼴*로 표시됩니다.

이 접근 방식에는 몇 가지 제한 사항이 있습니다.

{{% /alert %}}

{{% alert color="primary" %}}

- 서식은 디자인 타임(보고서 작성기, 보고 서비스 웹 포털 등)에 표시되지 않습니다. 대신 태그가 포함된 일반 텍스트 형식의 HTML 텍스트가 표시됩니다.
- Reporting Services 렌더링 확장 프로그램용 Aspose.PDF는 텍스트 상자의 HTML 코드를 인식하고 적절한 형식을 지정합니다. Reporting Services의 기본 PDF 렌더러는 이 마크업을 일반 텍스트로 내보냅니다.

```text
Parameter Name: IsHtmlTagSupported  
Date Type: Boolean  
Values supported: True, False (default)   
```

## 예

```xml
<Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>
```

보고서 디자이너에 이 매개 변수를 추가하려면 `Boolean` 데이터 유형을 사용하세요.

현재 Reporting Services용 Aspose.Pdf는 모든 HTML 태그의 하위 집합을 지원합니다. Aspose.PDF [문서](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom)에서 자세한 내용을 확인할 수 있습니다.

{{% /alert %}}
