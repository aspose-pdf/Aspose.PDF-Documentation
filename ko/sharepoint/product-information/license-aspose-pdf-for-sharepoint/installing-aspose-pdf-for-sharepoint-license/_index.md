---
title: Aspose.Pdf for SharePoint 라이선스 설치
type: docs
weight: 10
url: ko/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: 평가가 만족스러우면 PDF SharePoint API에 대한 라이선스를 구매하고 설치 지침을 따라 적용할 수 있습니다.
---

{{% alert color="primary" %}}

평가가 만족스러우면 [라이선스를 구매](https://purchase.aspose.com/buy)할 수 있습니다. 구매하기 전에 라이선스 구독 조건을 이해하고 동의했는지 확인하십시오.

{{% /alert %}}

{{% alert color="primary" %}}

주문이 결제된 후 라이선스가 이메일로 발송됩니다. 라이선스는 일반 SharePoint 솔루션 패키지를 포함하는 .zip 아카이브입니다.
{{% /alert %}}

이 아카이브에는 다음이 포함됩니다:

- Aspose.PDF.SharePoint.License.wsp

SharePoint 솔루션 패키지 파일. Aspose.PDF for SharePoint License는 서버 팜 전체에 배포/철회를 용이하게 하기 위해 SharePoint 솔루션으로 패키징되어 있습니다.

- readme.txt

라이선스 설치 지침.
 라이선스 설치는 서버 콘솔에서 stsadm.exe를 통해 수행됩니다. 라이선스를 설치하기 위해 필요한 단계는 아래에 제시되어 있습니다.

**참고:** 경로는 명확성을 위해 생략되었습니다. 실행할 때 stsadm.exe 및/또는 솔루션 파일에 실제 경로를 추가해야 할 수도 있습니다.

1. stsadm을 실행하여 솔루션을 SharePoint 솔루션 저장소에 추가합니다:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. 농장의 모든 서버에 솔루션을 배포합니다:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. 배포를 즉시 완료하기 위해 관리 타이머 작업을 실행합니다.

stsadm.exe -o execadmsvcjobs

**참고:** Windows SharePoint Services 관리 서비스가 시작되지 않은 경우 배포 단계를 실행할 때 경고를 받게 됩니다. Stsadm.exe는 이 서비스와 Windows SharePoint Timer Service에 의존하여 솔루션 데이터를 농장 전체에 복제합니다. 이러한 서비스가 서버 농장에서 실행되지 않는 경우, 각 서버에 라이선스를 배포해야 할 수도 있습니다.