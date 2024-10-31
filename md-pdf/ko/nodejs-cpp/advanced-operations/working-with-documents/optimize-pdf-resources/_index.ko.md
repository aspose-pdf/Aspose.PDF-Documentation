---
title: Node.js에서 PDF 리소스 최적화
linktitle: PDF 리소스 최적화
type: docs
weight: 15
url: /nodejs-cpp/optimize-pdf-resources/
description: Node.js 도구를 사용하여 빠른 웹 보기용 PDF 파일의 리소스를 최적화합니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 리소스 최적화

문서의 리소스를 최적화합니다:

1. 문서 페이지에서 사용되지 않는 리소스가 제거됩니다
1. 동일한 리소스가 단일 객체로 결합됩니다
1. 사용되지 않는 객체가 삭제됩니다
 

PDF 리소스를 최적화하려면 [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/) 함수를 사용할 수 있습니다.
Node.js 환경에서 PDF 리소스를 최적화하려면 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 리소스를 최적화할 PDF 파일의 이름을 지정합니다.

1. `AsposePdf`를 Promise로 호출하고 파일 최적화를 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/)를 호출합니다.
1. PDF 리소스를 최적화합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과가 "ResultPdfOptimizeResource.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 나타나면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일의 리소스를 최적화하고 "ResultPdfOptimizeResource.pdf"에 저장합니다.*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 리소스가 최적화될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/)를 호출합니다.
1. PDF 리소스를 최적화합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과는 "ResultPdfOptimizeResource.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일의 리소스를 최적화하고 "ResultPdfOptimizeResource.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```