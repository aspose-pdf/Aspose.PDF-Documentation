---
title: Node.js에서 PDF 페이지 삭제
linktitle: PDF 페이지 삭제
type: docs
weight: 30
url: ko/nodejs-cpp/delete-pages/
description: Aspose.PDF for Node.js via C++를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 페이지를 삭제하려면 [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) 함수를 사용할 수 있습니다.

이 함수의 특징은 numPages 매개변수로 여러 유형을 수용할 수 있다는 것입니다:

- 문자열: 이 경우 특정 페이지나 구간을 사용하여 페이지 집합을 언급할 수 있습니다. 예를 들어, 문자열 "7, 20, 30-32, 34"는 페이지 7, 20, 30에서 32, 34를 제거하고 싶다는 의미입니다.
- 배열: 이 경우 페이지만 언급할 수 있습니다. 배열 [3,7]은 페이지 3과 7을 제거하고 싶다는 의미입니다.
- 정수: 단일 페이지 번호.

Node.js 환경에서 PDF 페이지를 삭제하려면 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`을 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 삭제할 페이지가 있는 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 페이지를 제거하는 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/)를 호출합니다.
1. PDF 파일에서 특정 페이지를 제거합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultDeletePages.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, 포함할 페이지 번호: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, 페이지 번호 배열*/
      /*const numPages = [1,3];*/
      /*number, 페이지 번호*/
      const numPages = 1;
      /*PDF 파일에서 페이지를 삭제하고 "ResultDeletePages.pdf"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 페이지가 삭제될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) 함수를 호출합니다. 이 함수는 지정된 페이지를 PDF 파일에서 제거하는 데 도움이 됩니다. 작업은 페이지 간격이 포함된 문자열(예: "7, 20, 22, 30-32, 33, 36-40, 46"), 페이지 번호 배열 또는 단일 페이지 번호일 수 있는 numPages 변수에 의해 결정됩니다.
1. 특정 페이지를 PDF 파일에서 제거합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultDeletePages.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나는 경우 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*문자열, 페이지 간격을 포함한 페이지 번호: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*배열, 페이지 번호의 배열*/
  /*const numPages = [1,3];*/
  /*숫자, 페이지 번호*/
  const numPages = 1;
  /*PDF 파일에서 페이지를 삭제하고 "ResultDeletePages.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```