---
title: Reporting Services 서버에서 SharePoint 설정
type: docs
weight: 30
url: ko/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

이제 SharePoint WFE에서 수행한 것과 유사한 단계를 수행해야 합니다. 첫 번째로 사전 요구 사항을 설치하고 완료되면 SharePoint 설정을 시작합니다.

{{% /alert %}}

설정에서는 Server Farm과 전체 설치를 선택하여 SharePoint Box와 일치시키고, SharePoint의 독립 실행형 설치를 원하지 않습니다.

## SharePoint 구성

{{% alert color="primary" %}}

**SharePoint 구성 마법사에서 기존 농장에 연결하려고 합니다.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**이미지1:- SharePoint 구성 마법사**
{{% /alert %}}

{{% alert color="primary" %}}

**그 다음으로 우리 농장이 사용하고 있는 SharePoint_Config 데이터베이스를 가리킵니다.**
```  이 위치를 모르는 경우 중앙 관리의 시스템 설정 -> 이 농장의 서버 관리에서 확인할 수 있습니다.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**이미지2:- 데이터베이스 구성 설정 지정**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**이미지3:- SharePoint 구성 마법사**
{{% /alert %}}

{{% alert color="primary" %}}

**마법사가 완료되면, 이제 보고서 서버 박스에서 해야 할 모든 작업이 완료됩니다. ReportServer URL로 돌아가면 또 다른 오류가 나타나겠지만, 이는 중앙 관리자를 통해 구성하지 않았기 때문입니다.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**이미지4:- 보고서 서버 오류**
{{% /alert %}}