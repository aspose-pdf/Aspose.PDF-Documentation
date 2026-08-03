---
title: 보안 설정
linktitle: 보안 설정
type: docs
weight: 30
url: /reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

네트워크 보호, PDF 문서 보호 등 모든 분야에서 보안은 항상 가장 중요한 문제였습니다. 문서는 여러 가지 이유로 안전하게 만들어집니다. 문서 작성자는 문서의 내용을 안전하게 유지하고 다른 사람이 이를 변경하는 것을 허용하지 않기를 원할 수 있습니다.

Reporting Services용 Aspose.PDF는 개발자에게 PDF 문서를 보호하는 데 유용할 수 있는 이러한 기능을 제공함으로써 이러한 보안 측면에 많은 관심을 기울였습니다. 따라서 여기에는 개발자가 PDF 문서에 다양한 보안 조치를 적용할 수 있는 다양한 매개변수가 포함되어 있습니다.

이러한 조치 중 하나는 암호화 중에 PDF 문서를 암호로 보호하는 것입니다. 또한 콘텐츠 수정, 콘텐츠 복사, 문서 인쇄를 제한하거나 허용하거나 양식 작성을 허용/비활성화할 수 있습니다. 이러한 기능은 현재 기본 SQL Reporting Services PDF 내보내기에서 지원되지 않지만 Reporting Services용 Aspose.PDF를 사용하여 이러한 기능을 구현할 수 있습니다. 해당 보안 매개변수를 보고서 또는 보고서 서버 구성 파일에 추가하기만 하면 제한된 권한으로 안전한 PDF 문서를 만들 수 있습니다.

현재 Reporting Services 렌더러용 Aspose.PDF는 다음 보안 속성을 지원합니다.

{{% /alert %}}

```text
Parameter Name: User Password  
Date Type: String  
Values supported: Any plain text
```

```text
Parameter Name: Master Password  
Date Type: String  
Values supported: Any plain text 
```

```text
Parameter Name: IsCopyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsPrintingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

```text
Parameter Name: IsContentsModifyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsFormFillingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

## 예

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>False</IsCopyingAllowed>
    <IsPrintingAllowed>False</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>
```

