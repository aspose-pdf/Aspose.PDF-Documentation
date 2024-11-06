---
title: Node.js에서 PDF 분할
linktitle: PDF 파일 분할
type: docs
weight: 30
url: ko/nodejs-cpp/split-pdf/
description: 이 주제에서는 Aspose.PDF for Node.js via C++를 사용하여 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Node.js를 사용하여 PDF를 두 파일로 분할

단일 PDF를 여러 부분으로 분할하려는 경우, [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/) 함수를 사용할 수 있습니다.
다음 코드 스니펫을 확인하여 Node.js 환경에서 두 개의 PDF를 분할하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
2. 분할할 PDF 파일의 이름을 지정합니다.
3. `AsposePdf`를 Promise로 호출하고 파일을 분할하는 작업을 수행합니다. 성공하면 객체를 받습니다.
4. 함수 [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/)를 호출합니다.

1. 두 개의 PDF 파일을 분할합니다. PDF 파일을 1페이지에서 분할할 것임을 나타내기 위해 pageToSplit 변수를 1로 설정합니다. 
1. 따라서, 'json.errorCode'가 0이면, 작업의 결과가 "ResultSplit1.pdf"와 "ResultSplit2.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*분할할 페이지 수 설정*/
      const pageToSplit = 1;
      /*두 개의 PDF 파일로 분할하고 "ResultSplit1.pdf", "ResultSplit2.pdf"로 저장*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.

1. 분할할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/)를 호출합니다.
1. 두 개의 PDF 파일을 분할합니다. pageToSplit 변수를 1로 설정하여 PDF 파일이 페이지 1에서 분할됨을 나타냅니다.
1. 따라서, 'json.errorCode'가 0이면 작업의 결과가 "ResultSplit1.pdf"와 "ResultSplit2.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*분할할 페이지 번호를 설정합니다.*/
  const pageToSplit = 1;
  /*두 개의 PDF 파일로 분할하고 "ResultSplit1.pdf", "ResultSplit2.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```