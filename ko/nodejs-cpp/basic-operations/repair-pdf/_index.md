---
title: Node.js에서 PDF 복구
linktitle: PDF 복구
type: docs
weight: 10
url: /ko/nodejs-cpp/repair-pdf/
description: 이 항목에서는 Node.js 환경에서 PDF를 복구하는 방법을 설명합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js는 고품질 PDF 복구를 제공합니다. 프로그램이나 브라우저와 관계없이 어떤 이유로든 PDF 파일이 열리지 않을 수 있습니다. 경우에 따라 문서를 복원할 수 있으니, 아래 코드를 시도해 보고 직접 확인하십시오.
PDF 문서를 복구하고자 하는 경우, 다음을 사용할 수 있습니다. [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) 함수. 
Node.js 환경에서 PDF 파일을 복구하기 위해 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 복구될 PDF 파일의 이름을 지정합니다.
1. 호출 `AsposePdf` Promise로서 파일 복구 작업을 수행합니다. 성공하면 객체를 반환합니다.
1. 함수를 호출합니다. [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. PDF 파일을 복구합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPdfRepair.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 복구될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. PDF 파일을 복구합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPdfRepair.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```