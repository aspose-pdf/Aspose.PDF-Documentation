---
title: Reporting Services 설정
linktitle: Reporting Services 설정
type: docs
weight: 20
url: /ko/reportingservices/setting-up-reporting-services/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Reporting Services 서버에서 우리의 첫 번째 목적지는 Reporting Services 구성 관리자입니다.

{{% /alert %}}

## 서비스 계정:

**보고 서비스에 사용하는 서비스 계정을 반드시 이해하십시오. 문제가 발생하면 사용 중인 서비스 계정과 관련될 수 있습니다. 기본값은 Network Service입니다. 새 빌드를 배포할 때는 항상 도메인 계정을 사용합니다. 이는 문제가 발생하기 쉬운 지점이기 때문입니다. 이 서버 인스턴스에서는 RSService라는 도메인 계정을 사용했습니다.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Image1:- 서비스 계정 설정**

## Web Service URL:

{{% alert color="primary" %}}

**Web Service URL을 구성해야 합니다. 이는 Reporting Services에서 사용하는 Web Services를 호스팅하는 ReportServer 가상 디렉터리(vdir)이며, SharePoint가 통신하는 대상입니다. vdir의 속성(예: SSL, 포트, 호스트 헤더 등)을 사용자 지정하려는 경우가 아니라면, 여기서 Apply를 클릭하면 바로 사용할 수 있어야 합니다.**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- Web Service URL 설정 Web service URL이 설정되면, 다음 결과를 확인할 수 있어야 합니다**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- Web service URL 설정 성공**
{{% /alert %}}

## 데이터베이스:

**우리는 Reporting Services 카탈로그 데이터베이스를 생성해야 합니다. 이는 SQL 2008 또는 SQL 2008 R2 데이터베이스 엔진에 배치할 수 있습니다. SQL11도 괜찮게 작동하지만 아직 베타 단계입니다. 이 작업은 기본적으로 두 개의 데이터베이스인 ReportServer와 ReportServerTempDB를 생성합니다.**

{{% alert color="primary" %}}
**이와 관련된 또 다른 중요한 단계는 데이터베이스 유형으로 SharePoint Integrated를 선택했는지 확인하는 것입니다. 일단 이 선택을 하면 변경할 수 없습니다.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Image4:- 보고서 서버 데이터베이스 만들기**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Image5:- 데이터베이스 서버 및 인증 유형 설정**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Image6:- 데이터베이스 이름 및 모드 설정**
{{% /alert %}}

**자격 증명에 대해, 이것은 보고서 서버가 SQL Server와 통신하는 방식입니다. 선택한 계정은 RSExecRole을 통해 카탈로그 데이터베이스와 몇몇 시스템 데이터베이스에 특정 권한이 부여됩니다. MSDB는 SQL Agent를 사용하여 구독에 활용되는 데이터베이스 중 하나입니다.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Image7:- 보고서 서버 데이터베이스 자격 증명 설정**

{{% alert color="primary" %}}

**데이터베이스 자격 증명이 지정되면 아래에 명시된 결과를 얻을 수 있어야 합니다.**

![todo:image_alt_text](setting-up-reporting-services_8.png)

**Image8:- Report Server 데이터베이스 생성 진행 상황**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- Report Server 데이터베이스 완료 요약**
{{% /alert %}}

## 보고서 관리자 URL:

**SharePoint 통합 모드에서는 Report Manager URL이 사용되지 않으므로 생략할 수 있습니다. SharePoint가 프런트엔드입니다. Report Manager는 작동하지 않습니다.**

## 암호화 키:

{{% alert color="primary" %}}
**암호화 키를 백업하고 보관 위치를 반드시 확인하십시오. 데이터베이스를 마이그레이션하거나 복원해야 하는 상황이 생기면 이 키가 필요합니다.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- Report Server 암호화 키 백업**
{{% /alert %}}

{{% alert color="primary" %}}
**축하합니다! Configuration Manager를 사용하여 Reporting Services를 성공적으로 구성했습니다. Web Service URL 탭에서 URL을 탐색하면 다음과 유사한 내용이 표시됩니다.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- 설치 후 Report Server 액세스**

**오류 원인: SharePoint가 WFE에 설치되어 있고 Reporting Services 설정을 완료했습니다. 이 예에서는 Reporting Services와 SharePoint가 서로 다른 머신에 있습니다. 같은 머신에 있었다면 이 오류가 나타나지 않았을 것입니다. 기술적으로는 RS 박스에 SharePoint를 설치해야 합니다. 이는 IIS도 활성화된다는 의미입니다.**
{{% /alert %}}

