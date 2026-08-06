---
title: XML 파일을 만들고 PDF로 변환하는 방법
linktitle: XML 파일을 만들고 PDF로 변환하는 방법
type: docs
weight: 30
url: /ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: PDF SharePoint API는 XML 파일을 생성하고 PDF 형식으로 변환할 수 있습니다.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint is built on top of our award winning Aspose.PDF for .NET component. Aspose.PDF for .NET provides remarkable features from the creation of PDF document from scratch to manipulation of existing PDF files. Among these features, XML to PDF conversion is one of the great features support by this product. So we believe that Aspose.PDF for SharePoint will also be capable of converting XML files into PDF format.

{{% /alert %}}

## XML 파일 생성 및 PDF로 변환

{{% alert color="primary" %}}

이 문서에서는 XML 파일을 생성하고 PDF로 변환하는 과정을 단계별로 안내합니다.

1. [Create an XML file](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [PDF 템플릿 만들기](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [XML 템플릿을 로드합니다](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Specify the path to the source path](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [파일 속성을 지정하세요](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [파일을 PDF로 내보내기](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [PDF 파일 저장](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document)

### 1단계: XML 파일 생성

먼저 .NET 문서 개체 모델용 Aspose.PDF를 기반으로 XML 파일을 만듭니다.

.NET DOM용 Aspose.PDF에 따르면 PDF 문서에는 섹션 개체 컬렉션이 포함되어 있으며 섹션에는 하나 이상의 단락 요소가 포함되어 있습니다. 텍스트는 단락 수준 개체이며 하나 이상의 세그먼트를 포함할 수 있습니다. 아래에서는 샘플 텍스트 문자열이 Segment 개체에 추가되고 Text 개체에 추가됩니다. 마지막으로 Text 요소가 섹션 개체의 단락 컬렉션에 추가됩니다.

```xml

<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Hello World</Segment>

    </Text>

   </Section>

  </Pdf>

```

### 2단계: PDF 템플릿 만들기

계속하기 전에 변환이 수행될 시스템에 SharePoint Foundation Server 2010이 올바르게 설치 및 구성되어 있는지 확인하십시오.

1. SharePoint 사이트에 로그인합니다.
1. **사이트 작업** 및 **모든 항목**을 선택합니다.
1. **만들기** 옵션을 선택하고 목록에서 **PDF 템플릿**을 선택합니다.
1. 템플릿 이름을 입력하세요.
1. **만들기**를 클릭합니다.

![Create PDF Template](how-to-create-and-convert-an-xml-file-to-pdf_1.png)

### 3단계: XML 템플릿 로드

템플릿이 생성되면 [XML 파일](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/)을 로드합니다.

1. PDF 템플릿 페이지에서 **새 항목 추가**를 선택합니다.

![Load XML Template](how-to-create-and-convert-an-xml-file-to-pdf_2.png)

### 4단계: 소스 파일 경로 지정

문서 업로드 대화상자에서:

1. **찾아보기**를 클릭하고 시스템에서 XML 파일을 찾습니다. 기존 파일 옵션을 덮어쓰려면 확인란을 활성화할 수 있습니다.
1. **확인** 버튼을 누르세요.

![Specify Source File Path](how-to-create-and-convert-an-xml-file-to-pdf_3.png)

### 5단계: 파일 속성 지정

파일이 로드되면 필수 필드(빨간색 별표: *로 표시)에 정보를 추가합니다.

이 예에서는 샘플 설명이 추가되었으며 다음 필드가 완성되었습니다.

1. 문서에 대한 간략한 설명입니다.
1. **할당된 목록 유형** 필드에 **AllListTypes**를 입력합니다.
1. **유형** 메뉴에서 **목록**을 선택합니다.
   상태가 **활성**으로 유지되는지 확인하세요.
1. 속성을 저장하려면 **저장**을 클릭하세요.

![Specify File Properties](how-to-create-and-convert-an-xml-file-to-pdf_4.png)

### 6단계: PDF로 내보내기

XML 파일이 PDF 템플릿에 추가된 경우:
어느 하나:

1. test.xml 파일을 마우스 오른쪽 버튼으로 클릭합니다.
1. 메뉴에서 **PDF로 내보내기**를 선택합니다.

또는:

1. **라이브러리 도구**에서 **Aspose 도구**를 선택합니다.
1. **내보내기**를 클릭합니다.

![Export to PDF](how-to-create-and-convert-an-xml-file-to-pdf_5.png)

### 7단계: PDF 문서 저장

1. PDF로 내보내기 대화 상자에서 **템플릿 저장소**(소스 파일이 저장되는 위치)를 선택합니다.
1. **템플릿 이름** 메뉴에서 내보낼 파일을 선택합니다.
1. 최종 PDF 문서를 저장하려면 **PDF로 내보내기**를 클릭하세요.

![Save PDF Document](how-to-create-and-convert-an-xml-file-to-pdf_6.png)

## PDF 열기

PDF 문서가 저장되었으며 열 수 있습니다. 아래 이미지에서 XML의 세그먼트 태그에 있는 "Hello World"라는 문구를 확인하세요. 또한 PDF 생산자는 SharePoint용 Aspose.PDF입니다.

![Open the PDF](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}

