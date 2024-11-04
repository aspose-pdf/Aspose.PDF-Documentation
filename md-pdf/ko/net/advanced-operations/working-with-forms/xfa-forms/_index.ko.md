---
title: XFA 양식 작업
linktitle: XFA 양식
type: docs
weight: 20
url: /net/xfa-forms/
description: Aspose.PDF for .NET API는 PDF 문서에서 XFA 및 XFA Acroform 필드를 처리할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "XFA 양식 작업",
    "alternativeHeadline": "PDF에서 XFA 양식 채우기, 변환하기 및 가져오기",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, xfa 양식 채우기, xfa 양식 가져오기, xfa 양식 변환하기",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET API는 PDF 문서에서 XFA 및 XFA Acroform 필드를 처리할 수 있습니다."
}
</script>
{{% alert color="primary" %}}

동적 폼은 "XML Forms Architecture"로 알려진 XML 사양을 기반으로 합니다. 또한 동적 XFA 폼을 표준 Acroform으로 변환할 수 있습니다. 폼에 대한 정보( PDF 관점에서)는 매우 모호합니다 - 필드가 존재한다는 것과 속성 및 JavaScript 이벤트를 명시하지만, 렌더링을 명시하지 않습니다. XFA 폼의 객체는 문서를 로딩할 때 그려집니다.

{{% /alert %}}

Form 클래스는 정적 AcroForm을 다룰 수 있는 기능을 제공하며, Form 클래스의 GetFieldFacade(..) 메서드를 사용하여 특정 필드 인스턴스를 가져올 수 있습니다. 그러나, XFA 필드는 Form.GetFieldFacade(..) 메서드를 통해 접근할 수 없습니다. 대신, [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa)를 사용하여 필드 값을 가져오거나 설정하고 XFA 필드 템플릿을 조작하세요(필드 속성 설정).

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## XFA 필드 채우기

다음 코드 스니펫은 XFA 폼에서 필드를 채우는 방법을 보여줍니다.
다음 코드 스니펫은 XFA 양식의 필드를 채우는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 다음을 참조하세요 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// XFA 양식 로드
Document doc = new Document(dataDir + "FillXFAFields.pdf");

// XFA 양식 필드의 이름 가져오기
string[] names = doc.Form.XFA.FieldNames;

// 필드 값 설정
doc.Form.XFA[names[0]] = "Field 0";
doc.Form.XFA[names[1]] = "Field 1";
dataDir = dataDir + "Filled_XFA_out.pdf";
// 업데이트된 문서 저장
doc.Save(dataDir);
```

## XFA를 Acroform으로 변환

{{% alert color="primary" %}}

온라인 시도
Aspose.PDF 변환의 품질을 확인하고 결과를 온라인에서 확인할 수 있는 링크입니다: [products.aspose.app/pdf/xfa/](https://products.aspose.app/pdf/xfa/)

{{% /alert %}}

동적 양식은 "XML Forms Architecture"로 알려진 XML 사양을 기반으로 합니다.
동적 폼은 "XML Forms Architecture"로 알려진 XFA XML 사양을 기반으로 합니다.

현재 PDF는 데이터와 PDF 폼을 통합하기 위한 두 가지 다른 방법을 지원합니다:

- AcroForms(일명 Acrobat 폼), PDF 1.2 형식 사양에 도입되어 포함되었습니다.
- Adobe XML Forms Architecture(XFA) 폼, PDF 1.5 형식 사양에서 선택 기능으로 도입되었습니다( XFA 사양은 PDF 사양에 포함되어 있지 않으며, 참조만 됩니다.)

XFA 폼의 페이지를 추출하거나 조작할 수 없습니다. 왜냐하면 폼 내용은 XFA 폼을 보거나 렌더링하려는 애플리케이션 내에서 런타임( XFA 폼 보기 중)에 생성되기 때문입니다. Aspose.PDF에는 개발자가 XFA 폼을 표준 AcroForms로 변환할 수 있는 기능이 있습니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// 동적 XFA 폼을 로드합니다
Document document = new Document(dataDir + "DynamicXFAToAcroForm.pdf");

// 폼 필드 유형을 표준 AcroForm으로 설정합니다
document.Form.Type = FormType.Standard;

dataDir = dataDir + "Standard_AcroForm_out.pdf";
// 결과 PDF를 저장합니다
document.Save(dataDir);
```
## XFA 필드 속성 가져오기

필드 속성에 접근하려면 먼저 Document.Form.XFA.Teamplate를 사용하여 필드 템플릿에 접근하세요. 다음 코드 조각은 XFA 폼 필드의 X 및 Y 좌표를 가져오는 단계를 보여줍니다.

```csharp
// 전체 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// XFA 폼 로드
Document doc = new Document(dataDir + "GetXFAProperties.pdf");

string[] names = doc.Form.XFA.FieldNames;

// 필드 값 설정
doc.Form.XFA[names[0]] = "필드 0";
doc.Form.XFA[names[1]] = "필드 1";

// 필드 위치 가져오기
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);

// 필드 위치 가져오기
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);

dataDir = dataDir + "Filled_XFA_out.pdf";
// 업데이트된 문서 저장
doc.Save(dataDir);
```

