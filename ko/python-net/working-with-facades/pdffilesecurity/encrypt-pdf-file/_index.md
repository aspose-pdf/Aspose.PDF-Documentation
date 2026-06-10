---
title: PDF 파일 암호화
type: docs
weight: 30
url: /ko/python-net/encrypt-pdf-file/
description: PDF 문서를 암호화하고 권한을 구성하여 사용자가 파일로 수행할 수 있는 작업을 제어합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 암호화 및 사용자 작업 제어
Abstract: .NET을 통해 Python용 Aspose.PDF 를 사용하여 특정 사용자 권한을 정의하면서 PDF를 암호화하는 방법을 알아봅니다.이 안내서는 문서를 안전하게 유지하면서 인쇄 및 복사와 같은 작업을 허용하거나 제한하는 방법을 보여줍니다.
---

## 사용자 및 소유자 암호로 PDF 암호화

민감하거나 제한된 콘텐츠를 공유할 때는 PDF 문서의 보안이 필수적입니다.암호화를 통해 문서를 암호로 보호하고 사용자가 수행할 수 있는 작업을 정의할 수 있습니다.이 코드 스니펫은 PDF 파일을 보호하기 위한 액세스 권한과 함께 사용자 및 소유자 암호를 적용하는 방법을 보여줍니다.

1. PDF 파일 보안 개체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 문서 권한을 정의합니다.
1. PDF를 암호화합니다.
1. 암호화된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with User and Owner Password
def encrypt_pdf_with_user_owner_password(infile, outfile):
    """Encrypt a PDF document using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define document privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## 권한으로 PDF 암호화

다음 코드 스니펫은 인쇄 및 복사와 같은 선택된 작업을 허용하고 다른 작업은 제한하는 방법을 설명합니다.

1. 초기화 [PDF 파일 보안](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) 수업.
1. 입력 PDF를 바인딩합니다.
1. 문서 권한 설정.
1. '암호화_파일 () '메서드를 호출합니다.
1. 암호화된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Permissions
def encrypt_pdf_with_permissions(infile, outfile):
    """Encrypt a PDF document and configure specific permissions."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Configure privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## 암호화 알고리즘으로 PDF 암호화

PDF 암호화는 암호로 문서를 보호할 뿐만 아니라 암호화 알고리즘과 강도를 선택할 수 있도록 합니다.적절한 알고리즘을 선택하면 민감한 문서의 보안을 강화할 수 있습니다.

1. PDF 파일 보안 개체 만들기
1. 입력 PDF를 바인딩합니다.
1. 문서 권한을 정의합니다.
1. 알고리즘으로 PDF를 암호화합니다.
1. 암호화된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Encryption Algorithm
def encrypt_pdf_with_encryption_algorithm(infile, outfile):
    """Encrypt a PDF document using a specific encryption algorithm."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF using AES algorithm
    file_security.encrypt_file(
        "user_password",
        "owner_password",
        privilege,
        pdf_facades.KeySize.X256,
        pdf_facades.Algorithm.AES,
    )

    # Save encrypted PDF
    file_security.save(outfile)
```
