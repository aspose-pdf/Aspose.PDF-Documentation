---
title: JavaScript에서 PDF를 이미지 형식으로 변환
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /ko/javascript-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-01"
description: 이 주제는 Aspose.PDF를 사용하여 PDF를 TIFF, BMP, JPEG, PNG, SVG 등의 다양한 이미지 형식으로 변환하는 방법을 몇 줄의 코드로 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## JavaScript PDF를 이미지로 변환

이 기사에서는 PDF를 이미지 형식으로 변환하는 옵션을 보여줍니다.

이전에 스캔된 문서는 종종 PDF 파일 형식으로 저장됩니다. 그러나 그래픽 편집기에서 편집하거나 이미지 형식으로 더 보내야 할 필요가 있습니까? 우리는 PDF를 이미지를 사용하여 변환할 수 있는 범용 도구를 제공합니다. 가장 일반적인 작업은 전체 PDF 문서나 문서의 특정 페이지를 이미지 세트로 저장해야 할 때입니다. **JavaScript용 Aspose via C++**를 사용하면 특정 PDF 파일에서 이미지를 얻기 위해 필요한 단계를 단순화하여 PDF를 JPG 및 PNG 형식으로 변환할 수 있습니다.

**JavaScript용 Aspose.PDF via C++**는 다양한 PDF를 이미지 형식으로 변환하는 것을 지원합니다.
 Please check the section [Aspose.PDF 지원 파일 형식](https://docs.aspose.com/pdf/javascript-cpp/supported-file-formats/).

변환 작업은 문서의 페이지 수에 따라 달라지며 시간이 많이 소요될 수 있습니다. 따라서 Web Workers를 사용하는 것을 강력히 권장합니다.

이 코드는 리소스를 많이 소모하는 PDF 파일 변환 작업을 웹 워커로 오프로드하여 메인 UI 스레드가 차단되지 않도록 하는 방법을 보여줍니다. 또한 변환된 파일을 다운로드하는 사용자 친화적인 방법도 제공합니다.

{{% alert color="success" %}}
**PDF를 JPEG로 온라인 변환 시도하기**

Aspose.PDF for JavaScript는 ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg)라는 온라인 무료 응용 프로그램을 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![무료 앱으로 Aspose.PDF 변환 PDF to JPEG](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## PDF를 JPEG로 변환

```js

  /*Web Worker 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Worker에서 오류 발생: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로딩 완료!' :
        (evt.data.json.errorCode == 0) ? 
          `파일(페이지) 수: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileToJpg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*PDF 파일을 jpg 파일로 변환하고 템플릿 "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... 페이지 번호 형식), 해상도 150 DPI로 저장 - Web Worker 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToJpg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [코드 스니펫]

    /*결과 파일을 다운로드할 링크 생성*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일을 다운로드하려면 여기를 클릭하세요: " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```

다음 JavaScript 코드 스니펫은 PDF 페이지를 Jpeg 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestojpg/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예제에서는 "ResultPdfToJpg{0:D2}.jpg"로 설정됩니다.
1. 다음으로, 'json.errorCode'가 0이면, 결과 파일은 이전에 지정한 이름을 갖게 됩니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있을 경우, 이러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수가 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 해줍니다.

```js

  var ffileToJpg = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일을 jpg 파일로 변환하고, 템플릿 "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... 형식 페이지 번호), 해상도 150 DPI로 저장*/
      const json = AsposePdfPagesToJpg(event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "파일(페이지) 수: " + json.filesCount.toString();
        /*결과 파일에 대한 링크 생성*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**PDF를 TIFF로 온라인 변환 시도하기**

Aspose.PDF for JavaScript는 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF to TIFF 무료 앱](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## PDF를 TIFF로 변환

```js

  /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ? 
          `파일(페이지) 수: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/tiff", element) ) ?? ""}` : 
          `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileToTiff = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일을 TIFF로 변환 - 템플릿 "ResultPdfToTiff{0:D2}.tiff" 사용 ({0}, {0:D2}, {0:D3}, ... 페이지 번호 형식), 해상도 150 DPI로 저장 - 웹 워커에게 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToTiff', "params": [event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일 다운로드 링크 생성*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일을 다운로드하려면 여기를 클릭하세요: " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


다음 JavaScript 코드 스니펫은 PDF 페이지를 Tiff 파일로 변환하는 간단한 예를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 만듭니다.
1. [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestotiff/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예제에서는 "ResultPdfToTiff{0:D2}.tiff"입니다.
1. 다음으로, 'json.errorCode'가 0이면 DownloadFile이 이전에 지정한 이름을 갖게 됩니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있을 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있도록 합니다.

```js

    var ffileToTiff = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일을 "ResultPdfToTiff{0:D2}.tiff" 템플릿으로 변환 ({0}, {0:D2}, {0:D3}, ... 형식의 페이지 번호), 해상도 150 DPI로 저장*/
        const json = AsposePdfPagesToTiff(event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "파일(페이지) 수: " + json.filesCount.toString();
          /*결과 파일에 대한 링크 생성*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/tiff");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


{{% alert color="success" %}}
**PDF를 PNG로 온라인 변환 시도하기**

우리의 무료 애플리케이션이 어떻게 작동하는지 예시로 다음 기능을 확인하세요.

Aspose.PDF for JavaScript는 온라인 무료 애플리케이션 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)를 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![무료 앱을 사용하여 PDF를 PNG로 변환하는 방법](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## PDF를 PNG로 변환하기

```js

  /*웹 워커 생성하기*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커의 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로딩 완료!' :
        (evt.data.json.errorCode == 0) ? 
          `파일(페이지) 수: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/png", element) ) ?? ""}` : 
          `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileToPng = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*PDF 파일을 png 파일로 변환하여 템플릿 "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... 형식 페이지 번호), 해상도 150 DPI로 저장 - 웹 워커에 요청하기*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToPng', "params": [event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [코드 스니펫]

    /*결과 파일을 다운로드할 링크 만들기*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일을 다운로드하려면 여기를 클릭하세요 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


다음 JavaScript 코드 스니펫은 PDF 페이지를 PNG 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfPagesToPng](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestopng/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정되며, 이 예제에서는 "ResultPdfToPng{0:D2}.png"로 설정됩니다.
1. 다음으로 'json.errorCode'가 0이면, DownloadFile이 앞서 지정한 이름을 받습니다. 'json.errorCode' 매개 변수가 0이 아니고, 따라서 파일에 오류가 있는 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제로 결과 파일을 다운로드할 수 있게 합니다.

```js

  var ffileToPng = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일을 png 파일로 변환합니다. 템플릿 "ResultPdfToPng{0:D2}.png"을 사용하고 ({0}, {0:D2}, {0:D3}, ... 형식의 페이지 번호), 해상도 150 DPI로 저장합니다.*/
      const json = AsposePdfPagesToPng(event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "파일(페이지) 수: " + json.filesCount.toString();
        /*결과 파일에 대한 링크 생성*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/png");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**PDF를 SVG로 온라인으로 변환해 보세요**

Aspose.PDF for JavaScript는 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 작업 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF to SVG 무료 앱](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**스케일러블 벡터 그래픽스(SVG)**는 2차원 벡터 그래픽(정적 및 동적(대화형 또는 애니메이션))을 위한 XML 기반 파일 형식의 사양 가족입니다. SVG 사양은 1999년부터 World Wide Web Consortium (W3C)에 의해 개발된 공개 표준입니다.

## PDF를 SVG로 변환

```js

  /* 웹 워커 생성 */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커에서 오류 발생: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드됨!' :
        (evt.data.json.errorCode == 0) ? 
          `파일(페이지) 수: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/svg", element) ) ?? ""}` : 
          `오류: ${evt.data.json.errorText}`;

    /* 이벤트 핸들러 */
    const ffileToSvg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /* PDF 파일을 SVG로 변환 - 웹 워커 요청 */
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /* 결과 파일을 다운로드할 링크 만들기 */
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일을 다운로드하려면 여기를 클릭하세요: " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


다음 JavaScript 코드 스니펫은 PDF 페이지를 SVG 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvg/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정되며, 이 예제에서는 "ResultPdfToSvg.svg"입니다.
1. 다음으로, 'json.errorCode'가 0이면, DownloadFile에 이전에 지정한 이름이 부여됩니다. 'json.errorCode' 매개변수가 0이 아닌 경우 파일에 오류가 발생하며, 해당 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있도록 합니다.

```js

    var ffileToSvg = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일을 SVG로 변환합니다.*/
        const json = AsposePdfPagesToSvg(event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "파일(페이지) 수: " + json.filesCount.toString();
          /*결과 파일에 대한 링크를 만듭니다.*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/svg");
        }
        else document.getElementById('output').textContent = json.errorText;
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


### PDF를 압축된 SVG로 변환

```js

  /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/zip", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileToSvgZip = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일을 SVG(zip)로 변환하고 "ResultPdfToSvgZip.zip" 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvgZip', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일을 다운로드하는 링크 생성*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일을 다운로드하려면 여기를 클릭하세요 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


다음 JavaScript 코드 스니펫은 PDF 페이지를 SVG(zip) 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvgzip/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예제에서는 "ResultPdfToSvgZip.zip"입니다.
1. 다음으로, 'json.errorCode'가 0이면, 지정한 이름으로 DownloadFile이 주어집니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있는 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 합니다.

```js

    var ffileToSvgZip = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일을 SVG(zip)로 변환하고 "ResultPdfToSvgZip.zip"으로 저장*/
        const json = AsposePdfPagesToSvgZip(event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 수 있는 링크 생성*/
        DownloadFile(json.fileNameResult, "application/zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## PDF를 DICOM으로 변환

```js

  /*웹 워커 생성*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`웹 워커에서 오류 발생: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? '로드됨!' :
      (evt.data.json.errorCode == 0) ?
        `파일(페이지) 수: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
          (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "application/dicom", element) ) ?? ""}` :
        `오류: ${evt.data.json.errorText}`;

  /*이벤트 핸들러*/
  const ffileToDICOM = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*PDF 파일을 DICOM으로 변환 - 템플릿 "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... 페이지 번호 형식), 해상도 150 DPI로 저장 - 웹 워커에게 요청*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToDICOM', "params": [event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150] }, [event.target.result]);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

  /*결과 파일을 다운로드할 링크 생성*/
  const DownloadFile = (filename, mime, content) => {
      mime = mime || "application/octet-stream";
      var link = document.createElement("a"); 
      link.href = URL.createObjectURL(new Blob([content], {type: mime}));
      link.download = filename;
      link.innerHTML = "파일을 다운로드하려면 여기를 클릭하세요: " + filename;
      document.body.appendChild(link); 
      document.body.appendChild(document.createElement("br"));
      return filename;
    }
```


다음의 JavaScript 코드 스니펫은 PDF 페이지를 DICOM 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestodicom/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정되며, 이 예제에서는 "ResultPdfToDICOM{0:D2}.dcm"입니다.
1. 다음으로, 'json.errorCode'가 0이면, 결과 파일이 이전에 지정한 이름을 갖게 됩니다. 'json.errorCode' 매개변수가 0이 아니면, 파일에 오류가 있을 것이며, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수가 링크를 생성하고 사용자의 운영 체제로 결과 파일을 다운로드할 수 있도록 합니다.

```js

  var ffileToDICOM = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일을 DICOM으로 변환하는 템플릿 "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... 형식의 페이지 번호), 해상도 150 DPI로 저장합니다.*/
      const json = AsposePdfPagesToDICOM(event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "파일(페이지) 수: " + json.filesCount.toString();
        /*결과 파일에 대한 링크를 만듭니다.*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "application/dicom");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## PDF를 BMP로 변환

```js

    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커에서 오류 발생: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ? 
          `파일(페이지) 수: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/bmp", element) ) ?? ""}` : 
          `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileToBmp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일을 템플릿 "ResultPdfToBmp{0:D2}.bmp"로 BMP로 변환합니다. (페이지 번호 형식은 {0}, {0:D2}, {0:D3} 등), 해상도는 150 DPI이며 저장합니다 - 웹 워커에게 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToBmp', "params": [event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일을 다운로드할 링크 생성*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "여기를 클릭하여 파일을 다운로드하세요: " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


다음 JavaScript 코드 스니펫은 PDF 페이지를 BMP 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestobmp/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예제에서는 "ResultPdfToBmp{0:D2}.bmp"입니다.
1. 다음으로, 'json.errorCode'가 0이면, 이전에 지정한 이름으로 DownloadFile이 제공됩니다. 'json.errorCode' 매개변수가 0이 아니고, 파일에 오류가 있는 경우, 해당 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 합니다.

```js

    var ffileToBmp = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일을 템플릿 "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... 페이지 번호 형식), 해상도 150 DPI로 BMP로 변환하고 저장*/
        const json = AsposePdfPagesToBmp(event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "파일(페이지) 개수: " + json.filesCount.toString();
          /*결과 파일에 대한 링크 생성*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/bmp");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```