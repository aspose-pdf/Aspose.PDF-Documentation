---
title: Node.js에서 PDF의 배경 색을 설정합니다
linktitle: 배경 색을 설정합니다
type: docs
weight: 80
url: /ko/nodejs-cpp/set-background-color/
description: Node.js를 통해 C++로 귀하의 PDF 파일 배경 색을 설정합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF의 배경 색을 설정하려는 경우, 사용할 수 있습니다 [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) 함수. 

Node.js 환경에서 PDF의 배경 색을 설정하기 위해 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 배경 색을 설정하려는 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 배경 색상을 설정하는 작업을 수행합니다. 성공하면 객체를 수신합니다.
1. 함수를 호출합니다. [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. PDF 파일의 배경 색을 설정합니다. 이 함수에 3개의 인수를 전달해야 합니다: 입력 파일 이름, 16진수 형식의 원하는 색, 그리고 출력 파일 이름. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultRotation.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 배경 색을 설정하려는 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. PDF 파일의 배경 색상을 설정합니다. 배경 색상은 "#426bf4," 로 설정되며, 이는 파란색 음영을 나타내는 16진수 색상 코드입니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultRotation.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 표시되는 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```