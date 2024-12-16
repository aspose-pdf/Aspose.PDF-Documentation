---
title: Node.js에서 PDF의 북마크
linktitle: PDF의 북마크
type: docs
weight: 10
url: /ko/nodejs-cpp/bookmark/
description: Node.js 환경에서 PDF 문서에 북마크를 추가하거나 삭제할 수 있습니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 특정 북마크 삭제

C++를 통한 Aspose.PDF for Node.js를 사용하여 PDF 파일에서 북마크를 삭제할 수 있습니다. PDF에서 북마크를 삭제하려면 [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) 기능을 사용할 수 있습니다.
Node.js 환경에서 PDF 파일에서 북마크를 삭제하기 위해 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 북마크가 제거될 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 북마크를 제거하는 작업을 수행합니다. 성공하면 객체를 수신합니다.

1. 함수 [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/)를 호출합니다.
1. 북마크를 삭제합니다. 따라서 'json.errorCode'가 0이면, 작업 결과가 "ResultPdfDeleteBookmarks.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 나타나면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*PDF 파일에서 북마크를 삭제하고 "ResultPdfDeleteBookmarks.pdf"로 저장합니다.*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 북마크가 제거될 PDF 파일의 이름을 지정합니다.

1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/)를 호출합니다.
1. 책갈피를 삭제합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPdfDeleteBookmarks.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*PDF 파일에서 책갈피를 삭제하고 "ResultPdfDeleteBookmarks.pdf"로 저장합니다.*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```