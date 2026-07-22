---
title: Node.js에서 PDF 텍스트 추출
linktitle: PDF에서 텍스트 추출
type: docs
weight: 10
url: /ko/nodejs-cpp/extract-text/
description: 이 섹션에서는 Aspose.PDF for Node.js via C++ 툴킷을 사용하여 PDF 문서에서 텍스트를 추출하는 방법을 설명합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 추출

PDF에서 텍스트를 추출하는 것은 쉽지 않습니다. 일부 PDF 리더만 PDF 이미지나 스캔된 PDF에서 텍스트를 추출할 수 있습니다. 하지만 **Aspose.PDF for Node.js via C++** 도구를 사용하면 Node.js 환경에서 모든 PDF 파일의 텍스트를 쉽게 추출할 수 있습니다. 

이 코드는 AsposePDFforNode.js 모듈을 사용하여 지정된 PDF 파일에서 텍스트를 추출하고, 추출된 텍스트 또는 발생한 오류를 로그에 기록하는 방법을 보여줍니다.

코드 스니펫을 확인하고 PDF에서 텍스트를 추출하는 절차를 따르세요:

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 텍스트를 추출할 PDF 파일의 이름을 지정하세요.
1. 호출 `AsposePdf` Promise와 같이 텍스트를 추출하는 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. 추출된 텍스트는 JSON 객체에 저장됩니다. 따라서 ‘json.errorCode’가 0이면 console.log를 사용하여 추출된 텍스트가 표시됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생하면 오류 정보가 ‘json.errorText’에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract text from a PDF-file*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 텍스트를 추출할 PDF 파일의 이름을 지정하세요.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. 추출된 텍스트는 JSON 객체에 저장됩니다. 따라서 ‘json.errorCode’가 0이면 console.log를 사용하여 추출된 텍스트가 표시됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생하면 오류 정보가 ‘json.errorText’에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```
