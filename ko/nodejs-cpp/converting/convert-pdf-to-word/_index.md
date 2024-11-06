---
title: Node.js에서 PDF를 Word 문서로 변환
linktitle: PDF를 Word로 변환
type: docs
weight: 10
url: ko/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2023-11-16"
description: Node.js 환경에서 PDF를 DOC(DOCX)로 변환하는 방법을 배웁니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Microsoft Word 또는 DOC 및 DOCX 형식을 지원하는 다른 워드 프로세서에서 PDF 파일의 내용을 편집할 수 있습니다. PDF 파일은 편집 가능하지만 DOC 및 DOCX 파일은 더 유연하고 사용자 정의가 가능합니다.

{{% alert color="success" %}}
**PDF를 DOC로 온라인으로 변환해보세요**

Aspose.PDF for Node.js는 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)라는 무료 온라인 애플리케이션을 제공하여 기능과 품질을 확인할 수 있습니다.

[![Convert PDF to DOC](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF를 DOC로 변환

PDF 문서를 변환하려면 [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/) 함수를 사용할 수 있습니다.
 
해당 코드 스니펫을 Node.js 환경으로 변환하기 위해 아래 내용을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 임포트합니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/) 함수를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPDFtoDoc.doc"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 Doc으로 변환하고 "ResultPDFtoDoc.doc"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/) 함수를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPDFtoDoc.doc"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 Doc으로 변환하고 "ResultPDFtoDoc.doc"에 저장합니다.*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**PDF를 DOCX로 온라인 변환 시도하기**

Node.js용 Aspose.PDF는 온라인 무료 애플리케이션 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)를 제공합니다. 여기서 기능과 품질을 확인해볼 수 있습니다.

[![Aspose.PDF 변환 PDF에서 Word 무료 앱](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## PDF를 DOCX로 변환

C++를 통한 Node.js용 Aspose.PDF 툴킷을 사용하면 PDF 문서를 읽고 DOCX로 변환할 수 있습니다. DOCX는 구조가 간단한 이진 파일에서 XML과 이진 파일의 조합으로 변경된 Microsoft Word 문서의 잘 알려진 형식입니다. Docx 파일은 Word 2007 및 측면 버전으로 열 수 있지만 DOC 파일 확장명을 지원하는 이전 버전의 MS Word에서는 열 수 없습니다.

PDF 문서를 변환하려는 경우 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/) 함수를 사용할 수 있습니다.
Node.js 환경에서 변환하려면 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.

1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPDFtoDocX.docx"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 DocX로 변환하고 "ResultPDFtoDocX.docx"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.

1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPDFtoDocX.docx"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 DocX로 변환하고 "ResultPDFtoDocX.docx"로 저장합니다*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```