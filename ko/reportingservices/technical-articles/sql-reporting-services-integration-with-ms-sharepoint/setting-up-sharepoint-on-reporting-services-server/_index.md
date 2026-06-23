---
title: 보고 서비스 서버에 SharePoint 설정
linktitle: 보고 서비스 서버에 SharePoint 설정
type: docs
weight: 30
url: /ko/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

이제 SharePoint WFE에서 수행한 것과 유사한 단계를 진행해야 합니다. 첫 번째는 Prereq uisites 설치를 수행하고, 완료되면 SharePoint setup을 시작합니다.

{{% /alert %}}

설정을 위해 저는 Server Farm을 선택하고 SharePoint Box에 맞게 전체 설치를 합니다. SharePoint에 대한 독립형 설치를 원하지 않기 때문입니다.

## SharePoint 구성

{{% alert color="primary" %}}

**SharePoint 구성 마법사에서 기존 팜에 연결하고자 합니다.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Image1:- SharePoint 구성 마법사**
{{% /alert %}}

{{% alert color="primary" %}}

**그런 다음 우리 팜이 사용 중인 SharePoint_Config 데이터베이스를 지정합니다. 이 위치를 모른다면 중앙 관리에서 시스템 설정 -> Manager Servers 를 통해 이 팜에서 확인할 수 있습니다.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2:- 데이터베이스 구성 설정 지정**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3:- SharePoint 구성 마법사**
{{% /alert %}}

{{% alert color="primary" %}}

**마법사가 완료되면 현재는 Report Server 박스에서 해야 할 일은 이것뿐입니다. ReportServer URL로 돌아가면 또 다른 오류가 보이게 되는데, 이는 중앙 관리자(Central Administrator)를 통해 구성하지 않았기 때문입니다.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- 보고서 서버 오류**
{{% /alert %}}

