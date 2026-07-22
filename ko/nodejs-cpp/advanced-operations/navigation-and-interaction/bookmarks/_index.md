---
title: Node.js에서 PDF의 북마크
linktitle: PDF의 북마크
type: docs
weight: 10
url: /ko/nodejs-cpp/bookmark/
description: Node.js 환경에서 PDF 문서에 북마크를 추가하거나 삭제할 수 있습니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 특정 북마크 삭제

Aspose.PDF for Node.js via C++를 사용하여 PDF 파일에서 북마크를 삭제할 수 있습니다. PDF에서 북마크를 삭제하려는 경우, 다음과 같이 사용할 수 있습니다 [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) 함수. 
Node.js 환경에서 PDF 파일의 책갈피를 삭제하기 위해 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 책갈피를 제거할 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 북마크 제거 작업을 수행합니다. 성공하면 객체를 반환받습니다.
1. 함수를 호출합니다. [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. 책갈피를 삭제합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 "ResultPdfDeleteBookmarks.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 ‘json.errorText’에 포함됩니다.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 책갈피를 제거할 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. 책갈피를 삭제합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 "ResultPdfDeleteBookmarks.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 ‘json.errorText’에 포함됩니다.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```