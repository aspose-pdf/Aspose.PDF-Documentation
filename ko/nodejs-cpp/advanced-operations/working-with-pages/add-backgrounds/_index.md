---
title: Node.js에서 PDF에 배경을 추가
linktitle: 배경 추가
type: docs
weight: 10
url: /ko/nodejs-cpp/add-background/
description: Node.js에서 PDF 파일에 배경 이미지를 추가
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

다음 코드 스니펫은 PDF 페이지에 배경 이미지를 추가하는 방법을 보여줍니다, using the [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) Node.js에서 함수.

Node.js 환경에서 배경 이미지를 추가하기 위해 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 배경 이미지가 추가될 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 배경 이미지를 추가하는 작업을 수행합니다. 성공하면 객체를 반환받습니다.
1. 함수를 호출합니다. [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. PDF 파일에 배경 이미지를 추가합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 “ResultAddBackgroundImage.pdf”에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 ‘json.errorText’에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add background image to a PDF-file and save the "ResultBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 배경 이미지가 추가될 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. PDF 파일에 배경 이미지를 추가합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 “ResultAddBackgroundImage.pdf”에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 ‘json.errorText’에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*Add background image to a PDF-file and save the "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```