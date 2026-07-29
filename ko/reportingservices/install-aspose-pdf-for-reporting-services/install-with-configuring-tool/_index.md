---
title: 구성 도구를 사용하여 설치
linktitle: 구성 도구를 사용하여 설치
type: docs
weight: 30
url: /ko/reportingservices/install-with-configuring-tool/
description: 구성 도구를 사용하여 Aspose.PDF for Reporting Services를 원활하게 통합하기 위한 단계별 설치 가이드.
lastmod: "2026-07-29"
---

Aspose.PDF for Reporting Services Configuring Tool은 지원되는 모든 보고서 서버(RS) 버전에 대해 Aspose.PDF for Reporting Services 확장을 구성하는 데 도움을 줍니다. 현재 RS2016, RS2017, RS2019, RS2022 및 Power BI Report Server를 지원합니다. Configuring Tool은 .NET Framework 4.8이 필요합니다.

확장 기능을 설치하고 Report Server에 등록하려면 'Register' 작업 유형을 선택하십시오. 확장을 등록 취소하고 제거하려면 'Unregister' 작업 유형을 선택하십시오.

![todo:image_alt_text](install-with-configuring-tool_1.png)

**다음 단계에서는 이를 자세히 사용하는 방법을 설명합니다:**

1. Aspose.PDF for Reporting Services 확장 기능의 DLL 파일 경로를 입력하거나 찾아보세요;
1. 해당 작업 유형을 선택하세요: Register 또는 Unregister;
1. 구성하려는 Report Server 버전에 해당하는 탭을 선택하십시오. 해당 RS 버전에 맞는 DLL 파일을 선택했는지 확인하십시오. 요청한 제품 버전이 머신에 설치되어 있지 않으면 구성 도구가 팁을 안내합니다. 이름이 지정된 RS2016 인스턴스(기본 \u0027MSSQLSERVER\u0027 인스턴스가 아님)를 위해 확장을 구성하는 경우, 사용자 지정 인스턴스 이름을 입력한 다음 \u0027Refresh\u0027 버튼을 클릭하십시오.
1. 하단 텍스트 상자에 표시되는 구성 파일 경로와 이름이 올바른지 확인하십시오. 올바르지 않을 경우 \u0027Refresh\u0027 버튼을 눌러 RS 인스턴스를 다시 찾을 수 있으며, 수동으로 찾아볼 수도 있습니다.
1. \u0027Config\u0027 버튼을 클릭하십시오. 도구가 요청된 구성을 시도하며, 구성 성공 여부를 알려드립니다.
 
