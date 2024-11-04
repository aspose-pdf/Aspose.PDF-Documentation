---
title: JavaScript에서 PDF를 Excel로 변환
linktitle: PDF를 Excel로 변환
type: docs
weight: 20
url: /javascript-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-01"
keywords: javascript를 사용하여 PDF를 Excel로 변환, PDF를 XLSX로 변환, PDF를 CSV로 변환.
description: Aspose.PDF for JavaScript를 사용하면 PDF를 XLSX 및 CSV 형식으로 변환할 수 있습니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## JavaScript를 사용하여 PDF에서 스프레드시트 생성

**Aspose.PDF for JavaScript**는 PDF 파일을 Excel 및 CSV 형식으로 변환하는 기능을 지원합니다.

{{% alert color="success" %}}
**온라인에서 PDF를 Excel로 변환 시도하기**

Aspose.PDF for JavaScript는 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)라는 무료 온라인 애플리케이션을 제공합니다. 여기에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 무료 앱으로 PDF를 Excel로 변환](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

변환 작업은 문서의 페이지 수에 따라 달라지며 시간이 많이 소요될 수 있습니다.
 따라서, 우리는 웹 워커를 사용하는 것을 강력히 추천합니다.

이 코드는 리소스를 많이 소모하는 PDF 파일 변환 작업을 웹 워커로 오프로드하여 메인 UI 스레드를 차단하지 않도록 하는 방법을 보여줍니다. 또한, 변환된 파일을 다운로드하는 사용자 친화적인 방법을 제공합니다.

## PDF를 XLSX로 변환

```js

  /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커에서 오류 발생: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로딩됨!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileToXlsX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일을 XlsX로 변환하고 "ResultPDFtoXlsX.xlsx"로 저장 - 웹 워커에 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXlsX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx"] }, [event.target.result]);
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
        link.innerHTML = "파일 " + filename + "을(를) 다운로드하려면 여기를 클릭하세요";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```

다음의 JavaScript 코드 스니펫은 PDF 페이지를 XlsX 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfToXlsX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftoxlsx/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예제에서는 "ResultPDFtoXlsX.xlsx"입니다.
1. 다음으로, 'json.errorCode'가 0이면 결과 파일은 앞서 지정한 이름을 갖게 됩니다. 'json.errorCode' 매개변수가 0이 아닌 경우에는 파일에 오류가 발생하며, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수가 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있도록 합니다.

```js

  var ffileToXlsX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일을 XlsX로 변환하고 "ResultPDFtoXlsX.xlsx"로 저장*/
      const json = AsposePdfToXlsX(event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*결과 파일을 다운로드할 링크 생성*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


## PDF를 CSV로 변환

```js

    /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커의 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드됨!' :
        (evt.data.json.errorCode == 0) ? 
          `파일(테이블) 수: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "text/csv", element) ) ?? ""}` : 
          `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileToCSV = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일을 CSV로 변환하고(테이블 추출) 템플릿 "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... 형식 페이지 번호), 탭을 구분자로 사용하여 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfTablesToCSV', "params": [event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t"] }, [event.target.result]);
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


다음 JavaScript 코드 스니펫은 PDF를 CSV로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftablestocsv/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예제에서는 "ResultPdfTablesToCSV{0:D2}.csv"입니다.
1. 다음으로, 'json.errorCode'가 0이면 결과 파일에 이전에 지정한 이름이 부여됩니다. 'json.errorCode' 매개변수가 0이 아니면 파일에 오류가 발생하며, 이러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 결과 파일을 사용자의 운영 체제에 다운로드할 수 있게 합니다.

```js

  var ffileToCSV = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일을 CSV로 변환 (테이블 추출) 템플릿 "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... 형식의 페이지 번호), 탭을 구분자로 사용*/
        const json = AsposePdfTablesToCSV(event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "파일(테이블) 수: " + json.filesCount.toString();
          /*결과 파일에 대한 링크 생성*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "text/csv");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```