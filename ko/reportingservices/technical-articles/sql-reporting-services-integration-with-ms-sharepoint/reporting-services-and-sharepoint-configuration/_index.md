---
title: Reporting Services 및 SharePoint 구성
linktitle: Reporting Services 및 SharePoint 구성
type: docs
weight: 40
url: /ko/reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

이제 SharePoint가 RS 서버에 설치되고 구성되었으며 RS가 Reporting Services Configuration Manager를 통해 설정되었으니, Central Admin 내의 구성으로 이동할 수 있습니다. RS 2008 R2는 이 과정을 정말 간소화했습니다. 이전에는 이를 작동시키기 위해 3단계 프로세스를 수행해야 했습니다. 이제는 한 단계만 있으면 됩니다.

{{% /alert %}}

{{% alert color="primary" %}}

우리는 Central Administrator 웹 사이트로 이동한 다음 General Application Settings으로 들어갑니다. 아래쪽에 Reporting Services가 표시됩니다.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- SharePoint 구성 대화 상자

"Reporting Services Integration" 링크를 선택합니다. 다음 화면이 표시됩니다.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- 보고 서비스 통합 자격 증명 지정

{{% /alert %}}

## 웹 서비스 URL:

**우리는 Reporting Services Configuration Manager에서 찾은 보고 서버의 URL을 제공할 것입니다.**

## 인증 모드:

**인증 모드도 선택합니다. 다음 MSDN 링크에서 이들에 대해 자세히 알아볼 수 있습니다.
SharePoint 통합 모드에서 보고 서비스 보안 개요**

{{% alert color="primary" %}}

**요약하면, 사이트가 Claims 인증을 사용하고 있다면 여기에서 무엇을 선택하든 항상 Trusted Authentication을 사용하게 됩니다. Windows 자격 증명을 전달하려면 Windows Authentication을 선택해야 합니다. Trusted Authentication의 경우, 우리는 Windows 자격 증명에 의존하지 않고 SPUser 토큰을 전달합니다. 클래식 모드 사이트를 NTLM으로 구성하고 RS가 NTLM으로 설정된 경우에도 Trusted Authentication을 사용해야 합니다. Windows Authentication을 사용하고 데이터 원본에 이를 전달하려면 Kerberos가 필요합니다.**

{{% /alert %}}

## 기능 활성화:

{{% alert color="primary" %}}

**이 옵션을 사용하면 모든 사이트 컬렉션에 대해 Reporting Services를 활성화하거나, 활성화할 사이트를 선택할 수 있습니다. 이는 실제로 어떤 사이트가 Reporting Services를 사용할 수 있는지를 의미합니다. 완료되면 다음 결과가 표시됩니다**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Image3:**- Reporting Services와 SharePoint 환경의 성공적인 통합
{{% /alert %}}

{{% alert color="primary" %}}

ReportServer URL로 돌아가면, 다음과 유사한 내용을 보게 됩니다

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Image4:**- Reporting Services가 SharePoint 환경에 성공적으로 연결되었습니다

**NOTE:** ***SharePoint 사이트가 SSL로 구성된 경우 이 목록에 표시되지 않습니다. 이는 알려진 문제이며 문제가 있다는 의미는 아닙니다. 보고서는 여전히 작동해야 합니다.***
{{% /alert %}}

{{% alert color="primary" %}}

이제 두 제품을 성공적으로 통합했으므로 SharePoint 2010에서 Reporting Services를 사용할 준비가 되었습니다. 이전 버전과 마찬가지로 “Site Collection Feature”(Reporting Services Integration을 구성할 때 활성화됨)이라는 기능이 있습니다. 또한 설치 시 사이트에 추가할 3개의 콘텐츠 유형이 추가되었습니다. Image 7에서는 문서 라이브러리에 추가된 두 개의 콘텐츠 유형을 볼 수 있으며, 이를 사용하여 사용자 지정 보고서를 생성합니다, 아래 Image5에서 볼 수 있듯이.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Image5:**- Report Builder

“Reporter Builder”는 ActiveX 컨트롤이므로 아래 Image 6에서 볼 수 있듯이 서버를 통해 다운로드해야 합니다.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Image6:**- Report Builder 다운로드 및 설치
{{% /alert %}}

{{% alert color="primary" %}}

다운로드 과정이 완료되면 “Report Builder” 컨트롤을 로드합니다. 이제 아래 Image7에 표시된 것처럼 첫 번째 보고서를 디자인할 준비가 되었습니다.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Report Builder – 새 보고서 생성 마법사
{{% /alert %}}

{{% alert color="primary" %}}

보고서를 만든 후에는 SharePoint 2010에 보고서를 저장할 문서 라이브러리에 저장할 수 있습니다. 다른 콘텐츠 유형을 사용하여 데이터 원본으로 공유 연결을 만들고 이를 SharePoint의 문서 라이브러리에 저장해야 합니다. 문서 라이브러리를 만들고 해당 콘텐츠 유형을 추가한 다음, 보고서의 데이터 원본을 변경할 수 있는 연결을 사용할 수 있습니다.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Aspose.PDF for Reporting Services와 MS SharePoint의 성공적인 통합
{{% /alert %}}


