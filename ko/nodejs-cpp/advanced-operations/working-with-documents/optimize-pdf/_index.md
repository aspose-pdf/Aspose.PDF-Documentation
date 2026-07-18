---
title: Aspose.PDF for Node.js via C++를 사용하여 PDF 최적화
linktitle: PDF 파일 최적화
type: docs
weight: 10
url: /ko/nodejs-cpp/optimize-pdf/
description: Node.js 환경을 사용하여 빠른 웹 보기를 위해 PDF 파일을 최적화하고 압축합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF Document 최적화

Aspose.PDF for Node.js via C++의 툴킷을 사용하면 Node.js 환경을 위한 PDF 콘텐츠를 최적화할 수 있습니다. 

최적화(또는 선형화)는 웹 브라우저를 사용하여 온라인으로 브라우징하기에 적합한 PDF 파일을 만드는 과정을 말합니다.

PDF를 최적화하려는 경우 사용할 수 있습니다 [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/) 함수. 
Node.js 환경에서 PDF 파일을 최적화하기 위해 아래 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 최적화할 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 파일 최적화를 위한 작업을 수행하고, 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. PDF 파일을 최적화합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultOptimize.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 최적화할 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. PDF 파일을 최적화합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultOptimize.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```