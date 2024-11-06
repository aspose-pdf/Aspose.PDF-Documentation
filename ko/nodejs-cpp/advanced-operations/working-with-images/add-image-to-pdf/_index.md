---
title: Node.js에서 PDF에 이미지 추가 
linktitle: 이미지 추가
type: docs
weight: 10
url: ko/nodejs-cpp/add-image-to-pdf/
description: 이 섹션에서는 Aspose.PDF for Node.js via C++를 사용하여 기존 PDF 파일에 이미지를 추가하는 방법을 설명합니다.
lastmod: "2023-11-16"
---

## 기존 PDF 파일에 이미지 추가하기

이미지를 PDF 파일에 추가하려면 복잡한 특수 도구가 필요하다는 것이 일반적인 믿음입니다. 그러나 Aspose.PDF for Node.js를 사용하면 Node.js 환경에서 필요한 이미지를 PDF에 빠르고 쉽게 추가할 수 있습니다.

우리는 파일의 끝에만 이미지를 추가할 수 있으므로, 올바른 예는 스캔한 문서 페이지를 단일 PDF로 변환하는 것입니다.

이미지를 추가하려는 경우 [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) 함수를 사용할 수 있습니다. Node.js 환경에서 이미지를 추가하려면 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.

1. 이미지가 추가될 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 이미지 추가 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/)를 호출합니다.
1. PDF의 끝에 이미지를 추가합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultAddImage.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /* PDF 파일 끝에 이미지를 추가하고 "ResultImage.pdf"로 저장합니다 */
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 이미지가 추가될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/)를 호출합니다.
1. 이미지가 PDF의 끝에 추가됩니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultAddImage.pdf"에 저장됩니다. 만약 json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*PDF 파일의 끝에 이미지를 추가하고 "ResultImage.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```