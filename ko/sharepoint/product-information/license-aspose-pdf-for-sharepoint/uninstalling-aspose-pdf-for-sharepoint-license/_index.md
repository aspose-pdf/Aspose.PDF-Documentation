---
title: Aspose.Pdf for SharePoint 라이선스 제거
linktitle: Aspose.Pdf for SharePoint 라이선스 제거
type: docs
weight: 30
url: /ko/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: PDF SharePoint API 라이선스를 제거하려면 이 문서에 언급된 단계를 따라 주세요.
---

## 제거 단계

{{% alert color="primary" %}}

Aspose.PDF for SharePoint 라이선스를 제거하려면 서버 콘솔에서 아래 단계를 사용하십시오.

1. 팜에서 라이선스 솔루션을 회수하십시오:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. 관리자 타이머 작업을 실행하여 리트랙션을 즉시 완료합니다:

  stsadm.exe -o execadmsvcjobs

3. 리트랙션이 완료될 때까지 기다리세요. Central을 사용할 수 있습니다   

  Central Administration -> Operations -> Solution Management 아래에서 리트랙션이 완료되었는지 확인하려면 관리자를 사용할 수 있습니다

4. SharePoint 솔루션 저장소에서 솔루션을 제거합니다:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
