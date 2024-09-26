---
title: C#를 사용한 PDF 툴팁
linktitle: PDF 툴팁
type: docs
weight: 20
url: /net/pdf-tooltip/
description: C# 및 Aspose.PDF를 사용하여 PDF의 텍스트 조각에 툴팁을 추가하는 방법을 알아보세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#를 사용한 PDF 툴팁",
    "alternativeHeadline": "텍스트에 PDF 툴팁 추가",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, pdf 툴팁 추가",
    "wordcount": "302",
    "proficiencyLevel": "초보자",
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
    "url": "/net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-tooltip/"
    },
    "dateModified": "2022-02-04",
    "description": "C# 및 Aspose.PDF를 사용하여 PDF의 텍스트 조각에 툴팁을 추가하는 방법을 알아보세요."
}
</script>
다음 코드 조각도 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## 검색된 텍스트에 보이지 않는 버튼을 추가하여 툴팁 추가

PDF 문서에서 특정 문구나 단어에 대한 세부 정보를 툴팁으로 추가하여 사용자가 마우스 커서를 텍스트 위로 가져갔을 때 팝업되게 하는 것이 종종 필요합니다. Aspose.PDF for .NET은 검색된 텍스트 위에 보이지 않는 버튼을 추가하여 툴팁을 생성하는 기능을 제공합니다. 다음 코드 조각은 이 기능을 달성하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET에서 확인하세요
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string outputFile = dataDir + "Tooltip_out.pdf";

// 텍스트가 있는 샘플 문서 생성
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("마우스 커서를 여기로 옮기면 툴팁이 표시됩니다"));
doc.Pages[1].Paragraphs.Add(new TextFragment("마우스 커서를 여기로 옮기면 매우 긴 툴팁이 표시됩니다"));
doc.Save(outputFile);

// 텍스트가 있는 문서 열기
Document document = new Document(outputFile);
// 모든 문구에 일치하는 정규 표현식을 찾는 TextAbsorber 객체 생성
TextFragmentAbsorber absorber = new TextFragmentAbsorber("마우스 커서를 여기로 옮기면 툴팁이 표시됩니다");
// 문서 페이지에 absorber 적용
document.Pages.Accept(absorber);
// 추출된 텍스트 조각 가져오기
TextFragmentCollection textFragments = absorber.TextFragments;

// 조각들을 순회
foreach (TextFragment fragment in textFragments)
{
    // 텍스트 조각 위치에 보이지 않는 버튼 생성
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // AlternateName 값이 뷰어 애플리케이션에 의해 툴팁으로 표시됩니다
    field.AlternateName = "텍스트에 대한 툴팁입니다.";
    // 문서에 버튼 필드 추가
    document.Form.Add(field);
}

// 다음은 매우 긴 툴팁의 예제입니다
absorber = new TextFragmentAbsorber("마우스 커서를 여기로 옮기면 매우 긴 툴팁이 표시됩니다");
document.Pages.Accept(absorber);
textFragments = absorber.TextFragments;

foreach (TextFragment fragment in textFragments)
{
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // 매우 긴 텍스트 설정
    field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                            " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                            " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                            " Duis aute irure dolor in reprehenderit in voluptate velit" +
                            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                            " occaecat cupidatat non proident, sunt in culpa qui officia" +
                            " deserunt mollit anim id est laborum.";
    document.Form.Add(field);
}

// 문서 저장
document.Save(outputFile);
```
{{% alert color="primary" %}}

툴팁의 길이와 관련하여, 툴팁 텍스트는 PDF 문자열 타입으로 PDF 문서에 내용 스트림 외부에 포함되어 있습니다. PDF 파일에서 이러한 문자열에 대한 효과적인 제한은 없습니다 (PDF 참조 부록 C 참조). 그러나 특정 프로세서와 특정 운영 환경에서 실행되는 준수 리더(예: Adobe Acrobat)는 그러한 한계를 가지고 있습니다. PDF 리더 애플리케이션 문서를 참조하십시오.

{{% /alert %}}

## 마우스 오버 시 숨겨진 텍스트 블록 생성 및 표시

Aspose.PDF에서는 텍스트 박스 필드(또는 다른 유형의 주석)를 숨기거나 표시할 수 있는 기능을 숨기는 동작이 구현되어 있습니다. 이를 위해 Aspose.Pdf.Annotations.HideAction 클래스를 사용하여 텍스트 블록에 숨기기/표시하기 동작을 할당합니다. 다음 코드 스니펫을 사용하여 마우스 입력/종료시 텍스트 블록을 표시/숨기기하십시오.

PDF 문서에서 동작하는 PDF 동작은 준수 리더(예: 
PDF 문서에서 작동하는 모든 숨기기 작업은 Internet Explorer v.11.0에서 잘 작동합니다.
PDF 문서에서 작동하는 모든 숨기기 작동은 Opera v.12.14에서도 작동하지만 문서를 처음 열 때 일부 응답 지연이 발생합니다.
Google Chrome v.61.0에서 문서를 탐색하는 경우 필드 이름을 받아들이는 HideAction 생성자를 사용하는 구현만 작동합니다. Google Chrome에서 탐색이 중요한 경우 해당 생성자를 사용하십시오.

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string outputFile = dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

// 텍스트가 있는 샘플 문서를 생성합니다.
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("마우스 커서를 여기에 올리면 부동 텍스트가 표시됩니다."));
doc.Save(outputFile);

// 텍스트가 있는 문서를 엽니다.
Document document = new Document(outputFile);
// 정규 표현식에 일치하는 모든 구절을 찾기 위한 TextAbsorber 객체를 생성합니다.
TextFragmentAbsorber absorber = new TextFragmentAbsorber("마우스 커서를 여기에 올리면 부동 텍스트가 표시됩니다.");
// 문서 페이지에 대해 absorber를 수락합니다.
document.Pages.Accept(absorber);
// 추출된 첫 번째 텍스트 조각을 가져옵니다.
TextFragmentCollection textFragments = absorber.TextFragments;
TextFragment fragment = textFragments[1];

// 페이지의 지정된 사각형에 부동 텍스트 필드를 위한 숨겨진 텍스트 필드를 생성합니다.
TextBoxField floatingField = new TextBoxField(fragment.Page, new Rectangle(100, 700, 220, 740));
// 필드 값으로 표시할 텍스트를 설정합니다.
floatingField.Value = "이것은 \"부동 텍스트 필드\"입니다.";
// 이 시나리오에 대해 필드를 '읽기 전용'으로 설정하는 것이 좋습니다.
floatingField.ReadOnly = true;
// 문서 열기시 필드를 보이지 않게 하기 위해 '숨김' 플래그를 설정합니다.
floatingField.Flags |= AnnotationFlags.Hidden;

// 필드 이름을 고유하게 설정할 필요는 없지만 허용됩니다.
floatingField.PartialName = "FloatingField_1";

// 필드 외관의 특성을 설정할 필요는 없지만 더 나은 결과를 만듭니다.
floatingField.DefaultAppearance = new DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
floatingField.Border = new Border(floatingField);
floatingField.Border.Width = 1;
floatingField.Multiline = true;

// 문서에 텍스트 필드를 추가합니다.
document.Form.Add(floatingField);

// 텍스트 조각 위치에 보이지 않는 버튼을 생성합니다.
ButtonField buttonField = new ButtonField(fragment.Page, fragment.Rectangle);
// 지정된 필드(주석) 및 불투명 플래그에 대한 새로운 숨기기 작업을 생성합니다.
// (위에서 지정한 이름을 사용하여 부동 필드를 참조할 수도 있습니다.)
// 보이지 않는 버튼 필드에서 마우스 입력/종료 시 액션을 추가합니다.
buttonField.Actions.OnEnter = new HideAction(floatingField, false);
buttonField.Actions.OnExit = new HideAction(floatingField);

// 문서에 버튼 필드를 추가합니다.
document.Form.Add(buttonField);

// 문서를 저장합니다.
document.Save(outputFile);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET을 위한 PDF 조작 라이브러리",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

