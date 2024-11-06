---
title: Node.js에서 PDF 파일에서 이미지 삭제
linktitle: 이미지 삭제
type: docs
weight: 20
url: ko/nodejs-cpp/delete-images-from-pdf-file/
description: 이 섹션은 Aspose.PDF for Node.js via C++를 사용하여 PDF 파일에서 이미지를 삭제하는 방법을 설명합니다.
lastmod: "2023-11-16"
---

Aspose.PDF for Node.js via C++를 사용하여 PDF 파일에서 이미지를 삭제할 수 있습니다.

PDF에서 이미지를 삭제하려는 경우 [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) 함수를 사용할 수 있습니다.
Node.js 환경에서 이미지를 삭제하기 위해 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 이미지가 제거될 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 이미지 제거 작업을 수행합니다. 성공하면 객체를 받습니다.
1. [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) 함수를 호출합니다.

1. PDF에서 이미지를 삭제합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPdfDeleteImages.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*PDF 파일에서 이미지를 삭제하고 "ResultPdfDeleteImages.pdf"로 저장합니다.*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 이미지가 제거될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.

1. 함수 [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/)를 호출합니다.
1. PDF에서 이미지를 삭제합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과가 "ResultPdfDeleteImages.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보가 'json.errorText'에 포함됩니다.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*PDF 파일에서 이미지를 삭제하고 "ResultPdfDeleteImages.pdf"로 저장합니다.*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```