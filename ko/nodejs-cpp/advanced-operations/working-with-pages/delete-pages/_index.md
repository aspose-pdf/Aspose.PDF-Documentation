---
title: Node.js에서 PDF 페이지 삭제
linktitle: PDF 페이지 삭제
type: docs
weight: 30
url: /ko/nodejs-cpp/delete-pages/
description: Aspose.PDF for Node.js via C++를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 페이지를 삭제하려는 경우, 다음을 사용할 수 있습니다 [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) 함수. 

이 함수의 특징은 numPages 매개변수로 여러 유형을 받을 수 있다는 점입니다:

- string: 이 경우, 특정 페이지 또는 구간을 사용하여 페이지 집합을 지정할 수 있습니다. 예를 들어, string \u00227, 20, 30-32, 34\u0022는 페이지 7, 20, 30~32 및 34를 제거하고 싶다는 의미입니다.
- array: 이 경우 페이지만 지정할 수 있습니다. Array [3,7]는 페이지 3과 7을 제거하고 싶다는 의미입니다.
- int: 단일 페이지 번호.

Node.js 환경에서 PDF 페이지를 삭제하려면 다음 코드 조각을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 페이지를 삭제할 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 페이지를 제거하는 작업을 수행합니다. 성공하면 객체를 반환합니다.
1. 함수를 호출합니다. [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). 
1. PDF 파일에서 특정 페이지를 제거합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultDeletePages.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, array of number pages*/
      /*const numPages = [1,3];*/
      /*number, number page*/
      const numPages = 1;
      /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 페이지를 삭제할 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). 이 함수는 PDF 파일에서 지정된 페이지를 제거하는 데 도움이 됩니다. 동작은 numPages 변수에 의해 결정되며, 페이지 구간 문자열(예: "7, 20, 22, 30-32, 33, 36-40, 46"), 페이지 번호 배열 또는 단일 페이지 번호일 수 있습니다.
1. PDF 파일에서 특정 페이지를 제거합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultDeletePages.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, array of number pages*/
  /*const numPages = [1,3];*/
  /*number, number page*/
  const numPages = 1;
  /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```