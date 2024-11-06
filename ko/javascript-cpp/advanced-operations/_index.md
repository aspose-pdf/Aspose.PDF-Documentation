---
title: C++를 통한 JavaScript를 사용한 고급 작업
linktitle: 고급 작업
type: docs
weight: 60
url: ko/javascript-cpp/advanced-operations/
description: C++를 통한 JavaScript용 Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**고급 작업**은 [기본 작업](/pdf/javascript-cpp/basic-operations/)에서 다룬 Aspose.PDF로 생성된 문서든, Adobe Acrobat, Google Docs, Microsoft Office, Open Office 또는 기타 PDF 제작자로 생성된 PDF든 상관없이 기존 PDF 파일을 프로그래밍 방식으로 처리하는 방법에 관한 섹션입니다.

## 웹 워커 사용하기

버전 23.6에서는 웹 워커를 사용할 수 있는 기능이 추가되었습니다:

```js
const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
```

JavaScript를 통해 C++에서 웹 워커를 사용하면, 별도의 워커 스레드에서 인터페이스를 차단하지 않고 작업을 수행할 수 있습니다.

Web Workers는 백그라운드에서 스크립트를 실행하는 간단한 도구입니다. 이는 사용자 인터페이스를 방해하지 않고 별도의 워커 스레드에서 작업을 수행할 수 있게 해줍니다.

다양한 방법을 배우게 됩니다:

- [문서 작업하기](/pdf/javascript-cpp/working-with-documents/) - 문서를 압축, 분할, 병합하고 전체 문서에 대해 다른 작업을 수행합니다.
- [페이지 작업하기](/pdf/javascript-cpp/working-with-pages/) - 페이지 추가, 이동 또는 제거, 자르기, 스탬프 작업을 수행합니다.
- [PDF의 메타데이터](/pdf/javascript-cpp/pdf-file-metadata/) - 문서의 메타 데이터를 가져오거나 설정합니다.
- [이미지 작업하기](/pdf/javascript-cpp/working-with-images/) - 문서에 이미지를 삽입, 제거, 추출합니다.
- [탐색 및 상호작용](/pdf/javascript-cpp/navigation-and-interaction/) - 작업, 북마크 처리, 페이지 탐색을 다룹니다.
- [주석](/pdf/javascript-cpp/annotations/) - 주석은 사용자가 PDF 페이지에 사용자 정의 콘텐츠를 추가할 수 있도록 합니다. PDF 문서에서 주석을 추가, 삭제 및 수정할 수 있습니다.

- [보안 및 서명](/pdf/javascript-cpp/securing-and-signing/) - 프로그래밍 방식으로 PDF 문서를 보호하고 서명합니다.
- [Attachments](/pdf/javascript-cpp/attachments/) - PDF 문서는 파일 첨부를 포함할 수 있습니다. 이러한 첨부 파일은 다른 PDF 문서일 수도 있고, 오디오 파일, Microsoft Office 문서 등과 같은 모든 종류의 파일일 수 있습니다. PDF에 첨부 파일을 추가하고, 첨부 파일의 정보를 얻고, 파일로 저장하며, JavaScript를 사용하여 PDF에서 첨부 파일을 프로그래밍 방식으로 삭제하는 방법을 배우게 됩니다.