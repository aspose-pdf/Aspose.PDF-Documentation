---
title: Node.js에서 PDF를 이미지 형식으로 변환
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-16"
description: 이 주제는 Node.js 환경에서 몇 줄의 코드로 Aspose.PDF를 사용하여 PDF를 다양한 이미지 형식(e.g. TIFF, BMP, JPEG, PNG, SVG)으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js PDF를 이미지로 변환

이 문서에서는 PDF를 이미지 형식으로 변환하는 옵션을 보여드립니다.

이전에 스캔된 문서는 종종 PDF 파일 형식으로 저장됩니다. 그러나 그래픽 편집기에서 편집하거나 이미지 형식으로 더 보내야 할 필요가 있습니까? PDF를 이미지를 사용하여 변환할 수 있는 범용 도구가 있습니다. 가장 일반적인 작업은 전체 PDF 문서 또는 문서의 특정 페이지를 이미지 세트로 저장해야 할 때입니다.
 **Aspose for Node.js via C++** 은 특정 PDF 파일에서 이미지를 가져오는 데 필요한 단계를 간소화하기 위해 PDF를 JPG 및 PNG 형식으로 변환할 수 있습니다.

**Aspose.PDF for Node.js via C++** 는 다양한 PDF를 이미지 형식으로 변환하는 것을 지원합니다. [Aspose.PDF 지원 파일 형식](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/) 섹션을 확인하십시오.

{{% alert color="success" %}}
**PDF를 JPEG로 온라인 변환 시도하기**

Aspose.PDF for Node.js는 ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg)라는 무료 온라인 애플리케이션을 제공하며, 여기서 기능과 작동 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 PDF to JPEG with Free App](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## PDF를 JPEG로 변환하기

PDF 문서를 변환하려는 경우 [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/) 함수를 사용할 수 있습니다.

Node.js 환경에서 변환하기 위한 다음 코드 스니펫을 확인하십시오.
**CommonJS:**

1. `require`을 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환될 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과는 "ResultPdfToJpg{0:D2}.jpg"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI의 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 JPG로 변환하여 "ResultPdfToJpg{0:D2}.jpg" 템플릿({0}, {0:D2}, {0:D3}, ... 형식 페이지 번호), 해상도 150 DPI로 저장*/
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 반환받습니다.
1. 함수 [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면, 작업 결과는 "ResultPdfToJpg{0:D2}.jpg"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI 해상도로 저장됩니다. 만약 json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생하면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 "ResultPdfToJpg{0:D2}.jpg" 템플릿으로 JPG로 변환합니다. ({0}, {0:D2}, {0:D3}, ... 형식의 페이지 번호), 해상도 150 DPI로 저장*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**PDF를 TIFF로 온라인으로 변환 시도**

Node.js용 Aspose.PDF는 무료 온라인 애플리케이션 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)를 제공하여 기능과 품질을 조사할 수 있습니다.

[![무료 앱으로 Aspose.PDF 변환 PDF to TIFF](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## PDF를 TIFF로 변환

만약 PDF 문서를 변환하고 싶다면 [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/) 함수를 사용할 수 있습니다. 
Node.js 환경에서 변환하기 위해 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.

1. 함수 [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과가 "ResultPdfToTiff{0:D2}.tiff"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI의 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* 템플릿 "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... 형식의 페이지 번호), 해상도 150 DPI로 PDF 파일을 TIFF로 변환하고 저장합니다. */
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/) 함수를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면, 작업 결과가 "ResultPdfToTiff{0:D2}.tiff"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 "ResultPdfToTiff{0:D2}.tiff" 템플릿으로 변환합니다. ({0}, {0:D2}, {0:D3}, ... 페이지 번호 형식), 해상도 150 DPI로 저장*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**PDF를 PNG로 온라인에서 변환해보세요**

무료 애플리케이션이 어떻게 작동하는지 예를 들어 보려면 다음 기능을 확인하세요.

Aspose.PDF for Node.js는 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)라는 온라인 무료 애플리케이션을 제공하여 기능과 작동 품질을 조사할 수 있습니다.

[![무료 앱을 사용하여 PDF를 PNG로 변환하는 방법](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## PDF를 PNG로 변환하기

PDF 문서를 변환하려는 경우 [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/) 기능을 사용할 수 있습니다.
다음 코드 스니펫을 확인하여 Node.js 환경에서 변환을 수행하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공 시 객체를 수신합니다.

1. 함수 [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/)을 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과는 "ResultPdfToPng{0:D2}.png"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI의 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고, 이에 따라 파일에 오류가 나타나면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 PNG로 변환하여 "ResultPdfToPng{0:D2}.png" 템플릿으로 저장합니다 ({0}, {0:D2}, {0:D3}, ... 형식의 페이지 번호), 해상도 150 DPI*/
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/)을 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과는 "ResultPdfToPng{0:D2}.png"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 나타나면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 "ResultPdfToPng{0:D2}.png" 템플릿으로 PNG로 변환하고 (페이지 번호 형식: {0}, {0:D2}, {0:D3}, ...), 150 DPI 해상도로 저장합니다*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**PDF를 SVG로 온라인 변환 시도**

Aspose.PDF for Node.js는 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)라는 온라인 무료 애플리케이션을 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to SVG with Free App](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**스케일러블 벡터 그래픽스 (SVG)**는 정적 및 동적(상호작용 또는 애니메이션) 2차원 벡터 그래픽을 위한 XML 기반 파일 형식의 사양 가족입니다. SVG 사양은 1999년부터 월드 와이드 웹 컨소시엄(W3C)에 의해 개발되고 있는 오픈 표준입니다.

## PDF를 SVG로 변환

### PDF를 고전적인 SVG로 변환

PDF 문서를 변환하려는 경우, [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/) 함수를 사용할 수 있습니다.
Node.js 환경에서 변환하기 위한 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 임포트합니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPdfToSvg.svg"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 파일에 오류가 발생한 경우 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 SVG로 변환하고 "ResultPdfToSvg.svg"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPdfToSvg.svg"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 SVG로 변환하고 "ResultPdfToSvg.svg"로 저장*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### PDF를 압축된 SVG로 변환

PDF 문서를 변환하려는 경우, [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/) 함수를 사용할 수 있습니다.
 
다음 코드 스니펫을 확인하여 Node.js 환경에서 변환하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/)을 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPdfToSvgZip.zip"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 이에 따라 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 SVG(zip)로 변환하고 "ResultPdfToSvgZip.zip"에 저장합니다.*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/)을 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPdfToSvgZip.zip"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /* PDF 파일을 SVG zip으로 변환하고 "ResultPdfToSvgZip.zip"에 저장합니다 */
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## PDF를 DICOM으로 변환

PDF 문서를 변환하려는 경우, [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/) 함수를 사용할 수 있습니다.
 
다음 코드 스니펫을 확인하여 Node.js 환경에서 변환하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공 시 객체를 받습니다.
1. 함수 [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/)을 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과가 "ResultPdfToDICOM{0:D2}.dcm"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* PDF 파일을 DICOM으로 변환, 템플릿 "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... 형식 페이지 번호), 해상도 150 DPI로 저장 */
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/)을 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면, 작업 결과는 "ResultPdfToDICOM{0:D2}.dcm"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI의 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 DICOM으로 변환하여 "ResultPdfToDICOM{0:D2}.dcm" 템플릿으로 저장합니다 ({0}, {0:D2}, {0:D3}, ... 형식 페이지 번호), 해상도는 150 DPI*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


## PDF를 BMP로 변환

PDF 문서를 변환하려는 경우, [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/) 함수를 사용할 수 있습니다. Node.js 환경에서 변환하기 위한 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/) 함수를 호출합니다.

1. PDF 파일 변환. 따라서, 'json.errorCode'가 0이면, 작업의 결과는 "ResultPdfToBmp{0:D2}.bmp"에 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생한 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 BMP로 변환하여 "ResultPdfToBmp{0:D2}.bmp" 템플릿으로 저장 ({0}, {0:D2}, {0:D3}, ... 형식의 페이지 번호), 해상도 150 DPI로 저장*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.

1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과는 "ResultPdfToBmp{0:D2}.bmp"로 저장됩니다. 여기서 {0:D2}는 두 자리 형식의 페이지 번호를 나타냅니다. 이미지는 150 DPI의 해상도로 저장됩니다. json.errorCode 매개변수가 0이 아니고, 파일에 오류가 나타나는 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 BMP로 변환하고 템플릿 "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... 형식 페이지 번호), 해상도 150 DPI로 저장합니다*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```