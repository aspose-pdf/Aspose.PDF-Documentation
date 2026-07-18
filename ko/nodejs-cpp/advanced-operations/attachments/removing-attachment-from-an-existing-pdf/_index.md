---
title: Node.js에서 PDF 첨부 파일 제거
linktitle: 기존 PDF에서 첨부 파일 제거
type: docs
weight: 10
url: /ko/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF는 PDF 문서에서 첨부 파일을 제거할 수 있습니다. Aspose.PDF를 사용하여 PDF 파일의 첨부 파일을 제거하려면 Node.js 환경을 사용하십시오.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Node.js via C++를 사용하여 PDF 파일에서 첨부 파일을 삭제할 수 있습니다. PDF에서 첨부 파일을 삭제하려는 경우 사용할 수 있습니다. [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/) 함수. 
Node.js 환경에서 PDF 파일의 첨부 파일을 삭제하려면 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 첨부 파일을 제거할 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 첨부 파일 제거 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. 첨부 파일을 삭제합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 “ResultPdfDeleteAttachments.pdf”에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 나타나는 경우, 오류 정보는 ‘json.errorText’에 포함됩니다.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 첨부 파일을 제거할 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. 첨부 파일을 삭제합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 “ResultPdfDeleteAttachments.pdf”에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 나타나는 경우, 오류 정보는 ‘json.errorText’에 포함됩니다.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```