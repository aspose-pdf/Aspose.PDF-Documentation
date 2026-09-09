---
title: XML 파일을 생성하고 PDF로 변환하는 방법
linktitle: XML 파일을 생성하고 PDF로 변환하는 방법
type: docs
weight: 30
url: /ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2026-08-10"
description: PDF SharePoint API는 XML 파일을 생성하고 PDF 형식으로 변환할 수 있습니다.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint는 당사의 수상 경력에 빛나는 Aspose.PDF for .NET 구성 요소 위에 구축되었습니다. Aspose.PDF for .NET은 처음부터 PDF 문서를 생성하는 것부터 기존 PDF 파일을 조작하는 것까지 놀라운 기능을 제공합니다. 이러한 기능 중 XML을 PDF로 변환하는 기능은 이 제품에서 지원하는 주요 기능 중 하나입니다. 따라서 Aspose.PDF for SharePoint도 XML 파일을 PDF 형식으로 변환할 수 있을 것이라고 믿습니다.

{{% /alert %}}

## XML 파일을 생성하고 PDF로 변환하기

{{% alert color="primary" %}}

단계별로, 이 문서는 XML 파일을 생성하고 PDF로 변환하는 과정을 안내합니다:

1. [XML 파일을 생성합니다](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [PDF 템플릿을 생성합니다](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [XML 템플릿을 로드합니다](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [소스 경로를 지정합니다](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [파일 속성을 지정합니다](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [파일을 PDF로 내보내기](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [PDF 파일 저장](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document)

### 단계 1: XML 파일 만들기

먼저 Aspose.PDF for .NET 문서 개체 모델을 기반으로 XML 파일을 생성합니다.

Aspose.PDF for .NET DOM에 따르면, PDF 문서는 Section 개체의 컬렉션을 포함하고, Section은 하나 이상의 Paragraph 요소를 포함합니다. Text는 Paragraph 수준의 개체이며 하나 이상의 세그먼트를 포함할 수 있습니다. 아래에서는 샘플 텍스트 문자열을 Segment 개체에 추가하고 이를 Text 개체에 추가합니다. 마지막으로 Text 요소를 Section 객체의 paragraphs 컬렉션에 추가합니다.

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

### 단계 2: PDF 템플릿 만들기

계속하기 전에, 변환이 수행될 시스템에 SharePoint Foundation Server 2010이 올바르게 설치되고 구성되어 있는지 확인하십시오.

1. SharePoint 사이트에 로그인합니다.
1. **Site Action** 및 **All Items**를 선택합니다.
1. 목록에서 **Create** 옵션을 선택하고 **PDF Template**을 선택하십시오.
1. 템플릿 이름을 입력하십시오.
1. **Create**를 클릭하십시오.

![PDF 템플릿 만들기](how-to-create-and-convert-an-xml-file-to-pdf_1.png)

### 단계 3: XML 템플릿 로드

템플릿이 생성되면 로드하십시오. [XML 파일](/pdf/ko/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/)

1. PDF 템플릿 페이지에서 **Add new item**을 선택합니다.

![XML 템플릿 로드](how-to-create-and-convert-an-xml-file-to-pdf_2.png)

### 단계 4: 소스 파일 경로 지정

문서 업로드 대화 상자에서:

1. **Browse**를 클릭하고 시스템에서 XML 파일을 찾습니다. 기존 파일을 덮어쓰는 옵션의 체크 박스를 활성화할 수 있습니다.
1. **OK** 버튼을 누르세요.

![원본 파일 경로 지정](how-to-create-and-convert-an-xml-file-to-pdf_3.png)

### 5단계: 파일 속성 지정

파일이 로드되면 필수 필드(빨간 별표(*)로 표시됨)에 정보를 추가합니다.

이 예제에서는 샘플 설명이 추가되고 다음 필드가 작성되었습니다:

1. 문서에 대한 간략한 설명.
1. **Assigned List Types** 필드에 **AllListTypes** 를 입력합니다.
1. **Type** 메뉴에서 **List** 를 선택하십시오.
   상태가 **Active** 로 유지되는지 확인하십시오.
1. 속성을 저장하려면 **Save** 를 클릭하십시오.

![파일 속성 지정](how-to-create-and-convert-an-xml-file-to-pdf_4.png)

### 단계 6: PDF로 내보내기

XML 파일이 PDF 템플릿에 추가된 경우:
둘 중 하나:

1. test.xml 파일을 마우스 오른쪽 버튼으로 클릭합니다.
1. 메뉴에서 **Export to PDF**를 선택합니다.

또는:

1. **Library Tools**에서 **Aspose Tools**를 선택합니다.
1. 클릭 **Export**.

![PDF로 내보내기](how-to-create-and-convert-an-xml-file-to-pdf_5.png)

### 단계 7: PDF 문서 저장

1. PDF로 내보내기 대화 상자에서 **Template storage**를 선택합니다(소스 파일이 저장된 위치).
1. **Template name** 메뉴에서 내보낼 파일을 선택합니다.
1. 최종 PDF 문서를 저장하려면 **Export to PDF**를 클릭합니다.

![PDF 문서 저장](how-to-create-and-convert-an-xml-file-to-pdf_6.png)

## PDF 열기

PDF 문서가 저장되었으며 열 수 있습니다. 아래 이미지에서 XML의 segment 태그에 있던 “Hello World”라는 문구를 확인하십시오. 또한 PDF Producer가 Aspose.PDF for SharePoint임을 확인하십시오.

![PDF 열기](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}
