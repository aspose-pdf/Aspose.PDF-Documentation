---
title: JavaScript를 통해 C++에서 디지털 서명 또는 PDF에 디지털 서명 추가
linktitle: PDF에 디지털 서명
type: docs
weight: 70
url: /ko/javascript-cpp/sign-pdf/
description: JavaScript를 통해 C++로 PDF 문서에 디지털 서명합니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서의 디지털 서명은 문서의 진위성과 무결성을 확인하는 방법입니다. 이는 PDF 문서에 개인 키와 디지털 인증서를 사용하여 전자 서명을 하는 과정입니다. 이 서명은 서명 이후 문서가 변경되지 않았으며 서명자가 승인한 사람임을 보장합니다. JavaScript로 PDF에 서명하려면 Aspose.PDF 도구를 사용하세요.

C++를 통한 JavaScript용 Aspose.PDF는 [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsignpkcs7/)을 사용하여 PDF 파일에 디지털 서명하는 기능을 지원합니다.

## 디지털 서명을 사용하여 PDF 서명

```js

    /*기본 PKCS7 키 파일 이름 설정*/
    var fileSign = "/test.pfx";

    var ffileSign = function (e) {
      const file_reader = new FileReader();
      /*PKCS7 키 파일 이름 설정*/
      fileImage = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*처리를 위해 메모리 FS에 BLOB 저장*/
        AsposePdfPrepare(event.target.result, fileSign);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*기본 이미지 (서명 외관) 파일 이름 설정*/
    var signatureAppearance = "/Aspose.jpg";

    var ffileImage = function (e) {
      const file_reader = new FileReader();
      /*이미지 파일 이름 설정*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*처리를 위해 메모리 FS에 BLOB 저장*/
        AsposePdfPrepare(event.target.result, signatureAppearance);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    var ffileSignPKCS7 = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        let pswSign = document.getElementById("passwordSign").value;
        /*디지털 서명을 사용하여 PDF 파일 서명 및 "ResultSignPKCS7.pdf"로 저장*/
        const json = AsposePdfSignPKCS7(event.target.result, e.target.files[0].name, 1, fileSign, pswSign, 200, 200, 200, 100, "TEST", "test@test.com", "EU", 1, signatureAppearance,"ResultSignPKCS7.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 링크 생성*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### 웹 워커 사용하기

```js

    /* 웹 워커 생성하기 */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ?
          `결과:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '파일 준비 완료!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `오류: ${evt.data.json.errorText}`;

    /* 기본 PKCS7 키 파일 이름 설정 */
    var fileSign = "test.pfx";
    /* 기본 이미지 (서명 모양) 파일 이름 설정: 'Aspose.jpg'는 이미 로드되어 있습니다. 'settings.json'의 설정을 참조하세요 */
    var signatureAppearance = "Aspose.jpg";

    /* 이벤트 핸들러 */
    const ffileSignPKCS7 = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pageNum = 1;
        const pswSign = document.getElementById("passwordSign").value;
        const setXIndent = 100;
        const setYIndent = 100;
        const setHeight = 200;
        const setWidth = 100;
        const reason = '이유';
        const contact = 'contact@test.com';
        const location = '위치';
        const isVisible = 1;
        /* 디지털 서명으로 PDF 파일에 서명하고 "ResultSignPKCS7.pdf"로 저장 - 웹 워커 요청 */
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSignPKCS7',
            "params": [event.target.result, e.target.files[0].name, pageNum, fileSign, pswSign, setXIndent, setYIndent,
                      setHeight, setWidth, reason, contact, location, isVisible, signatureAppearance, "ResultSignPKCS7.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileSign = e => {
      const file_reader = new FileReader();
      /* PKCS7 키 파일 이름 설정 */
      fileSign = e.target.files[0].name;
      file_reader.onload = event => {
        /* 처리를 위해 메모리 FS에 BLOB 저장 */
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, fileSign] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /* 이미지 파일 이름 설정 */
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = event => {
        /* 처리를 위해 메모리 FS에 BLOB 저장 */
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, signatureAppearance] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /* 결과 파일을 다운로드할 링크 만들기 */
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