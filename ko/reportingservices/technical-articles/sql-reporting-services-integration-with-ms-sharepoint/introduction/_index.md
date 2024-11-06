---
title: Introduction
type: docs
weight: 10
url: ko/reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services는 SQL Reporting Services를 통한 PDF 생성에 있어 수년간 매우 주목할 만한 성과를 보였으며, SQL Reporting Services에서 기본적으로 지원하지 않는 다양한 구성 및 매개변수화 옵션을 제공합니다. 최근에 Aspose.PDF for Reporting Services의 SharePoint 통합에 대한 요청을 받았습니다. 이 기사에서는 MS SharePoint 2010에 중점을 둘 것입니다. 계속 진행하기 전에 SharePoint Farm 설정이 이미 되어 있다고 가정합니다. 이 예에서는 전체 SharePoint Cloud를 사용할 것입니다. 그러나 SharePoint Foundation Server의 경우에도 절차는 유사합니다.

{{% /alert %}}

{{% alert color="primary" %}}

계속 진행하기 전에 이 기사를 준비하는 동안 참조한 주제를 살펴보겠습니다.

- [Reporting Services 및 SharePoint 기술 통합 개요](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Deployment Topologies for Reporting Services in SharePoint Integrated Mode](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configuring Reporting Services for SharePoint 2010 Integration](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## 환경 설정

우리의 설정은 4대의 서버로 구성됩니다. 도메인 컨트롤러, SQL 서버, SharePoint 서버, 보고 서비스용 서버를 포함합니다. SharePoint와 보고 서비스를 같은 박스에 배치할 수 있으며, 이는 이 과정을 약간 단순화할 수 있고 몇 가지 차이점을 지적하겠습니다.

## 설치 전제 조건

{{% alert color="primary" %}}

SharePoint용 보고 서비스 추가 기능은 통합이 제대로 작동하도록 하는 주요 구성 요소 중 하나입니다. The Add-In needs to be installed on any of the Web Front Ends (WFE) that is in your SharePoint farm along with the Central Admin server. One of the new changes with SQL 2008 R2 & SharePoint 2010 is that the 2008 R2 Add-In is now a pre-requisite for the SharePoint Install. This means that the RS Add-In will be laid down when you go to install SharePoint. It has been shown and highlighted in figure below. This actually avoids a lot of issues we saw with SP 2007 and RS 2008 when installing the Add-In.

![todo:image_alt_text](introduction_1.png)

**Image1 :- Reporting Services Add-in for Share Point**
{{% /alert %}}

## SharePoint Authentication

**Before we jump into the RS Integration pieces, one thing I want to point out about the SharePoint Farm is how you setup the Site.**

Add-In은 중앙 관리 서버와 함께 SharePoint 팜에 있는 모든 웹 프론트 엔드(WFE)에 설치되어야 합니다. SQL 2008 R2 및 SharePoint 2010의 새로운 변경 사항 중 하나는 2008 R2 Add-In이 이제 SharePoint 설치의 사전 요구 사항이라는 것입니다. 즉, SharePoint를 설치할 때 RS Add-In이 설치됩니다. 이는 아래 그림에 표시되고 강조되었습니다. 이는 Add-In을 설치할 때 SP 2007 및 RS 2008에서 발생한 많은 문제를 실제로 피할 수 있습니다.

## SharePoint 인증

**RS 통합 부분으로 넘어가기 전에 SharePoint 팜에 대해 지적하고 싶은 한 가지는 사이트를 설정하는 방법입니다.** 더 구체적으로는 사이트에 대한 인증을 어떻게 구성하는지입니다. 클래식 또는 클레임 중 어느 것을 선택할 것인지입니다. 이 선택은 처음에 중요합니다. 이 옵션을 설정한 후에는 변경할 수 없다고 생각합니다. 만약 변경할 수 있다면, 간단한 과정은 아닐 것입니다.

참고: ***Reporting Services 2008 R2는 클레임을 인식하지 못합니다***

SharePoint 사이트를 클레임을 사용하도록 선택하더라도, Reporting Services 자체는 클레임을 인식하지 못합니다. 그렇긴 해도, 인증 방식에 영향을 미칩니다. 그렇다면, Reporting Services의 관점에서 차이점은 무엇일까요? 사용자의 자격 증명을 데이터 소스로 전달할 것인지 여부에 달려 있습니다. 클래식: Kerberos를 사용할 수 있으며 사용자의 자격 증명을 백엔드 데이터 소스로 전달할 수 있습니다(이를 위해 Kerberos를 사용해야 합니다). 클레임: 클레임 토큰이 사용되며 Windows 토큰이 아닙니다. 이 시나리오에서 RS는 항상 신뢰할 수 있는 인증을 사용하고 SPUser 토큰에만 액세스할 수 있습니다. 데이터 소스 내에 자격 증명을 저장해야 할 것입니다.

클래식: Kerberos를 사용할 수 있으며 사용자의 자격 증명을 백엔드 데이터 소스로 전달할 수 있습니다(이를 위해 Kerberos를 사용해야 합니다).
Claims :- Claims 토큰이 사용되며 윈도우 토큰은 사용되지 않습니다. 이 시나리오에서는 RS가 항상 신뢰할 수 있는 인증을 사용하며 SPUser 토큰에만 접근할 수 있습니다. 데이터 소스 내에 자격 증명을 저장해야 합니다.

현재 우리는 RS 설정에 집중하고 싶습니다. 이 시점에서 SharePoint가 내 SharePoint Box에 설치되어 있으며 포트 80에서 고전 인증 사이트와 함께 설정되었습니다. RS 서버에서는 Reporting Services만 설치되어 있습니다.