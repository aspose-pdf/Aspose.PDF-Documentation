---
title: FDF, XML 및 XFDF 형식의 차이점은 무엇인가요
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: 이 섹션에서는 Aspose.PDF Facades의 Form Class를 사용하여 XML, FDF 및 XFDF 양식 간의 차이를 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats is the difference between FDF, XML, and XFDF formats",
    "alternativeHeadline": "Understanding FDF, XML, and XFDF Formats in Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET을 통해 PDF 양식 데이터 조작에서 FDF, XML 및 XFDF 형식 간의 차이를 발견하세요. 이 기능은 개발자가 각기 다른 구문을 가진 다양한 형식으로 대화형 양식 필드 값을 원활하게 내보낼 수 있도록 하여 PDF 처리에서 이러한 필수 파일 유형의 이해와 사용을 향상시킵니다. 다양한 데이터 형식에서 양식 필드를 표현하는 방법에 대한 자세한 통찰력을 통해 PDF 양식 처리를 최적화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1045",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/whats-the-difference-between-xml-fdf-and-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whats-the-difference-between-xml-fdf-and-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

{{% alert color="primary" %}}

FDF, XML 및 XFDF와 같은 다양한 용어를 혼합했습니다. 이 모든 용어는 서로 관련이 있습니다. 이 문서에서는 이러한 개념과 그 상호 관계를 탐구합니다.

{{% /alert %}}

## 양식 해독하기

Aspose.PDF for .NET은 Adobe에서 표준화한 PDF 문서를 조작하는 데 사용됩니다. PDF 문서에는 AcroForms라고 하는 대화형 양식이 포함되어 있습니다. 이러한 대화형 양식에는 콤보, 텍스트 상자 및 라디오 버튼과 같은 여러 양식 필드가 있습니다. Adobe의 대화형 양식 및 양식 필드는 HTML 양식 및 그 양식 필드와 동일한 방식으로 작동합니다.

양식 필드의 값을 별도의 파일에 저장하는 것이 가능합니다: FDF(Forms Data Format) 파일입니다. 이 파일은 키/값 쌍 방식으로 양식 필드의 값을 포함합니다. FDF 파일은 여전히 이 용도로 사용됩니다. 그러나 Adobe는 XFDF라고 하는 XML 인코딩 형식의 FDF도 제공합니다. XFDF 파일은 XML 태그를 사용하여 계층적으로 양식 필드의 값을 저장합니다.

Aspose.PDF를 사용하면 개발자는 PDF 양식 필드의 값을 FDF 또는 XFDF 파일뿐만 아니라 XML 파일로도 내보낼 수 있습니다. 이러한 모든 파일은 PDF 양식 필드 값을 저장하기 위해 서로 다른 구문을 사용합니다. 아래 예제는 차이점을 설명합니다.

PDF 양식 필드의 값이 FDF, XML 및 XFDF 형식으로 표현되어야 한다고 가정해 보겠습니다. 이러한 가정된 양식 필드와 그 필드 이름 및 값은 아래에 표시됩니다:

|**필드 이름**|**필드 값**|
| :- | :- |
|회사|Aspose.com|
|주소.1|호주 시드니|
|주소.2|추가 주소 줄|
이제 이러한 값을 FDF, XML 및 XFDF 형식으로 표현하는 방법을 살펴보겠습니다.

### FDF 형식이란 무엇인가요?

FDF 파일은 키/값 쌍 방식으로 데이터를 저장하며, 여기서 /T는 키를 나타내고, /V는 값을 나타내며, 괄호 () 안의 데이터는 키 또는 값의 내용을 나타냅니다. 예를 들어, /T(Company)는 Company가 필드 키임을 의미하고 /V(Aspose.com)는 필드 값에 해당합니다.

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Additional Address Line)

### XML 형식이란 무엇인가요?

개발자는 각 PDF 양식 필드를 `<field>` 태그의 형태로 표현할 수 있습니다. 각 필드 태그는 필드 이름을 나타내는 name 속성과 필드 값을 나타내는 하위 태그 `<value>`를 가집니다. 아래와 같이 표시됩니다:

```xml
 <?xml version="1.0" ?>
 <fields>
  <field name="Company">
    <value>Aspose.com</value>
  </field>
  <field name="Address.1">
    <value>Sydney, Australia</value>
  </field>
  <field name="Address.2">
    <value>Additional Address Line</value>
  </field>
 </fields>
```

### XFDF 형식이란 무엇인가요?

위 데이터를 XFDF 형식으로 표현하는 것은 XML 형식과 유사하지만 몇 가지 차이가 있습니다. XFDF 파일에서는 XML 네임스페이스인 <http://ns.adpbe.com/xfdf/>를 추가하고, PDF 문서를 가리키는 `<f>`라는 추가 태그가 있습니다. XML과 마찬가지로 XFDF는 필드 태그 `<field>`의 형태로 필드를 포함합니다. 아래와 같이 표시됩니다:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">   
   <f href="CompanyForm.pdf"/> 
   <fields>
      <field name="Company">
         <value>Aspose.com</value>
      </field>
      <field name="Address">
         <field name="1">
            <value>Sydney, Australia</value>
         </field>
         <field name="2">
            <value>Additional Address Line</value>
         </field>
      </field>
   </fields>
 </xfdf>
```

### 양식 필드 이름 식별하기

Aspose.PDF for .NET은 이미 생성된 PDF 양식을 생성, 편집 및 채울 수 있는 기능을 제공합니다. [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 클래스에는 [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index)라는 함수가 있으며, 이 함수는 채워야 할 필드 이름과 필드 값을 매개변수로 받습니다. 따라서 양식 필드를 채우기 위해서는 정확한 양식 필드 이름을 알아야 합니다.
우리는 종종 Adobe Designer와 같은 도구에서 생성된 양식을 채워야 하는 상황에 직면하며, 이때 양식 필드 이름이 확실하지 않을 수 있습니다. 우리의 요구를 충족하기 위해서는 모든 PDF 양식 필드의 이름을 읽어야 합니다. [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 클래스는 모든 필드 이름을 반환하고 PDF에 필드가 없으면 null을 반환하는 [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames)라는 속성을 제공합니다. 그러나 이 속성은 모든 PDF 양식 필드의 이름을 반환하며, 우리는 어떤 이름이 양식의 어떤 필드에 해당하는지 확실하지 않을 것입니다.

이 문제의 해결책으로 각 필드의 외관 속성이 필요합니다. [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) 클래스에는 위치, 색상, 테두리 스타일, 글꼴, 목록 항목 등을 포함한 속성을 반환하는 GetFieldFacade라는 함수가 있습니다. 이러한 값을 저장하기 위해 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 클래스를 사용하여 필드의 시각적 속성을 기록합니다. 이러한 속성을 얻으면 각 필드 아래에 필드 이름을 표시하는 텍스트 필드를 추가할 수 있습니다. 여기서 텍스트 필드를 추가할 위치를 어떻게 결정할 것인지에 대한 질문이 발생합니다. 이 문제의 해결책은 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 클래스의 Box 속성으로, 필드의 위치를 저장합니다. 이러한 값을 사각형 유형의 배열에 저장하고 이 값을 사용하여 새 텍스트 필드를 추가할 위치를 식별합니다.
Aspose.Pdf.Facades 네임스페이스에는 PDF 양식을 조작할 수 있는 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)라는 클래스가 있으며, 기존의 모든 양식 필드 아래에 텍스트 필드를 추가하고 새 이름으로 PDF 양식을 저장할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DifferenceBetweenFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // First a input pdf file should be assigned
    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf"))
    {
        // Get all field names
        String[] allfields = form.FieldNames;
        // Create an array which will hold the location coordinates of Form fields
        var box = new System.Drawing.Rectangle[allfields.Length];
        for (int i = 0; i < allfields.Length; i++)
        {
            // Get the appearance attributes of each field, consecutively
            var facade = form.GetFieldFacade(allfields[i]);
            // Box in FormFieldFacade class holds field's location.
            box[i] = facade.Box;
        }
        // Save PDF document
        form.Save(dataDir + "DifferenceBetweenFile_out.pdf");
            
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
        {
            // Now we need to add a textfield just upon the original one
            FormEditor editor = new Aspose.Pdf.Facades.FormEditor(document);
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "TextField" + i, allfields[i], 1, box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "DifferenceBetweenFile_out.pdf");
        }
    }
}
```