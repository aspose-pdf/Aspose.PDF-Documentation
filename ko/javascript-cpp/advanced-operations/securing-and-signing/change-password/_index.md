---
title: PDF 파일의 비밀번호 변경
linktitle: 비밀번호 변경
type: docs
weight: 50
url: /ko/javascript-cpp/change-password-pdf/
description: C++를 통한 JavaScript용 Aspose.PDF로 PDF 파일의 비밀번호를 변경합니다.
lastmod: "2023-09-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 파일의 비밀번호 변경

PDF 파일의 비밀번호를 "owner"에서 "newowner"로 변경하려면 다음 코드 스니펫을 시도해 보세요:

1. PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfChangePassword](https://reference.aspose.com/pdf/javascript-cpp/security/asposepdfchangepassword/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정되며, 이 예제에서는 "ResultPdfChangePassword.pdf"입니다.
1. 다음으로, 'json.errorCode'가 0이면, DownloadFile에 이전에 지정한 이름이 부여됩니다. 'json.errorCode' 매개변수가 0과 같지 않으면, 파일에 오류가 발생하며, 이러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.

1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제로 결과 파일을 다운로드할 수 있게 해줍니다.

```js

    var ffilePdfChangePassword = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일의 비밀번호를 "owner"에서 "newowner"로 변경하고 "ResultPdfChangePassword.pdf"로 저장합니다.*/
        const json = AsposePdfChangePassword(event.target.result, e.target.files[0].name, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 수 있는 링크를 만듭니다.*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## 웹 워커 사용하기

```js

  /*웹 워커 생성하기*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffilePdfChangePassword = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const ownerPassword = 'owner'; /*소유자 비밀번호*/
        const newUserPassword = "newuser"; /*새 사용자 비밀번호*/
        const newOwnerPassword = "newowner"; /*새 소유자 비밀번호*/
        /*PDF 파일의 비밀번호를 "owner"에서 "newowner"로 변경하고 "ResultPdfChangePassword.pdf"로 저장합니다 - 웹 워커에게 요청합니다.*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfChangePassword', "params": [event.target.result, e.target.files[0].name, ownerPassword, newUserPassword, newOwnerPassword, "ResultPdfChangePassword.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [코드 스니펫]

    /*결과 파일을 다운로드할 수 있는 링크를 만듭니다.*/
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