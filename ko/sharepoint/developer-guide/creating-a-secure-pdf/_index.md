---
title: SharePoint에서 보안 PDF 만들기
linktitle: 보안 PDF 만들기
type: docs
weight: 60
url: /ko/sharepoint/creating-a-secure-pdf/
lastmod: "2026-08-10"
description: PDF SharePoint API를 사용하면 안전하고 암호화된 PDF를 생성하고 SharePoint에서 비밀번호를 지정할 수 있습니다.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint는 보안 PDF 생성을 지원합니다. Aspose.PDF for SharePoint를 설치하면 Site Setting에 **PDF Secure Settings** 옵션이 추가됩니다. 여기에서 사용자 비밀번호, 소유자 비밀번호 및 알고리즘 목록 중 원하는 값을 지정하여 출력 PDF를 암호화할 수 있습니다. 알고리즘 목록은 다양한 암호화 알고리즘과 키 크기의 조합을 제공합니다. 원하는 값을 전달하십시오.

이 문서에서는 Aspose.PDF for SharePoint를 사용하여 암호화된 PDF를 생성하는 방법을 보여줍니다.

{{% /alert %}}

## 보안 PDF 만들기

기능을 시연하려면 먼저 소유자 비밀번호와 사용자 비밀번호, 그리고 암호화 알고리즘에 대한 **PDF Secure Setting** 옵션을 구성합니다. 그런 다음 예제에서는 문서 라이브러리의 두 문서를 병합합니다.

### PDF Secure Setting 옵션 설정

사이트 설정에서 **PDF Secure Settings** 옵션을 열고 알고리즘, 소유자 비밀번호 및 사용자 비밀번호를 설정합니다.

PDF 파일을 암호화하는 동안 서로 다른 사용자 비밀번호와 소유자 비밀번호를 지정합니다.

- 사용자 비밀번호가 설정된 경우, PDF를 열기 위해 제공해야 하는 비밀번호입니다. Acrobat Reader는 사용자에게 사용자 비밀번호 입력을 요청합니다. 비밀번호가 틀리면 문서는 열리지 않습니다.
- 소유자 비밀번호가 설정된 경우, 인쇄, 편집, 추출, 댓글 달기 등과 같은 권한을 제어합니다. Acrobat Reader는 권한 설정에 따라 이러한 기능을 사용할 수 없게 합니다. Acrobat은 권한을 설정/변경하려면 이 비밀번호가 필요합니다.

![PDF 보안 설정](creating-a-secure-pdf_1.png)

### 문서 병합

**Convert to PDF** 옵션을 사용하여 두 개의 문서를 병합합니다. 이 기능은 여러 비PDF 파일(HTML, 텍스트 또는 이미지)을 PDF 파일로 병합합니다.

1. 문서 라이브러리를 열고 목록에서 원하는 문서를 선택합니다.

![문서 병합](creating-a-secure-pdf_2.png)

1. Library Tools의 **Merge to PDF** 옵션을 사용하여 출력 파일을 저장합니다. 출력 파일을 디스크에 저장하라는 프롬프트가 표시됩니다.

![PDF로 병합](creating-a-secure-pdf_3.png)

### 출력

출력 파일이 암호화되었습니다.

![출력](creating-a-secure-pdf_4.png)

