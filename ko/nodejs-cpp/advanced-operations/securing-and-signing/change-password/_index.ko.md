---
title: PDF 파일의 비밀번호 변경 in Node.js
linktitle: 비밀번호 변경
type: docs
weight: 50
url: /nodejs-cpp/change-password-pdf/
description: Aspose.PDF for Node.js via C++로 PDF 파일의 비밀번호를 변경합니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 파일의 비밀번호 변경

PDF의 비밀번호를 변경하려면 [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/) 함수를 사용할 수 있습니다. 이 함수는 사용자 비밀번호와 소유자 비밀번호를 소유자 비밀번호로 변경하며, 원래의 보안 설정을 유지합니다. PDF 파일의 비밀번호를 "owner"에서 "newowner" 또는 "newuser"로 변경하려면 다음 코드 스니펫을 시도해보세요:

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 비밀번호를 변경할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 비밀번호 변경 작업을 수행합니다. 성공 시 객체를 받습니다.

1. 함수 [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/)를 호출합니다.
1. 비밀번호 변경. 기존 소유자 비밀번호는 "owner"로 설정되어 있으며, 새 사용자 비밀번호 "newuser"와 함께 "newowner"로 변경됩니다.
1. 따라서 'json.errorCode'가 0이면, 작업의 결과는 "ResultPdfChangePassword.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 이에 따라 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일의 비밀번호를 "owner"에서 "newowner"로 변경하고 "ResultPdfChangePassword.pdf"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


비밀번호가 빈 문자열인 경우 주의하세요:

1. 사용자 비밀번호가 비어 있으면 - PDF는 비밀번호를 묻지 않고 열립니다 (하지만 여전히 암호화되어 있습니다).
1. 소유자 비밀번호가 비어 있으면, PDF는 사용자 비밀번호 요청과 함께 열립니다.
1. 두 비밀번호가 모두 비어 있으면 - PDF는 비밀번호를 묻지 않고 열립니다 (하지만 여전히 암호화되어 있습니다).

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 비밀번호가 변경될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/)를 호출합니다.
1. 비밀번호를 변경합니다. 기존 소유자 비밀번호는 "owner"로 설정되어 있으며, 새 소유자 비밀번호 "newowner"와 새 사용자 비밀번호 "newuser"로 변경됩니다.

1. 따라서 'json.errorCode'가 0이면, 작업의 결과는 "ResultPdfChangePassword.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 나타나는 경우 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*PDF 파일의 비밀번호를 "owner"에서 "newowner"로 변경하고 "ResultPdfChangePassword.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```