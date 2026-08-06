---
title: SharePoint 라이센스용 Aspose.PDF 설치
linktitle: SharePoint 라이센스용 Aspose.PDF 설치
type: docs
weight: 10
url: /ko/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: 평가 결과가 만족스러우면 PDF SharePoint API 라이선스를 구매하고 설치 지침에 따라 적용할 수 있습니다.
---

{{% alert color="primary" %}}

평가가 만족스러우면 다음을 수행할 수 있습니다. [라이센스를 구매하다](https://purchase.aspose.com/buy). 구매하기 전에 라이센스 구독 조건을 이해하고 동의해야 합니다.

{{% /alert %}}

{{% alert color="primary" %}}

라이센스는 주문이 결제된 후 이메일로 전송됩니다. 라이선스는 일반 SharePoint 솔루션 패키지가 포함된 .zip 아카이브입니다.

이 아카이브에는 다음이 포함되어 있습니다:

- Aspose.PDF.SharePoint.License.wsp

SharePoint 솔루션 패키지 파일. SharePoint 라이센스용 Aspose.PDF는 서버 팜 전반에 걸쳐 배포/철회를 용이하게 하기 위해 SharePoint 솔루션으로 패키지됩니다.

- 읽어보기.txt

라이센스 설치 지침. 라이센스 설치는 stsadm.exe를 통해 서버 콘솔에서 수행됩니다. 라이센스를 설치하는 데 필요한 단계는 다음과 같습니다.

**참고:** 명확성을 위해 경로는 생략되었습니다. stsadm.exe 및/또는 솔루션 파일을 실행할 때 실제 경로를 추가해야 할 수도 있습니다.

1. stsadm을 실행하여 SharePoint 솔루션 저장소에 솔루션을 추가합니다.

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. 팜의 모든 서버에 솔루션을 배포합니다.

stsadm.exe -o 배포 솔루션 - 이름 Aspose.PDF.SharePoint.License.wsp -immediate -force

3. 배포를 즉시 완료하려면 관리 타이머 작업을 실행하세요.

stsadm.exe -o execadmsvcjobs

**참고:** Windows SharePoint Services 관리 서비스가 시작되지 않은 경우 배포 단계를 실행할 때 경고가 표시됩니다. Stsadm.exe는 이 서비스와 Windows SharePoint Timer Service를 사용하여 팜 전체에 솔루션 데이터를 복제합니다. 서버 팜에서 이러한 서비스가 실행되지 않는 경우 각 서버에 라이선스를 배포해야 할 수도 있습니다.

{{% /alert %}}

