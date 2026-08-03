---
title: 보고서 서버에 설치
linktitle: 보고서 서버에 설치
type: docs
weight: 10
url: /reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

MSI 설치 프로그램을 사용하지 않고 Reporting Services용 Aspose.PDF를 수동으로 설치하는 경우에만 다음 단계를 수행하면 됩니다. MSI 설치 프로그램은 필요한 모든 설치 및 등록 작업을 자동으로 수행합니다.

{{% /alert %}}

다음 단계에서는 Microsoft SQL Server Reporting Services가 설치된 디렉터리에서 파일을 복사하고 수정해야 합니다. SSRS 2016 어셈블리는 zip 패키지의 \Bin\SSRS2016 디렉터리에 있습니다. SSRS 2017 어셈블리는 \Bin\SSRS2017 디렉터리에 있습니다. SSRS 2019 어셈블리는 \Bin\SSRS2019 디렉터리에 있습니다. SSRS 2022 어셈블리는 \Bin\SSRS2022 디렉터리에 있습니다. Power BI Report Server 어셈블리는 \Bin\PowerBI 디렉터리에 있습니다.

**1단계.** 보고서 서버 설치 디렉터리를 찾습니다. Microsoft SQL Server의 루트 디렉터리는 일반적으로 C:\Program Files\Microsoft SQL Server입니다. Reporting Services 2016, Reporting Services 2017 이상 및 Power BI Report Server의 추가 프로세스는 약간 다릅니다.

- 보고서 서버 2016은 기본적으로 C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer 디렉터리에 설치됩니다. 기본 인스턴스 대신 명명된 사용자 지정 인스턴스를 사용하는 경우 기본 경로는 C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer입니다.
- 보고서 서버 2017 이상은 기본적으로 C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer 디렉터리에 설치됩니다.
- Power BI Report Server는 기본적으로 C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer 디렉터리에 설치됩니다.

다음 텍스트에서 보고 서비스의 설치 디렉터리(앞서 언급한 경로 중 하나)는 `<Instance>`으로 참조됩니다.

**2단계.** 해당 SSRS 버전에 대한 Aspose.Pdf.ReportingServices.dll을 `<Instance>\bin` 폴더에 복사합니다.

**3단계.** Reporting Services용 Aspose.PDF를 렌더링 확장 프로그램으로 등록합니다. `<Instance>\rsreportserver.config` 파일을 열고 `<Render>` 요소에 다음 줄을 추가합니다.

## 예

```xml
<Render>
...
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>
</Render>
```

**4단계.** 실행 권한이 있는 Reporting Services용 Aspose.PDF를 제공합니다. `<Instance>\rssrvpolicy.config` 파일을 열고 다음 텍스트를 `<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):`이어야 하는 외부 `<CodeGroup>` 요소의 두 번째 마지막 항목으로 추가합니다.

## 예

```xml

 <CodeGroup>
...

<CodeGroup>
...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="This code group grants full trust to the AP4SSRS assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--End here. -->

</CodeGroup>

</CodeGroup>
```

**5단계.** Reporting Services용 Aspose.PDF가 성공적으로 설치되었는지 확인합니다. Reporting Services 웹 포털을 열고 보고서에 사용 가능한 내보내기 형식 목록을 확인하세요. 웹 브라우저를 시작하고 주소 표시줄에 보고 서비스 웹 포털 URL(기본적으로 http://@@KEEP_0@@/reports/).)을 입력하여 웹 포털을 시작할 수 있습니다. 웹 포털에서 사용할 수 있는 보고서 중 하나를 선택하고 내보내기 드롭다운 목록을 당겨서 웹 포털을 시작할 수 있습니다. 보고 서비스 확장을 위한 Aspose.PDF에서 제공하는 형식을 포함하여 내보내기 형식 목록이 표시되어야 합니다. Aspose.PDF 항목을 통해 PDF를 선택하세요.

![Install to report server](install-to-report-server_1.png)

선택한 항목을 클릭하세요. 선택한 형식으로 보고서를 생성하여 클라이언트에 보내고, 웹 브라우저 설정에 따라 내보낸 보고서를 저장할 위치를 선택할 수 있는 파일 저장 대화 상자를 표시하거나 파일을 다운로드 폴더에 자동으로 다운로드합니다.

축하합니다. Reporting Services용 Aspose.PDF를 성공적으로 설치하고 보고서를 PDF 문서로 내보냈습니다!


