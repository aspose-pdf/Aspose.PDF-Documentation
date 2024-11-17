---
title: PDF를 EPUB, TeX, Text, XPS로 변환하기 in Node.js
linktitle: PDF를 다른 형식으로 변환하기
type: docs
weight: 90
url: /ko/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-16"
description: 이 주제는 Node.js 환경에서 PDF 파일을 EPUB, LaTeX, Text, XPS 등과 같은 다른 파일 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**온라인으로 PDF를 EPUB로 변환해보세요**

Aspose.PDF for Node.js는 온라인 무료 애플리케이션 ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 PDF to EPUB 무료 앱과 함께](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## PDF를 EPUB로 변환하기

**<abbr title="Electronic Publication">EPUB</abbr>**은 국제 디지털 출판 포럼(IDPF)에서 제공하는 무료 및 오픈 전자책 표준입니다.
 파일의 확장자는 .epub입니다.  
EPUB은 리플로우 가능한 콘텐츠를 위해 설계되었으며, 이는 EPUB 리더가 특정 디스플레이 장치에 맞춰 텍스트를 최적화할 수 있음을 의미합니다. EPUB은 고정 레이아웃 콘텐츠도 지원합니다. 이 형식은 출판사와 변환 업체가 내부적으로 사용할 수 있는 단일 형식으로 의도되었으며, 배포 및 판매를 위해서도 사용됩니다. 이는 Open eBook 표준을 대체합니다.

PDF 문서를 변환하려는 경우, [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/) 함수를 사용할 수 있습니다. Node.js 환경에서 변환하기 위해 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/)을 호출합니다.
1. PDF 파일 변환. 따라서 'json.errorCode'가 0이면, 작업의 결과는 "ResultPDFtoEPUB.epub"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 ePub으로 변환하고 "ResultPDFtoEPUB.epub"으로 저장*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/)을 호출합니다.

1. PDF 파일 변환. 따라서 'json.errorCode'가 0이면, 작업의 결과는 "ResultPDFtoEPUB.epub"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 ePub으로 변환하고 "ResultPDFtoEPUB.epub"에 저장합니다*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**PDF를 LaTeX/TeX로 온라인 변환 시도하기**

Aspose.PDF for Node.js는 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)라는 무료 온라인 응용 프로그램을 제공합니다. 여기서 기능과 품질을 조사해 볼 수 있습니다.


[![Aspose.PDF 변환 PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## PDF를 TeX로 변환

**Aspose.PDF for Node.js**는 PDF를 TeX로 변환하는 것을 지원합니다.
PDF 문서를 변환하려는 경우 [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/) 함수를 사용할 수 있습니다.
Node.js 환경에서 변환하려면 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. `require`을 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPDFtoTeX.tex"에 저장됩니다. json.errorCode 매개변수가 0이 아니며, 따라서 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 TeX로 변환하고 "ResultPDFtoTeX.tex"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 수신합니다.
1. 함수 [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/)을 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPDFtoTeX.tex"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 따라서 파일에 오류가 나타나면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 TeX로 변환하고 "ResultPDFtoTeX.tex"에 저장합니다.*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**온라인으로 PDF를 텍스트로 변환해 보세요**

Node.js용 Aspose.PDF는 온라인 무료 애플리케이션 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)를 제공하여 기능과 작업의 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF를 TXT로 변환

PDF 문서를 변환하려면 [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/) 기능을 사용할 수 있습니다. Node.js 환경에서 변환하기 위해 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/)를 호출합니다.

1. PDF 파일 변환. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPDFtoTxt.txt"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 Txt로 변환하고 "ResultPDFtoTxt.txt"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/)를 호출합니다.

1. PDF 파일 변환. 따라서 'json.errorCode'가 0이면, 작업의 결과가 "ResultPDFtoTxt.txt"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 Txt로 변환하고 "ResultPDFtoTxt.txt"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**온라인에서 PDF를 XPS로 변환해보세요**

Aspose.PDF for Node.js는 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해 볼 수 있습니다.


[![Aspose.PDF 변환 PDF를 XPS로 무료 앱](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## PDF를 XPS로 변환

XPS 파일 형식은 주로 Microsoft Corporation의 XML Paper Specification과 관련이 있습니다. XML Paper Specification (XPS)은 이전에 메트로라는 코드명이었으며 차세대 인쇄 경로(NGPP) 마케팅 개념을 포함하는 Microsoft의 Windows 운영 체제에 문서 생성 및 보기 기능을 통합하려는 이니셔티브입니다.

**Aspose.PDF for Node.js**는 PDF 파일을 <abbr title="XML Paper Specification">XPS</abbr> 형식으로 변환할 수 있는 기능을 제공합니다. 제시된 코드 스니펫을 사용하여 Node.js에서 PDF 파일을 XPS 형식으로 변환해 보겠습니다.

PDF 문서를 변환하려면 [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/) 함수를 사용할 수 있습니다. Node.js 환경에서 변환하려면 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.

1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPDFtoXps.xps"에 저장됩니다. json.errorCode 매개 변수가 0이 아니고, 파일에 오류가 발생한 경우 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 Xps로 변환하고 "ResultPDFtoXps.xps"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.

1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/) 함수를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면, 작업 결과는 "ResultPDFtoXps.xps"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 오류가 파일에 나타나는 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 Xps로 변환하고 "ResultPDFtoXps.xps"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## PDF를 그레이스케일 PDF로 변환

Aspose.PDF for Node.js를 통해 C++ 툴킷으로 PDF를 흑백으로 변환합니다. 
왜 PDF를 그레이스케일로 변환해야 하나요?
 PDF 파일에 많은 컬러 이미지가 포함되어 있고, 파일 크기가 색상보다 중요하다면 변환하여 공간을 절약할 수 있습니다. PDF 파일을 흑백으로 인쇄하면 변환을 통해 최종 결과물이 어떻게 보일지 시각적으로 확인할 수 있습니다.

PDF 문서를 변환하려는 경우, [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) 함수를 사용할 수 있습니다. Node.js 환경에서 변환하려면 다음 코드 조각을 확인하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 수신합니다.
1. 함수 [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/)을 호출합니다.
1. PDF 파일 변환. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultConvertToGrayscale.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /*PDF 파일을 그레이스케일로 변환하고 "ResultConvertToGrayscale.pdf"로 저장*/
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.

1. 함수 [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과가 "ResultConvertToGrayscale.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 그레이스케일로 변환하고 "ResultConvertToGrayscale.pdf"로 저장합니다*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```