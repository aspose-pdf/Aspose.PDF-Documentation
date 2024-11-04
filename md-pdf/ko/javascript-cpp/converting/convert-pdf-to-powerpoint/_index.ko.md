---
title: JavaScript에서 PDF를 PPTX로 변환
linktitle: PDF를 PowerPoint로 변환
type: docs
weight: 30
url: /javascript-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-01"
description: Aspose.PDF를 사용하면 JavaScript를 통해 웹에서 PDF를 PPTX 형식으로 직접 변환할 수 있습니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

변환 작업은 문서의 페이지 수에 따라 달라지며 매우 시간이 많이 걸릴 수 있습니다. 따라서 Web Workers를 사용하는 것을 강력히 권장합니다.

이 코드는 리소스를 많이 소모하는 PDF 파일 변환 작업을 웹 워커에 오프로드하여 메인 UI 스레드의 차단을 방지하는 방법을 보여줍니다. 또한 변환된 파일을 다운로드하는 사용자 친화적인 방법을 제공합니다.

{{% alert color="success" %}}
**PDF를 PowerPoint로 온라인 변환해보세요**

Aspose.PDF for JavaScript는 온라인 무료 애플리케이션 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)를 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## PDF를 PPTX로 변환

```js

  /*웹 워커 생성*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`웹 워커에서 오류 발생: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? '로드 완료!' :
      (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

  /*이벤트 핸들러*/
  const ffileToPptX = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /* PDF 파일을 PptX로 변환하고 "ResultPDFtoPptX.pptx"로 저장 - 웹 워커에 요청 */
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToPptX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx"] }, [event.target.result]);
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


다음의 JavaScript 코드 스니펫은 PDF를 PPTX 파일로 변환하는 간단한 예제를 보여줍니다:

1. 변환할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfToPptX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftopptx/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예제에서는 "ResultPDFtoPptX.pptx"입니다.
1. 다음으로, 'json.errorCode'가 0이면, 결과 파일은 이전에 지정한 이름을 가지게 됩니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있는 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수가 링크를 생성하고 사용자 운영 체제에 결과 파일을 다운로드할 수 있게 해줍니다.

```js

  var ffileToPptX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일을 PptX로 변환하고 "ResultPDFtoPptX.pptx"로 저장합니다*/
      const json = AsposePdfToPptX(event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*결과 파일을 다운로드할 링크를 만듭니다*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```