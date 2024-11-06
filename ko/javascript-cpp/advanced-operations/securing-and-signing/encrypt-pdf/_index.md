---
title: PDF 암호화하기 JavaScript
linktitle: PDF 파일 암호화
type: docs
weight: 50
url: ko/javascript-cpp/encrypt-pdf/
description: Aspose.PDF for JavaScript via C++를 사용하여 PDF 파일 암호화하기.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 사용자 또는 소유자 비밀번호를 사용하여 PDF 파일 암호화하기

PDF 첨부 파일에 기밀 정보를 포함하여 이메일을 보낼 때, 잘못된 사람의 손에 들어가지 않도록 보안을 추가하고자 할 수 있습니다. PDF 문서에 대한 무단 접근을 제한하는 가장 좋은 방법은 비밀번호로 보호하는 것입니다. 문서를 쉽고 안전하게 암호화하려면 Aspose.PDF for JavaScript via C++를 사용할 수 있습니다.

> PDF 파일을 암호화할 때 다른 사용자 및 소유자 비밀번호를 지정하십시오.

- **사용자 비밀번호**는 설정된 경우 PDF를 열기 위해 제공해야 하는 비밀번호입니다. Acrobat/Reader는 사용자에게 사용자 비밀번호를 입력하라고 요청합니다. 올바르지 않으면 문서가 열리지 않습니다.
- **소유자 비밀번호**는 설정된 경우 인쇄, 편집, 추출, 주석 등과 같은 권한을 제어합니다.
 Acrobat/Reader는 권한 설정에 따라 이러한 작업을 허용하지 않습니다. 권한을 설정/변경하려면 Acrobat에서 이 비밀번호가 필요합니다.

다음 코드 스니펫은 PDF 파일을 암호화하는 방법을 보여줍니다.

1. 암호화할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfEncrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfencrypt/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예에서는 "ResultEncrypt.pdf"입니다.
1. 다음으로, 'json.errorCode'가 0이면, DownloadFile에 이전에 지정한 이름이 주어집니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 해당 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 해줍니다.

```js

  var ffileEncrypt = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일을 "user"와 "owner" 비밀번호로 암호화하고, "ResultDecrypt.pdf"로 저장합니다.*/
      const json = AsposePdfEncrypt(event.target.result, e.target.files[0].name, "user", "owner", Module.Permissions.PrintDocument, Module.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*결과 파일을 다운로드할 수 있는 링크를 만듭니다.*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## 웹 워커 사용

```js

    /* 웹 워커 생성 */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커에서 오류 발생: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ?
          `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `오류: ${evt.data.json.errorText}`;

    /* 이벤트 핸들러 */
    const ffileEncrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password_user = 'user';
        const password_owner = 'owner';
        const permissions = 'Module.Permissions.PrintDocument';
        const algorithm = 'Module.CryptoAlgorithm.RC4x40';
        /* PDF 파일을 "user"와 "owner" 비밀번호로 암호화하고 "ResultEncrypt.pdf"로 저장합니다 - 웹 워커에 요청 */
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfEncrypt',
            "params": [event.target.result, e.target.files[0].name, password_user, password_owner,
                      permissions, algorithm, "ResultEncrypt.pdf"] },
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
        link.innerHTML = "파일을 다운로드하려면 여기를 클릭하세요 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```