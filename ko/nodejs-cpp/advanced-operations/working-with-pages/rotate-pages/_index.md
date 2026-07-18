---
title: Node.js에서 PDF 페이지 회전
linktitle: PDF 페이지 회전
type: docs
weight: 50
url: /ko/nodejs-cpp/rotate-pages/
description: 이 항목에서는 Node.js 환경에서 기존 PDF 파일의 페이지 방향을 프로그래밍 방식으로 회전하는 방법을 설명합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

이 섹션에서는 Aspose.PDF for Node.js via C\u002B\u002B를 사용하여 기존 PDF 파일의 페이지를 회전하는 방법을 설명합니다.

PDF 페이지를 회전하려는 경우, 다음을 사용할 수 있습니다. [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) 함수. 이 함수는 회전 값을 위한 특수 매개변수 'AsposePdfModule.Rotation'을 사용합니다. 이를 통해 PDF를 회전시켜야 할 각도를 설정할 수 있습니다. 옵션은 다음과 같습니다: None, 90, 180, 또는 270도.

Node.js 환경에서 PDF 페이지를 회전하기 위해 아래 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 회전할 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise 로서 페이지 회전을 수행하는 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. 모든 PDF 파일을 회전합니다. 회전값은 270도 (on270)로 설정됩니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultRotation.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 회전할 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. 모든 PDF 파일을 회전합니다. 회전값은 270도 (on270)로 설정됩니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultRotation.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```