---
title: SharePoint 라이센스용 Aspose.PDF 제거
linktitle: SharePoint 라이센스용 Aspose.PDF 제거
type: docs
weight: 30
url: /ko/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: PDF SharePoint API 라이센스를 제거하려면 이 문서에 언급된 단계를 따르십시오.
---

## 제거 단계

{{% alert color="primary" %}}

SharePoint 라이센스용 Aspose.PDF를 제거하려면 서버 콘솔에서 아래 단계를 사용하십시오.

1. 팜에서 라이선스 솔루션을 철회합니다.

  stsadm.exe -o 철회 솔루션 - 이름 Aspose.PDF.SharePoint.License.wsp -즉시

2. 철회를 즉시 완료하려면 관리 타이머 작업을 실행하세요.

  stsadm.exe -o execadmsvcjobs

3. 철회가 완료될 때까지 기다리십시오. 센트럴을 이용하시면 됩니다   

  중앙 관리 -> 운영 -> 솔루션 관리에서 철회 완료 여부를 확인하는 관리

4. SharePoint 솔루션 저장소에서 솔루션을 제거합니다.

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}

