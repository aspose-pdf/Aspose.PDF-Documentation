---
title: Node.js에서 PDF를 Word 문서로 변환
linktitle: PDF를 Word로 변환
type: docs
weight: 10
url: /ko/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2026-07-18"
description: Node.js 환경에서 PDF를 DOC(DOCX)로 변환하는 방법을 배우세요.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Microsoft Word 또는 DOC와 DOCX 형식을 지원하는 다른 워드 프로세서에서 PDF 파일의 내용을 편집하려면. PDF 파일은 편집이 가능하지만, DOC와 DOCX 파일이 더 유연하고 맞춤형입니다.

{{% alert color="success" %}}
**PDF를 DOC로 온라인 변환해 보세요**

Aspose.PDF for Node.js는 온라인 무료 애플리케이션을 제공합니다 ["PDF를 DOC로"](https://products.aspose.app/pdf/conversion/pdf-to-doc), 여기서 기능과 품질을 직접 확인해 볼 수 있습니다.

[![PDF를 DOC로 변환](/pdf/ko/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF를 DOC로 변환

PDF 문서를 변환하려는 경우, 다음을 사용할 수 있습니다 [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/) 함수. 
Node.js 환경에서 변환하려면 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 변환될 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로 파일 변환 작업을 수행하고, 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPDFtoDoc.doc"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 나타나는 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 변환될 PDF 파일의 이름을 지정하십시오
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPDFtoDoc.doc"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 나타나는 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**PDF를 DOCX로 온라인 변환해 보세요**

Aspose.PDF for Node.js는 온라인 무료 애플리케이션을 제공합니다 ["PDF를 Word로"](https://products.aspose.app/pdf/conversion/pdf-to-docx), 여기서 기능과 품질을 직접 확인해 볼 수 있습니다.

[![Aspose.PDF PDF를 Word로 변환 무료 앱](/pdf/ko/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## PDF를 DOCX로 변환

Aspose.PDF for Node.js via C++ 툴킷을 사용하면 PDF 문서를 읽고 DOCX로 변환할 수 있습니다. DOCX는 Microsoft Word 문서의 널리 알려진 형식으로, 구조가 기존의 순수 바이너리에서 XML과 바이너리 파일의 조합으로 변경되었습니다. Docx 파일은 Word 2007 및 이후 버전에서 열 수 있지만, DOC 파일 확장자를 지원하는 이전 버전의 MS Word에서는 열 수 없습니다.

PDF 문서를 변환하려는 경우, 다음을 사용할 수 있습니다 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/) 함수. 
Node.js 환경에서 변환하려면 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 변환될 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로 파일 변환 작업을 수행하고, 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPDFtoDocX.docx"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 나타나는 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 변환될 PDF 파일의 이름을 지정하십시오
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPDFtoDocX.docx"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 나타나는 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


