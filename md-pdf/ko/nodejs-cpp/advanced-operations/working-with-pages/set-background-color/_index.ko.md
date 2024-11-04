---
title: Node.js에서 PDF의 배경색 설정
linktitle: 배경색 설정
type: docs
weight: 80
url: /nodejs-cpp/set-background-color/
description: C++를 통해 Node.js에서 PDF 파일의 배경색을 설정합니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF의 배경색을 설정하려면 [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) 함수를 사용할 수 있습니다.

Node.js 환경에서 PDF의 배경색을 설정하기 위한 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
2. 배경색을 설정하려는 PDF 파일의 이름을 지정합니다.
3. `AsposePdf`를 Promise로 호출하고 배경색 설정 작업을 수행합니다. 성공하면 객체를 받습니다.

1. 함수 [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/)를 호출하십시오. 
1. PDF 파일의 배경색을 설정하십시오. 이 함수에 3개의 인수를 전달해야 합니다: 입력 파일 이름, 원하는 색상(16진수 형식), 출력 파일 이름. 따라서 'json.errorCode'가 0이면, 작업의 결과는 "ResultRotation.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일의 배경색을 설정하고 "ResultPdfSetBackgroundColor.pdf"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 배경색을 설정할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/)를 호출합니다.
1. PDF 파일의 배경색을 설정합니다. 배경색은 "#426bf4"로 설정되며, 이는 파란색의 색조를 나타내는 16진수 색상 코드입니다. 따라서 'json.errorCode'가 0이면, 작업의 결과가 "ResultRotation.pdf"에 저장됩니다. 만약 json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일의 배경색을 설정하고 "ResultPdfSetBackgroundColor.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```