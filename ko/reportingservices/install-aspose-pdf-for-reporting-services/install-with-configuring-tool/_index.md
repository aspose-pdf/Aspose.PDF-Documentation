---
title: Configuring Tool로 설치
type: docs
weight: 30
url: /ko/reportingservices/install-with-configuring-tool/
lastmod: "2021-06-05"
---

Aspose.Pdf for Reporting Services 구성 도구는 지원되는 보고서 서버(RS) 버전에 대해 Aspose.Pdf for Reporting Services 확장을 구성하는 데 도움을 줄 수 있습니다. 현재 RS2016, RS2017, RS2019, RS2022 및 Power BI 보고서 서버를 지원합니다. 구성 도구는 .NET Framework 4.8이 필요합니다.

확장을 설치하고 보고서 서버에 등록하려면 'Register' 작업 유형을 선택하세요. 확장을 등록 취소하고 제거하려면 'Unregister' 작업 유형을 선택하세요.

![todo:image_alt_text](install-with-configuring-tool_1.png)

**다음 단계는 사용 방법을 자세히 설명합니다:**

1. Aspose.Pdf for Reporting Services 확장의 DLL 파일 경로를 입력하거나 찾아보기;
1. 해당 작업 유형 선택: Register 또는 Unregister;
1. Select the tab corresponding to the version of the Report Server you want to configure. Please ensure that you selected the DLL file that is intended for your RS version. If the requested version of the product is not installed on the machine, the configuration tool will inform you with tips. If you are configuring the extension for the named RS2016 instance (not the default 'MSSQLSERVER' one), please input the custom instance name, then press the 'Refresh' button. 1. Make sure that the configuration files paths and names shown in the bottom textboxes are correct. If they are not, you can press the 'Refresh' button to try to find the RS instance again, or you may look them up manually. 1. Press the 'Config' button. The tool will now attempt to make the requested configuration, and will inform you whether the configuration is successful or not.

버전 서버 보고서의 버전에 해당하는 탭을 선택하십시오. RS 버전에 맞는 DLL 파일을 선택했는지 확인하십시오. 이 제품의 요청된 버전이 컴퓨터에 설치되어 있지 않은 경우, 구성 도구는 팁을 제공하여 알립니다. 명명된 RS2016 인스턴스(기본 'MSSQLSERVER'가 아님)의 확장을 구성하는 경우 사용자 정의 인스턴스 이름을 입력한 다음 '새로 고침' 버튼을 누르십시오. 1. 아래 텍스트 상자에 표시된 구성 파일 경로와 이름이 올바른지 확인하십시오. 그렇지 않은 경우 '새로 고침' 버튼을 눌러 RS 인스턴스를 다시 찾거나 수동으로 검색할 수 있습니다. 1. '구성' 버튼을 누르십시오. 도구가 요청된 구성을 시도하며, 구성이 성공적인지 여부를 알려줍니다.