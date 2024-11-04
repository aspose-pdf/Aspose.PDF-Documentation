```
title: SharePoint에서 안전한 PDF 생성

linktitle: 안전한 PDF 생성

type: docs

weight: 60

url: /sharepoint/creating-a-secure-pdf/

lastmod: "2020-12-16"

description: PDF SharePoint API를 사용하여 SharePoint에서 안전하고 암호화된 PDF를 생성하고 비밀번호를 지정할 수 있습니다.

```

{{% alert color="primary" %}}

Aspose.PDF for SharePoint는 안전한 PDF 생성을 지원합니다. Aspose.PDF for SharePoint를 설치하면 사이트 설정에 **PDF 보안 설정** 옵션이 추가됩니다. 여기에서 사용자 비밀번호, 소유자 비밀번호 및 알고리즘 목록에서 값을 설정하여 출력 PDF를 암호화할 수 있습니다. 알고리즘 목록은 암호화 알고리즘과 키 크기의 다양한 조합을 제공합니다. 원하는 값을 전달하세요.

이 문서는 SharePoint에서 Aspose.PDF를 사용하여 암호화된 PDF를 생성하는 방법을 설명합니다.

{{% /alert %}}

## **안전한 PDF 생성**

기능을 설명하기 위해 먼저 소유자와 사용자 비밀번호 및 암호화 알고리즘에 대해 **PDF 보안 설정** 옵션을 구성합니다. 이 예시는 문서 라이브러리에서 두 문서를 병합합니다.



### **PDF 보안 설정 옵션 설정**



사이트 설정에서 **PDF 보안 설정** 옵션을 열고 알고리즘, 소유자 비밀번호 및 사용자 비밀번호를 설정합니다.



PDF 파일을 암호화할 때 다른 사용자 및 소유자 비밀번호를 지정합니다.



- 사용자 비밀번호가 설정된 경우, PDF를 열기 위해 제공해야 하는 비밀번호입니다. Acrobat Reader는 사용자가 사용자 비밀번호를 입력하도록 요청합니다. 비밀번호가 틀리면 문서가 열리지 않습니다.

- 소유자 비밀번호가 설정된 경우, 인쇄, 편집, 추출, 주석 등과 같은 권한을 제어합니다. Acrobat Reader는 권한 설정에 따라 이러한 기능을 허용하지 않습니다. 권한을 설정/변경하려면 이 비밀번호가 필요합니다.



![todo:image_alt_text](creating-a-secure-pdf_1.png)



### **문서 병합**



**PDF로 변환** 옵션을 사용하여 두 문서를 병합합니다. 이 기능은 여러 개의 비PDF 파일(HTML, 텍스트 또는 이미지)을 PDF 파일로 병합합니다.



1. ```
문서 라이브러리를 열고 목록에서 원하는 문서를 선택합니다.

![todo:image_alt_text](creating-a-secure-pdf_2.png)

1. 라이브러리 도구에서 **Merge to PDF** 옵션을 사용하여 출력 파일을 저장합니다. 출력 파일을 디스크에 저장하라는 메시지가 나타납니다.

![todo:image_alt_text](creating-a-secure-pdf_3.png)

### **Output**

출력 파일이 암호화됩니다.

![todo:image_alt_text](creating-a-secure-pdf_4.png)
```