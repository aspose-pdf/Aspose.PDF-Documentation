---
title: 소개
linktitle: 소개
type: docs
weight: 10
url: /reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services용 Aspose.PDF는 수년 동안 SQL Reporting Services를 통한 PDF 생성에 있어 매우 뛰어난 기능을 수행했으며 SQL Reporting Services에서 기본적으로 지원되지 않는 다양한 구성 및 매개 변수화 옵션을 제공합니다. 최근 우리는 SharePoint와의 Reporting Services 통합을 위한 Aspose.PDF에 관한 요청을 받았습니다. 이 기사에서는 MS SharePoint 2010에 중점을 둘 것입니다. 더 진행하기 전에 이미 SharePoint Farm 설정이 있다고 가정합니다. 이 예에서는 전체 SharePoint Cloud를 사용하겠습니다. 그러나 단계는 SharePoint Foundation Server와 유사합니다.

{{% /alert %}}

{{% alert color="primary" %}}

더 진행하기 전에 이 기사를 준비하는 동안 참고한 참고 주제를 살펴보겠습니다.

- [보고 서비스 및 SharePoint 기술 통합 개요](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [SharePoint 통합 모드의 Reporting Services 배포 토폴로지](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [SharePoint 2010 통합을 위한 보고 서비스 구성](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## 환경설정

Out 설정은 4개의 서버로 구성됩니다. 여기에는 도메인 컨트롤러, SQL Server, SharePoint Server 및 Reporting Services용 서버가 포함됩니다. SharePoint와 Reporting Services를 동일한 상자에 포함하도록 선택할 수도 있습니다. 이렇게 하면 이 작업이 약간 단순화되고 몇 가지 차이점을 지적하겠습니다.

## 설치 전제조건

{{% alert color="primary" %}}

SharePoint용 Reporting Services 추가 기능은 통합이 제대로 작동하도록 하는 핵심 구성 요소 중 하나입니다. 추가 기능은 중앙 관리 서버와 함께 SharePoint 팜에 있는 WFE(웹 프런트 엔드)에 설치해야 합니다. SQL 2008 R2 및 SharePoint 2010의 새로운 변경 사항 중 하나는 2008 R2 추가 기능이 이제 SharePoint 설치를 위한 필수 구성 요소라는 것입니다. 이는 SharePoint를 설치할 때 RS 추가 기능이 설치된다는 의미입니다. 아래 그림에 표시되어 강조되어 있습니다. 이렇게 하면 실제로 추가 기능을 설치할 때 SP 2007 및 RS 2008에서 볼 수 있는 많은 문제를 피할 수 있습니다.

![Introduction](introduction_1.png)

**이미지1 :- Share Point용 보고 서비스 추가 기능**
{{% /alert %}}

## SharePoint 인증

**RS 통합 부분을 살펴보기 전에 SharePoint 팜에 대해 지적하고 싶은 한 가지는 사이트 설정 방법입니다. 보다 구체적으로 사이트에 대한 인증을 구성하는 방법입니다. 클래식인지 클레임인지 여부. 이 선택은 처음에 중요합니다. 나는 이 옵션이 일단 완료되면 변경할 수 있다고 믿지 않습니다. 변경할 수 있다면 간단한 과정이 아닐 것입니다.

참고: ***Reporting Services 2008 R2는 클레임을 인식하지 않습니다***

클레임을 사용하기 위해 SharePoint 사이트를 선택하더라도 Reporting Services 자체는 클레임을 인식하지 못합니다. 즉, Reporting Services에서 인증이 작동하는 방식에 영향을 미칩니다. 그렇다면 Reporting Services 관점과의 차이점은 무엇입니까? 사용자 자격 증명을 데이터 소스에 전달할지 여부가 결정됩니다. 클래식:- Kerberos를 사용하고 사용자의 자격 증명을 백엔드 데이터 소스에 전달할 수 있습니다(이를 위해서는 Kerberos를 사용해야 함). 클레임:- Windows 토큰이 아닌 클레임 토큰이 사용됩니다. RS는 이 시나리오에서 항상 신뢰할 수 있는 인증을 사용하며 SPUser 토큰에만 액세스할 수 있습니다. 데이터 소스 내에 자격 증명을 저장해야 합니다.

클래식 :- Kerberos를 사용하고 사용자의 자격 증명을 백엔드 데이터 소스에 전달할 수 있습니다(이를 위해서는 Kerberos를 사용해야 합니다.

클레임 :-Windows 토큰이 아닌 클레임 토큰이 사용됩니다. RS는 이 시나리오에서 항상 신뢰할 수 있는 인증을 사용하며 SPUser 토큰에만 액세스할 수 있습니다. 데이터 소스 내에 자격 증명을 저장해야 합니다.

지금은 RS 설정에만 집중하고 싶습니다. 이 시점에서 SharePoint는 내 SharePoint Box에 설치되고 포트 80의 클래식 인증 사이트로 설정됩니다. RS 서버에는 방금 보고 서비스를 설치했으며 그게 전부입니다.
