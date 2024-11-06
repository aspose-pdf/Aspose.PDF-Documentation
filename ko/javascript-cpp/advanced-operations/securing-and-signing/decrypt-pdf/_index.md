---
title: JavaScript를 사용하여 PDF 복호화
linktitle: PDF 파일 복호화
type: docs
weight: 40
url: ko/javascript-cpp/decrypt-pdf/
description: C++를 통해 JavaScript용 Aspose.PDF로 PDF 파일 복호화.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 소유자 암호를 사용하여 PDF 파일 복호화

최근에는 인터넷 사기의 피해자가 되지 않고 문서를 보호하기 위해 암호화된 문서를 주고받는 사용자가 점점 많아지고 있습니다. 이러한 이유로, 인가된 사용자만이 접근할 수 있는 암호화된 PDF 파일에 접근해야 할 필요성이 생깁니다. 또한, 사람들은 PDF 파일을 복호화하기 위한 다양한 솔루션을 찾고 있습니다.

이 문제는 C++를 통해 JavaScript용 Aspose.PDF를 웹 브라우저에서 직접 사용하여 한 번에 해결하는 것이 좋습니다. 다음 코드 스니펫은 PDF 파일을 복호화하는 방법을 보여줍니다.

1. 복호화할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfDecrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdecrypt/) 함수가 실행됩니다.

1. 결과 파일의 이름이 설정되며, 이 예에서는 "ResultDecrypt.pdf"입니다.
1. 다음으로, 'json.errorCode'가 0이면 DownloadFile이 이전에 지정한 이름으로 제공됩니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있을 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있도록 합니다.

```js

    var ffileDecrypt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*암호가 "owner"인 PDF 파일을 해독하고 "ResultDecrypt.pdf"로 저장합니다.*/
        const json = AsposePdfDecrypt(event.target.result, e.target.files[0].name, "owner", "ResultDecrypt.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 링크를 만듭니다.*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


## 웹 워커 사용하기

```js

    /* 웹 워커 생성 */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로딩 완료!' :
        (evt.data.json.errorCode == 0) ?
          `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `오류: ${evt.data.json.errorText}`;

    /* 이벤트 핸들러 */
    const ffileDecrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /* 비밀번호가 "owner"인 PDF 파일을 해독하고 "ResultDecrypt.pdf"로 저장 - 웹 워커 요청 */
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDecrypt',
            "params": [event.target.result, e.target.files[0].name, password, "ResultDecrypt.pdf"] }, 
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /* 결과 파일을 다운로드할 링크 생성 */
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