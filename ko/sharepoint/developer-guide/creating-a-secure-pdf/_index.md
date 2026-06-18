---
title: SharePoint에서 보안 PDF 만들기
linktitle: 보안 PDF 만들기
type: docs
weight: 60
url: /ko/sharepoint/creating-a-secure-pdf/
lastmod: "2026-06-18"
description: PDF SharePoint API를 사용하면 안전하고 암호화된 PDF를 생성하고 SharePoint에서 비밀번호를 지정할 수 있습니다.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint는 보안 PDF 생성을 지원합니다. Aspose.PDF for SharePoint를 설치하면 사이트 설정에 **PDF Secure Settings** 옵션이 추가됩니다. 여기에서 사용자 비밀번호, 소유자 비밀번호 및 알고리즘 목록 중 원하는 값을 설정하여 출력 PDF를 암호화할 수 있습니다. 알고리즘 목록은 다양한 암호화 알고리즘 및 키 크기의 조합을 제공합니다. 원하는 값을 전달하십시오.

이 문서는 Aspose.PDF for SharePoint를 사용하여 암호화된 PDF를 생성하는 방법을 보여줍니다.

{{% /alert %}}

## **보안 PDF 만들기**

기능을 시연하기 위해 먼저 **PDF Secure Setting** 옵션에서 소유자 및 사용자 비밀번호와 암호화 알고리즘을 구성합니다. 예제에서는 문서 라이브러리에서 두 개의 문서를 병합합니다.

### **PDF Secure Setting 옵션 설정**

사이트 설정에서 **PDF Secure Settings** 옵션을 열고 알고리즘, 소유자 비밀번호 및 사용자 비밀번호를 설정합니다.

PDF 파일을 암호화하는 동안 서로 다른 사용자 비밀번호와 소유자 비밀번호를 지정합니다.

- 사용자 비밀번호가 설정된 경우 PDF를 열기 위해 제공해야 하는 것입니다. Acrobat Reader는 사용자에게 사용자 비밀번호를 입력하라는 메시지를 표시합니다. 비밀번호가 틀리면 문서가 열리지 않습니다.
- 소유자 비밀번호가 설정된 경우 인쇄, 편집, 추출, 주석 달기 등과 같은 권한을 제어합니다. Acrobat Reader는 권한 설정에 따라 이러한 기능을 허용하지 않습니다. 권한을 설정하거나 변경하려면 Acrobat에서 이 비밀번호가 필요합니다.

![todo:image_alt_text](creating-a-secure-pdf_1.png)

### **문서 병합**

두 문서를 **Convert to PDF** 옵션을 사용하여 병합합니다. 이 기능은 여러 비-PDF 파일(HTML, 텍스트 또는 이미지)을 PDF 파일로 병합합니다.

1. 문서 라이브러리를 열고 목록에서 원하는 문서를 선택합니다.

![todo:image_alt_text](creating-a-secure-pdf_2.png)


1. 라이브러리 도구의 **Merge to PDF** 옵션을 사용하여 출력 파일을 저장합니다. 출력 파일을 디스크에 저장하라는 메시지가 표시됩니다.

![todo:image_alt_text](creating-a-secure-pdf_3.png)

### **출력**

출력 파일이 암호화되었습니다.

![todo:image_alt_text](creating-a-secure-pdf_4.png)

