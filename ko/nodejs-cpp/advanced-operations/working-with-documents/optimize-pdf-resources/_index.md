---
title: Node.js에서 PDF 리소스 최적화
linktitle: PDF 리소스 최적화
type: docs
weight: 15
url: /ko/nodejs-cpp/optimize-pdf-resources/
description: Node.js 도구를 사용하여 빠른 웹 보기를 위한 PDF 파일 리소스를 최적화합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 리소스 최적화

문서의 리소스 최적화:

1. 문서 페이지에서 사용되지 않는 리소스는 제거됩니다.
1. 동일한 리소스가 하나의 객체로 결합됩니다.
1. 사용되지 않은 개체가 삭제됩니다.
 

PDF 리소스를 최적화하려는 경우, 다음을 사용할 수 있습니다. [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/) 함수. 
Node.js 환경에서 PDF 리소스를 최적화하려면 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 리소스를 최적화할 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 파일 최적화를 위한 작업을 수행하고, 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. PDF 리소스를 최적화합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPdfOptimizeResource.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 리소스를 최적화할 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. PDF 리소스를 최적화합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPdfOptimizeResource.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```