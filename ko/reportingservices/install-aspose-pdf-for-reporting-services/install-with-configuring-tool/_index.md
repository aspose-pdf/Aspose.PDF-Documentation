---
title: 구성 도구를 사용하여 설치
linktitle: 구성 도구를 사용하여 설치
type: docs
weight: 30
url: /reportingservices/install-with-configuring-tool/
description: 원활한 통합을 위한 구성 도구를 사용하여 Reporting Services용 Aspose.PDF를 설치하는 단계별 가이드입니다.
lastmod: "2021-06-05"
---

보고 서비스용 Aspose.PDF 구성 도구를 사용하면 지원되는 RS(보고서 서버) 버전에 대해 보고 서비스 확장용 Aspose.PDF를 구성하는 데 도움이 됩니다. 현재 RS2016, RS2017, RS2019, RS2022 및 Power BI Report Server를 지원합니다. 구성 도구에는 .NET Framework 4.8이 필요합니다.

확장을 설치하고 보고서 서버에 등록하려면 `Register` 작업 유형을 선택합니다. 확장 프로그램을 등록 취소하고 제거하려면 `Unregister` 작업 유형을 선택하세요.

![Install with configuring tool](install-with-configuring-tool_1.png)

**다음 단계에서는 사용 방법을 자세히 설명합니다.**

1. Reporting Services 확장을 위한 Aspose.PDF의 DLL 파일 경로를 입력하거나 찾아보세요.
1. 해당 작업 유형을 선택합니다: 등록 또는 등록 취소;
1. 구성하려는 보고서 서버 버전에 해당하는 탭을 선택하십시오. RS 버전용 DLL 파일을 선택했는지 확인하십시오. 요청한 제품 버전이 시스템에 설치되어 있지 않으면 구성 도구에서 팁을 알려줍니다. 명명된 RS2016 인스턴스(기본 'MSSQLSERVER' 인스턴스 아님)에 대한 확장을 구성하는 경우 사용자 정의 인스턴스 이름을 입력한 후 '새로 고침' 버튼을 누르세요.
1. 하단 텍스트 상자에 표시된 구성 파일 경로와 이름이 올바른지 확인하십시오. 그렇지 않은 경우 '새로 고침' 버튼을 눌러 RS 인스턴스를 다시 찾거나 수동으로 찾아볼 수 있습니다.
1. '구성' 버튼을 누르세요. 이제 도구는 요청된 구성을 시도하고 구성의 성공 여부를 알려줍니다.
