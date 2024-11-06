---
title: PDF를 PDF/A 포맷으로 변환
linktitle: PDF를 PDF/A 포맷으로 변환
type: docs
weight: 100
url: ko/javascript-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-01"
description: 이 주제에서는 Aspose.PDF를 사용하여 PDF 파일을 PDF/A 호환 PDF 파일로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for JavaScript**는 PDF 파일을 <abbr title="Portable Document Format / A">PDF/A</abbr> 호환 PDF 파일로 변환할 수 있게 해줍니다.

변환 작업은 문서의 페이지 수에 따라 달라지며 시간이 많이 소요될 수 있습니다. 따라서 웹 워커 사용을 강력히 권장합니다.

이 코드는 리소스를 많이 소모하는 PDF 파일 변환 작업을 웹 워커로 오프로드하여 메인 UI 스레드가 차단되는 것을 방지하는 방법을 보여줍니다. 또한 변환된 파일을 다운로드하는 사용자 친화적인 방법을 제공합니다.

{{% alert color="success" %}}
**PDF를 PDF/A로 온라인 변환 시도**

Aspose.PDF for JavaScript는 온라인 무료 애플리케이션 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)를 제공하여 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## PDF를 PDF/A 형식으로 변환

```js

  /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로딩 완료!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}\n${DownloadFile(evt.data.json.fileNameLogResult, "application/xml", evt.data.params[1])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffilePdfConvertToPDFA = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pdfFormat = 'Module.PdfFormat.PDF_A_1A';
        /*PDF 파일을 PDF/A(1A)로 변환하고 "ResultConvertToPDFA.pdf"로 저장*/
        /*변환 과정에서 검증도 수행됨, "ResultConvertToPDFA.xml" - 웹 워커에게 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToPDFA', "params": [event.target.result, e.target.files[0].name, pdfFormat, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml"] }, [event.target.result]);
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
        link.innerHTML = "파일 다운로드를 위해 여기를 클릭하세요 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


다음 JavaScript 코드 스니펫은 PDF를 PDF/A 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttopdfa/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정되며, 이 예제에서는 "ResultConvertToPDFA.pdf"입니다. 변환 과정에서 검증도 수행되며, "ResultConvertToPDFA.xml"입니다.
1. 다음으로, 'json.errorCode'가 0이면, 지정한 이름으로 DownloadFile이 제공됩니다. 'json.errorCode' 매개변수가 0이 아니면, 파일에 오류가 발생하며, 이러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자 운영 체제로 결과 파일을 다운로드할 수 있는 링크를 제공합니다. 로그 (xml) 파일을 다운로드할 수 있는 링크도 제공합니다.

```js

  var ffilePdfConvertToPDFA = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일을 PDF/A(1A)로 변환하고 "ResultConvertToPDFA.pdf"로 저장합니다.*/
      /*변환 과정에서 검증도 수행되며, "ResultConvertToPDFA.xml"입니다.*/
      const json = AsposePdfConvertToPDFA(event.target.result, e.target.files[0].name, Module.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml");
      if (json.errorCode == 0)
      {
        document.getElementById('output').textContent = json.fileNameResult + "\n로그 파일 (xml 형식): " + json.fileNameLogResult;
        /*결과 파일을 다운로드할 수 있는 링크 생성*/
        DownloadFile(json.fileNameResult, "application/pdf");
      }
      else document.getElementById('output').textContent = json.errorText + "\n로그 파일 (xml 형식): " + json.fileNameLogResult;
      /*로그 (xml)를 다운로드할 수 있는 링크 생성*/
      DownloadFile(json.fileNameLogResult, "application/xml");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```