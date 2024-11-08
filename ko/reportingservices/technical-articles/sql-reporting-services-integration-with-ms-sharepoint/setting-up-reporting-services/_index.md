---
title: Reporting Services 설정하기
type: docs
weight: 20
url: /ko/reportingservices/setting-up-reporting-services/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services Server에서 처음으로 방문할 곳은 Reporting Services Configuration Manager입니다.

{{% /alert %}}

## 서비스 계정:

**Reporting Services에 어떤 서비스 계정을 사용하는지 반드시 이해해야 합니다. 문제가 발생할 경우, 사용하는 서비스 계정과 관련이 있을 수 있습니다. 기본값은 Network Service입니다. 새로운 빌드를 배포할 때, 우리는 항상 도메인 계정을 사용합니다. 그곳에서 문제가 발생할 가능성이 높기 때문입니다. 이 서버 인스턴스의 경우, RSService라는 도메인 계정을 사용했습니다.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**이미지1:- 서비스 계정 설정하기**

## 웹 서비스 URL:

{{% alert color="primary" %}}

**웹 서비스 URL을 구성해야 합니다.  이것은 Web Services Reporting Services가 사용하는 ReportServer 가상 디렉터리(vdir)이며 SharePoint가 통신할 것입니다. vdir의 속성(예: SSL, 포트, 호스트 헤더 등)을 사용자 정의하려는 것이 아니라면, 여기에서 적용을 클릭하고 진행할 수 있습니다.**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- 웹 서비스 URL 설정 웹 서비스 URL이 설정되면 다음 결과를 볼 수 있어야 합니다**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- 웹 서비스 URL의 성공적인 설정**
{{% /alert %}}

## 데이터베이스:

**Reporting Services 카탈로그 데이터베이스를 생성해야 합니다. 이는 SQL 2008 또는 SQL 2008 R2 데이터베이스 엔진에 배치할 수 있습니다. SQL11도 작동하지만 여전히 BETA 상태입니다. 이 작업은 기본적으로 두 개의 데이터베이스, ReportServer 및 ReportServerTempDB를 생성합니다.**

{{% alert color="primary" %}}
**이와 관련된 또 다른 중요한 단계는 데이터베이스 유형으로 SharePoint 통합을 선택해야 한다는 것입니다.  일단 이 선택이 이루어지면 변경할 수 없습니다.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**이미지4:- 보고서 서버 데이터베이스 생성**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**이미지5:- 데이터베이스 서버 및 인증 유형 설정**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**이미지6:- 데이터베이스 이름 및 모드 설정**
{{% /alert %}}

**자격 증명의 경우, 이것이 보고서 서버가 SQL 서버와 통신하는 방법입니다. 선택한 계정에는 카탈로그 데이터베이스와 몇몇 시스템 데이터베이스 내에서 RSExecRole을 통해 특정 권한이 부여됩니다. MSDB는 SQL 에이전트를 사용하기 때문에 구독 용도로 사용하는 데이터베이스 중 하나입니다.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**이미지7:- 보고서 서버 데이터베이스 자격 증명 설정**

{{% alert color="primary" %}}

**데이터베이스 자격 증명이 지정되면 아래에 명시된 결과를 얻을 수 있어야 합니다.**


![todo:image_alt_text](setting-up-reporting-services_8.png)
**Image8:- 보고서 서버 데이터베이스 생성 진행 상황**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- 보고서 서버 데이터베이스 완료 요약**
{{% /alert %}}

## 보고서 관리자 URL:

**SharePoint 통합 모드에서는 사용되지 않기 때문에 보고서 관리자 URL은 건너뛸 수 있습니다. SharePoint가 우리의 프론트엔드입니다. 보고서 관리자는 작동하지 않습니다.**

## 암호화 키:

{{% alert color="primary" %}}
**암호화 키를 백업하고 어디에 보관하는지 반드시 확인하십시오. 데이터베이스를 마이그레이션하거나 복원해야 하는 상황에 직면할 경우, 이 키가 필요합니다.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- 보고서 서버 암호화 키 백업**
{{% /alert %}}

{{% alert color="primary" %}}
**축하합니다! 구성 관리자를 사용하여 보고서 서비스를 성공적으로 구성했습니다. 웹 서비스 URL 탭의 URL을 탐색하면 다음과 유사한 내용이 표시될 것입니다.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- 설치 후 보고서 서버 액세스**

**오류의 원인: SharePoint가 WFE에 설치되어 있으며 Reporting Services 설정을 완료했습니다. 이 예에서는 Reporting Services와 SharePoint가 다른 기계에 있습니다. 동일한 기계에 있었다면 이 오류를 보지 않았을 것입니다. 기술적으로 RS Box에 SharePoint를 설치해야 합니다. 이는 IIS도 활성화된다는 것을 의미합니다.**  
{{% /alert %}}