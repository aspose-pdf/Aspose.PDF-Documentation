---
title: PDF를 EPUB, TeX, 텍스트, XPS로 변환하는 JavaScript
linktitle: PDF를 다른 형식으로 변환
type: docs
weight: 90
url: /javascript-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-01"
keywords: 변환, PDF, EPUB, TeX, 텍스트, XPS, JavaScript
description: 이 주제에서는 JavaScript 또는 JavaScript를 사용하여 PDF 파일을 EPUB, LaTeX, 텍스트, XPS 등과 같은 다른 파일 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

변환 작업은 문서의 페이지 수에 따라 달라지며 시간이 많이 소요될 수 있습니다. 따라서 Web Workers를 사용하는 것을 강력히 권장합니다.

이 코드는 리소스를 많이 소모하는 PDF 파일 변환 작업을 웹 워커로 오프로드하여 메인 UI 스레드가 차단되지 않도록 하는 방법을 보여줍니다. 또한 변환된 파일을 다운로드하는 사용자 친화적인 방법을 제공합니다.

{{% alert color="success" %}}
**PDF를 EPUB로 온라인 변환 시도하기**

Aspose.PDF for JavaScript는 온라인 무료 애플리케이션 ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)를 제공합니다. 여기서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 EPUB으로 변환하는 무료 앱](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## PDF를 EPUB으로 변환

**<abbr title="Electronic Publication">EPUB</abbr>**은 국제 디지털 출판 포럼(IDPF)에서 제공하는 무료 오픈 전자책 표준입니다. 파일 확장자는 .epub입니다. EPUB은 리플로우 가능한 콘텐츠를 위해 설계되었으며, EPUB 리더는 특정 디스플레이 장치에 맞게 텍스트를 최적화할 수 있습니다. EPUB은 고정 레이아웃 콘텐츠도 지원합니다. 이 형식은 출판사와 변환 업체가 내부적으로 사용하며 배포 및 판매를 위한 단일 형식으로 의도되었습니다. 이는 Open eBook 표준을 대체합니다.

```js

    /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커에서 오류 발생: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드됨!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/epub+zip", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileToEPUB = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일을 ePub으로 변환하고 "ResultPDFtoEPUB.epub"로 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToEPUB', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일을 다운로드할 링크 생성*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일 다운로드를 위해 여기를 클릭하세요 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


다음 JavaScript 코드 스니펫은 PDF 페이지를 EPUB 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
2. 'FileReader'를 생성합니다.
3. [AsposePdfToEPUB](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoepub/) 함수가 실행됩니다.
4. 결과 파일의 이름이 설정되며, 이 예제에서는 "ResultPDFtoEPUB.epub"입니다.
5. 다음으로, 'json.errorCode'가 0이면, 결과 파일은 이전에 지정한 이름을 갖게 됩니다. 'json.errorCode' 매개변수가 0이 아니고, 이에 따라 파일에 오류가 발생하면, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
6. 결과적으로 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있도록 합니다.

```js

    var ffileToEPUB = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일을 EPUB로 변환하고 "ResultPDFtoEPUB.epub"로 저장합니다*/
        const json = AsposePdfToEPUB(event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 링크를 만듭니다*/
        DownloadFile(json.fileNameResult, "application/epub+zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**PDF를 LaTeX/TeX로 온라인 변환 시도**

Aspose.PDF for JavaScript는 무료 온라인 애플리케이션 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)를 제공하여 기능과 품질을 조사할 수 있습니다.

[![Aspose.PDF 변환 PDF to LaTeX/TeX 무료 앱](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## PDF를 TeX로 변환

**Aspose.PDF for JavaScript**는 PDF를 TeX로 변환하는 것을 지원합니다. LaTeX 파일 형식은 특별한 마크업이 있는 텍스트 파일 형식이며, 고품질 조판을 위한 TeX 기반 문서 준비 시스템에서 사용됩니다.

```js

  /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/x-tex", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileToTeX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일을 TeX로 변환하고 "ResultPDFtoTeX.tex"로 저장 - 웹 워커에 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTeX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일 다운로드 링크 생성*/
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


다음 JavaScript 코드 스니펫은 PDF 페이지를 TEX 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfToTeX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotex/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정되며, 이 예제에서는 "ResultPDFtoTeX.tex"입니다.
1. 다음으로, 'json.errorCode'가 0인 경우, 결과 파일은 이전에 지정한 이름을 갖게 됩니다. 'json.errorCode' 매개변수가 0이 아닌 경우, 파일에 오류가 발생하게 되며, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제로 결과 파일을 다운로드할 수 있게 합니다.

```js

    var ffileToTeX = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일을 TeX로 변환하고 "ResultPDFtoTeX.tex"로 저장합니다.*/
        const json = AsposePdfToTeX(event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드하는 링크를 만듭니다.*/
        DownloadFile(json.fileNameResult, "application/x-tex");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**PDF를 텍스트로 온라인 변환 시도**

Aspose.PDF for JavaScript는 온라인 무료 애플리케이션 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)을 제공합니다. 여기서 기능과 작동 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 텍스트로 자유로운 앱으로](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF를 TXT로 변환

```js

    /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "text/plain", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileToTxt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일을 Txt로 변환하고 "ResultPDFtoTxt.txt"로 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTxt', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일을 다운로드할 링크 생성*/
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


다음의 JavaScript 코드 스니펫은 PDF 페이지를 TXT 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfToTxt](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotxt/) 함수가 실행됩니다.
1. 결과 파일의 이름을 설정합니다. 이 예제에서는 "ResultPDFtoTxt.txt"입니다.
1. 다음으로 'json.errorCode'가 0이면, 결과 파일은 이전에 지정한 이름을 갖게 됩니다. 'json.errorCode' 매개변수가 0과 같지 않으면, 파일에 오류가 발생하므로 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자 운영 체제로 결과 파일을 다운로드할 수 있도록 합니다.

```js

    var ffileToTxt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일을 Txt로 변환하고 "ResultPDFtoTxt.txt"로 저장합니다.*/
        const json = AsposePdfToTxt(event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 링크를 만듭니다.*/
        DownloadFile(json.fileNameResult, "text/plain");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**PDF를 XPS로 온라인 변환 시도**

Aspose.PDF for JavaScript는 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)라는 무료 온라인 애플리케이션을 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 XPS로 무료 앱과 함께](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## PDF를 XPS로 변환

XPS 파일 형식은 주로 Microsoft Corporation의 XML Paper Specification과 관련이 있습니다. XML Paper Specification(XPS)은 이전에 Metro라는 코드명이 붙었고 Next Generation Print Path(NGPP) 마케팅 개념을 포함하며, Windows 운영 체제에 문서 생성 및 보기 기능을 통합하려는 Microsoft의 이니셔티브입니다.

**Aspose.PDF for JavaScript**는 PDF 파일을 <abbr title="XML Paper Specification">XPS</abbr> 형식으로 변환할 수 있는 기능을 제공합니다. JavaScript를 사용하여 PDF 파일을 XPS 형식으로 변환하기 위해 제시된 코드 스니펫을 사용해 보십시오.

```js

    /* 웹 워커 생성 */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.ms-xpsdocument", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /* 이벤트 핸들러 */
    const ffileToXps = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /* PDF 파일을 XPS로 변환하고 "ResultPDFtoXps.xps"로 저장 - 웹 워커에 요청 */
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXps', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /* 결과 파일을 다운로드할 링크 생성 */
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일 다운로드를 클릭하세요: " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


다음 JavaScript 코드 스니펫은 PDF 페이지를 XPS 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfToXps](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoxps/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예에서는 "ResultPDFtoXps.xps"입니다.
1. 다음으로, 'json.errorCode'가 0이면 결과 파일에 앞서 지정한 이름이 부여됩니다. 'json.errorCode' 매개변수가 0이 아닌 경우, 파일에 오류가 발생하며, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있도록 합니다.

```js

    var ffileToXps = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일을 Xps로 변환하고 "ResultPDFtoXps.xps"로 저장합니다.*/
        const json = AsposePdfToXps(event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 수 있는 링크를 만듭니다.*/
        DownloadFile(json.fileNameResult, "application/vnd.ms-xpsdocument");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## PDF를 회색조 PDF로 변환

Aspose.PDF for JavaScript를 통해 PDF를 흑백으로 변환 C++ 웹 툴킷을 사용합니다. PDF를 회색조로 변환해야 하는 이유는 무엇인가요? PDF 파일에 많은 컬러 이미지가 포함되어 있고 파일 크기가 중요할 때 컬러 대신 변환하면 공간을 절약할 수 있습니다. PDF 파일을 흑백으로 인쇄할 경우 변환하면 최종 결과가 어떻게 보일지 시각적으로 확인할 수 있습니다.

```js

  /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileConvertToGrayscale = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일을 회색조로 변환하고 "ResultConvertToGrayscale.pdf"로 저장 - 웹 워커에 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToGrayscale', "params": [event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf"] }, [event.target.result]);
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
        link.innerHTML = "파일 " + filename + " 다운로드하려면 여기를 클릭하세요.";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


다음 JavaScript 코드 스니펫은 PDF 페이지를 그레이스케일 PDF로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttograyscale/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정되며, 이 예제에서는 "ResultConvertToGrayscale.pdf"입니다.
1. 다음으로, 'json.errorCode'가 0이면, DownloadFile이 이전에 지정한 이름을 부여받습니다. 'json.errorCode' 매개변수가 0이 아니고, 이에 따라 파일에 오류가 있는 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있도록 합니다.

```js

  var ffileConvertToGrayscale = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일을 그레이스케일로 변환하고 "ResultConvertToGrayscale.pdf"로 저장*/
      const json = AsposePdfConvertToGrayscale(event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*결과 파일을 다운로드할 링크 생성*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```