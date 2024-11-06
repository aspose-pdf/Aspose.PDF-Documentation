---
title: Aspose.Pdf for SharePoint 라이선스 제거
type: docs
weight: 30
url: ko/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: PDF SharePoint API 라이선스를 제거하려면 이 문서에 언급된 단계를 따르십시오.
---

## 제거 단계

{{% alert color="primary" %}}

Aspose.PDF for SharePoint 라이선스를 제거하려면 서버 콘솔에서 아래 단계를 사용하십시오.

1. 농장에서 라이선스 솔루션을 철회하십시오:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. 철회를 즉시 완료하기 위해 관리 타이머 작업을 실행하십시오:

  stsadm.exe -o execadmsvcjobs

3. 철회가 완료될 때까지 기다리십시오. 중앙 관리를 사용하여 중앙 관리 -> 운영 -> 솔루션 관리 하에서 철회가 완료되었는지 확인할 수 있습니다.

4. SharePoint 솔루션 저장소에서 솔루션을 제거하십시오:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}