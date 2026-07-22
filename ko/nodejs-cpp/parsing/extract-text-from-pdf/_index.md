---
title: Node.js에서 PDF 텍스트 파싱
linktitle: PDF에서 텍스트 파싱
type: docs
weight: 30
url: /ko/nodejs-cpp/extract-text-from-pdf/
description: 이 문서는 Aspose.PDF for Node.js via C++를 사용하여 PDF 문서에서 텍스트를 파싱하는 다양한 방법을 설명합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 텍스트 파싱

PDF 문서에서 텍스트를 파싱하는 것은 매우 일반적이고 유용한 작업입니다. 
PDF에서 텍스트를 추출하는 것은 검색 및 접근성 향상부터 비즈니스, 연구, 정보 관리와 같은 다양한 분야에서 데이터 분석 및 자동화를 가능하게 하는 등 다양한 목적에 활용됩니다.

PDF 문서에서 텍스트를 추출하고자 할 경우, 다음을 사용할 수 있습니다 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) 함수. 
Node.js via C++를 사용하여 PDF 파일에서 텍스트를 추출하기 위해 아래 코드 스니펫을 확인하십시오.

코드 스니펫을 확인하고 PDF에서 텍스트를 추출하는 단계를 따르세요:

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 텍스트를 추출할 PDF 파일의 이름을 지정합니다.
1. 호출 `AsposePdf` Promise로 반환하고 텍스트를 추출하는 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. 추출된 텍스트는 JSON 객체에 저장됩니다. 따라서 ‘json.errorCode’가 0이면 console.log를 사용하여 추출된 텍스트가 표시됩니다. ‘json.errorCode’ 매개변수가 0이 아니고 파일에 오류가 발생한 경우, 오류 정보는 ‘json.errorText’에 포함됩니다.

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
1. 텍스트를 추출할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. 추출된 텍스트는 JSON 객체에 저장됩니다. 따라서 ‘json.errorCode’가 0이면 console.log를 사용하여 추출된 텍스트가 표시됩니다. ‘json.errorCode’ 매개변수가 0이 아니고 파일에 오류가 발생한 경우, 오류 정보는 ‘json.errorText’에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```