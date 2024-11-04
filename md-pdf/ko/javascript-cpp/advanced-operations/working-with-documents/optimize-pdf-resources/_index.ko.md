---
title: JavaScript를 통한 C++로 PDF 리소스 최적화
linktitle: PDF 리소스 최적화
type: docs
weight: 15
url: /javascript-cpp/optimize-pdf-resources/
description: JavaScript 도구를 사용하여 빠른 웹 뷰를 위해 PDF 파일의 리소스를 최적화합니다.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 리소스 최적화

문서에서 리소스를 최적화합니다:

  1. 문서 페이지에서 사용되지 않는 리소스가 제거됩니다.
  1. 동일한 리소스가 단일 객체로 결합됩니다.
  1. 사용되지 않는 객체가 삭제됩니다.
 
1. 최적화를 위해 PDF 파일을 선택합니다.
1. 'FileReader'를 만듭니다.
1. [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfoptimizeresource/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예에서는 "ResultPdfOptimizeResource.pdf"입니다.

1. 다음으로, 'json.errorCode'가 0이면 DownloadFile은 이전에 지정한 이름을 갖게 됩니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있는 경우, 이러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 해줍니다.

다음 코드 스니펫은 PDF 문서를 최적화하는 방법을 보여줍니다.

```js

    var ffilePdfOptimizeResource = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일의 리소스를 최적화하고 "ResultPdfOptimizeResource.pdf"로 저장합니다.*/
        const json = AsposePdfOptimizeResource(event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 링크 생성*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


## 웹 워커 사용하기

```js

    /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffilePdfOptimizeResource = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일의 리소스를 최적화하여 "ResultPdfOptimizeResource.pdf"로 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfOptimizeResource', "params": [event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf"] }, [event.target.result]);
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
        link.innerHTML = "파일을 다운로드하려면 여기를 클릭하세요 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```