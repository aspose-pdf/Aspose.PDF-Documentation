---
title: Node.js에서 PDF에 이미지 스탬프 추가
linktitle: PDF 파일의 이미지 스탬프
type: docs
weight: 60
url: /ko/nodejs-cpp/stamping/
description: Node.js 도구와 함께 AsposePdfAddStamp를 사용하여 PDF 문서에 이미지 스탬프를 추가합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에 이미지 스탬프 추가

PDF 문서에 스탬프를 찍는 것은 종이 문서에 스탬프를 찍는 것과 유사합니다. PDF 파일의 스탬프는 다른 사람이 PDF 파일을 사용할 수 있도록 보호하고, PDF 파일 내용의 보안을 확인하는 등 추가 정보를 제공합니다.
다음과 같이 사용할 수 있습니다 [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) Node.js를 사용하여 PDF 파일에 이미지 스탬프를 추가하는 기능.

Node.js 환경에서 PDF 파일에 이미지 스탬프를 추가하기 위해 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 이미지 스탬프가 추가될 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 이미지 스탬프 추가 작업을 수행합니다. 성공하면 객체를 반환받습니다.
1. 함수를 호출합니다. [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. PDF 파일에 스탬프를 추가합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 “ResultImage.pdf”에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 ‘json.errorText’에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 이미지 스탬프가 추가될 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. PDF 파일에 스탬프를 추가합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 “ResultImage.pdf”에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 ‘json.errorText’에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```