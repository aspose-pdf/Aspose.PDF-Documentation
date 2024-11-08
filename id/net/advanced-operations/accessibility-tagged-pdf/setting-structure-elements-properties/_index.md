---
title: Mengatur Properti Elemen Struktur
linktitle: Mengatur Properti Elemen Struktur
type: docs
weight: 30
url: /id/net/setting-structure-elements-properties/
description: Anda dapat mengatur berbagai properti elemen struktur dalam dokumen PDF dengan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Mengatur Properti Elemen Struktur",
    "alternativeHeadline": "Cara mengatur properti elemen struktural",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, mengatur struktur teks, mengatur bahasa, mengatur judul, mengatur elemen struktur Catatan",
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
    "url": "/net/setting-structure-elements-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/setting-structure-elements-properties/"
    },
    "dateModified": "2022-02-04",
    "description": "Anda dapat mengatur berbagai properti elemen struktur dalam dokumen PDF dengan Aspose.PDF untuk .NET."
}
</script>
Untuk mengatur properti elemen struktur dalam Dokumen PDF Bertag, Aspose.PDF menawarkan metode [CreateSectElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createsectelement) dan [CreateHeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createheaderelement/index) dari antarmuka [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent).

Potongan kode berikut menunjukkan cara mengatur properti elemen struktur dari Dokumen PDF Bertag:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Atur Judul dan Bahasa untuk Dokumen
taggedContent.SetTitle("Dokumen Pdf Bertag");
taggedContent.SetLanguage("en-US");

// Buat Elemen Struktur
StructureElement rootElement = taggedContent.RootElement;

SectElement sect = taggedContent.CreateSectElement();
rootElement.AppendChild(sect);

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
sect.AppendChild(h1);
h1.SetText("Judul");

h1.Title = "Judul";
h1.Language = "en-US";
h1.AlternativeText = "Teks Alternatif";
h1.ExpansionText = "Teks Ekspansi";
h1.ActualText = "Teks Sebenarnya";

// Simpan Dokumen Pdf Bertag
document.Save(dataDir + "StructureElementsProperties.pdf");
```
## Menetapkan Elemen Struktur Teks

Untuk menetapkan elemen struktur teks dari Dokumen PDF Bertag, Aspose.PDF menawarkan kelas [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). Cuplikan kode berikut menunjukkan cara menetapkan elemen struktur teks dari Dokumen PDF Bertag:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Membuat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Menetapkan Judul dan Bahasa untuk Dokumen
taggedContent.SetTitle("Dokumen Pdf Bertag");
taggedContent.SetLanguage("en-US");

// Dapatkan Elemen Struktur Akar
StructureElement rootElement = taggedContent.RootElement;

ParagraphElement p = taggedContent.CreateParagraphElement();
// Menetapkan Teks ke Elemen Struktur Teks
p.SetText("Paragraf.");
rootElement.AppendChild(p);


// Simpan Dokumen Pdf Bertag
document.Save(dataDir + "TextStructureElement.pdf");
```
## Mengatur Elemen Struktur Blok Teks

Untuk mengatur elemen struktur blok teks dari Dokumen PDF Bertanda, Aspose.PDF menawarkan kelas [HeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/headerelement) dan [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). Anda dapat menambahkan objek dari kelas ini sebagai anak dari objek [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement).
Potongan kode berikut menunjukkan cara mengatur elemen struktur blok teks dari Dokumen PDF Bertanda:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Membuat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Atur Judul dan Bahasa untuk Dokumen
taggedContent.SetTitle("Dokumen Pdf Bertanda");
taggedContent.SetLanguage("en-US");

// Dapatkan Elemen Struktur Akar
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
h1.SetText("H1. Header Tingkat 1");
h2.SetText("H2. Header Tingkat 2");
h3.SetText("H3. Header Tingkat 3");
h4.SetText("H4. Header Tingkat 4");
h5.SetText("H5. Header Tingkat 5");
h6.SetText("H6. Header Tingkat 6");
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.AppendChild(p);

// Simpan Dokumen Pdf Bertanda
document.Save(dataDir + "TextBlockStructureElements.pdf");
```
## Mengatur Elemen Struktur Inline

Untuk mengatur elemen struktur inline dari Dokumen PDF Bertag, Aspose.PDF menawarkan kelas [SpanElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/spanelement) dan [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). Anda dapat menambahkan objek dari kelas ini sebagai anak dari objek [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). Cuplikan kode berikut menunjukkan cara mengatur elemen struktur inline dari Dokumen PDF Bertag:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Membuat Dokumen Pdf
Document document = new Document();

// Mendapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Mengatur Judul dan Bahasa untuk Dokumen
taggedContent.SetTitle("Dokumen Pdf Bertag");
taggedContent.SetLanguage("en-US");

// Mendapatkan Elemen Struktur Akar
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

SpanElement spanH11 = taggedContent.CreateSpanElement();
spanH11.SetText("H1. ");
h1.AppendChild(spanH11);
SpanElement spanH12 = taggedContent.CreateSpanElement();
spanH12.SetText("Header Tingkat 1");
h1.AppendChild(spanH12);

SpanElement spanH21 = taggedContent.CreateSpanElement();
spanH21.SetText("H2. ");
h2.AppendChild(spanH21);
SpanElement spanH22 = taggedContent.CreateSpanElement();
spanH22.SetText("Header Tingkat 2");
h2.AppendChild(spanH22);

SpanElement spanH31 = taggedContent.CreateSpanElement();
spanH31.SetText("H3. ");
h3.AppendChild(spanH31);
SpanElement spanH32 = taggedContent.CreateSpanElement();
spanH32.SetText("Header Tingkat 3");
h3.AppendChild(spanH32);

SpanElement spanH41 = taggedContent.CreateSpanElement();
spanH41.SetText("H4. ");
h4.AppendChild(spanH41);
SpanElement spanH42 = taggedContent.CreateSpanElement();
spanH42.SetText("Header Tingkat 4");
h4.AppendChild(spanH42);

SpanElement spanH51 = taggedContent.CreateSpanElement();
spanH51.SetText("H5. ");
h5.AppendChild(spanH51);
SpanElement spanH52 = taggedContent.CreateSpanElement();
spanH52.SetText("Header Tingkat 5");
h5.AppendChild(spanH52);

SpanElement spanH61 = taggedContent.CreateSpanElement();
spanH61.SetText("H6. ");
h6.AppendChild(spanH61);
SpanElement spanH62 = taggedContent.CreateSpanElement();
spanH62.SetText("Header Tingkat 6");
h6.AppendChild(spanH62);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. ");
rootElement.AppendChild(p);
SpanElement span1 = taggedContent.CreateSpanElement();
span1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
p.AppendChild(span1);
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Aenean nec lectus ac sem faucibus imperdiet. ");
p.AppendChild(span2);
SpanElement span3 = taggedContent.CreateSpanElement();
span3.SetText("Sed ut erat ac magna ullamcorper hendrerit. ");
p.AppendChild(span3);
SpanElement span4 = taggedContent.CreateSpanElement();
span4.SetText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
p.AppendChild(span4);
SpanElement span5 = taggedContent.CreateSpanElement();
span5.SetText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
p.AppendChild(span5);
SpanElement span6 = taggedContent.CreateSpanElement();
span6.SetText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
p.AppendChild(span6);
SpanElement span7 = taggedContent.CreateSpanElement();
span7.SetText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
p.AppendChild(span7);
SpanElement span8 = taggedContent.CreateSpanElement();
span8.SetText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
p.AppendChild(span8);
SpanElement span9 = taggedContent.CreateSpanElement();
span9.SetText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
p.AppendChild(span9);
SpanElement span10 = taggedContent.CreateSpanElement();
span10.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
p.AppendChild(span10);

// Menyimpan Dokumen Pdf Bertag
document.Save(dataDir + "InlineStructureElements.pdf");
```
## Mengatur Nama Tag Kustom

Untuk mengatur nama tag kustom dari elemen-elemen dalam Dokumen PDF Bertag, Aspose.PDF menawarkan metode [SetTag](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/methods/settag) dari kelas StructureElement untuk elemen-elemen. Cuplikan kode berikut menunjukkan cara mengatur nama tag kustom:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Atur Judul dan Bahasa untuk Dokumen
taggedContent.SetTitle("Dokumen Pdf Bertag");
taggedContent.SetLanguage("en-US");

// Buat Elemen Struktur Logis
SectElement sect = taggedContent.CreateSectElement();
taggedContent.RootElement.AppendChild(sect);

ParagraphElement p1 = taggedContent.CreateParagraphElement();
ParagraphElement p2 = taggedContent.CreateParagraphElement();
ParagraphElement p3 = taggedContent.CreateParagraphElement();
ParagraphElement p4 = taggedContent.CreateParagraphElement();

p1.SetText("P1. ");
p2.SetText("P2. ");
p3.SetText("P3. ");
p4.SetText("P4. ");

p1.SetTag("P1");
p2.SetTag("Para");
p3.SetTag("Para");
p4.SetTag("Paragraph");

sect.AppendChild(p1);
sect.AppendChild(p2);
sect.AppendChild(p3);
sect.AppendChild(p4);

SpanElement span1 = taggedContent.CreateSpanElement();
SpanElement span2 = taggedContent.CreateSpanElement();
SpanElement span3 = taggedContent.CreateSpanElement();
SpanElement span4 = taggedContent.CreateSpanElement();

span1.SetText("Span 1.");
span2.SetText("Span 2.");
span3.SetText("Span 3.");
span4.SetText("Span 4.");

span1.SetTag("SPAN");
span2.SetTag("Sp");
span3.SetTag("Sp");
span4.SetTag("TheSpan");

p1.AppendChild(span1);
p2.AppendChild(span2);
p3.AppendChild(span3);
p4.AppendChild(span4);

// Simpan Dokumen Pdf Bertag
document.Save(dataDir + "CustomTag.pdf");
```
## Menambahkan Elemen Struktur ke dalam Elemen

**Fitur ini didukung oleh versi 19.4 atau lebih tinggi.**

Untuk mengatur elemen struktur tautan dalam Dokumen PDF Bertanda, Aspose.PDF menawarkan metode [CreateLinkElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createlinkelement) dari antarmuka [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent). Potongan kode berikut menunjukkan cara mengatur elemen struktur dalam paragraf dengan teks Dokumen PDF Bertanda:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "LinkStructureElements_Output.pdf";
string logFile = dataDir + "46035_log.xml";
string imgFile = dataDir + "google-icon-512.png";

// Membuat dokumen dan mendapatkan Konten Pdf Bertanda
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// Mengatur Judul dan Bahasa Alami untuk dokumen
taggedContent.SetTitle("Contoh Elemen Tautan");
taggedContent.SetLanguage("en-US");

// Mendapatkan elemen struktur Akar (elemen struktur Dokumen)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
LinkElement link1 = taggedContent.CreateLinkElement();
p1.AppendChild(link1);
link1.Hyperlink = new WebHyperlink("http://google.com");
link1.SetText("Google");
link1.AlternateDescriptions = "Tautan ke Google";


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
LinkElement link2 = taggedContent.CreateLinkElement();
p2.AppendChild(link2);
link2.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Google");
link2.AppendChild(span2);
link2.AlternateDescriptions = "Tautan ke Google";


ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
LinkElement link3 = taggedContent.CreateLinkElement();
p3.AppendChild(link3);
link3.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("G");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText("oogle");
link3.AppendChild(span31);
link3.SetText("-");
link3.AppendChild(span32);
link3.AlternateDescriptions = "Tautan ke Google";


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
LinkElement link4 = taggedContent.CreateLinkElement();
p4.AppendChild(link4);
link4.Hyperlink = new WebHyperlink("http://google.com");
link4.SetText("Tautan multiline: Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google");
link4.AlternateDescriptions = "Tautan ke Google (multiline)";


ParagraphElement p5 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p5);
LinkElement link5 = taggedContent.CreateLinkElement();
p5.AppendChild(link5);
link5.Hyperlink = new WebHyperlink("http://google.com");
FigureElement figure5 = taggedContent.CreateFigureElement();
figure5.SetImage(imgFile, 1200);
figure5.AlternativeText = "Ikon Google";
StructureAttributes linkLayoutAttributes = link5.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
StructureAttribute placementAttribute = new StructureAttribute(AttributeKey.Placement);
placementAttribute.SetNameValue(AttributeName.Placement_Block);
linkLayoutAttributes.SetAttribute(placementAttribute);
link5.AppendChild(figure5);
link5.AlternateDescriptions = "Tautan ke Google";


// Menyimpan Dokumen Pdf Bertanda
document.Save(outFile);

// Memeriksa kepatuhan PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Kepatuhan PDF/UA: {0}", isPdfUaCompliance));
```
## Menetapkan Struktur Link Elemen

**Fitur ini didukung oleh versi 19.4 atau lebih tinggi.**

Aspose.PDF untuk .NET API juga memungkinkan Anda untuk menambahkan elemen struktur link. Cuplikan kode berikut menunjukkan bagaimana menambahkan elemen struktur link ke dalam Dokumen PDF Bertanda:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
string logFile = dataDir + "46144_log.xml";

// Pembuatan dokumen dan mendapatkan Konten Pdf Bertanda
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// Menetapkan Judul dan Bahasa Alamiah untuk dokumen
taggedContent.SetTitle("Contoh Elemen Teks");
taggedContent.SetLanguage("en-US");

// Mendapatkan Elemen struktur Root (Elemen struktur Dokumen)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
SpanElement span11 = taggedContent.CreateSpanElement();
span11.SetText("Span_11");
SpanElement span12 = taggedContent.CreateSpanElement();
span12.SetText(" dan Span_12.");
p1.SetText("Paragraf dengan ");
p1.AppendChild(span11);
p1.AppendChild(span12);


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
SpanElement span21 = taggedContent.CreateSpanElement();
span21.SetText("Span_21");
SpanElement span22 = taggedContent.CreateSpanElement();
span22.SetText("Span_22.");
p2.AppendChild(span21);
p2.SetText(" dan ");
p2.AppendChild(span22);


ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("Span_31");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText(" dan Span_32");
p3.AppendChild(span31);
p3.AppendChild(span32);
p3.SetText(".");


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
SpanElement span41 = taggedContent.CreateSpanElement();
SpanElement span411 = taggedContent.CreateSpanElement();
span411.SetText("Span_411, ");
span41.SetText("Span_41, ");
span41.AppendChild(span411);
SpanElement span42 = taggedContent.CreateSpanElement();
SpanElement span421 = taggedContent.CreateSpanElement();
span421.SetText("Span 421 dan ");
span42.AppendChild(span421);
span42.SetText("Span_42");
p4.AppendChild(span41);
p4.AppendChild(span42);
p4.SetText(".");


// Menyimpan Dokumen PDF Bertanda
document.Save(outFile);

// Memeriksa kepatuhan PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Kepatuhan PDF/UA: {0}", isPdfUaCompliance));
```
## Menetapkan Struktur Elemen Catatan

Aspose.PDF untuk API .NET juga memungkinkan Anda untuk menambahkan [NoteElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/noteelement) dalam dokumen PDF yang diberi tag. Cuplikan kode berikut menunjukkan cara menambahkan elemen catatan dalam Dokumen PDF yang Diberi Tag:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "45929_doc.pdf";
string logFile = dataDir + "45929_log.xml";

// Membuat Dokumen Pdf
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("Contoh Elemen Catatan");
taggedContent.SetLanguage("en-US");

// Menambahkan Elemen Paragraf
ParagraphElement paragraph = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(paragraph);

// Menambahkan NoteElement
NoteElement note1 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note1);
note1.SetText("Catatan dengan ID otomatis tergenerate. ");

// Menambahkan NoteElement
NoteElement note2 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note2);
note2.SetText("Catatan dengan ID = 'note_002'. ");
note2.SetId("note_002");

// Menambahkan NoteElement
NoteElement note3 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note3);
note3.SetText("Catatan dengan ID = 'note_003'. ");
note3.SetId("note_003");

// Harus melempar pengecualian - Aspose.Pdf.Tagged.TaggedException : Elemen struktur dengan ID='note_002' sudah ada
//note3.SetId("note_002");

// Dokumen hasil tidak mematuhi PDF/UA jika ClearId() digunakan untuk Elemen Struktur Catatan
//note3.ClearId();


// Menyimpan Dokumen PDF yang Diberi Tag
document.Save(outFile);

// Memeriksa kepatuhan PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Kepatuhan PDF/UA: {0}", isPdfUaCompliance));
```
## Pengaturan Bahasa dan Judul

**Fitur ini didukung oleh versi 19.6 atau lebih tinggi.**

Aspose.PDF untuk API .NET juga memungkinkan Anda untuk mengatur bahasa dan judul untuk dokumen sesuai dengan spesifikasi PDF/UA. Bahasa dapat diatur baik untuk seluruh dokumen maupun untuk elemen struktural terpisahnya. Potongan kode berikut menunjukkan cara mengatur bahasa dan judul dalam Dokumen PDF Bertag:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Document document = new Document();
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Dapatkan TaggedContent
Tagged.ITaggedContent taggedContent = document.TaggedContent;

// Atur Judul dan Bahasa
taggedContent.SetTitle("Dokumen Bertag Contoh");
taggedContent.SetLanguage("en-US");

// Header (en-US, diwarisi dari dokumen)
LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
h1.SetText("Frase dalam berbagai bahasa");
taggedContent.RootElement.AppendChild(h1);

// Paragraf (Inggris)
LogicalStructure.ParagraphElement pEN = taggedContent.CreateParagraphElement();
pEN.SetText("Hello, World!");
pEN.Language = "en-US";
taggedContent.RootElement.AppendChild(pEN);

// Paragraf (Jerman)
LogicalStructure.ParagraphElement pDE = taggedContent.CreateParagraphElement();
pDE.SetText("Hallo Welt!");
pDE.Language = "de-DE";
taggedContent.RootElement.AppendChild(pDE);

// Paragraf (Perancis)
LogicalStructure.ParagraphElement pFR = taggedContent.CreateParagraphElement();
pFR.SetText("Bonjour le monde!");
pFR.Language = "fr-FR";
taggedContent.RootElement.AppendChild(pFR);

// Paragraf (Spanyol)
LogicalStructure.ParagraphElement pSP = taggedContent.CreateParagraphElement();
pSP.SetText("¡Hola Mundo!");
pSP.Language = "es-ES";
taggedContent.RootElement.AppendChild(pSP);

// Simpan Dokumen PDF Bertag
document.Save(dataDir + "SetupLanguageAndTitle.pdf");
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
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

