---
title: How to Create and Convert an XML File to PDF
type: docs
weight: 30
url: /sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: PDF SharePoint API is capable of creating and converting XML files into PDF format.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint는 수상 경력이 있는 Aspose.PDF for .NET 컴포넌트를 기반으로 구축되었습니다. Aspose.PDF for .NET은 PDF 문서를 처음부터 생성하여 기존 PDF 파일을 조작하는 것까지 뛰어난 기능을 제공합니다. 이러한 기능 중 XML을 PDF로 변환하는 것은 이 제품이 지원하는 훌륭한 기능 중 하나입니다. 따라서 Aspose.PDF for SharePoint도 XML 파일을 PDF 형식으로 변환할 수 있다고 믿습니다.

{{% /alert %}}

## **XML 파일 생성 및 PDF로 변환**

{{% alert color="primary" %}}

이 기사에서는 단계별로 XML 파일을 생성하고 PDF로 변환하는 과정을 안내합니다:


1. [XML 파일 생성](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [PDF 템플릿 생성](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [XML 템플릿 로드](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [소스 경로 지정](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [파일 속성 지정](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [파일을 PDF로 내보내기](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [PDF 파일 저장](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).
#### **Step 1: XML 파일 생성**
먼저 Aspose.PDF for .NET 문서 객체 모델을 기반으로 XML 파일을 생성합니다.

Aspose.PDF for .NET DOM에 따르면, PDF 문서는 Section 객체의 컬렉션을 포함하며, Section은 하나 이상의 Paragraph 요소를 포함합니다.
 텍스트는 단락 수준 객체이며 하나 이상의 세그먼트를 포함할 수 있습니다. 아래의 샘플 텍스트 문자열은 Segment 객체에 추가되고 Text 객체에 추가됩니다. 마지막으로 Text 요소는 Section 객체의 paragraphs 컬렉션에 추가됩니다.

**XML**

{{< highlight csharp >}}



<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Hello World</Segment>

    </Text>

   </Section>

  </Pdf>



{{< /highlight >}}
#### **2단계: PDF 템플릿 생성**
계속하기 전에 SharePoint Foundation 서버 2010이 변환이 이루어질 시스템에 제대로 설치되고 구성되어 있는지 확인하십시오.

1. SharePoint 사이트에 로그인합니다.
1. **사이트 작업** 및 **모든 항목**을 선택합니다.
1. **생성** 옵션을 선택하고 목록에서 **PDF 템플릿**을 선택합니다.
1. 템플릿 이름을 입력합니다.
1. **생성**을 클릭합니다.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **3단계: XML 템플릿 로드**

템플릿이 생성되면, [XML 파일](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/)을 로드합니다:
1. PDF 템플릿 페이지에서 **새 항목 추가**를 선택하세요.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **4단계: 소스 파일 경로 지정**
문서 업로드 대화 상자에서:

1. **찾아보기**를 클릭하여 시스템에서 XML 파일을 찾습니다. 기존 파일 옵션을 덮어쓰는 체크 박스를 활성화할 수 있습니다.
1. **확인** 버튼을 누르세요.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **5단계: 파일 속성 지정**
파일이 로드되면 필수 필드(빨간색 별표: *)에 정보를 추가합니다.

이 예에서는 샘플 설명이 추가되었으며 다음 필드가 완료되었습니다:

1. 문서의 간단한 설명.
1. **지정된 목록 유형** 필드에 **AllListTypes**를 입력합니다.
1. **유형** 메뉴에서 **목록**을 선택합니다. 상태가 **활성**으로 유지되도록 합니다.
1. **저장**을 클릭하여 속성을 저장하세요.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **6단계: PDF로 내보내기**

XML 파일이 PDF 템플릿에 추가되었을 때:
Either:

1. test.xml 파일을 마우스 오른쪽 버튼으로 클릭합니다.
1. 메뉴에서 **PDF로 내보내기**를 선택합니다.

Or:

1. **라이브러리 도구**에서 **Aspose 도구**를 선택합니다.
1. **내보내기**를 클릭합니다.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **7단계: PDF 문서 저장**
1. PDF로 내보내기 대화 상자에서 **템플릿 저장소**(소스 파일이 저장된 위치)를 선택합니다.
1. **템플릿 이름** 메뉴에서 내보낼 파일을 선택합니다.
1. **PDF로 내보내기**를 클릭하여 최종 PDF 문서를 저장합니다.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **PDF 열기**
PDF 문서가 저장되어 열 수 있습니다. 아래 이미지에서 XML의 {segment] 태그에 있던 "Hello World"라는 구문을 확인하세요. 또한 PDF 제작자가 Aspose.PDF for SharePoint임을 확인하세요.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}