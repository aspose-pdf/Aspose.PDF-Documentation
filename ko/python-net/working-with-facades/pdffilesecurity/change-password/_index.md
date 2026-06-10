---
title: PDF 파일의 암호 변경
linktitle: PDF 파일의 암호 변경
type: docs
weight: 10
url: /ko/python-net/change-password/
description: .NET을 통해 Python용 Aspose.PDF 를 사용하여 보안 PDF 문서의 사용자 및 소유자 암호를 변경합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 암호 업데이트
Abstract: .NET을 통해 Python용 Aspose.PDF 파일을 사용하여 보안 PDF 파일에서 사용자 암호와 소유자 암호를 모두 변경하는 방법을 알아봅니다.이 예제는 기존 암호화와 권한을 그대로 유지하면서 액세스 자격 증명을 안전하게 업데이트하는 방법을 보여줍니다.
---

## 사용자 및 소유자 암호 변경

대부분의 경우 기존 보안 설정을 변경하지 않고 보호된 PDF의 암호를 업데이트해야 할 수 있습니다.이는 자격 증명을 교체하거나 소유권을 이전하거나 문서 보안을 강화할 때 유용할 수 있습니다.

의 '비밀번호 변경' 메서드 [PDF 파일 보안](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) 클래스를 통해 다음을 수행할 수 있습니다.

- 사용자 암호 업데이트 (문서를 여는 데 필요)
- 소유자 암호 업데이트 (권한 제어에 사용)
- 현재 암호화 및 권한 설정 유지

1. 'PDF 파일 보안' 객체를 생성합니다.
1. 입력 PDF를 바인딩합니다.
1. '변경_암호 () '메서드를 사용하여 암호를 변경합니다.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change User and Owner Password
def change_user_and_owner_password(infile, outfile):
    """Change user and owner passwords while keeping existing security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Change passwords
    file_security.change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save updated PDF
    file_security.save(outfile)
```

## 암호 변경 및 보안 재설정

보안 PDF 문서로 작업할 때는 단순히 암호를 변경하는 것만으로는 충분하지 않을 수 있습니다.인쇄, 복사 또는 편집 권한과 같은 권한을 조정해야 할 수도 있습니다.

.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 보안 설정을 재설정하는 동안 사용자 및 소유자 암호를 업데이트하는 방법을 알아봅니다.이 예제에서는 새 액세스 자격 증명과 함께 문서 권한 및 암호화 강도를 재정의하는 방법을 보여줍니다.

1. 'PDF 파일 보안' 객체를 생성합니다.
1. 입력 PDF를 바인딩합니다.
1. 'DocumentPrivilege' 객체를 생성하고 허용된 작업을 구성합니다.
1. 암호를 변경하고 보안을 재설정합니다.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change Password and Reset Security
def change_password_and_reset_security(infile, outfile):
    """Change passwords and reset document security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define new privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Change passwords and reset security
    file_security.change_password(
        "owner_password",
        "new_user_password",
        "new_owner_password",
        privilege,
        pdf_facades.KeySize.X128,
    )

    # Save updated PDF
    file_security.save(outfile)
```

## 예외 없이 비밀번호 변경 시도

일부 워크플로우, 특히 배치 처리 또는 자동화 시스템에서는 실행을 방해할 수 있는 예외를 방지하는 것이 중요합니다.오류가 발생하는 대신 성공 또는 실패를 보고하는 안전한 작업을 선호할 수 있습니다.

의 '시도_변경_암호' 메서드 [PDF 파일 보안](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) class는 다음과 같은 방법으로 이 기능을 제공합니다.

1. 'PDF 파일 보안' 객체를 생성합니다.
1. 'bind_pdf () '메서드를 사용하여 PDF 문서를 로드합니다.
1. 암호 변경을 시도합니다.
1. 결과를 확인하세요.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Change Password Without Exception
def try_change_password_without_exception(infile, outfile):
    """Attempt to change passwords without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to change passwords
    result = file_security.try_change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Password change failed. Check owner password or document security.")
```
