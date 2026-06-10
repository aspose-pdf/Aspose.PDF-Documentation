---
title: 파이썬에서 PDF 파일 암호화 및 암호 해독
linktitle: PDF 파일 암호화 및 암호 해독
type: docs
weight: 70
url: /ko/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Python에서 PDF 권한을 설정하고, 파일을 암호화하고, 보호된 PDF의 암호를 해독하고, 암호를 변경하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 권한 설정 및 암호화 관리
Abstract: >
    이 설명서 페이지에서는 Python용 Aspose.PDF 를 사용하여 문서 권한을 설정하고, 암호화를 적용하고, PDF 파일을 해독하는 방법을 설명합니다.개발자는 사용자 및 소유자 암호를 구성하고 액세스 제한 (예: 인쇄, 복사 또는 편집) 을 정의하는 과정을 안내합니다.코드 예제는 Python 응용 프로그램 내에서 민감한 콘텐츠를 보호하고 PDF 보안을 효과적으로 관리하여 액세스 제어와 데이터 기밀성을 보장하는 방법을 보여줍니다.
---

민감하거나 비즈니스에 중요한 콘텐츠를 다룰 때는 문서 보안 관리가 필수적입니다..NET을 통한 Python용 Aspose.PDF 프로그램은 프로그래밍 방식으로 암호화를 적용하고, 권한을 통해 액세스를 제어하고, 보호된 PDF 파일을 해독하기 위한 강력한 API를 제공합니다.

이 글은 Python 개발자들에게 권한 설정, 암호화 적용 및 제거, 암호 변경, 보호 상태 탐지에 대한 실제 예제를 모두 PDF 워크플로우에서 안내합니다.

.NET을 통한 파이썬용 Aspose.PDF 기능을 통해 개발자는 PDF 보안을 완벽하게 제어할 수 있습니다.

**권한 설정** - 권한을 사용한 세분화된 액세스 제어.
**파일 암호화** - 사용자 지정 암호로 AES 또는 RC4 암호화를 적용합니다.
**파일 암호 해독** - 소유자 암호를 사용하여 보안을 제거합니다.
**암호 변경** - 콘텐츠를 변경하지 않고 자격 증명을 교체하거나 업데이트합니다.
**보안 검사** - 암호화 상태 또는 필수 암호 유형을 감지합니다.

PDF 문서를 암호로 보호하거나, 인쇄 또는 복사를 제한하거나, 자격 증명을 교체하거나, 문서가 암호화되었는지 여부를 검사해야 할 때 이 페이지를 사용하십시오.

## 기존 PDF 파일에 권한 설정

액세스 권한과 함께 사용자 및 소유자 암호를 할당하여 특정 작업 (예: 인쇄, 복사, 양식 작성) 을 제한하거나 허용할 수 있습니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def set_privileges_on_existing_pdf_file(infile: str, outfile: str) -> None:
    """Set restricted privileges on an existing PDF document."""
    with ap.Document(infile) as document:
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        document_privilege.allow_screen_readers = True
        document.encrypt(
            "user",
            "owner",
            document_privilege,
            ap.CryptoAlgorithm.AESx128,
            False,
        )
        document.save(outfile)
```

## 다양한 암호화 유형 및 알고리즘을 사용하여 PDF 파일 암호화

PDF를 암호화하면 유효한 자격 증명을 가진 사용자만 파일을 열거나 수정할 수 있습니다.

>주요 용어:

- 사용자 암호.문서를 여는 데 필요합니다.

- 소유자 암호.권한을 변경하거나 암호화를 제거하는 데 필요합니다.

- 키 크기.최신 워크플로우에서 보안을 극대화하려면 AE_SX128을 사용하십시오.

다음 코드 스니펫은 PDF 파일을 암호화하는 방법을 보여줍니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def encrypt_pdf_file(infile: str, outfile: str) -> None:
    """Encrypt a PDF document with user and owner passwords."""
    with ap.Document(infile) as document:
        document.encrypt(
            "user",
            "owner",
            ap.Permissions.EXTRACT_CONTENT,
            ap.CryptoAlgorithm.AESx128,
        )
        document.save(outfile)
```

## 소유자 암호를 사용하여 PDF 파일 암호 해독

암호 보호를 제거하고 전체 액세스 권한을 복원하려면:

1. 올바른 암호 ('암호'는 사용자 또는 소유자 암호) 를 사용하여 암호화된 PDF를 로드합니다.
1. 문서에서 모든 암호 보호 및 암호화 설정을 제거합니다.
1. 현재 보호되지 않은 PDF를 지정된 출력 파일에 저장합니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def decrypt_pdf_file(infile: str, outfile: str) -> None:
    """Decrypt a password-protected PDF document."""
    with ap.Document(infile, "password") as document:
        document.decrypt()
        document.save(outfile)
```

## 공개 키 인증서로 PDF 암호화 및 암호 해독

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def pub_sec_encryption(
    crypto_algorithm,
    pub_cert: str,
    in_pfx: str,
    outfile: str,
) -> None:
    """Demonstrate public-key encryption and decryption."""
    pfx_password = "12345"

    with ap.Document() as document:
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("Hello World!"))

        with open(pub_cert, "rb") as file_stream:
            byte_content = file_stream.read()

        document.encrypt(
            ap.Permissions.PRINT_DOCUMENT,
            crypto_algorithm,
            [byte_content],
        )
        document.save(outfile)

    with ap.Document(
        outfile,
        ap.security.CertificateEncryptionOptions(pub_cert, in_pfx, pfx_password),
    ) as document:
        print(document.info.title)
        print(document.info.author)

        text_absorber = ap.text.TextAbsorber()
        document.pages[1].accept(text_absorber)
        print(text_absorber.text)

        document.decrypt()
        document.save(path.join(path.dirname(outfile), "pubsec_decrypted_out.pdf"))
```

## PDF 파일의 암호 변경

내용과 구조를 보존하면서 PDF 문서의 보안 자격 증명 (사용자 및 소유자 암호) 을 업데이트합니다.

1. 기존 소유자 암호 ('소유자') 를 사용하여 PDF를 엽니다. 이 암호는 보안 설정 변경 권한을 비롯한 모든 권한을 부여합니다.
1. 이전 암호를 새 사용자 암호 ('newuser') 와 새 소유자 암호 ('newowner') 로 바꿉니다.
1. 업데이트된 암호 설정과 함께 PDF를 저장합니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def change_password(infile: str, outfile: str) -> None:
    """Change the passwords of a password-protected PDF document."""
    with ap.Document(infile, "owner") as document:
        document.change_passwords("owner", "newuser", "newowner")
        document.save(outfile)
```

## 방법 - 원본 PDF가 암호로 보호되어 있는지 확인

### 어레이에서 올바른 암호 확인

일부 시나리오에서는 보안 PDF에 액세스하기 위해 잠재적 후보 목록에서 올바른 암호를 식별해야 할 수 있습니다.아래 코드 스니펫은 PDF 파일이 암호로 보호되어 있는지 확인한 다음 Aspose.PDF for Python.NET을 사용하여 미리 정의된 암호 목록을 반복하여 잠금을 해제하는 방법을 보여줍니다.

프로세스에는 다음이 포함됩니다.

1. PDF파일정보를 사용하여 PDF가 암호화되었는지 여부를 감지합니다.
1. AP.Document () 를 사용하여 각 암호로 PDF를 열려고 시도합니다.
1. 성공하면 페이지 수가 인쇄됩니다.
1. 그렇지 않으면 예외를 포착하고 실패한 암호를 보고합니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def determine_correct_password_from_array(infile: str) -> None:
    """Try a list of passwords until the document opens successfully."""
    with ap.facades.PdfFileInfo() as pdf_file_info:
        pdf_file_info.bind_pdf(infile)
        print(f"File is password protected {pdf_file_info.is_encrypted}")

    passwords = ["test", "test1", "test2", "test3", "sample"]

    for password in passwords:
        try:
            with ap.Document(infile, password) as document:
                if len(document.pages) > 0:
                    print(f"Password = {password} is correct")
                    print(f"Number of pages in document = {len(document.pages)}")
                    break
        except Exception:
            print(f"Password = {password} is not correct")
```

## 관련 보안 주제

- [파이썬으로 PDF 파일 보안 및 서명](/pdf/ko/python-net/securing-and-signing/)
- [파이썬으로 PDF 파일에 디지털 서명](/pdf/ko/python-net/digitally-sign-pdf-file/)
- [Python에서 PDF에서 서명 정보를 추출합니다.](/pdf/ko/python-net/extract-image-and-signature-information/)
- [Python에서 스마트 카드에서 PDF 문서에 서명하기](/pdf/ko/python-net/sign-pdf-document-from-smart-card/)

