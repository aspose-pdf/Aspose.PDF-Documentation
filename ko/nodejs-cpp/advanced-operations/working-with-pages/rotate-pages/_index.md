---
title: Node.js에서 PDF 페이지 회전
linktitle: PDF 페이지 회전
type: docs
weight: 50
url: ko/nodejs-cpp/rotate-pages/
description: 이 주제는 Node.js 환경에서 기존 PDF 파일의 페이지 방향을 프로그래밍 방식으로 회전하는 방법에 대해 설명합니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

이 섹션에서는 C++를 통해 Aspose.PDF for Node.js를 사용하여 기존 PDF 파일의 페이지를 회전하는 방법에 대해 설명합니다.

PDF 페이지를 회전하려는 경우 [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) 함수를 사용할 수 있습니다. 이 함수는 회전 값을 위한 특수 매개변수 'AsposePdfModule.Rotation'을 사용합니다. 이를 통해 PDF를 몇 도 회전할지 설정할 수 있습니다. 선택 가능한 각도는 없음, 90도, 180도 또는 270도입니다.

Node.js 환경에서 PDF 페이지를 회전하기 위해 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.

1. 회전할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 페이지 회전 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/)를 호출합니다.
1. 모든 PDF 파일을 회전합니다. 회전은 270도(on270)로 설정됩니다. 따라서 'json.errorCode'가 0이면 작업 결과는 "ResultRotation.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 페이지를 회전하고 "ResultRotation.pdf"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 회전할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/)를 호출합니다.
1. 모든 PDF 파일을 회전시킵니다. 회전은 270도(on270)로 설정됩니다. 따라서 'json.errorCode'가 0이면 연산의 결과가 "ResultRotation.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 페이지를 회전하고 "ResultRotation.pdf"로 저장합니다*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```