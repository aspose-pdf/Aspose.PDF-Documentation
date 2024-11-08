---
title: Add Header and Footer to PDF via JavaScript via C++
linktitle: PDF에 헤더와 푸터 추가
type: docs
weight: 70
url: /ko/javascript-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for JavaScript via C++를 사용하여 PDF 파일에 헤더와 푸터를 추가할 수 있습니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for JavaScript via C++**를 사용하면 기존 PDF 파일에 헤더와 푸터를 추가할 수 있습니다.

1. 'FileReader'를 생성합니다.
1. [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddtextheaderfooter/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정되며, 이 예제에서는 "ResultAddHeader.pdf"입니다.

1. 다음으로, 'json.errorCode'가 0이면 DownloadFile은 이전에 지정한 이름이 부여됩니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있는 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 해줍니다.

다음 코드 스니펫은 JavaScript를 사용하여 PDF 파일의 헤더에 텍스트를 추가하는 방법을 보여줍니다.

```js

  var ffileAddTextHeaderFooter = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일에 페이지 헤더 추가 및 "ResultAddHeader.pdf"로 저장*/
      const json = AsposePdfAddTextHeaderFooter(event.target.result, e.target.files[0].name, "Aspose.PDF for JavaScript via C++", "", "ResultAddHeader.pdf");
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
        (evt.data.json.errorCode == 0) ?
          `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileAddTextHeaderFooter = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const header = 'Aspose.PDF for JavaScript via C++';
        const footer = 'ASPOSE';
        /*PDF 파일의 헤더/푸터에 텍스트 추가하고 "ResultAddHeaderFooter.pdf"로 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddTextHeaderFooter',
            "params": [event.target.result, e.target.files[0].name, header, footer, "ResultAddHeaderFooter.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

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