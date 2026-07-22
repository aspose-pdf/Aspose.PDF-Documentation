---
title: Node.js에서 PDF 파일의 비밀번호 변경
linktitle: 비밀번호 변경
type: docs
weight: 50
url: /ko/nodejs-cpp/change-password-pdf/
description: Aspose.PDF for Node.js via C++를 사용하여 PDF 파일의 비밀번호를 변경합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 파일의 비밀번호 변경

PDF 비밀번호를 변경하려는 경우, 사용할 수 있습니다 [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/) 함수. 원본 보안 설정을 유지하면서 소유자 비밀번호를 사용하여 사용자 비밀번호와 소유자 비밀번호를 변경합니다.
PDF 파일의 비밀번호를 "owner"에서 "newowner" 또는 "newuser"로 변경하려면 다음 코드 스니펫을 사용해 보세요:

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 비밀번호를 변경할 PDF 파일의 이름을 지정합니다.
1. 호출 `AsposePdf` Promise 형태로 비밀번호 변경 작업을 수행합니다. 성공하면 객체를 반환받습니다.
1. 함수를 호출합니다. [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. 비밀번호를 변경합니다. 기존 소유자 비밀번호가 "owner"로 설정되어 있으며, 이를 새 사용자 비밀번호 "newuser"와 함께 새 소유자 비밀번호 "newowner"로 변경합니다.
1. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPdfChangePassword.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

비밀번호가 빈 문자열인 경우에 유의하십시오:

1. 사용자 비밀번호가 비어 있는 경우 - PDF가 비밀번호를 요구하지 않고 열리지만 (여전히 암호화되어 있습니다).
1. 소유자 비밀번호가 비어 있으면, PDF가 사용자 비밀번호 요청과 함께 열립니다.
1. 두 비밀번호가 모두 비어 있으면  - PDF가 비밀번호를 묻지 않고 열립니다(하지만 여전히 암호화되어 있습니다).


**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 비밀번호를 변경할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. 비밀번호를 변경합니다. 기존 소유자 비밀번호가 "owner"로 설정되어 있으며, 이를 새 사용자 비밀번호 "newuser"와 함께 새 소유자 비밀번호 "newowner"로 변경합니다.
1. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPdfChangePassword.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```