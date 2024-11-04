---
title: Node.js에서 PDF 파일 메타데이터 작업하기
linktitle: PDF 파일 메타데이터
type: docs
weight: 130
url: /nodejs-cpp/pdf-file-metadata/
description: 이 섹션에서는 Node.js에서 PDF 파일 정보를 가져오고, PDF 파일에서 메타데이터를 가져오고, PDF 파일 정보를 설정하는 방법을 설명합니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일 정보 가져오기

PDF 파일 정보를 가져오려면 [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) 함수를 사용할 수 있습니다. Node.js 환경에서 PDF 파일 정보를 얻기 위한 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 정보가 추출될 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 정보를 추출하는 작업을 수행합니다. 성공하면 객체를 받습니다.

1. 함수 [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/)를 호출합니다.
1. 추출된 메타데이터는 JSON 객체에 저장됩니다. 따라서 'json.errorCode'가 0이면, 추출된 메타데이터는 console.log를 사용하여 표시됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* PDF 파일에서 정보(메타데이터) 가져오기 */
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        제목             : json.title
        작성자           : json.creator
        저자             : json.author
        주제             : json.subject
        키워드           : json.keywords
        생성 날짜         : json.creation
        수정 날짜         : json.mod
        PDF 형식         : json.format
        PDF 버전         : json.version
        PDF가 PDF/A 여부  : json.ispdfa
        PDF가 PDF/UA 여부 : json.ispdfua
        PDF가 선형화 여부 : json.islinearized
        PDF가 암호화 여부 : json.isencrypted
        PDF 권한         : json.permission
        PDF 페이지 크기   : json.size
        페이지 수         : json.pagecount
        주석 수           : json.annotationcount
        북마크 수         : json.bookmarkcount
        첨부 파일 수      : json.attachmentcount
        메타데이터 수     : json.metadatacount
        JavaScript 수     : json.javascriptcount
        이미지 수         : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? '제목: ' + json.title : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 정보를 추출할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) 함수를 호출합니다.
1. 추출된 메타데이터는 JSON 객체에 저장됩니다. 따라서 'json.errorCode'가 0이면 추출된 메타데이터가 console.log를 사용하여 표시됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생한 경우 오류 정보는 'json.errorText'에 포함됩니다.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /* PDF 파일에서 정보(메타데이터) 가져오기 */
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      제목               : json.title
      제작자             : json.creator
      저자               : json.author
      주제               : json.subject
      키워드             : json.keywords
      생성 날짜          : json.creation
      수정 날짜          : json.mod
      PDF 형식           : json.format
      PDF 버전           : json.version
      PDF는 PDF/A        : json.ispdfa
      PDF는 PDF/UA       : json.ispdfua
      PDF는 선형화됨     : json.islinearized
      PDF는 암호화됨     : json.isencrypted
      PDF 권한           : json.permission
      PDF 페이지 크기    : json.size
      페이지 수          : json.pagecount
      주석 수            : json.annotationcount
      북마크 수          : json.bookmarkcount
      첨부 파일 수       : json.attachmentcount
      메타데이터 수      : json.metadatacount
      JavaScript 수      : json.javascriptcount
      이미지 수          : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```


## 모든 폰트 가져오기

PDF 파일에서 폰트를 가져오는 것은 다른 문서나 애플리케이션에서 폰트를 재사용하는 유용한 방법이 될 수 있습니다.

PDF 파일에서 폰트를 가져오고 싶다면, [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) 함수를 사용할 수 있습니다.
Node.js 환경에서 PDF 파일에서 폰트를 가져오기 위해 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 폰트를 추출할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 폰트 추출 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/)를 호출합니다.

1. 추출된 글꼴은 JSON 객체에 저장됩니다. 따라서 'json.errorCode'가 0이면 글꼴 이름, 포함 여부 및 접근성 상태를 포함한 글꼴 세부 정보 배열을 console.log를 사용하여 표시합니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일에서 글꼴 목록 가져오기*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - 글꼴 배열: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 글꼴을 추출할 PDF 파일의 이름을 지정합니다.

 1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/)를 호출합니다.
1. 추출된 글꼴은 JSON 객체에 저장됩니다. 따라서 'json.errorCode'가 0이면 글꼴 이름, 포함 여부, 접근성 상태를 포함한 글꼴 세부 사항 배열을 console.log를 사용하여 표시합니다. json.errorCode 매개변수가 0이 아니고, 파일에 오류가 나타나는 경우 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일에서 글꼴 목록 가져오기*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - 글꼴 배열: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## PDF 파일 정보 설정


Aspose.PDF for Node.js via C++를 사용하면 PDF에 대한 파일별 정보를 설정할 수 있습니다. 이 정보에는 작성자, 생성 날짜, 주제 및 제목이 포함됩니다. 이 정보를 설정하려면 다음을 수행하십시오:

파일별 정보를 설정하려면 [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/) 기능을 사용할 수 있습니다. Node.js 환경에서 파일 정보를 설정하려면 다음 코드 스니펫을 확인하십시오.

설정 가능:
- 제목
- 작성자
- 저자
- 주제
- 키워드 목록
- 생성 날짜
- 수정 날짜
- 결과 파일 이름

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 정보를 설정할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 작업을 수행합니다. 성공하면 객체를 수신합니다.
1. 함수 [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/)를 호출합니다.

1. PDF 파일 정보를 설정합니다. 제목, 제작자, 저자, 주제, 키워드, 생성 날짜 및 수정 날짜와 같은 정보가 매개변수로 제공됩니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultSetInfo.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 정보 설정: 제목, 제작자, 저자, 주제, 키워드, 생성(날짜), 수정(날짜 수정)*/
      /*값을 설정할 필요가 없으면 undefined 또는 ""(빈 문자열)을 사용하십시오.*/
      /*PDF 파일에 정보(메타데이터)를 설정하고 "ResultSetInfo.pdf"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "PDF 문서 정보 설정", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 정보가 설정될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/)를 호출합니다.
1. PDF 파일 정보를 설정합니다. 제목, 제작자, 저자, 주제, 키워드, 생성일, 수정일 등의 정보가 매개변수로 제공됩니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultSetInfo.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 정보 설정: 제목, 제작자, 저자, 주제, 키워드, 생성일, 수정일*/
  /*값을 설정할 필요가 없으면 undefined 또는 ""(빈 문자열)을 사용하세요*/
  /*PDF 파일에 정보(메타데이터) 설정하고 "ResultSetInfo.pdf"로 저장합니다*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


## PDF 파일 정보 제거

Aspose.PDF for Node.js via C++는 PDF 파일 메타데이터를 제거할 수 있습니다:

PDF에서 메타데이터를 제거하려는 경우, [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) 함수를 사용할 수 있습니다.
Node.js 환경에서 PDF의 메타데이터를 제거하려면 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. AsposePDFforNode.js 모듈을 요구합니다.
1. 정보가 제거될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) 함수를 호출합니다.
1. PDF 파일 정보를 삭제합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPdfRemoveMetadata.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일에서 메타데이터를 제거하고 "ResultPdfRemoveMetadata.pdf"로 저장*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 정보가 제거될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/)를 호출합니다.
1. PDF 파일 정보를 삭제합니다. 따라서 'json.errorCode'가 0인 경우 작업 결과가 "ResultPdfRemoveMetadata.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 나타나는 경우 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일에서 메타데이터를 제거하고 "ResultPdfRemoveMetadata.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```