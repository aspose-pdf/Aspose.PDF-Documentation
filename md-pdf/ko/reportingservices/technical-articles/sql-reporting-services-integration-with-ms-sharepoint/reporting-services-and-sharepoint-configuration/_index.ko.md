---
title: Reporting Services 및 SharePoint 구성
type: docs
weight: 40
url: /reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

이제 SharePoint가 RS 서버에 설치되고 구성되었으며, RS가 Reporting Services 구성 관리자를 통해 설정되고 구성되었으므로 중앙 관리 내에서 구성을 계속 진행할 수 있습니다. RS 2008 R2는 이 과정을 정말 간소화했습니다. 예전에는 이 작업을 수행하기 위해 3단계 과정을 거쳐야 했지만, 이제는 단 한 단계만 필요합니다.

{{% /alert %}}

{{% alert color="primary" %}}

중앙 관리자 웹 사이트로 이동한 후 일반 응용 프로그램 설정으로 들어가고 싶습니다. 하단 쪽에 Reporting Services가 표시됩니다.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- SharePoint 구성 대화상자

"Reporting Services 통합" 링크를 선택하십시오. 다음 화면이 표시됩니다.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)

**Image2**:- Reporting Services 통합 자격 증명 지정

{{% /alert %}}

## 웹 서비스 URL:

**Reporting Services 구성 관리자에서 찾은 보고서 서버의 URL을 제공합니다.**

## 인증 모드:

**인증 모드를 선택합니다. 다음 MSDN 링크는 이러한 모드에 대해 자세히 설명합니다.
SharePoint 통합 모드에서의 Reporting Services에 대한 보안 개요**

{{% alert color="primary" %}}

**간단히 말해, 사이트가 Claims 인증을 사용하는 경우, 여기에서 선택한 것과 상관없이 항상 신뢰할 수 있는 인증을 사용하게 됩니다. Windows 자격 증명을 전달하려면 Windows 인증을 선택하세요. 신뢰할 수 있는 인증의 경우 SPUser 토큰을 전달하고 Windows 자격 증명에 의존하지 않습니다. 클래식 모드 사이트를 NTLM으로 구성하고 RS가 NTLM으로 설정된 경우에도 신뢰할 수 있는 인증을 사용하고 싶을 것입니다. Windows 인증을 사용하고 데이터 소스를 통해 이를 전달하려면 Kerberos가 필요합니다.**

{{% /alert %}}

## 기능 활성화:

{{% alert color="primary" %}}

**모든 사이트 컬렉션에서 보고 서비스 활성화를 선택할 수 있는 옵션을 제공합니다. 또는 활성화할 사이트를 선택할 수 있습니다. 이는 실제로 어떤 사이트가 보고 서비스를 사용할 수 있는지를 의미합니다. 완료되면 다음과 같은 결과를 볼 수 있습니다.**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**이미지3:**- SharePoint 환경과의 보고 서비스의 성공적인 통합
{{% /alert %}}

{{% alert color="primary" %}}

ReportServer URL로 돌아가면 다음과 유사한 것을 볼 수 있습니다.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**이미지4:**- 보고 서비스가 SharePoint 환경과 성공적으로 연결됨

**참고:** ***SharePoint 사이트가 SSL로 구성된 경우, 이 목록에 표시되지 않을 것입니다. 이는 알려진 문제이며 문제가 있다는 것을 의미하지 않습니다. 보고서는 여전히 작동해야 합니다.***
{{% /alert %}}
{{% alert color="primary" %}}

이제 두 제품을 성공적으로 통합했으므로 SharePoint 2010에서 보고서 서비스를 사용할 준비가 되었습니다. 이전 버전과 마찬가지로 "사이트 컬렉션 기능"에서 보고서 서비스 통합을 구성할 때 활성화되는 기능이 있습니다. 또한 설치 과정에서 사이트에 추가할 수 있는 3개의 콘텐츠 유형이 추가되었습니다. 이미지 7에서 문서 라이브러리에 추가된 2개의 콘텐츠 유형을 확인할 수 있으며, 아래 이미지 5에서 볼 수 있듯이 사용자 정의 보고서를 생성할 수 있습니다.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Image5:**- 리포트 빌더

"리포트 빌더"는 ActiveX 컨트롤이므로 서버를 통해 다운로드해야 하며, 아래 이미지 6에서 볼 수 있습니다.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Image6:**- 리포트 빌더 다운로드 및 설치
{{% /alert %}}

{{% alert color="primary" %}}

다운로드 과정이 완료되면 "리포트 빌더" 컨트롤을 로드합니다. 이제 아래 이미지 7에 표시된 대로 첫 번째 보고서를 디자인할 준비가 되었습니다.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- 보고서 작성기 – 새 보고서 생성 마법사
{{% /alert %}}

{{% alert color="primary" %}}

보고서를 생성한 후에는 SharePoint 2010에 보고서를 저장하기 위해 생성된 문서 라이브러리에 저장할 수 있습니다. 다른 콘텐츠 유형은 데이터 소스로 공유 연결을 생성하고 이를 SharePoint의 문서 라이브러리에 저장하는 데 사용해야 합니다. 문서 라이브러리를 생성하고 이 콘텐츠 유형을 추가한 후에는 보고서의 데이터 소스를 변경할 수 있는 연결을 사용할 수 있습니다.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Aspose.PDF for Reporting Services와 MS SharePoint의 성공적인 통합
{{% /alert %}}