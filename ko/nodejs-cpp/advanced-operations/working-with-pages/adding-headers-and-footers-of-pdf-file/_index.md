---
title: Node.js에서 PDF에 머리글 및 바닥글 추가
linktitle: PDF에 머리글 및 바닥글 추가
type: docs
weight: 70
url: ko/nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Node.js via C++를 사용하여 PDF 파일에 머리글 및 바닥글을 추가할 수 있습니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Node.js via C++**를 사용하면 기존의 PDF 파일에 머리글과 바닥글을 추가할 수 있습니다. 

머리글과 바닥글을 추가하려면 [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/) 기능을 사용할 수 있습니다. 

다음 코드 스니펫을 확인하여 Node.js 환경에서 PDF 파일에 머리글 및 바닥글을 추가하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 머리글 및 바닥글이 추가될 PDF 파일의 이름을 지정합니다.

1. `AsposePdf`를 Promise로 호출하고 헤더 및 푸터 추가 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/)를 호출합니다.
1. PDF 파일의 헤더와 푸터에 텍스트를 추가합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultAddHeaderFooter.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일의 헤더/푸터에 텍스트를 추가하고 "ResultAddHeaderFooter.pdf"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 머리글과 바닥글이 추가될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/)를 호출합니다.
1. PDF 파일의 머리글과 바닥글에 텍스트를 추가합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultAddHeaderFooter.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 나타나면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일의 머리글/바닥글에 텍스트를 추가하고 "ResultAddHeaderFooter.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```