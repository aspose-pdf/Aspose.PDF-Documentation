---
title: Extract Text from PDF in Node.js
linktitle: Extract Text from PDF
type: docs
weight: 10
url: /nodejs-cpp/extract-text/
description: 이 섹션에서는 C++ 툴킷을 통해 Node.js용 Aspose.PDF를 사용하여 PDF 문서에서 텍스트를 추출하는 방법을 설명합니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 추출하기

PDF에서 텍스트를 추출하는 것은 쉽지 않습니다. PDF 이미지나 스캔된 PDF에서 텍스트를 추출할 수 있는 PDF 리더는 몇 안 됩니다. 하지만 **Node.js용 C++ 경유 Aspose.PDF** 도구를 사용하면 Node.js 환경에서 PDF 파일의 모든 텍스트를 쉽게 추출할 수 있습니다.

이 코드는 지정된 PDF 파일에서 텍스트를 추출하고 추출된 텍스트나 발생한 오류를 기록하는 방법을 보여줍니다.

코드 스니펫을 확인하고 PDF에서 텍스트를 추출하는 단계를 따라하세요:

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.

1. 텍스트가 추출될 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 텍스트를 추출하는 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/)를 호출합니다.
1. 추출된 텍스트는 JSON 객체에 저장됩니다. 따라서 'json.errorCode'가 0이면 추출된 텍스트가 console.log를 사용하여 표시됩니다. json.errorCode 매개변수가 0이 아니고, 이에 따라 파일에 오류가 나타나면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일에서 텍스트 추출*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.

1. 텍스트를 추출할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/)를 호출합니다.
1. 추출된 텍스트는 JSON 객체에 저장됩니다. 따라서 'json.errorCode'가 0이면 추출된 텍스트가 console.log를 통해 표시됩니다. json.errorCode 매개변수가 0이 아니고, 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일에서 텍스트 추출*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```