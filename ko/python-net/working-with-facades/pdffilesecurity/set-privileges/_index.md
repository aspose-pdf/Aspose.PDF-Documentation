---
title: 기존 PDF 파일에 권한 설정
type: docs
weight: 40
url: /ko/python-net/set-privileges/
description: PDF 문서 권한을 설정하고 관리하여 인쇄, 복사 및 편집과 같은 사용자 작업을 제어합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 권한 및 액세스 제어 관리
Abstract: .NET을 통해 Python용 Aspose.PDF 를 사용하여 문서 권한을 설정하여 사용자가 PDF로 수행할 수 있는 작업을 제어하는 방법을 알아봅니다.이 가이드에서는 암호를 사용하거나 사용하지 않고 권한을 적용하여 인쇄, 복사 또는 편집과 같은 작업을 제한하는 방법을 설명합니다.
---

## 암호 없이 PDF 권한 설정

.NET을 통해 Python용 Aspose.PDF 를 사용하여 사용자 또는 소유자 암호를 지정하지 않고 PDF에 문서 권한을 적용하는 방법을 확인하십시오.이 코드 스니펫은 문서에 대한 액세스 권한을 유지하면서 허용된 작업을 제어하는 방법을 보여줍니다.

1. 'PDF 파일 보안' 객체를 생성합니다.
1. 입력 PDF를 바인딩합니다.
1. 문서 권한을 정의합니다.
1. 암호를 전달하지 않고 'set_privilege () '메서드를 호출합니다.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges Without Passwords
def set_pdf_privileges_without_passwords(infile, outfile):
    """Set PDF privileges without specifying user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Apply privileges (owner password will be generated automatically)
    file_security.set_privilege(privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## 사용자 및 소유자 암호로 PDF 권한 설정

PDF 문서를 완벽하게 보호하려면 액세스 제어 (암호) 와 사용 제한 (권한) 이 모두 필요한 경우가 많습니다.이 두 가지를 조합하면 인증된 사용자만 문서를 열고 특정 작업을 수행할 수 있도록 할 수 있습니다.

set_privilege 메서드를 암호 매개 변수와 함께 사용하면 다음을 수행할 수 있습니다.

- 사용자 암호로 문서 보호
- 전체 제어를 위한 소유자 암호 정의
- 허용 및 제한 작업 구성
- 문서 수준의 보안 정책 적용

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges with User and Owner Passwords
def set_pdf_privileges_with_passwords(infile, outfile):
    """Set PDF privileges using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = False

    # Apply privileges with passwords
    file_security.set_privilege("user_password", "owner_password", privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## 예외 없이 PDF 권한 설정 시도

이 코드 스니펫은 액세스를 제어하고 복사와 같은 작업을 제한하는 동시에 인쇄와 같은 다른 작업을 허용하는 방법을 설명합니다.

1. 'PDF 파일 보안' 객체를 생성합니다.
1. 'bind_pdf () '메서드를 사용하여 소스 PDF를 로드합니다.
1. 문서 권한을 정의합니다.
1. 암호와 함께 권한 적용.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Set PDF Privileges Without Exception
def try_set_pdf_privileges_without_exception(infile, outfile):
    """Attempt to set PDF privileges without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Attempt to apply privileges
    result = file_security.try_set_privilege(
        "user_password", "owner_password", privilege
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Setting privileges failed. Check passwords or document state.")
```
