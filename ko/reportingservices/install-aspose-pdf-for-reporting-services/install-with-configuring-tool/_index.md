---
title: Configuring Tool을 사용하여 설치
linktitle: Configuring Tool을 사용하여 설치
type: docs
weight: 30
url: /ko/reportingservices/install-with-configuring-tool/
description: 구성 도구를 사용한 Aspose.PDF for Reporting Services 설치 단계별 가이드(원활한 통합을 위해)
lastmod: "2026-06-19"
---

Aspose.Pdf for Reporting Services Configuring Tool은 지원되는 모든 Report Server(RS) 버전에 대해 Aspose.Pdf for Reporting Services 확장을 구성하는 데 도움을 줄 수 있습니다. 현재 RS2016, RS2017, RS2019, RS2022 및 Power BI Report Server를 지원합니다. Configuring Tool은 .NET Framework 4.8이 필요합니다.

확장 기능을 설치하고 Report Server에 등록하려면 'Register' 작업 유형을 선택하세요. 확장 기능을 등록 취소하고 제거하려면 'Unregister' 작업 유형을 선택하세요.

![todo:image_alt_text](install-with-configuring-tool_1.png)

**다음 단계에서는 이를 자세히 사용하는 방법을 설명합니다:**

1. Aspose.Pdf for Reporting Services 확장 기능의 DLL 파일 경로를 입력하거나 찾아보세요;
1. 해당 작업 유형을 선택하세요: Register 또는 Unregister;
1. 구성하려는 Report Server 버전에 해당하는 탭을 선택하십시오. 선택한 DLL 파일이 해당 RS 버전에 맞는지 확인하십시오. 제품의 요청된 버전이 머신에 설치되지 않은 경우, 구성 도구가 팁으로 알려줍니다. 이름이 지정된 RS2016 인스턴스(기본 'MSSQLSERVER'가 아닌)를 위해 확장 기능을 구성하고 있다면, 사용자 정의 인스턴스 이름을 입력한 뒤 'Refresh' 버튼을 누르세요.
1. 아래 텍스트 상자에 표시된 구성 파일 경로와 이름이 올바른지 확인하십시오. 올바르지 않은 경우, 'Refresh' 버튼을 눌러 RS 인스턴스를 다시 찾을 수 있으며, 또는 직접 수동으로 찾아볼 수 있습니다.
1. 'Config' 버튼을 누르십시오. 도구가 이제 요청된 구성을 시도하고, 구성이 성공했는지 여부를 알려줄 것입니다.
 

