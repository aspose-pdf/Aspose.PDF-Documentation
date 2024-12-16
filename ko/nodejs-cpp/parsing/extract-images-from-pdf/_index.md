---
title: PDF에서 이미지 추출하기 (Node.js)
linktitle: PDF에서 이미지 추출
type: docs
weight: 20
url: /ko/nodejs-cpp/extract-images-from-the-pdf-file/
description: Aspose.PDF for Node.js via C++ 툴킷을 사용하여 PDF에서 이미지의 일부를 추출하는 방법.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Node.js 환경에서 PDF 파일에서 이미지 추출하기

PDF 문서에서 이미지를 추출하고자 하는 경우, [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/) 함수를 사용할 수 있습니다. 
이 함수에는 세 개의 인수를 전달해야 합니다: 입력 파일 이름, 출력 파일 이름, 해상도.
Node.js를 사용하여 PDF 파일에서 이미지를 추출하는 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 import합니다.
1. 이미지가 추출될 PDF 파일의 이름을 지정합니다.

1. `AsposePdf`를 Promise로 호출하여 이미지 추출 작업을 수행합니다. 성공하면 개체를 받습니다.
1. 함수 [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/)를 호출합니다.
1. PDF 파일에서 이미지를 추출합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPdfExtractImage{0:D2}.jpg"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI의 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*템플릿 "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... 형식 페이지 번호), 해상도 150 DPI로 PDF 파일에서 이미지 추출 및 저장*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 이미지가 추출될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/)를 호출합니다.
1. PDF 파일에서 이미지를 추출합니다. 이렇게 하여 'json.errorCode'가 0이면, 작업의 결과는 "ResultPdfExtractImage{0:D2}.jpg"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고, 파일에 오류가 발생한 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*PDF 파일에서 이미지를 추출하여 템플릿 "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... 형식 페이지 번호), 해상도 150 DPI로 저장*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```