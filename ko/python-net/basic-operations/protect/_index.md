---
title: 파이썬에서 PDF 파일 보호
linktitle: PDF 파일 암호화 및 암호 해독
type: docs
weight: 70
url: /ko/python-net/protect-pdf-file/
description: Python에서 파일을 암호화하고, 보호된 PDF를 해독하고, 암호를 변경하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 권한 설정 및 암호화 관리
Abstract: >
    이 페이지에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 문서 권한을 설정하고, 암호화를 적용하고, PDF 파일을 해독하고, 암호를 변경하는 방법을 설명합니다.사용자 및 소유자 암호 구성, 액세스 제한 정의 (예: 인쇄, 복사 및 편집), Python 응용 프로그램에서의 PDF 보안 관리에 대해 설명합니다.
---

## 암호와 권한으로 PDF 암호화

.NET을 통해 Python용 Aspose.PDF 파일을 사용하여 암호 기반 암호화 및 제한된 권한으로 PDF 문서를 보호하십시오.

1. PDF 문서를 로드합니다.
1. 만들기 `DocumentPrivilege` 권한 객체.
1. 필요한 권한을 활성화합니다.
1. 사용자 및 소유자 암호를 설정합니다.
1. 암호화 알고리즘을 선택합니다.
1. 문서에 암호화를 적용합니다.
1. 암호화된 PDF를 저장합니다.

```python
import aspose.pdf as ap

def encrypt_password(infile, outfile):
    """
    Encrypt PDF with password and permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_password("sample.pdf", "sample_protected.pdf")

    Note:
        Uses AES 128-bit encryption. Allows screen readers, forbids all other operations.
        User password: "userpassword", Owner password: "ownerpassword".
    """
    document = ap.Document(infile)
    document_privilege = ap.facades.DocumentPrivilege.forbid_all
    document_privilege.allow_screen_readers = True

    document.encrypt(
        "userpassword",
        "ownerpassword",
        document_privilege,
        ap.CryptoAlgorithm.AESx128,
        False,
    )
    document.save(outfile)
```

## 전체 권한으로 PDF 암호화

.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 전체 액세스 권한을 허용하면서 PDF 문서를 암호화합니다.이 예에서는 이전 PDF 뷰어와의 호환성을 위해 RC4 128비트 암호화를 사용합니다.

1. PDF 문서를 로드합니다.
1. 사용자 및 소유자 암호를 정의합니다.
1. 전체 액세스 권한을 설정합니다.
1. 암호화 알고리즘을 선택합니다.
1. 전화 `encrypt()` 암호, 권한 및 알고리즘이 포함됩니다.
1. 암호화된 PDF를 저장합니다.

```python
import aspose.pdf as ap

def encrypt_pdf_file(infile, outfile):
    """
    Encrypt PDF with full permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_pdf_file("sample.pdf", "sample_protected.pdf")

    Note:
        Uses RC4 128-bit encryption with allow_all privileges.
    """
    document = ap.Document(infile)
    document.encrypt(
        "userpassword",
        "ownerpassword",
        ap.facades.DocumentPrivilege.allow_all,
        ap.CryptoAlgorithm.RC4x128,
        False,
    )
    document.save(outfile)
```

## 소유자 암호를 사용하여 PDF 파일 암호 해독

암호 보호를 제거하고 전체 액세스 권한을 복원하려면:

1. 올바른 암호 (사용자 또는 소유자) 를 사용하여 암호화된 PDF를 로드합니다.
1. 문서에서 모든 암호 보호 및 암호화 설정을 제거합니다.
1. 현재 보호되지 않은 PDF를 지정된 출력 파일에 저장합니다.

```python
import aspose.pdf as ap

def decrypt_pdf_file(infile, outfile):
    """
    Decrypt password-protected PDF.

    Args:
        infile (str): Input encrypted PDF filename
        outfile (str): Output decrypted PDF filename

    Returns:
        None

    Example:
        decrypt_pdf_file("sample_protected.pdf", "sample_unprotected.pdf")

    Note:
        Requires user password to open document.
    """
    document = ap.Document(infile, "userpassword")
    document.decrypt()
    document.save(outfile)
```

## PDF 파일의 암호 변경

내용과 구조를 보존하면서 PDF 문서의 보안 자격 증명 (사용자 및 소유자 암호) 을 업데이트합니다.

1. 보안 설정에 대한 전체 액세스를 제공하는 기존 소유자 암호를 사용하여 PDF를 엽니다.
1. 이전 암호를 새 사용자 암호와 새 소유자 암호로 교체합니다.
1. 업데이트된 암호 설정으로 PDF를 저장합니다.

```python
import aspose.pdf as ap

def change_password(infile, outfile):
    """
    Change user and owner passwords.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        change_password("sample_protected.pdf", "sample_changepassword.pdf")

    Note:
        Changes from ownerpassword to newuser/newowner.
    """
    document = ap.Document(infile, "ownerpassword")
    document.change_passwords("ownerpassword", "newuser", "newowner")
    document.save(outfile)

```

## 어레이에서 올바른 암호 확인

일부 시나리오에서는 보안 PDF에 액세스하기 위해 가능한 후보 목록에서 올바른 암호를 식별해야 할 수 있습니다.아래 스니펫은 PDF 파일이 암호화되어 있는지 확인한 다음 미리 정의된 암호 목록을 반복하여 열려고 시도합니다.

프로세스에는 다음이 포함됩니다.

1. 용도 `PdfFileInfo` PDF가 암호화되었는지 여부를 감지합니다.
1. 를 사용하여 각 암호로 PDF를 엽니다. `ap.Document()`.
1. 성공하면 페이지 수가 인쇄됩니다.
1. 그렇지 않으면 예외를 포착하고 실패한 암호를 보고합니다.

```python
import aspose.pdf as ap

def determine_correct_password_from_list(infile):
    """
    Test multiple passwords to find correct one.

    Args:
        infile (str): Input encrypted PDF filename

    Returns:
        None

    Example:
        determine_correct_password_from_list("sample_protected.pdf")

    Note:
        Tries passwords: test, test1, test2, test3, userpassword.
        Prints page count if password is correct.
    """
    info = ap.facades.PdfFileInfo(infile)
    print(f"File is password protected {info.is_encrypted}")

    passwords = "test", "test1", "test2", "test3", "userpassword"

    for password in passwords:
        try:
            document = ap.Document(infile, password)
            count = len(document.pages)
            if count > 0:
                print(f"Number of Page in document are = {count}")
        except RuntimeError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
```
