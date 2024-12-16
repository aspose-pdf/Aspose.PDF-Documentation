---
title: AcroForm 생성 - C#에서 수정 가능한 PDF 만들기
linktitle: AcroForm 생성
type: docs
weight: 10
url: /ko/net/create-form/
description: Aspose.PDF for .NET을 사용하여 PDF 파일에서 처음부터 양식을 생성할 수 있습니다
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "AcroForm 생성",
    "alternativeHeadline": "PDF에서 AcroForm 생성 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, AcroForm 생성",
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
    "url": "/net/create-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET을 사용하여 PDF 파일에서 처음부터 양식을 생성할 수 있습니다"
}
</script>
다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 처음부터 양식 만들기

### PDF 문서에 양식 필드 추가

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스는 PDF 문서에서 양식 필드를 관리하는 데 도움이 되는 [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form)이라는 컬렉션을 제공합니다.

양식 필드를 추가하려면:

1. 추가하려는 양식 필드를 생성합니다.
1. [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form) 컬렉션의 Add 메소드를 호출합니다.

### TextBoxField 추가하기

아래 예는 [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield)를 추가하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// 문서 열기
Document pdfDocument = new Document(dataDir + "TextField.pdf");

// 필드 생성
TextBoxField textBoxField = new TextBoxField(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
textBoxField.PartialName = "textbox1";
textBoxField.Value = "Text Box";

// TextBoxField.Border = new Border(
Border border = new Border(textBoxField);
border.Width = 5;
border.Dash = new Dash(1, 1);
textBoxField.Border = border;

textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

// 문서에 필드 추가
pdfDocument.Form.Add(textBoxField, 1);

dataDir = dataDir + "TextBox_out.pdf";
// 수정된 PDF 저장
pdfDocument.Save(dataDir);
```
### RadioButtonField 추가하기

다음 코드 스니펫은 PDF 문서에 [RadioButtonField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/radiobuttonfield)를 추가하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Document 객체를 인스턴스화합니다
Document pdfDocument = new Document();
// PDF 파일에 페이지를 추가합니다
pdfDocument.Pages.Add();
// 페이지 번호를 인자로 사용하여 RadioButtonField 객체를 인스턴스화합니다
RadioButtonField radio = new RadioButtonField(pdfDocument.Pages[1]);
// 첫 번째 라디오 버튼 옵션을 추가하고 Rectangle 객체를 사용하여 원점을 지정합니다
radio.AddOption("Test", new Rectangle(0, 0, 20, 20));
// 두 번째 라디오 버튼 옵션을 추가합니다
radio.AddOption("Test1", new Rectangle(20, 20, 40, 40));
// Document 객체의 form 객체에 라디오 버튼을 추가합니다
pdfDocument.Form.Add(radio);

dataDir = dataDir + "RadioButton_out.pdf";
// PDF 파일을 저장합니다
pdfDocument.Save(dataDir);
```
다음 코드 스니펫은 세 가지 옵션을 가진 RadioButtonField를 추가하고 테이블 셀 안에 배치하는 단계를 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "120 120 120";
page.Paragraphs.Add(table);
Row r1 = table.Rows.Add();
Cell c1 = r1.Cells.Add();
Cell c2 = r1.Cells.Add();
Cell c3 = r1.Cells.Add();

RadioButtonField rf = new RadioButtonField(page);
rf.PartialName = "radio";
doc.Form.Add(rf, 1);

RadioButtonOptionField opt1 = new RadioButtonOptionField();
RadioButtonOptionField opt2 = new RadioButtonOptionField();
RadioButtonOptionField opt3 = new RadioButtonOptionField();

opt1.OptionName = "Item1";
opt2.OptionName = "Item2";
opt3.OptionName = "Item3";

opt1.Width = 15;
opt1.Height = 15;
opt2.Width = 15;
opt2.Height = 15;
opt3.Width = 15;
opt3.Height = 15;

rf.Add(opt1);
rf.Add(opt2);
rf.Add(opt3);

opt1.Border = new Border(opt1);
opt1.Border.Width = 1;
opt1.Border.Style = BorderStyle.Solid;
opt1.Characteristics.Border = System.Drawing.Color.Black;
opt1.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt1.Caption = new TextFragment("Item1");
opt2.Border = new Border(opt1);
opt2.Border.Width = 1;
opt2.Border.Style = BorderStyle.Solid;
opt2.Characteristics.Border = System.Drawing.Color.Black;
opt2.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt2.Caption = new TextFragment("Item2");
opt3.Border = new Border(opt1);
opt3.Border.Width = 1;
opt3.Border.Style = BorderStyle.Solid;
opt3.Characteristics.Border = System.Drawing.Color.Black;
opt3.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt3.Caption = new TextFragment("Item3");
c1.Paragraphs.Add(opt1);
c2.Paragraphs.Add(opt2);
c3.Paragraphs.Add(opt3);

dataDir = dataDir + "RadioButtonWithOptions_out.pdf";
// PDF 파일 저장
doc.Save(dataDir);
```
### 라디오 버튼 필드에 캡션 추가하기

다음 코드 스니펫은 라디오 버튼 필드와 연관된 캡션을 추가하는 방법을 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일을 보려면 다음을 방문하세요 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// 소스 PDF 폼을 로드합니다
Aspose.Pdf.Facades.Form form1 = new Aspose.Pdf.Facades.Form(dataDir + "RadioButtonField.pdf");
Document PDF_Template_PDF_HTML = new Document(dataDir + "RadioButtonField.pdf");
foreach (var item in form1.FieldNames)
{
    Console.WriteLine(item.ToString());
    Dictionary<string, string> radioOptions = form1.GetButtonOptionValues(item);
    if (item.Contains("radio1"))
    {
        Aspose.Pdf.Forms.RadioButtonField field0 = PDF_Template_PDF_HTML.Form[item] as Aspose.Pdf.Forms.RadioButtonField;
        Aspose.Pdf.Forms.RadioButtonOptionField fieldoption = new Aspose.Pdf.Forms.RadioButtonOptionField();
        fieldoption.OptionName = "Yes";
        fieldoption.PartialName = "Yesname";

        var updatedFragment = new Aspose.Pdf.Text.TextFragment("test123");
        updatedFragment.TextState.Font = FontRepository.FindFont("Arial");
        updatedFragment.TextState.FontSize = 10;
        updatedFragment.TextState.LineSpacing = 6.32f;

        // TextParagraph 객체를 생성합니다
        TextParagraph par = new TextParagraph();

        // 단락 위치를 설정합니다
        par.Position = new Position(field0.Rect.LLX, field0.Rect.LLY + updatedFragment.TextState.FontSize);
        // 단어 단위로 줄 바꿈 모드를 지정합니다
        par.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;

        // 단락에 새 TextFragment를 추가합니다
        par.AppendLine(updatedFragment);

        // TextBuilder를 사용하여 TextParagraph를 추가합니다
        TextBuilder textBuilder = new TextBuilder(PDF_Template_PDF_HTML.Pages[1]);
        textBuilder.AppendParagraph(par);

        field0.DeleteOption("item1");
    }
}
PDF_Template_PDF_HTML.Save(dataDir + "RadioButtonField_out.pdf");
```
### ComboBox 필드 추가하기

다음 코드 스니펫은 PDF 문서에 ComboBox 필드를 추가하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Document 객체 생성
Document doc = new Document();

// 문서 객체에 페이지 추가
doc.Pages.Add();

// ComboBox Field 객체 인스턴스화
ComboBoxField combo = new ComboBoxField(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

// ComboBox에 옵션 추가
combo.AddOption("Red");
combo.AddOption("Yellow");
combo.AddOption("Green");
combo.AddOption("Blue");

// 문서 객체의 폼 필드 컬렉션에 콤보 박스 객체 추가
doc.Form.Add(combo);
dataDir = dataDir + "ComboBox_out.pdf";
// PDF 문서 저장
doc.Save(dataDir);
```

### 폼 필드에 툴팁 추가

Document 클래스는 PDF 문서의 폼 필드를 관리하는 Form이라는 컬렉션을 제공합니다.
Document 클래스는 PDF 문서의 양식 필드를 관리하는 Form이라는 컬렉션을 제공합니다.

다음 코드 스니펫은 양식 필드에 툴팁을 추가하는 방법을 보여줍니다. 먼저 C#을 사용한 다음 Visual Basic을 사용합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// 소스 PDF 양식을 로드합니다.
Document doc = new Document(dataDir + "AddTooltipToField.pdf");

// 텍스트필드에 대한 툴팁 설정
(doc.Form["textbox1"] as Field).AlternateName = "텍스트 박스 툴팁";

dataDir = dataDir + "AddTooltipToField_out.pdf";
// 업데이트된 문서를 저장합니다.
doc.Save(dataDir);
```

