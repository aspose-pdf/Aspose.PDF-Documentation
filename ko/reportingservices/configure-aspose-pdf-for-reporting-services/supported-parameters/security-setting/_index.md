---
title: Security Setting
type: docs
weight: 30
url: ko/reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

보안은 네트워크 보호나 PDF 문서 보호 등 모든 분야에서 항상 가장 중요한 문제였습니다. 문서는 여러 가지 이유로 보안이 강화됩니다: 문서 작성자는 문서의 내용을 안전하게 유지하고 다른 사람이 변경하지 않기를 원할 수 있습니다.

Aspose.Pdf for Reporting Services는 PDF 문서를 보호하는 데 유용한 기능을 개발자에게 제공함으로써 이러한 보안 측면을 매우 주의 깊게 고려했습니다. 따라서 개발자가 PDF 문서에 다양한 보안 조치를 적용할 수 있는 여러 매개 변수를 포함하고 있습니다.

이러한 조치 중 하나는 암호화를 통해 PDF 문서를 암호로 보호하는 것입니다. 당신은 또한 콘텐츠 수정, 콘텐츠 복사, 문서 인쇄를 제한하거나 허용하거나 양식 채우기를 허용/비활성화할 수 있습니다. 이러한 기능은 기본 SQL 보고 서비스 PDF 내보내기에서는 현재 지원되지 않지만 Aspose.Pdf for Reporting Services를 사용하여 이러한 기능을 구현할 수 있습니다. 보고서 또는 보고서 서버 구성 파일에 해당 보안 매개변수를 추가하면 제한된 권한으로 안전한 PDF 문서를 만들 수 있습니다.

현재 Aspose.Pdf for Reporting Services 렌더러는 다음 보안 속성을 지원합니다:

{{% /alert %}}

{{% alert color="primary" %}}

**매개변수 이름**: 사용자 비밀번호  
**데이터 유형**: 문자열  
**지원되는 값**: 모든 일반 텍스트

**매개변수 이름**: 마스터 비밀번호  
**데이터 유형**: 문자열  
**지원되는 값**: 모든 일반 텍스트

**매개변수 이름**: 복사 허용 여부  
**데이터 유형**: 불리언  
**지원되는 값**: True, False (기본값)

**매개변수 이름**: 인쇄 허용 여부  
**데이터 유형**: 불리언  

**지원되는 값**: True, False (기본값)
**Parameter Name**: IsContentsModifyingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (기본값)  

**Parameter Name**: IsFormFillingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (기본값)  

**Example**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% /alert %}}