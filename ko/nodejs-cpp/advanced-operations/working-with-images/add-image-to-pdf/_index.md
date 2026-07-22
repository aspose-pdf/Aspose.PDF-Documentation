---
title: Node.js에서 PDF에 이미지 추가
linktitle: 이미지 추가
type: docs
weight: 10
url: /ko/nodejs-cpp/add-image-to-pdf/
description: 이 섹션에서는 Aspose.PDF for Node.js via C++를 사용하여 기존 PDF 파일에 이미지를 추가하는 방법을 설명합니다.
lastmod: "2026-07-18"
---

## 기존 PDF 파일에 이미지 추가

PDF 파일에 이미지를 추가하려면 복잡한 특수 도구가 필요하다고 일반적으로 생각됩니다. 하지만 Aspose.PDF for Node.js를 사용하면 Node.js 환경에서 PDF에 필요한 이미지를 빠르고 쉽게 추가할 수 있습니다.

우리는 파일의 끝에만 이미지를 추가할 수 있으므로, 올바른 예는 스캔한 문서 페이지가 몇 페이지 있고 이를 하나의 PDF로 변환하는 경우입니다.

이미지를 추가하려는 경우, 사용할 수 있습니다 [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) 함수. 
Node.js 환경에서 이미지를 추가하려면 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 이미지를 추가할 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 이미지 추가 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. PDF 끝에 이미지를 추가합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultAddImage.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 이미지를 추가할 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. PDF 끝에 이미지를 추가합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultAddImage.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```