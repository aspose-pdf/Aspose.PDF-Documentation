---
title: PDF에서 텍스트 추출하기 in Node.js
linktitle: PDF에서 텍스트 추출하기
type: docs
weight: 30
url: ko/nodejs-cpp/extract-text-from-pdf/
description: 이 문서에서는 Aspose.PDF for Node.js via C++를 사용하여 PDF 문서에서 텍스트를 추출하는 다양한 방법을 설명합니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 텍스트 추출하기

PDF 문서에서 텍스트를 추출하는 것은 매우 일반적이고 유용한 작업입니다. PDF에서 텍스트를 추출하는 것은 검색 및 가용성을 개선하는 것부터 비즈니스, 연구 및 정보 관리와 같은 다양한 분야에서 데이터의 분석 및 자동화를 가능하게 하는 것에 이르기까지 다양한 목적을 제공합니다.

PDF 문서에서 텍스트를 추출하고자 하는 경우 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) 함수를 사용할 수 있습니다. C++를 통해 Node.js를 사용하여 PDF 파일에서 텍스트를 추출하기 위해 다음 코드 스니펫을 확인하십시오.

코드 스니펫을 확인하고 PDF에서 텍스트를 추출하는 단계를 따르세요:

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로서 가져옵니다.
1. 텍스트가 추출될 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 텍스트를 추출하는 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/)를 호출합니다.
1. 추출된 텍스트는 JSON 객체에 저장됩니다. 따라서 'json.errorCode'가 0이면 추출된 텍스트가 console.log를 사용하여 표시됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

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
1. 추출된 텍스트는 JSON 객체에 저장됩니다. 따라서 'json.errorCode'가 0이면, 추출된 텍스트는 console.log를 사용하여 표시됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일에서 텍스트 추출*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```