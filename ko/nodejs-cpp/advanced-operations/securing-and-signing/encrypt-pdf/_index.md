---
title: PDF 암호화 in Node.js
linktitle: PDF 파일 암호화
type: docs
weight: 50
url: /ko/nodejs-cpp/encrypt-pdf/
description: C++를 통한 Aspose.PDF for Node.js로 PDF 파일 암호화.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 사용자 또는 소유자 암호를 사용하여 PDF 파일 암호화

기밀 정보를 포함한 PDF 첨부 파일을 이메일로 보낼 때, 이를 잘못된 손에 넘어가지 않도록 보안을 추가하고 싶을 수 있습니다. PDF 문서에 대한 무단 접근을 제한하는 가장 좋은 방법은 암호로 보호하는 것입니다. 간단하고 안전하게 문서를 암호화하려면 C++를 통한 Aspose.PDF for Node.js를 사용할 수 있습니다.

>PDF 파일을 암호화할 때 서로 다른 사용자 및 소유자 암호를 지정하십시오.

- **사용자 암호**는 설정된 경우 PDF를 열기 위해 제공해야 하는 암호입니다. Acrobat/Reader는 사용자에게 사용자 암호를 입력하라는 메시지를 표시합니다. 올바르지 않으면 문서가 열리지 않습니다.
- **소유자 암호**는 설정된 경우 인쇄, 편집, 추출, 주석 등과 같은 권한을 제어합니다.
 Acrobat/Reader는 권한 설정에 따라 이러한 작업을 허용하지 않습니다. Acrobat에서 권한을 설정/변경하려면 이 비밀번호가 필요합니다.

PDF 파일을 암호화하려면 [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) 함수를 사용할 수 있습니다. 
PDF 파일을 암호화하려면 다음 코드 스니펫을 시도하세요:

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
2. 암호화할 PDF 파일의 이름을 지정합니다.
3. Promise로 `AsposePdf`를 호출하고 파일 암호화 작업을 수행합니다. 성공하면 객체를 받습니다.
4. [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) 함수를 호출합니다.
5. PDF 파일을 "user" 및 "owner" 비밀번호로 암호화합니다.
1. 따라서 'json.errorCode'가 0이면, 작업의 결과가 "ResultEncrypt.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 "user"와 "owner" 비밀번호로 암호화하고, "ResultEncrypt.pdf"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

다양한 [암호화 권한](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c)이 있습니다:

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtractContent

- Module.Permissions.ModifyTextAnnotations
- Module.Permissions.FillForm
- Module.Permissions.ExtractContentWithDisabilities
- Module.Permissions.AssembleDocument
- Module.Permissions.PrintingQuality

다양한 [암호화 알고리즘](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66)이 있습니다:

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 암호화가 변경될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) 함수를 호출합니다.
1. "user"와 "owner"의 비밀번호로 PDF 파일의 암호를 해제합니다.

1. 따라서, 'json.errorCode'가 0이면, 작업의 결과는 "ResultEncrypt.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /* PDF 파일을 "user"와 "owner" 비밀번호로 암호화하고, "ResultEncrypt.pdf"로 저장합니다 */
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```