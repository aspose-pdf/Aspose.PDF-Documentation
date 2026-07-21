---
title:  Node.js에서 PDF 암호화
linktitle: PDF 파일 암호화
type: docs
weight: 50
url: /ko/nodejs-cpp/encrypt-pdf/
description: Aspose.PDF for Node.js via C++를 사용하여 PDF 파일을 암호화합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 사용자 비밀번호 또는 소유자 비밀번호를 사용하여 PDF 파일 암호화

PDF 첨부 파일에 기밀 정보가 포함된 이메일을 누군가에게 보내는 경우, 먼저 보안을 추가하여 잘못된 손에 넘어가지 않도록 할 수 있습니다. PDF 문서에 대한 무단 접근을 제한하는 가장 좋은 방법은 비밀번호로 보호하는 것입니다. 문서를 쉽고 안전하게 암호화하려면 Aspose.PDF for Node.js via C++를 사용할 수 있습니다.

>PDF 파일을 암호화하는 동안 서로 다른 사용자 비밀번호와 소유자 비밀번호를 지정하십시오.

- **사용자 비밀번호(User password)**가 설정된 경우, PDF를 열기 위해 제공해야 하는 비밀번호입니다. Acrobat/Reader는 사용자에게 사용자 비밀번호를 입력하라는 메시지를 표시합니다. 비밀번호가 올바르지 않으면 문서가 열리지 않습니다.
- **소유자 비밀번호(Owner password)**가 설정된 경우, 인쇄, 편집, 추출, 주석 등과 같은 권한을 제어합니다. Acrobat/Reader는 권한 설정에 따라 이러한 작업을 허용하지 않습니다. 권한을 설정하거나 변경하려면 Acrobat이 이 비밀번호를 요구합니다.

PDF 파일을 암호화하려는 경우, 다음을 사용할 수 있습니다. [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) 함수. 
PDF 파일을 암호화하려면 다음 코드를 시도해 보세요:

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 암호화될 PDF 파일의 이름을 지정합니다.
1. 호출 `AsposePdf` Promise로서 파일 암호화 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 호출하십시오 [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) 함수. 
1. 비밀번호 "user"와 "owner"를 사용하여 PDF 파일을 암호화합니다.
1. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultEncrypt.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

다른 것이 있습니다 [암호화 권한](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtractContent
- Module.Permissions.ModifyTextAnnotations
- Module.Permissions.FillForm
- Module.Permissions.ExtractContentWithDisabilities
- Module.Permissions.AssembleDocument
- Module.Permissions.PrintingQuality

다양한 것이 있습니다 [암호화 알고리즘](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66):

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 암호화가 변경될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 호출하십시오 [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) 함수. 
1. PDF 파일을 "user" 및 "owner" 비밀번호로 복호화합니다.
1. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultEncrypt.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```