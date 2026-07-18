---
title: Node.js에서 PDF 이미지 추출
linktitle: PDF에서 이미지 추출
type: docs
weight: 20
url: /ko/nodejs-cpp/extract-images-from-the-pdf-file/
description: Aspose.PDF for Node.js via C\u002B\u002B 툴킷을 사용하여 PDF에서 이미지의 일부를 추출하는 방법.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Node.js 환경에서 PDF 파일의 이미지를 추출

PDF 문서에서 이미지를 추출하려는 경우, 다음을 사용할 수 있습니다 [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/) 함수. 
이 함수에 세 개의 인수를 전달해야 합니다: 입력 및 출력 파일 이름과 해상도.
Node.js를 사용하여 PDF 파일에서 이미지를 추출하는 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 이미지를 추출할 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise 로서 이미지를 추출하는 작업을 수행합니다. 성공하면 객체를 받으세요.
1. 함수를 호출합니다. [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. PDF 파일에서 이미지를 추출합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 "ResultPdfExtractImage{0:D2}.jpg"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 ‘json.errorText’에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 이미지를 추출할 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. PDF 파일에서 이미지를 추출합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 "ResultPdfExtractImage{0:D2}.jpg"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 ‘json.errorText’에 포함됩니다.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```
