---
title: Membuat AcroForm - Membuat PDF yang Dapat Diisi di C#
linktitle: Membuat AcroForm
type: docs
weight: 10
url: /id/net/create-form/
description: Dengan Aspose.PDF untuk .NET Anda dapat membuat formulir dari awal di file PDF Anda
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Membuat AcroForm",
    "alternativeHeadline": "Cara membuat AcroForm di PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, membuat acroform",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
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
    "description": "Dengan Aspose.PDF untuk .NET Anda dapat membuat formulir dari awal di file PDF Anda"
}
</script>
Snippet kode berikut juga dapat bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Buat formulir dari awal

### Tambahkan Form Field dalam Dokumen PDF

Kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) menyediakan koleksi bernama [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form) yang membantu Anda mengelola form field dalam dokumen PDF.

Untuk menambahkan form field:

1. Buat form field yang ingin Anda tambahkan.
1. Panggil metode Add dari koleksi [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form).

### Menambahkan TextBoxField

Contoh di bawah ini menunjukkan cara menambahkan [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "TextField.pdf");

// Buat sebuah field
TextBoxField textBoxField = new TextBoxField(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
textBoxField.PartialName = "textbox1";
textBoxField.Value = "Text Box";

// TextBoxField.Border = new Border(
Border border = new Border(textBoxField);
border.Width = 5;
border.Dash = new Dash(1, 1);
textBoxField.Border = border;

textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

// Tambahkan field ke dokumen
pdfDocument.Form.Add(textBoxField, 1);

dataDir = dataDir + "TextBox_out.pdf";
// Simpan PDF yang dimodifikasi
pdfDocument.Save(dataDir);
```
### Menambahkan RadioButtonField

Berikut ini adalah cuplikan kode yang menunjukkan cara menambahkan [RadioButtonField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/radiobuttonfield) dalam dokumen PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Instansiasi objek Document
Document pdfDocument = new Document();
// Tambahkan halaman ke file PDF
pdfDocument.Pages.Add();
// Instansiasi objek RadioButtonField dengan nomor halaman sebagai argumen
RadioButtonField radio = new RadioButtonField(pdfDocument.Pages[1]);
// Tambahkan opsi tombol radio pertama dan juga tentukan asalnya menggunakan objek Rectangle
radio.AddOption("Test", new Rectangle(0, 0, 20, 20));
// Tambahkan opsi tombol radio kedua
radio.AddOption("Test1", new Rectangle(20, 20, 40, 40));
// Tambahkan tombol radio ke objek formulir dari objek Dokumen
pdfDocument.Form.Add(radio);

dataDir = dataDir + "RadioButton_out.pdf";
// Simpan file PDF
pdfDocument.Save(dataDir);
```
Potongan kode berikut menunjukkan langkah-langkah untuk menambahkan RadioButtonField dengan tiga opsi dan menempatkannya di dalam sel tabel.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
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
// Simpan file PDF
doc.Save(dataDir);
```
### Menambahkan Keterangan pada RadioButtonField

Potongan kode berikut menunjukkan cara menambahkan keterangan yang akan dikaitkan dengan RadioButtonField:

```csharp
// Untuk contoh lengkap dan file data, silahkan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Memuat formulir PDF sumber
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

        // Membuat objek TextParagraph
        TextParagraph par = new TextParagraph();

        // Mengatur posisi paragraf
        par.Position = new Position(field0.Rect.LLX, field0.Rect.LLY + updatedFragment.TextState.FontSize);
        // Menentukan mode pembungkusan kata
        par.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;

        // Menambahkan TextFragment baru ke paragraf
        par.AppendLine(updatedFragment);

        // Menambahkan TextParagraph menggunakan TextBuilder
        TextBuilder textBuilder = new TextBuilder(PDF_Template_PDF_HTML.Pages[1]);
        textBuilder.AppendParagraph(par);

        field0.DeleteOption("item1");
    }
}
PDF_Template_PDF_HTML.Save(dataDir + "RadioButtonField_out.pdf");
```
### Menambahkan Bidang ComboBox

Potongan kode berikut menunjukkan cara menambahkan bidang ComboBox dalam dokumen PDF.

```csharp
// Untuk contoh lengkap dan file data, silahkan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Buat objek Dokumen
Document doc = new Document();

// Tambahkan halaman ke objek dokumen
doc.Pages.Add();

// Instansiasi objek Bidang ComboBox
ComboBoxField combo = new ComboBoxField(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

// Tambahkan opsi ke ComboBox
combo.AddOption("Red");
combo.AddOption("Yellow");
combo.AddOption("Green");
combo.AddOption("Blue");

// Tambahkan objek combo box ke koleksi bidang formulir dari objek dokumen
doc.Form.Add(combo);
dataDir = dataDir + "ComboBox_out.pdf";
// Simpan dokumen PDF
doc.Save(dataDir);
```

### Menambahkan Tooltip ke Bidang Formulir

Kelas Dokumen menyediakan koleksi bernama Form yang mengelola bidang formulir dalam dokumen PDF.
Kelas Document menyediakan koleksi bernama Form yang mengelola bidang formulir dalam dokumen PDF.

Potongan kode berikut menunjukkan cara menambahkan tooltip ke bidang formulir, pertama menggunakan C# dan kemudian Visual Basic.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Memuat formulir PDF sumber
Document doc = new Document(dataDir + "AddTooltipToField.pdf");

// Mengatur tooltip untuk textfield
(doc.Form["textbox1"] as Field).AlternateName = "Text box tool tip";

dataDir = dataDir + "AddTooltipToField_out.pdf";
// Menyimpan dokumen yang telah diperbarui
doc.Save(dataDir);
```

