---
title: 보고 서비스 및 SharePoint 구성
linktitle: 보고 서비스 및 SharePoint 구성
type: docs
weight: 40
url: /reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

이제 SharePoint가 RS 서버에 설치 및 구성되고 RS가 Reporting Services 구성 관리자를 통해 설정 및 설정되었으므로 중앙 관리 내의 구성으로 이동할 수 있습니다. RS 2008 R2는 이 프로세스를 매우 단순화했습니다. 우리는 이것을 작동시키기 위해 수행해야 하는 3단계 프로세스를 사용했습니다. 이제 한 단계만 남았습니다.

{{% /alert %}}

{{% alert color="primary" %}}

중앙 관리자 웹 사이트로 이동한 다음 일반 응용 프로그램 설정으로 이동하려고 합니다. 아래쪽에는 보고 서비스가 표시됩니다.

![Configuration-step1](reporting-services-and-sharepoint-configuration_1.png)
**이미지1**:- SharePoint 구성 대화 상자

"보고 서비스 통합" 링크를 선택합니다. 다음 화면이 표시됩니다.

![Configuration-step2](reporting-services-and-sharepoint-configuration_2.png)
**이미지2**:- Reporting Services 통합 자격 증명 지정

{{% /alert %}}

## 웹 서비스 URL:

**보고 서비스 구성 관리자에서 찾은 보고서 서버의 URL을 제공하겠습니다.**

## 인증 모드:

**인증 모드도 선택합니다. 다음 MSDN 링크는 이것이 무엇인지 자세히 설명합니다.
SharePoint 통합 모드의 Reporting Services에 대한 보안 개요**

{{% alert color="primary" %}}

**간단히 말하면, 사이트에서 클레임 인증을 사용하는 경우 여기에서 선택한 항목에 관계없이 항상 신뢰할 수 있는 인증을 사용하게 됩니다. Windows 자격 증명을 전달하려면 Windows 인증을 선택해야 합니다. 신뢰할 수 있는 인증의 경우 Windows 자격 증명을 사용하지 않고 SPUser 토큰을 전달합니다. NTLM용 클래식 모드 사이트를 구성했고 RS가 NTLM용으로 설정된 경우에도 신뢰할 수 있는 인증을 사용하고 싶을 것입니다. Windows 인증을 사용하고 이를 데이터 소스에 전달하려면 Kerberos가 필요합니다.**

{{% /alert %}}

## 기능 활성화:

{{% alert color="primary" %}}

**이렇게 하면 모든 사이트 모음에서 보고 서비스를 활성화할 수 있는 옵션이 제공됩니다. 또는 활성화하려는 모음을 선택할 수도 있습니다. 이는 실제로 보고 서비스를 사용할 수 있는 사이트를 의미합니다. 완료되면 다음 결과가 표시됩니다**

![Configuration-step3](reporting-services-and-sharepoint-configuration_3.png)

**이미지3:**- Reporting Services와 SharePoint 환경의 성공적인 통합
{{% /alert %}}

{{% alert color="primary" %}}

ReportServer URL로 돌아가면 다음과 비슷한 내용이 표시됩니다.

![Configuration-step4](reporting-services-and-sharepoint-configuration_4.png)

**이미지4:**- Reporting Services가 SharePoint 환경과 성공적으로 연결되었습니다.

**참고:** ***SharePoint 사이트가 SSL용으로 구성된 경우 이 목록에 표시되지 않습니다. 이는 알려진 문제이며 문제가 있다는 의미는 아닙니다. 귀하의 보고서는 계속 작동할 것입니다.***
{{% /alert %}}

{{% alert color="primary" %}}

이제 두 제품을 성공적으로 통합했으므로 SharePoint 2010에서 보고 서비스를 사용할 준비가 되었습니다. 이전 버전에는 "사이트 모음 기능"에 기능(보고 서비스 통합을 구성할 때 활성화됨)이 있습니다. 또한 설치로 인해 사이트에 추가할 3가지 콘텐츠 유형이 추가되었습니다. 이미지 7에서는 아래 이미지 5에서 볼 수 있듯이 ing을 사용하여 사용자 지정 보고서를 만들기 위해 문서 라이브러리에 추가된 콘텐츠 유형 중 2개를 볼 수 있습니다.

![Configuration-step5](reporting-services-and-sharepoint-configuration_5.png)

**이미지5:**- 보고서 작성기

"Reporter Builder"는 ActiveX 컨트롤이므로 아래 이미지 6에서 볼 수 있듯이 서버를 통해 다운로드해야 합니다.

![Configuration-step6](reporting-services-and-sharepoint-configuration_6.png)

**이미지6:**- 보고서 작성기 다운로드 및 설치
{{% /alert %}}

{{% alert color="primary" %}}

다운로드 프로세스가 완료되면 "보고서 작성기" 컨트롤을 로드합니다. 이제 아래 이미지 7과 같이 첫 번째 보고서를 디자인할 준비가 되었습니다.

![Configuration-step7](reporting-services-and-sharepoint-configuration_7.png)

**이미지7:**- 보고서 작성기 – 새 보고서 생성 마법사
{{% /alert %}}

{{% alert color="primary" %}}

보고서를 만든 후에는 보고서를 SharePoint 2010에 넣기 위해 만든 문서 라이브러리에 저장할 수 있습니다. 다른 콘텐츠 형식을 사용하여 데이터 원본으로 공유 연결을 만들고 이를 SharePoint의 문서 라이브러리에 저장해야 합니다. 문서 라이브러리를 만들고 이 콘텐츠 유형을 추가한 후 연결을 사용하여 보고서의 데이터 원본을 변경할 수 있습니다.

![Configuration-step8](reporting-services-and-sharepoint-configuration_8.png)

**이미지8:**- 보고 서비스용 Aspose.PDF와 MS SharePoint의 성공적인 통합
{{% /alert %}}

