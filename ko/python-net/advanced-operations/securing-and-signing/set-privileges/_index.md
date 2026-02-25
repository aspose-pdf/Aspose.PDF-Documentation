---
title: PDF 권한 설정, 암호화 및 복호화
linktitle: PDF 파일 암호화 및 복호화
type: docs
weight: 70
url: /ko/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: 다양한 암호화 유형 및 알고리즘을 사용하여 Python으로 PDF 파일을 암호화합니다. 또한 소유자 비밀번호를 사용하여 PDF 파일을 복호화합니다.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF 파일 암호화 또는 복호화
Abstract: 이 문서 페이지에서는 Aspose.PDF for Python을 사용하여 문서 권한을 설정하고, 암호화를 적용하며, PDF 파일을 복호화하는 방법을 설명합니다. 개발자가 사용자 및 소유자 비밀번호를 구성하고, 인쇄, 복사, 편집과 같은 접근 제한을 정의하도록 안내합니다. 코드 예제는 민감한 콘텐츠를 보호하고 Python 애플리케이션 내에서 PDF 보안을 효과적으로 관리하는 방법을 보여주며, 접근 제어와 데이터 기밀성을 보장합니다.
---

민감하거나 비즈니스에 중요한 콘텐츠를 다룰 때 문서 보안을 관리하는 것이 필수적입니다. Aspose.PDF for Python via .NET은 프로그래밍 방식으로 암호화를 적용하고, 권한을 통해 접근을 제어하며, 보호된 PDF 파일을 복호화하는 강력한 API를 제공합니다.

이 기사에서는 Python 개발자를 위해 권한 설정, 암호화 적용 및 제거, 비밀번호 변경, 보호 상태 감지 등 PDF 워크플로우 전반에 걸친 실용적인 예제를 단계별로 안내합니다.

Aspose.PDF for Python via .NET은 개발자에게 PDF 보안에 대한 완전한 제어 권한을 제공합니다:

**권한 설정** - 권한을 사용한 세밀한 접근 제어.
**파일 암호화** - 맞춤 비밀번호로 AES 또는 RC4 암호화를 적용합니다.
**파일 복호화** - 소유자 비밀번호를 사용해 보안을 제거합니다.
**비밀번호 변경** - 내용을 변경하지 않고 자격 증명을 교체하거나 업데이트합니다.
**보안 검사** - 암호화 상태 또는 필요 비밀번호 유형을 감지합니다.

## 기존 PDF 파일에 권한 설정

사용자 및 소유자 비밀번호와 접근 권한을 지정함으로써 특정 작업(예: 인쇄, 복사, 양식 작성)을 제한하거나 허용할 수 있습니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate Document Privileges object
        # Apply restrictions on all privileges
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        # Only allow screen reading
        document_privilege.allow_screen_readers = True
        # Encrypt the file with User and Owner password
        # Need to set the password, so that once the user views the file with user password
        # Only screen reading option is enabled
        document.encrypt("user", "owner", document_privilege, ap.CryptoAlgorithm.AE_SX128, False)
        # Save PDF document
        document.save(path_outfile)
```

## 다양한 암호화 유형 및 알고리즘을 사용한 PDF 파일 암호화

PDF를 암호화하면 유효한 자격 증명을 가진 사용자만 파일을 열거나 수정할 수 있습니다.

>핵심 용어:

- 사용자 비밀번호. 문서를 열기 위해 필요합니다.

- 소유자 비밀번호. 권한을 변경하거나 암호화를 제거하기 위해 필요합니다.

- 키 크기. 최신 워크플로에서 최고 보안을 위해 AE_SX128을 사용하세요.

다음 코드 조각은 PDF 파일을 암호화하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Encrypt PDF
        document.encrypt("user", "owner", ap.Permissions.EXTRACT_CONTENT, ap.CryptoAlgorithm.AE_SX128)
        # Save PDF document
        document.save(path_outfile)
```

## 소유자 비밀번호를 사용한 PDF 파일 복호화

비밀번호 보호를 제거하고 전체 접근을 복원하려면:

1. 올바른 비밀번호('password'는 사용자 또는 소유자 비밀번호)를 사용하여 암호화된 PDF를 로드합니다.
1. 문서에서 모든 비밀번호 보호 및 암호화 설정을 제거합니다.
1. 이제 보호되지 않은 PDF를 지정된 출력 파일에 저장합니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "password") as document:
        # Decrypt PDF
        document.decrypt()
        # Save PDF document
        document.save(path_outfile)
```

## PDF 파일 비밀번호 변경

PDF 문서의 보안 자격 증명(사용자 및 소유자 비밀번호)을 내용과 구조를 유지하면서 업데이트하려면.

1. 기존 소유자 비밀번호('owner')를 사용하여 PDF를 열고, 보안 설정 변경 권한을 포함한 전체 접근을 획득합니다.
1. 기존 비밀번호를 새 사용자 비밀번호('newuser')와 새 소유자 비밀번호('newowner')로 교체합니다.
1. 업데이트된 비밀번호 설정으로 PDF를 저장합니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "owner") as document:
        # Change password
        document.change_passwords("owner", "newuser", "newowner")
        # Save PDF document
        document.save(path_outfile)
```

## 방법 - 원본 PDF가 비밀번호로 보호되는지 확인하는 방법

### 배열에서 올바른 비밀번호 결정

특정 상황에서는 보안이 적용된 PDF에 접근하기 위해 후보 비밀번호 목록 중 올바른 비밀번호를 찾아야 할 수 있습니다. 아래 코드 조각은 PDF 파일이 비밀번호로 보호되는지 확인하고, Aspose.PDF for Python via .NET을 사용하여 미리 정의된 비밀번호 목록을 순회하면서 잠금을 해제하는 방법을 보여줍니다.

프로세스는 다음을 포함합니다:

1. PdfFileInfo를 사용하여 PDF가 암호화되었는지 감지합니다.
1. ap.Document()를 사용해 각 비밀번호로 PDF를 열어봅니다.
1. 성공하면 페이지 수를 출력합니다.
1. 실패하면 예외를 잡아 실패한 비밀번호를 보고합니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    with ap.facades.PdfFileInfo() as pdf_file_info:
        # Bind PDF document
        pdf_file_info.bind_pdf(path_infile)
        # Determine if the source PDF is encrypted
        print("File is password protected " + str(pdf_file_info.is_encrypted))

        passwords = ["test", "test1", "test2", "test3", "sample"]

        for password_index in range(len(passwords)):
            try:
                with ap.Document(path_infile, passwords[password_index]) as document:
                    if len(document.pages) > 0:
                        print("Number of Pages in document are = " + str(len(document.pages)))
                    password_index = password_index + 1
            except Exception as e:
                print("Password = " + passwords[password_index] + " is not correct")
                password_index = password_index + 1
```


