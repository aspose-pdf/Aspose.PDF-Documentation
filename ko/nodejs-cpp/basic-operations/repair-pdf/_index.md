---
title: Node.js에서 PDF 복구
linktitle: PDF 복구
type: docs
weight: 10
url: /ko/nodejs-cpp/repair-pdf/
description: 이 주제는 Node.js 환경에서 PDF를 복구하는 방법을 설명합니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js는 고품질의 PDF 복구를 제공합니다. 프로그램이나 브라우저와 상관없이 PDF 파일이 열리지 않을 수 있습니다. 경우에 따라 문서를 복원할 수 있으며, 다음 코드를 시도해보고 직접 확인해보세요. PDF 문서를 복구하려면 [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) 함수를 사용할 수 있습니다. Node.js 환경에서 PDF 파일을 복구하기 위해 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 복구할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 복구 작업을 수행합니다. 성공하면 객체를 받습니다.

1. [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) 함수를 호출합니다.
1. PDF 파일을 복구합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPdfRepair.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*PDF 파일을 복구하고 "ResultPdfRepair.pdf"를 저장합니다.*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 복구할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 수신합니다.

1. 함수 [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/)를 호출합니다.
1. PDF 파일을 복구합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과가 "ResultPdfRepair.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 복구하고 "ResultPdfRepair.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```