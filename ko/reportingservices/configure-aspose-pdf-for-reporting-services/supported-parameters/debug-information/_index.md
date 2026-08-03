---
title: 디버그 정보
linktitle: 디버그 정보
type: docs
weight: 90
url: /reportingservices/debug-information/
description: Reporting Services용 Aspose.PDF에서 PDF 렌더링에 대한 디버그 정보에 액세스하고 분석하여 문제를 효과적으로 해결합니다.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

렌더링이나 렌더링 결과에 문제가 있는 것은 불가피합니다. 보안이나 개인 정보 보호 등의 이유로 인해 사용자의 보고서에 사용된 데이터 소스를 얻을 수 없어 보고서에서 오류를 재현할 수 없었습니다. 고객과 개발자 간의 커뮤니케이션을 보다 쉽고 원활하게 하기 위해 이 매개변수를 추가합니다. Reporting Services용 Aspose.PDF를 사용하여 보고서를 렌더링할 때 문제가 발생하는 경우 이 보고서 매개 변수를 설정하면 XML 형식으로 렌더링된 문서를 받게 됩니다. 그런 다음 제품 포럼에 XML 파일을 게시해 주세요.

{{% /alert %}}

{{% alert color="primary" %}}

```txt
Parameter Name: SavingXmlFormat
Date Type: Boolean  
Values supported**: True, False (default)
```

## 예

```xml
<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>
```

{{% /alert %}}
