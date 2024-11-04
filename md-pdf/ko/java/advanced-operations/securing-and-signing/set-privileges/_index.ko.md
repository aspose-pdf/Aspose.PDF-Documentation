---
title: 권한 설정, PDF 파일 암호화 및 해독
linktitle: PDF 파일 암호화 및 해독
type: docs
weight: 20
url: /java/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: pdf 암호화, pdf 암호 보호, pdf 해독, java
description: Java를 사용하여 다양한 암호화 유형 및 알고리즘으로 PDF 파일을 암호화합니다. 또한 소유자 비밀번호를 사용하여 PDF 파일을 해독합니다.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 기존 PDF 파일에 권한 설정

PDF 파일에 권한을 설정하려면 DocumentPrivilege 클래스의 객체를 생성하고 문서에 적용할 권한을 지정하십시오.
 권한이 정의되면 이 객체를 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-boolean-) 메서드에 인수로 전달하십시오. 다음 코드 스니펫은 PDF 파일의 권한을 설정하는 방법을 보여줍니다.

```java
  public static void SetPrivilegesOnExistingPDF()
  {
   // 소스 PDF 파일 로드
   Document document = new Document(_dataDir + "input.pdf");

   // Document Privileges 객체 인스턴스화
   // 모든 권한에 제한 적용
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // 화면 읽기만 허용
   documentPrivilege.setAllowScreenReaders(true);
   // 사용자와 소유자 비밀번호로 파일 암호화
   // 사용자가 사용자 비밀번호로 파일을 볼 때
   // 화면 읽기 옵션만 활성화되도록 비밀번호를 설정해야 합니다.
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // 업데이트된 문서 저장
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## 다양한 암호화 유형 및 알고리즘을 사용하여 PDF 파일 암호화

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) 메서드를 사용하여 PDF 파일을 암호화할 수 있습니다. [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) 메서드에 사용자 비밀번호, 소유자 비밀번호 및 권한을 전달할 수 있습니다. 또한, [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/CryptoAlgorithm) 열거형의 값을 전달할 수 있습니다. 이 열거형은 암호화 알고리즘과 키 크기의 다양한 조합을 제공합니다. 원하는 값을 전달할 수 있습니다. 마지막으로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) 메서드를 사용하여 암호화된 PDF 파일을 저장합니다.

>PDF 파일을 암호화할 때 서로 다른 사용자 비밀번호와 소유자 비밀번호를 지정하십시오.

다음 코드 스니펫은 PDF 파일을 암호화하는 방법을 보여줍니다.

```java
public static void EncryptPDFFile() {
   // 소스 PDF 파일을 로드
   Document document = new Document(_dataDir + "input.pdf");

   // Document Privileges 객체를 인스턴스화
   // 모든 권한에 제한 적용
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // 화면 읽기만 허용
   documentPrivilege.setAllowScreenReaders(true);
   // 사용자 및 소유자 비밀번호로 파일 암호화
   // 사용자가 사용자 비밀번호로 파일을 볼 때
   // 화면 읽기 옵션만 활성화되도록 비밀번호 설정 필요
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // 업데이트된 문서 저장
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## 소유자 비밀번호를 사용하여 PDF 파일 복호화

PDF 파일을 복호화하기 위해서는 먼저 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 생성하고 소유자 비밀번호를 사용하여 PDF를 열어야 합니다.
 그런 다음 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [Decrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#decrypt--) 메서드를 호출해야 합니다. 마지막으로, [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Save 메서드를 사용하여 업데이트된 PDF 파일을 저장하십시오. 다음 코드 스니펫은 PDF 파일을 해독하는 방법을 보여줍니다.

```java
public static void DecryptPDFFile() {
   // 문서 열기
   Document document = new Document(_dataDir + "Decrypt.pdf", "password");
   // PDF 해독
   document.decrypt();

   // 업데이트된 PDF 저장
   document.save(_dataDir + "Decrypt_out.pdf");
  }
```

## PDF 파일의 비밀번호 변경

PDF 파일의 비밀번호를 변경하려면 먼저 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 사용하여 소유자 비밀번호로 PDF 파일을 열어야 합니다. 그 후, [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [ChangePasswords](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#changePasswords-java.lang.String-java.lang.String-java.lang.String-) 메서드를 호출해야 합니다. 이 메서드에 현재 소유자 비밀번호와 새 사용자 비밀번호 및 새 소유자 비밀번호를 전달해야 합니다. 마지막으로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Save 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일의 비밀번호를 변경하는 방법을 보여줍니다.

```java
public static void ChangePassword_PDF_File() {
   // 문서 열기
   Document document = new Document(_dataDir+ "ChangePassword.pdf", "owner");
   // 비밀번호 변경
   document.changePasswords("owner", "newuser", "newowner");
   // 업데이트된 PDF 저장
   document.save(_dataDir + "ChangePassword_out.pdf");
  }
```

## 방법 - 원본 PDF가 비밀번호로 보호되어 있는지 확인하기

Aspose.PDF for Java는 PDF 문서를 처리하는 뛰어난 기능을 제공합니다. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 com.aspose.pdf 패키지를 사용하여 암호로 보호된 PDF 문서를 열 때, Document 생성자에 암호 정보를 인수로 제공해야 하며, 이 정보가 제공되지 않으면 오류 메시지가 생성됩니다. 사실 Document 객체로 PDF 파일을 열려고 할 때, 생성자는 PDF 파일의 내용을 읽으려고 하며, 올바른 암호가 제공되지 않으면 오류 메시지가 생성됩니다 (이는 문서의 무단 액세스를 방지하기 위해 발생합니다).

암호화된 PDF 파일을 다룰 때, PDF에 열기 암호와/또는 편집 암호가 있는지 감지하는 데 관심이 있을 수 있습니다. 때때로 문서를 열 때 비밀번호 정보가 필요하지 않지만, 파일의 내용을 편집하기 위해 정보가 필요한 문서가 있습니다. 이러한 요구 사항을 충족하기 위해 com.aspose.pdf.facades 패키지에 있는 PdfFileInfo 클래스는 필요한 정보를 결정하는 데 도움이 되는 메서드를 제공합니다.

### PDF 문서 보안에 대한 정보 얻기

PdfFileInfo는 PDF 문서 보안에 대한 정보를 얻기 위한 세 가지 메서드를 포함하고 있습니다.

1. getPasswordType() 메서드는 PasswordType 열거형 값을 반환합니다:
    1. PasswordType.None - 문서는 비밀번호로 보호되지 않음
    1. PasswordType.User - 사용자(또는 문서 열기) 비밀번호로 문서가 열림
    1. PasswordType.Owner - 소유자(또는 권한, 편집) 비밀번호로 문서가 열림
    1. PasswordType.Inaccessible - 문서는 비밀번호로 보호되었지만 비밀번호가 필요하며 잘못된 비밀번호(또는 비밀번호 없음)가 제공됨.
1. `hasOpenPassword()` 메서드는 입력 파일을 열 때 비밀번호가 필요한지를 결정하는 데 사용됩니다.
1. `hasEditPassword()` 메서드는 입력 파일의 내용을 편집하기 위해 비밀번호가 필요한지를 결정하는 데 사용됩니다.

### 배열에서 올바른 비밀번호 결정하기

때때로 배열에서 올바른 비밀번호를 찾아서 문서를 올바른 비밀번호로 여는 것이 필요할 수 있습니다. 다음 코드 스니펫은 비밀번호 배열을 반복하면서 올바른 비밀번호로 문서를 여는 단계를 보여줍니다.

```java
public static void DetermineCorrectPasswordFromArray() {
     // 소스 PDF 파일 로드
   PdfFileInfo info = new PdfFileInfo();
   info.bindPdf(_dataDir + "IsPasswordProtected.pdf");
   // 소스 PDF가 암호화되어 있는지 확인
   System.out.println("파일이 비밀번호로 보호되어 있습니다: " + info.isEncrypted());
   String[] passwords = { "test", "test1", "test2", "test3", "sample" };
   for (int passwordcount = 0; passwordcount < passwords.length; passwordcount++)
   {
    try
    {
     Document doc = new Document(_dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
     if (doc.getPages().size() > 0)
      System.out.println("문서의 페이지 수 = " + doc.getPages().size());
    }
    catch (InvalidPasswordException ex)
    {
     System.out.println("비밀번호 = " + passwords[passwordcount] + "  은(는) 올바르지 않습니다");
    }
   }
```