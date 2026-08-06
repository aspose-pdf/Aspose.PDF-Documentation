---
title: SharePoint에서 보안 PDF 만들기
linktitle: 보안 PDF 만들기
type: docs
weight: 60
url: /ko/sharepoint/creating-a-secure-pdf/
lastmod: "2020-12-16"
description: Using the PDF SharePoint API, you may produce safe, encrypted PDFs and specify their passwords in SharePoint.
---

{{% alert color="primary" %}}

SharePoint용 Aspose.PDF는 보안 PDF 생성을 지원합니다. SharePoint용 Aspose.PDF를 설치하면 사이트 설정에 **PDF 보안 설정** 옵션이 추가됩니다. 여기에서 사용자 비밀번호, 소유자 비밀번호 및 알고리즘 목록의 값을 설정하여 출력 PDF를 암호화할 수 있습니다. 알고리즘 목록은 암호화 알고리즘과 키 크기의 다양한 조합을 제공합니다. 원하는 값을 전달하세요.

이 문서에서는 SharePoint용 Aspose.PDF를 사용하여 암호화된 PDF를 생성하는 방법을 보여줍니다.

{{% /alert %}}

## 보안 PDF 만들기

기능을 시연하기 위해 먼저 소유자 및 사용자 비밀번호와 암호화 알고리즘에 대한 **PDF 보안 설정** 옵션을 구성합니다. 그런 다음 문서 라이브러리의 두 문서를 병합합니다.

### PDF 보안 설정 옵션 설정

사이트 설정에서 **PDF 보안 설정** 옵션을 열고 알고리즘, 소유자 비밀번호 및 사용자 비밀번호를 설정하세요.

PDF 파일을 암호화하는 동안 다른 사용자 및 소유자 비밀번호를 지정하십시오.

- 사용자 비밀번호가 설정된 경우 PDF를 열기 위해 제공해야 하는 비밀번호입니다. Acrobat Reader는 사용자에게 사용자 비밀번호를 입력하라는 메시지를 표시합니다. 틀리면 문서가 열리지 않습니다.
- 설정된 경우 소유자 암호는 인쇄, 편집, 추출, 주석 달기 등과 같은 권한을 제어합니다. Acrobat Reader는 권한 설정에 따라 이러한 기능을 허용하지 않습니다. 권한을 설정/변경하려면 Acrobat에 이 암호가 필요합니다.

![PDF Secure Settings](creating-a-secure-pdf_1.png)

### Merge Documents

**PDF로 변환** 옵션을 사용하여 두 문서를 병합합니다. 이 기능은 PDF가 아닌 여러 파일(HTML, 텍스트 또는 이미지)을 PDF 파일로 병합합니다.

1. 문서 라이브러리를 열고 목록에서 원하는 문서를 선택하세요.

![Merge Documents](creating-a-secure-pdf_2.png)

1. 라이브러리 도구에서 **PDF로 병합** 옵션을 사용하여 출력 파일을 저장합니다. 출력 파일을 디스크에 저장하라는 메시지가 표시됩니다.

![Merge to PDF](creating-a-secure-pdf_3.png)

### 산출

출력 파일이 암호화되었습니다.

![Output](creating-a-secure-pdf_4.png)


