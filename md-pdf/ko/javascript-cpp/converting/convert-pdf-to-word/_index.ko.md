---
title: JavaScript로 PDF를 Word 문서로 변환하기
linktitle: PDF를 Word로 변환
type: docs
weight: 10
url: /javascript-cpp/convert-pdf-to-doc/
lastmod: "2023-08-04"
description: 웹에서 PDF를 DOC(DOCX)로 변환하기 위한 JavaScript 코드를 작성하는 방법을 배우세요.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

변환 작업은 문서의 페이지 수에 따라 달라지며 매우 시간이 많이 걸릴 수 있습니다. 따라서 Web Workers를 사용하는 것을 강력히 추천합니다.

이 코드는 리소스를 많이 소모하는 PDF 파일 변환 작업을 웹 워커로 오프로드하여 메인 UI 스레드의 차단을 방지하는 방법을 보여줍니다. 또한 변환된 파일을 다운로드하는 사용자 친화적인 방법을 제공합니다.

Microsoft Word 또는 DOC와 DOCX 형식을 지원하는 기타 워드 프로세서에서 PDF 파일의 내용을 편집하려면 PDF 파일은 편집 가능하지만 DOC 및 DOCX 파일은 더 유연하고 사용자 정의가 가능합니다.

{{% alert color="success" %}}
**PDF를 DOC로 온라인 변환 시도하기**

Aspose.PDF for JavaScript는 여러분에게 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)라는 온라인 무료 애플리케이션을 제공합니다. 여기에서 기능과 품질을 조사해 볼 수 있습니다.

[![PDF를 DOC로 변환](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF를 DOC로 변환

```js

  /*웹 워커 생성*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`웹 워커에서 오류 발생: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? '로드 완료!' :
      (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/msword", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

  /*이벤트 핸들러*/
  const ffileToDoc = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*PDF 파일을 Doc으로 변환하고 "ResultPDFtoDoc.doc"로 저장 - 웹 워커 요청*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDoc', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc"] }, [event.target.result]);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

  /*결과 파일을 다운로드할 링크 만들기*/
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


다음 JavaScript 코드 스니펫은 PDF 페이지를 DOC 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfToDoc](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftodoc/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예제에서는 "ResultPDFtoDoc.doc"입니다.
1. 다음으로, 'json.errorCode'가 0이면 결과 파일은 이전에 지정한 이름을 갖습니다. 'json.errorCode' 파라미터가 0이 아니고, 따라서 파일에 오류가 있는 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제로 결과 파일을 다운로드할 수 있게 합니다.

```js

  var ffileToDoc = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일을 Doc으로 변환하고 "ResultPDFtoDoc.doc"로 저장합니다.*/
      const json = AsposePdfToDoc(event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*결과 파일을 다운로드할 링크를 만듭니다.*/
      DownloadFile(json.fileNameResult, "application/msword");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


{{% alert color="warning" %}}
**PDF를 DOCX로 온라인 변환 시도**

Aspose.PDF for JavaScript는 온라인 무료 애플리케이션 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)를 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## PDF를 DOCX로 변환

Aspose.PDF for JavaScript API를 사용하면 PDF 문서를 DOCX로 읽고 변환할 수 있습니다. DOCX는 Microsoft Word 문서의 잘 알려진 형식으로, 구조가 일반 바이너리에서 XML과 바이너리 파일의 조합으로 변경되었습니다. Docx 파일은 Word 2007 및 이후 버전에서 열 수 있지만, DOC 파일 확장자를 지원하는 이전 버전의 MS Word에서는 열 수 없습니다.

```js

  /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileToDocX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일을 DocX로 변환하고 "ResultPDFtoDocX.docx"로 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDocX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx"] }, [event.target.result]);
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


다음 JavaScript 코드 스니펫은 PDF 페이지를 DOCX 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfToDocX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftodocx/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예제에서는 "ResultPDFtoDocX.docx"입니다.
1. 다음으로, 'json.errorCode'가 0이면, 결과 파일은 이전에 지정한 이름을 갖습니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있는 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결국, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수가 링크를 생성하고 사용자의 운영 체제로 결과 파일을 다운로드할 수 있게 합니다.

```js

  var ffileToDocX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일을 DocX로 변환하고 "ResultPDFtoDocX.docx"로 저장합니다.*/
      const json = AsposePdfToDocX(event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*결과 파일을 다운로드할 링크를 만듭니다.*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```