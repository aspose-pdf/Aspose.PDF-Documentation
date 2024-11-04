---
title: Node.js에서 PDF에 이미지 스탬프 추가
linktitle: PDF 파일의 이미지 스탬프
type: docs
weight: 60
url: /nodejs-cpp/stamping/
description: AsposePdfAddStamp를 사용하여 Node.js 도구로 PDF 문서에 이미지 스탬프를 추가합니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에 이미지 스탬프 추가

PDF 문서에 스탬프를 찍는 것은 종이 문서에 스탬프를 찍는 것과 비슷합니다. PDF 파일의 스탬프는 다른 사용자가 PDF 파일을 사용하는 것을 보호하고 PDF 파일의 내용 보안을 확인하는 등의 추가 정보를 제공합니다. Node.js를 사용하여 PDF 파일에 이미지 스탬프를 추가하려면 [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) 기능을 사용할 수 있습니다.

Node.js 환경에서 PDF 파일에 이미지 스탬프를 추가하려면 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.

1. 이미지 스탬프가 추가될 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 이미지 스탬프 추가 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/)를 호출합니다.
1. PDF 파일에 스탬프를 추가합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultImage.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생한 경우 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일에 스탬프를 추가하고 "ResultImage.pdf"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 이미지 스탬프가 추가될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/)를 호출합니다.
1. PDF 파일에 스탬프를 추가합니다. 따라서 'json.errorCode'가 0이면 작업 결과는 "ResultImage.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*PDF 파일에 스탬프를 추가하고 "ResultImage.pdf"로 저장합니다*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```