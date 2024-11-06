---
title: Encrypt and Decrypt PDF
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 30
url: ko/python-cpp/set-privileges-encrypt-and-decrypt-pdf-file/
description: Python을 통해 C++ 응용 프로그램으로 PDF 파일 암호화 및 해독.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 다양한 암호화 유형 및 알고리즘을 사용하여 PDF 파일 암호화

PDF 파일을 보호하는 효과적인 방법 중 하나는 암호화입니다. 이 문서에서는 Aspose.PDF 라이브러리의 도움으로 Python을 사용하여 PDF 문서를 암호화하는 방법을 살펴보겠습니다.

PDF 암호화는 암호 알고리즘을 사용하여 PDF 문서의 내용을 암호화하여 무단 액세스를 방지하는 것을 포함합니다. 암호화된 PDF 파일은 열기 위해 비밀번호가 필요하며 인쇄, 복사 및 편집과 같은 작업에 제한이 있을 수 있습니다.

- **사용자 비밀번호**를 설정하면 PDF를 열기 위해 제공해야 합니다. Acrobat/Reader는 사용자가 사용자 비밀번호를 입력하도록 요청합니다. 올바르지 않으면 문서가 열리지 않습니다.
- **소유자 비밀번호**는 인쇄, 편집, 추출, 댓글 작성 등과 같은 권한을 제어합니다.
 Acrobat/Reader는 권한 설정에 따라 이러한 작업을 허용하지 않습니다. 권한을 설정/변경하려면 Acrobat이 이 암호를 요구할 것입니다.

다음 코드 스니펫은 PDF 파일을 암호화하는 방법을 보여줍니다.

1. 입력 및 출력 파일 경로 생성
1. AsposePDFPythonWrappers를 사용하여 PDF 문서 로드
1. 암호화된 문서에 대한 권한 정의
1. 사용할 암호화 알고리즘 정의
1. 'document.encrypt' 메소드를 사용하여 지정된 사용자 및 소유자 암호, 권한 및 암호화 알고리즘으로 문서 암호화
1. 'document.save' 메소드를 사용하여 암호화된 문서를 지정된 출력 파일에 저장

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # 샘플 파일의 디렉토리 경로 설정
    dataDir = os.path.join(os.getcwd(), "samples")

    # 입력 파일 경로 설정
    input_file = os.path.join(dataDir, "sample.pdf")

    # 출력 파일 경로 설정
    output_file = os.path.join(dataDir, "results", "sample-enc.pdf")

    # AsposePDFPythonWrappers를 사용하여 PDF 문서 로드
    document = apw.Document(inputFile)

    # 암호화된 문서에 대한 권한 정의
    permission = apCore.Permissions(apCore.Permissions.ExtractContent | apCore.ModifyContent)

    # 사용할 암호화 알고리즘 정의
    cryptoAlgorithm = apCore.CryptoAlgorithm.RC4x128

    # 지정된 사용자 및 소유자 암호, 권한 및 암호화 알고리즘으로 문서 암호화
    document.encrypt("user", "owner", permission, cryptoAlgorithm)

    # 암호화된 문서를 지정된 출력 파일에 저장
    document.save(output_file)
```

## 소유자 암호를 사용하여 PDF 파일 해독

1. 입력 및 출력 파일 경로 생성
1. AsposePDFPythonWrappers 모듈에서 Document 클래스의 새로운 인스턴스 생성
1. [document_decrypt](https://reference.aspose.com/pdf/python-cpp/core/document_decrypt/) 메서드를 사용하여 문서 해독
1. [document_save](https://reference.aspose.com/pdf/python-cpp/core/document_save/) 함수를 사용하여 save() 메서드로 해독한 문서를 출력 파일 경로에 저장

```Python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # 샘플 파일의 디렉토리 경로 설정
    dataDir = os.path.join(os.getcwd(), "samples")

    # 입력 파일 경로 설정
    input_file = os.path.join(dataDir, "sample_enc.pdf")

    # 출력 파일 경로 설정
    output_file = os.path.join(dataDir, "results", "sample-dec.pdf")

    # AsposePDFPythonWrappers 모듈에서 Document 클래스의 새로운 인스턴스 생성
    document = apw.Document(input_file, "owner")

    # decrypt() 메서드를 사용하여 문서 해독
    document.decrypt()

    # save() 메서드를 사용하여 해독한 문서를 출력 파일 경로에 저장
    document.save(output_file)
```