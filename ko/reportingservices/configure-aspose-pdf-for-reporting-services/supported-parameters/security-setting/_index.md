---
title: 보안 설정
linktitle: 보안 설정
type: docs
weight: 30
url: /ko/reportingservices/security-setting/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

보안은 네트워크 보호이든 PDF 문서이든 모든 분야에서 항상 가장 중요한 문제였습니다. 문서는 다양한 이유로 안전하게 보호됩니다: 문서 작성자는 문서의 내용을 안전하게 유지하고 싶으며, 다른 사람이 변경하지 못하도록 하기를 원합니다 등.

Aspose.Pdf for Reporting Services는 PDF 문서를 보호하는 데 유용한 기능들을 개발자에게 제공함으로써 이러한 보안 측면을 충분히 고려했습니다. 따라서, PDF 문서에 다양한 보안 조치를 적용할 수 있는 여러 매개 변수를 포함하고 있습니다.

이러한 조치 중 하나는 암호화 과정에서 PDF 문서를 비밀번호로 보호하는 것입니다. 또한 내용 수정, 내용 복사, 문서 인쇄를 제한하거나 허용하고, 양식 채우기를 허용하거나 비활성화할 수 있습니다. 이러한 기능은 현재 기본 SQL Reporting Services PDF 내보내기에서는 지원되지 않지만, Aspose.Pdf for Reporting Services를 사용하여 구현할 수 있습니다. 보고서 또는 보고서 서버 구성 파일에 해당 보안 매개변수를 추가하기만 하면 제한된 권한으로 보안이 강화된 PDF 문서를 만들 수 있습니다.

현재 Aspose.Pdf for Reporting Services 렌더러는 다음 보안 속성을 지원합니다:

{{% /alert %}}

{{% alert color="primary" %}}

**Parameter Name**: 사용자 비밀번호  
**Date Type**: 문자열  
**Values supported**: 모든 일반 텍스트

**Parameter Name**: 마스터 비밀번호  
**Date Type**: 문자열  
**Values supported**: 모든 일반 텍스트 

**매개변수 이름**: IsCopyingAllowed  
**데이터 유형**: Boolean  
**지원되는 값**: True, False (기본값)  

**매개변수 이름**: IsPrintingAllowed  
**데이터 유형**: Boolean  
**지원되는 값**: True, False (기본값)  

**매개변수 이름**: IsContentsModifyingAllowed  
**데이터 유형**: Boolean  
**지원되는 값**: True, False (기본값)  

**매개변수 이름**: IsFormFillingAllowed  
**데이터 유형**: Boolean  
**지원되는 값**: True, False (기본값)  

**예시**

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


