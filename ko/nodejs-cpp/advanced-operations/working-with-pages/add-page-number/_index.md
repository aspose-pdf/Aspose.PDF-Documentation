---
title: Node.js에서 PDF에 페이지 번호 매기기 추가
linktitle: 페이지 번호 추가
type: docs
weight: 100
url: /ko/nodejs-cpp/add-page-number/
description: Aspose.PDF for Node.js via C++는 AsposePdfAddPageNum을 사용하여 PDF 파일에 페이지 번호 스탬프를 추가할 수 있도록 합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

페이지 번호는 독자가 문서의 다양한 부분을 찾기 쉽게 합니다. 다음 코드 스니펫은 페이지 번호를 PDF 페이지에 추가하는 방법을 보여줍니다. [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) Node.js에서 함수.

Node.js 환경에서 PDF에 페이지 번호를 추가하려면 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 페이지 번호가 추가될 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 페이지 번호를 추가하는 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. PDF 파일에 페이지 번호를 추가합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultAddPageNum.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add page number to a PDF-file save the "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 페이지 번호가 추가될 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. PDF 파일에 페이지 번호를 추가합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultAddPageNum.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add page number to a PDF-file and save the "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```