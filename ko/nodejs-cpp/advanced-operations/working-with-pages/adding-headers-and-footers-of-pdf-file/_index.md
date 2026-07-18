---
title: Node.js에서 PDF에 머리글 및 바닥글 추가
linktitle: PDF에 머리글 및 바닥글 추가
type: docs
weight: 70
url: /ko/nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Node.js via C++는 AsposePdfAddTextHeaderFooter를 사용하여 PDF 파일에 머리글 및 바닥글을 추가할 수 있도록 합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Node.js via C++**는 기존 PDF 파일에 머리글 및 바닥글을 추가할 수 있게 해줍니다. 

머리글과 바닥글을 추가하려는 경우, 다음을 사용할 수 있습니다 [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/) 함수. 

Node.js 환경에서 PDF 파일에 헤더와 푸터를 추가하기 위해 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 헤더와 푸터가 추가될 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 헤더와 푸터를 추가하는 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. PDF 파일의 헤더와 푸터에 텍스트를 추가합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 “ResultAddHeaderFooter.pdf”에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 나타나는 경우, 오류 정보는 ‘json.errorText’에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add text in Header/Footer of a PDF-file and save the "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 헤더와 푸터가 추가될 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. PDF 파일의 헤더와 푸터에 텍스트를 추가합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 “ResultAddHeaderFooter.pdf”에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 나타나는 경우, 오류 정보는 ‘json.errorText’에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add text in Header/Footer of a PDF-file and save the "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```