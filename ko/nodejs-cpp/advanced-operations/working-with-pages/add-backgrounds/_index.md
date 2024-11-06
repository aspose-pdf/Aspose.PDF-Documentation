---
title: Node.js에서 PDF에 배경 추가
linktitle: 배경 추가
type: docs
weight: 10
url: ko/nodejs-cpp/add-background/
description: Node.js에서 PDF 파일에 배경 이미지를 추가합니다
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

다음 코드 스니펫은 Node.js에서 [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) 함수를 사용하여 PDF 페이지에 배경 이미지를 추가하는 방법을 보여줍니다.

Node.js 환경에서 배경 이미지를 추가하기 위해 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
2. 배경 이미지가 추가될 PDF 파일의 이름을 지정합니다.
3. `AsposePdf`를 Promise로 호출하고 배경 이미지 추가 작업을 수행합니다. 성공하면 객체를 받습니다.
4. 함수 [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/)를 호출합니다.

1. PDF 파일에 배경 이미지를 추가합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultAddBackgroundImage.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일에 배경 이미지를 추가하고 "ResultBackgroundImage.pdf"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 배경 이미지가 추가될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.

1. 함수 [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/)를 호출합니다.
1. PDF 파일에 배경 이미지를 추가합니다. 따라서 'json.errorCode'가 0이면, 작업 결과는 "ResultAddBackgroundImage.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생한 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*PDF 파일에 배경 이미지를 추가하고 "ResultBackgroundImage.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```