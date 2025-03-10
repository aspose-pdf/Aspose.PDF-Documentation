---
title: JavaScript 작업하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /ko/net/working-with-javascript/
description: Aspose.PDF for .NET을 사용하여 PDF 문서에 JavaScript를 추가, 수정 및 실행하는 방법을 배우십시오. 상호작용성과 자동화를 향상시킵니다.
lastmod: "2025-02-07"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with JavaScript",
    "alternativeHeadline": "Enhance PDF with Custom JavaScript Actions",
    "abstract": "Aspose.PDF for .NET을 통해 PDF 문서 내에서 JavaScript 통합의 향상된 기능을 발견하십시오. 이 새로운 기능은 개발자가 문서 및 페이지 수준에서 JavaScript 작업을 추가하고 관리할 수 있게 하여, 사용자 참여 및 기능성을 향상시키는 상호작용적이고 동적인 PDF 경험을 가능하게 합니다. 웹과 유사한 동작을 모방하는 정교한 PDF 양식을 생성하기 위해 JavaScript의 잠재력을 활용하십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "JavaScript, Acrobat JavaScript, PDF document generation, JavaScript collection, document level JavaScript, JavaScript Action, interactive PDF forms, manipulate PDF files, HTML JavaScript, Aspose.PDF for .NET",
    "wordcount": "423",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## JavaScript 추가하기 (DOM)

### Acrobat JavaScript란 무엇인가요?

Acrobat JavaScript는 ISO-16262의 JavaScript 버전 1.5의 핵심을 기반으로 한 언어로, 이전에 ECMAScript로 알려졌던 Netscape Communications에서 개발한 객체 지향 스크립팅 언어입니다. JavaScript는 웹 기반 애플리케이션에서 서버에서 클라이언트로 웹 페이지 처리를 오프로드하기 위해 만들어졌습니다. Acrobat JavaScript는 JavaScript 언어에 새로운 객체와 그에 수반되는 메서드 및 속성의 형태로 확장을 구현합니다. 이러한 Acrobat 전용 객체는 개발자가 문서 보안을 관리하고, 데이터베이스와 통신하며, 파일 첨부를 처리하고, PDF 파일을 상호작용적이고 웹 지원 양식처럼 작동하도록 조작하는 등의 작업을 가능하게 합니다. Acrobat 전용 객체는 핵심 JavaScript 위에 추가되므로 Math, String, Date, Array 및 RegExp를 포함한 표준 클래스에 여전히 접근할 수 있습니다.

### Acrobat JavaScript와 HTML (웹) JavaScript 비교

PDF 문서는 Acrobat 소프트웨어와 웹 브라우저 모두에서 표시될 수 있기 때문에 Acrobat JavaScript와 웹 브라우저에서 사용되는 JavaScript(HTML JavaScript라고도 함) 간의 차이를 인식하는 것이 중요합니다:

- Acrobat JavaScript는 HTML 페이지 내의 객체에 접근할 수 없습니다. 마찬가지로 HTML JavaScript는 PDF 파일 내의 객체에 접근할 수 없습니다.
- HTML JavaScript는 Window와 같은 객체를 조작할 수 있습니다. Acrobat JavaScript는 이 특정 객체에 접근할 수 없지만 PDF 전용 객체를 조작할 수 있습니다.

문서 및 페이지 수준 모두에서 JavaScript를 추가할 수 있습니다 [Aspose.PDF for .NET](/pdf/ko/net/). JavaScript를 추가하려면:

### 문서 또는 페이지 작업에 JavaScript 추가하기

1. 원하는 JavaScript 문을 생성자 인수로 사용하여 JavascriptAction 객체를 선언하고 인스턴스화합니다.
1. JavascriptAction 객체를 PDF 문서 또는 페이지의 원하는 작업에 할당합니다.

아래 예제는 특정 문서에 OpenAction을 적용합니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Adding JavaScript at Document Level
        // Instantiate JavascriptAction with desired JavaScript statement
        var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

        // Assign JavascriptAction object to desired action of Document
        document.OpenAction = javaScript;

        // Adding JavaScript at Page Level
        document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
        document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

        // Save PDF Document
        document.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Adding JavaScript at Document Level
    // Instantiate JavascriptAction with desired JavaScript statement
    var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    // Assign JavascriptAction object to desired action of Document
    document.OpenAction = javaScript;

    // Adding JavaScript at Page Level
    document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
    document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

    // Save PDF Document
    document.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### 문서 수준에서 JavaScript 추가/제거하기

Document 클래스에 JavaScript 컬렉션 유형의 JavaScript라는 새 속성이 추가되어 키를 통해 JavaScript 시나리오에 접근할 수 있습니다. 이 속성은 문서 수준 JavaScript를 추가하는 데 사용됩니다. JavaScript 컬렉션은 다음과 같은 속성과 메서드를 가지고 있습니다:

- string this(string key)– 이름으로 JavaScript를 가져오거나 설정합니다.
- IList Keys – JavaScript 컬렉션에 있는 기존 키 목록을 제공합니다.
- bool Remove(string key) – 키로 JavaScript를 제거합니다.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        document.JavaScript["func1"] = "function func1() { hello(); }";
        document.JavaScript["func2"] = "function func2() { hello(); }";
        document.Save(dataDir + "AddJavascript.pdf");
    }

    // Remove Document level JavaScript
    using (var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf"))
    {
        var keys = (IList)document1.JavaScript.Keys;

        Console.WriteLine("=============================== ");

        foreach (string key in keys)
        {
            Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
        }

        document1.JavaScript.Remove("func1");

        Console.WriteLine("Key 'func1' removed ");
        Console.WriteLine("=============================== ");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();
    document.JavaScript["func1"] = "function func1() { hello(); }";
    document.JavaScript["func2"] = "function func2() { hello(); }";
    document.Save(dataDir + "AddJavascript.pdf");

    // Remove Document level JavaScript
    using var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf");
    IList keys = (IList)document1.JavaScript.Keys;

    Console.WriteLine("=============================== ");

    foreach (string key in keys)
    {
        Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
    }

    document1.JavaScript.Remove("func1");

    Console.WriteLine("Key 'func1' removed ");
    Console.WriteLine("=============================== ");
}
```
{{< /tab >}}
{{< /tabs >}}

### JavaScript 작업을 사용하여 PDF 문서의 만료 날짜 설정하기

Aspose.PDF는 JavaScript 작업을 삽입하여 PDF 문서의 만료 날짜를 설정할 수 있습니다. 이 기능은 지정된 날짜와 시간 이후에 PDF에 접근할 수 없도록 하여 문서 보안 및 제어를 강화합니다. JavaScript 작업을 활용하여 초 단위까지 정확한 만료 조건을 정의할 수 있어 문서의 접근성을 엄격하게 규제할 수 있습니다.

**다음 단계를 따라 이 작업을 수행할 수 있습니다**

1. **문서 초기화:** 새 PDF 문서를 만들고 빈 페이지를 추가하거나 기존 PDF 문서를 엽니다.
2. **만료 날짜 및 시간 정의:** 문서가 만료될 날짜와 시간을 설정합니다.
3. **JavaScript 코드 준비:** 
    - 현재 날짜와 시간을 가져옵니다.
    - 만료 날짜와 시간을 정확하게 정의합니다. JavaScript에서 월은 0부터 시작합니다.
    - 현재 날짜와 시간을 만료 날짜와 시간과 비교합니다.
    - 현재 날짜와 시간이 만료 날짜와 시간을 초과하면 경고를 표시하고 문서를 닫습니다.
4. **Open Action 설정:** JavaScript 작업을 문서의 열기 작업과 연결합니다.
5. **문서 저장:** 만료 조건을 시행하는 JavaScript가 삽입된 PDF를 저장합니다.

아래는 C# (.NET) 및 Java에서 이 기능을 보여주는 코드 스니펫입니다.

다음 C# 코드 스니펫은 Aspose.PDF를 사용하여 PDF 문서의 만료 날짜와 시간을 설정하는 방법을 보여줍니다:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();

        // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
        DateTime expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

        // Create JavaScript code to enforce the expiry date and time
        string jsCode =
            // Get the current date and time
            "var rightNow = new Date();\n" +
            // Set the expiry date and time
            "var endDate = new Date(" +
            $"{expiryDateTime.Year}," +
            $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
            $"{expiryDateTime.Day}," +
            $"{expiryDateTime.Hour}," +
            $"{expiryDateTime.Minute}," +
            $"{expiryDateTime.Second}" +
            ");\n" +
            "if(rightNow > endDate)\n" +
            "{\n" +
            "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
            "    this.closeDoc();\n" +
            "}";

        // Create a JavascriptAction with the defined JavaScript code
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

        // Set the JavaScript action to execute when the document is opened
        document.OpenAction = javaScript;

        // Save PDF document
        document.Save(dataDir + "PDFExpiry_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();

    // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
    var expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

    // Create JavaScript code to enforce the expiry date and time
    string jsCode =
        // Get the current date and time
        "var rightNow = new Date();\n" +
        // Set the expiry date and time
        "var endDate = new Date(" +
        $"{expiryDateTime.Year}," +
        $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
        $"{expiryDateTime.Day}," +
        $"{expiryDateTime.Hour}," +
        $"{expiryDateTime.Minute}," +
        $"{expiryDateTime.Second}" +
        ");\n" +
        "if(rightNow > endDate)\n" +
        "{\n" +
        "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
        "    this.closeDoc();\n" +
        "}";

    // Create a JavascriptAction with the defined JavaScript code
    var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

    // Set the JavaScript action to execute when the document is opened
    document.OpenAction = javaScript;

    // Save PDF document
    document.Save(dataDir + "PDFExpiry_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

- **JavaScript 날짜 객체:** JavaScript에서 월 인덱스는 1월에 대해 `0`에서 시작하고 12월에 대해 `11`로 끝납니다. 만료 날짜와 시간을 설정할 때 월 값을 적절히 조정해야 합니다.
  
- **보안 고려 사항:** JavaScript 작업은 PDF 문서의 동작을 제어할 수 있지만, PDF 뷰어가 JavaScript를 지원해야 합니다. 모든 PDF 뷰어가 이러한 스크립트를 준수하지 않을 수 있으며, 사용자가 보안상의 이유로 JavaScript 실행을 비활성화할 수 있습니다.

- **사용자 정의:** 만료 시 특정 기능을 비활성화하거나 특정 페이지로 리디렉션하거나 이벤트를 기록하는 등의 추가 작업을 수행하도록 JavaScript 코드를 수정할 수 있습니다. 또한 필요에 따라 시간을 지정하지 않고 만료 날짜만 확인할 수 있습니다.

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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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