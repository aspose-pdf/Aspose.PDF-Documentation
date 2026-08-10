---
title: 추가 설치 세부 정보
linktitle: 추가 설치 세부 정보
type: docs
weight: 30
url: /ko/sharepoint/more-installation-details/
lastmod: "2026-08-10"
description: PDF SharePoint API 설치에 대한 추가 정보는 사이트 컬렉션에 배포, 활성화 및 비활성화하는 방법을 설명합니다.
---

## 배포

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint은 배포 중 다음 작업을 수행합니다:**
- Aspose.PDF.SharePoint.dll을 Global Assembly Cache에 설치하고 web.config 파일에 SafeControl 항목을 추가합니다.
- 특성 매니페스트와 기타 필요한 파일을 적절한 디렉터리에 설치합니다.
- SharePoint 데이터베이스에 특성을 등록하고 특성 범위에서 활성화할 수 있도록 합니다.

{{% /alert %}}

## 활성화

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint는 사이트(사이트 컬렉션) 수준의 특성으로 패키징되며 사이트 컬렉션에서 활성화 및 비활성화할 수 있습니다.**

{{% /alert %}}

{{% alert color="primary" %}}

활성화 중에, 이 특성은 사이트 컬렉션의 상위 웹 애플리케이션 가상 디렉터리에 몇 가지 변경을 수행합니다: 변환 설정 페이지를 사이트맵 파일에 추가합니다. 필요한 리소스 파일을 가상 디렉터리의 App_GlobalResources 폴더에 복사합니다.

{{% /alert %}}
