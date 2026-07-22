---
title: Node.js에서 PDF에 디지털 서명 추가
linktitle: PDF에 디지털 서명하기
type: docs
weight: 70
url: /ko/nodejs-cpp/sign-pdf/
description: Node.js 환경에서 PDF 문서에 디지털 서명합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


PDF 문서의 디지털 서명은 문서의 진위와 무결성을 확인하는 방법입니다. 이는 개인 키와 디지털 인증서를 사용하여 PDF 문서에 전자 서명을 하는 프로세스입니다. 이 서명은 서명 이후 문서가 변경되지 않았으며 서명자가 해당 문서를 승인한 사람임을 보증합니다. Node.js로 PDF에 서명하려면 Aspose.PDF 도구를 사용하십시오.

PDF 파일에 서명하려는 경우, 다음을 사용할 수 있습니다 [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) 함수.

서명과 관련된 **parameters**를 사용할 수 있습니다:

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- setYIndent
- setHeight
- setWidth
- reason
- contact
- location
- isVisible
- signatureAppearance
- fileNameResult 

이 코드 스니펫은 Node.js 환경에서 AsposePDFforNode.js 모듈을 활용하여 PKCS7 서명을 사용해 PDF 파일에 디지털 서명을 수행합니다.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 서명할 PDF 파일 이름, PKCS7 키 파일, 그리고 서명 외관 이미지 파일을 지정합니다. 인증서와 이미지는 PDF 서명을 위해 업로드하는 파일 시스템의 어느 위치에든 배치할 수 있습니다.
1. 호출 `AsposePdf` Promise로서 파일 서명 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 호출하십시오 [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) 함수. 
1. 디지털 서명을 사용하여 PDF 파일에 서명합니다. 서명과 관련된 매개변수(키 파일, 비밀번호, 좌표, 이유, 연락처, 위치 등). 
1. 따라서 \u0027json.errorCode\u0027가 0이면 작업 결과가 \u0022ResultSignPKCS7.pdf\u0022에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면 오류 정보는 \u0027json.errorText\u0027에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Key PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Signature appearance*/
      const sign_img_file = 'Aspose.jpg';
      /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 서명할 PDF 파일의 이름, PKCS7 키 파일 및 서명 모양 이미지 파일을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 호출하십시오 [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) 함수. 
1. 디지털 서명을 사용하여 PDF 파일에 서명합니다. 서명과 관련된 매개변수(키 파일, 비밀번호, 좌표, 이유, 연락처, 위치 등). 
1. 따라서 \u0027json.errorCode\u0027가 0이면 작업 결과가 \u0022ResultSignPKCS7.pdf\u0022에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면 오류 정보는 \u0027json.errorText\u0027에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Key PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Signature appearance*/
  const sign_img_file = 'Aspose.jpg';
  /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```