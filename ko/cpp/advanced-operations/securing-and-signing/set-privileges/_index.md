---
title: 권한 설정, PDF 파일 암호화 및 해독 C++ 사용
linktitle: PDF 파일 암호화 및 해독
type: docs
weight: 20
url: ko/cpp/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: pdf 암호화,pdf 비밀번호 보호,pdf 해독,c++
description: 다양한 암호화 유형 및 알고리즘을 사용하여 C++로 PDF 파일을 암호화합니다. 또한 소유자 비밀번호를 사용하여 PDF 파일을 해독합니다.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 기존 PDF 파일에 권한 설정

기존 PDF 파일에 권한을 설정하기 위해 Aspose.PDF for C++는 [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.document_privilege/) 클래스를 사용하여 문서에 적용할 권한을 지정합니다. 권한이 정의되면 이 객체를 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) 메서드의 인수로 전달합니다.

다음 코드 스니펫은 PDF 파일의 권한을 설정하는 방법을 보여줍니다.

```cpp
void SecuringAndSigning::SetPrivilegesOnExistingPDF() {
    // 경로 이름을 위한 문자열입니다.
    String _dataDir("C:\\Samples\\");

    // 소스 PDF 파일을 로드합니다.
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Document Privileges 객체를 인스턴스화합니다.

    // 모든 권한에 대한 제한을 적용합니다.
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // 화면 읽기만 허용합니다.
    documentPrivilege->set_AllowScreenReaders(true);

    // 사용자 및 소유자 비밀번호로 파일을 암호화합니다.
    // 사용자가 사용자 비밀번호로 파일을 볼 수 있도록 비밀번호를 설정해야 합니다.

    // 화면 읽기 옵션만 활성화됩니다.
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);

    // 업데이트된 문서를 저장합니다.
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## 다양한 암호화 유형 및 알고리즘을 사용하여 PDF 파일 암호화

PDF 파일을 암호화하려면 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) 메서드를 사용하여 PDF 파일을 암호화하십시오.


다음 코드 스니펫은 PDF 파일을 암호화하는 방법을 보여줍니다.

```cpp
void SecuringAndSigning::EncryptPDFFile() {
    // 경로명을 위한 문자열.
    String _dataDir("C:\\Samples\\");

    // 소스 PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Document Privileges 객체 인스턴스화
    // 모든 권한에 제한 적용
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // 화면 읽기만 허용
    documentPrivilege->set_AllowScreenReaders(true);
    // 사용자 및 소유자 비밀번호로 파일 암호화.
    // 사용자가 사용자 비밀번호로 파일을 볼 때
    // 화면 읽기 옵션만 활성화되도록 비밀번호 설정 필요
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);
    // 업데이트된 문서 저장
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## 소유자 비밀번호를 사용하여 PDF 파일 해독

PDF 파일을 해독하려면 먼저 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 생성하고 소유자 비밀번호를 사용하여 PDF를 열어야 합니다. 그런 다음 [Decrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9c26014465f4368edc6fc62b7ef3d76a) 메서드를 호출해야 합니다.

```cpp
void SecuringAndSigning::DecryptPDFFile() {


// 경로 이름을 위한 문자열.

String _dataDir("C:\\Samples\\");


// 문서 열기

auto document = MakeObject<Document>(_dataDir + u"Decrypt.pdf", u"password");

// PDF 복호화

document->Decrypt();


// 업데이트된 PDF 저장

document->Save(_dataDir + u"Decrypt_out.pdf");
}
```

## PDF 파일의 비밀번호 변경

PDF에는 중요한 기밀 정보가 포함될 수 있으므로 안전하게 유지되어야 합니다. 따라서 PDF 문서의 비밀번호를 변경해야 할 수 있습니다.

PDF 파일의 비밀번호를 변경하려면 먼저 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 사용하여 소유자 비밀번호로 PDF 파일을 열어야 합니다. 그런 다음 [ChangePasswords](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9952055c2ac0afea827ce400b5ec951d) 메서드를 호출해야 합니다.

다음 코드 스니펫은 PDF 파일의 비밀번호를 변경하는 방법을 보여줍니다.
```cpp
void SecuringAndSigning::ChangePassword_PDF_File() {

// String for path name.

String _dataDir("C:\\Samples\\");


// Open document

auto document = MakeObject<Document>(_dataDir + u"ChangePassword.pdf", u"owner");

// Change password

document->ChangePasswords(u"owner", u"newuser", u"newowner");

// Save updated PDF

document->Save(_dataDir + u"ChangePassword_out.pdf");
}
```

## 방법 - 소스 PDF가 암호로 보호되어 있는지 확인하는 방법

사용자 암호로 암호화된 PDF 문서는 암호 없이는 열 수 없습니다. 우리는 문서를 열기 전에 비밀번호로 보호되어 있는지 확인하는 것이 좋습니다. 때때로 문서를 열 때 비밀번호 정보가 필요하지 않지만 파일의 내용을 편집하기 위해 정보가 필요한 문서가 있습니다. 따라서 위의 요구 사항을 충족하기 위해 Aspose.PDF.Facades에 있는 [PdfFileInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_info/) 클래스는 필요한 정보를 확인하는 데 도움이 되는 속성을 제공합니다.

### PDF 문서 보안 정보 얻기

PdfFileInfo는 PDF 문서 보안에 대한 정보를 얻기 위한 세 가지 속성을 포함합니다.

1. 속성 PasswordType은 PasswordType 열거형 값을 반환합니다:
    - PasswordType.None - 문서는 비밀번호로 보호되어 있지 않습니다
    - PasswordType.User - 문서는 사용자(또는 문서 열기) 비밀번호로 열렸습니다
    - PasswordType.Owner - 문서는 소유자(또는 권한, 편집) 비밀번호로 열렸습니다

    - PasswordType.Inaccessible - 문서는 비밀번호로 보호되어 있지만 잘못된 비밀번호(또는 비밀번호 없음)가 제공된 경우 열기 위해 비밀번호가 필요합니다.2. boolean 속성 HasOpenPassword - 입력 파일을 열 때 암호가 필요한지를 결정하는 데 사용됩니다.  
3. boolean 속성 HasEditPassword - 입력 파일의 내용을 편집하기 위해 암호가 필요한지를 결정하는 데 사용됩니다.

### 배열에서 올바른 암호 결정

때때로 배열에서 올바른 암호를 결정하고 올바른 암호로 문서를 열어야 할 때가 있습니다. 다음 코드 스니펫은 암호 배열을 반복하고 올바른 암호로 문서를 열려고 시도하는 단계를 보여줍니다.

```cpp
void SecuringAndSigning::DetermineCorrectPasswordFromArray() {


// 경로 이름에 대한 문자열입니다.

String _dataDir("C:\\Samples\\");


// 소스 PDF 파일 로드

auto info = MakeObject<PdfFileInfo>(_dataDir + u"IsPasswordProtected.pdf");


// 소스 PDF가 암호화되어 있는지 확인

Console::WriteLine(u"파일이 암호로 보호됨 {0}", info->get_IsEncrypted());

const int count = 5;

String passwords[count] = { u"test", u"test1", u"test2", u"owner", u"sample" };


for (int passwordcount = 0; passwordcount < count; passwordcount++)

{


try


{



auto document = MakeObject<Document>(_dataDir + u"IsPasswordProtected.pdf", passwords[passwordcount]);



auto pages = document->get_Pages()->get_Count();



if (pages > 0)




Console::WriteLine(u"문서의 페이지 수 = {0}", pages);


}


catch (Aspose::Pdf::InvalidPasswordException ex)


{



Console::WriteLine(u"암호 = {0}이(가) 올바르지 않음", passwords[passwordcount]);


}

}

Console::WriteLine(u"테스트 완료");
}
```