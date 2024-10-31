---
title: Node.js에서 PDF에 페이지 번호 추가하기
linktitle: 페이지 번호 추가
type: docs
weight: 100
url: /nodejs-cpp/add-page-number/
description: Aspose.PDF for Node.js via C++를 사용하여 PDF 파일에 AsposePdfAddPageNum을 사용하여 페이지 번호 스탬프를 추가할 수 있습니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

페이지 번호는 독자가 문서의 다양한 부분을 쉽게 찾을 수 있게 해줍니다. 다음 코드 스니펫은 Node.js에서 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) 함수를 사용하여 PDF 페이지에 페이지 번호를 추가하는 방법을 보여줍니다.

Node.js 환경에서 PDF에 페이지 번호를 추가하려면 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 페이지 번호가 추가될 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 페이지 번호를 추가하는 작업을 수행합니다. 성공하면 객체를 받습니다.

1. 함수 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/)을 호출합니다.
1. PDF 파일에 페이지 번호를 추가합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과가 "ResultAddPageNum.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* PDF 파일에 페이지 번호를 추가하고 "ResultAddPageNum.pdf"로 저장합니다 */
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 페이지 번호가 추가될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.

1. 함수 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/)을 호출합니다.
1. PDF 파일에 페이지 번호를 추가합니다. 따라서 'json.errorCode'가 0이면, 작업 결과는 "ResultAddPageNum.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일에 페이지 번호를 추가하고 "ResultAddPageNum.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```