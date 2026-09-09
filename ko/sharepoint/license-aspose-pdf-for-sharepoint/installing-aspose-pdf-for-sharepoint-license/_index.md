---
title: Aspose.PDF for SharePoint 라이선스 설치
linktitle: Aspose.PDF for SharePoint 라이선스 설치
type: docs
weight: 10
url: /ko/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2026-08-10"
description: 평가에 만족하시면 PDF SharePoint API 라이선스를 구매하고 설치 지침에 따라 적용할 수 있습니다.
---

{{% alert color="primary" %}}

평가에 만족하시면 [라이선스를 구매하십시오](https://purchase.aspose.com/buy). 구매하기 전에 라이선스 구독 조건을 이해하고 동의하는지 확인하십시오.

{{% /alert %}}

{{% alert color="primary" %}}

주문이 결제된 후 라이선스가 이메일로 발송됩니다. 라이선스는 일반 SharePoint 솔루션 패키지를 포함하는 .zip 압축 파일입니다.

이 압축 파일에는 다음이 포함됩니다:

- Aspose.PDF.SharePoint.License.wsp

SharePoint 솔루션 패키지 파일. Aspose.PDF for SharePoint 라이선스는 서버 팜 전체에 배포/철회를 용이하게 하기 위해 SharePoint 솔루션으로 패키징됩니다.

- readme.txt

라이선스 설치 지침. 라이선스 설치는 stsadm.exe를 통해 서버 콘솔에서 수행됩니다. 라이선스를 설치하는 데 필요한 단계는 아래에 나와 있습니다.

**Note:** 경로는 명확성을 위해 생략되었습니다. 실행 시 stsadm.exe 및/또는 솔루션 파일의 실제 경로를 추가해야 할 수 있습니다.

1. stsadm을 실행하여 솔루션을 SharePoint 솔루션 저장소에 추가합니다:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. 솔루션을 팜의 모든 서버에 배포합니다:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. 배포를 즉시 완료하기 위해 관리 타이머 작업을 실행합니다.

stsadm.exe -o execadmsvcjobs

**Note:** Windows SharePoint Services Administration 서비스가 시작되지 않은 경우 배포 단계 실행 시 경고가 표시됩니다. Stsadm.exe는 이 서비스와 Windows SharePoint Timer Service에 의존하여 팜 전체에 솔루션 데이터를 복제합니다. 이러한 서비스가 서버 팜에서 실행 중이 아니라면 각 서버에 라이선스를 배포해야 할 수 있습니다.

{{% /alert %}}
