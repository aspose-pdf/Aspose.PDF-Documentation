---
title: Node.js에서 PDF 파일 메타데이터 작업
linktitle: PDF 파일 메타데이터
type: docs
weight: 130
url: /ko/nodejs-cpp/pdf-file-metadata/
description: 이 섹션에서는 PDF 파일 정보 가져오기, PDF 파일에서 메타데이터 가져오기, Node.js에서 PDF 파일 정보를 설정하는 방법을 설명합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일 정보 가져오기

PDF 파일 정보를 얻고 싶을 경우, 사용할 수 있습니다 [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) 함수. 
Node.js 환경에서 PDF 파일 정보를 가져오기 위해 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 정보를 추출할 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 정보를 추출하는 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. 추출된 메타데이터는 JSON 객체에 저장됩니다. 따라서 'json.errorCode'가 0이면, 추출된 메타데이터가 console.log를 사용하여 표시됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get info (metadata) from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Title             : json.title
        Creator           : json.creator
        Author            : json.author
        Subject           : json.subject
        Keywords          : json.keywords
        Creation Date     : json.creation
        Modify Date       : json.mod
        PDF format        : json.format
        PDF version       : json.version
        PDF is PDF/A      : json.ispdfa
        PDF is PDF/UA     : json.ispdfua
        PDF is linearized : json.islinearized
        PDF is encrypted  : json.isencrypted
        PDF permission    : json.permission
        PDF page size     : json.size
        Page count        : json.pagecount
        Annotation count  : json.annotationcount
        Bookmark count    : json.bookmarkcount
        Attachment count  : json.attachmentcount
        Metadata count    : json.metadatacount
        JavaScript count  : json.javascriptcount
        Image count       : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 정보를 추출할 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. 추출된 메타데이터는 JSON 객체에 저장됩니다. 따라서 'json.errorCode'가 0이면, 추출된 메타데이터가 console.log를 사용하여 표시됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Get info (metadata) from a PDF-file*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      Title             : json.title
      Creator           : json.creator
      Author            : json.author
      Subject           : json.subject
      Keywords          : json.keywords
      Creation Date     : json.creation
      Modify Date       : json.mod
      PDF format        : json.format
      PDF version       : json.version
      PDF is PDF/A      : json.ispdfa
      PDF is PDF/UA     : json.ispdfua
      PDF is linearized : json.islinearized
      PDF is encrypted  : json.isencrypted
      PDF permission    : json.permission
      PDF page size     : json.size
      Page count        : json.pagecount
      Annotation count  : json.annotationcount
      Bookmark count    : json.bookmarkcount
      Attachment count  : json.attachmentcount
      Metadata count    : json.metadatacount
      JavaScript count  : json.javascriptcount
      Image count       : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```

## 모든 글꼴 가져오기

PDF 파일에서 글꼴을 가져오는 것은 다른 문서나 애플리케이션에서 글꼴을 재사용하는 유용한 방법이 될 수 있습니다. 

PDF 파일에서 글꼴을 가져오고 싶을 경우, 다음을 사용할 수 있습니다 [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) 함수. 
Node.js 환경에서 PDF 파일의 폰트를 가져오기 위해 다음 코드 스니펫을 확인해 주세요.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 폰트를 추출할 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 글꼴을 추출하는 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. 추출된 폰트는 JSON 객체에 저장됩니다. 따라서 'json.errorCode'가 0이면 console.log를 사용하여 폰트 이름, 임베드 여부 및 접근성 상태를 포함한 폰트 상세 배열을 표시합니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get list fonts from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 폰트를 추출할 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. 추출된 폰트는 JSON 객체에 저장됩니다. 따라서 'json.errorCode'가 0이면 console.log를 사용하여 폰트 이름, 임베드 여부 및 접근성 상태를 포함한 폰트 상세 배열을 표시합니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Get list fonts from a PDF-file*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## PDF 파일 정보 설정

Aspose.PDF for Node.js via C++는 PDF에 대한 파일별 정보를 설정할 수 있도록 해줍니다. 예를 들어 저자, 생성 날짜, 주제 및 제목과 같은 정보입니다. 이 정보를 설정하려면:

파일별 정보를 설정하려는 경우, 다음을 사용할 수 있습니다 [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/) 함수. 
Node.js 환경에서 파일 정보를 설정하기 위해 다음 코드 스니펫을 확인하십시오.

설정 가능: 
- 제목
- 제작자
- 저자
- 제목
- 키워드 목록
- 생성 날짜
- 수정 날짜
- 결과 파일 이름

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 정보가 설정될 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. PDF 파일 정보를 설정합니다. 제목, 작성자, 저자, 주제, 키워드, 생성 날짜 및 수정 날짜와 같은 정보는 매개변수로 제공됩니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultSetInfo.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
      /*If not need to set value, use undefined or "" (empty string)*/
      /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 정보가 설정될 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. PDF 파일 정보를 설정합니다. 제목, 작성자, 저자, 주제, 키워드, 생성 날짜 및 수정 날짜와 같은 정보는 매개변수로 제공됩니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultSetInfo.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
  /*If not need to set value, use undefined or "" (empty string)*/
  /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## PDF 파일 정보 제거

Aspose.PDF for Node.js via C++는 PDF 파일 메타데이터를 제거할 수 있습니다:

PDF에서 메타데이터를 제거하려는 경우, 사용할 수 있습니다. [AsposePdf 메타데이터 제거](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) 함수. 
Node.js 환경에서 PDF 메타데이터를 제거하기 위해 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. AsposePDFforNode.js 모듈을 요구합니다.
1. 정보가 제거될 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdf 메타데이터 제거](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. PDF 파일 정보를 삭제합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPdfRemoveMetadata.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 정보가 제거될 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdf 메타데이터 제거](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. PDF 파일 정보를 삭제합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPdfRemoveMetadata.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```