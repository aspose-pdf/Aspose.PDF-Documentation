---
title: Mengekstrak Konten Bertag dari PDF
linktitle: Mengekstrak Konten Bertag
type: docs
weight: 20
url: /net/extract-tagged-content-from-tagged-pdfs/
description: Artikel ini menjelaskan cara mengekstrak konten bertag dari dokumen PDF menggunakan Aspose.PDF untuk .NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Mengekstrak Konten Bertag dari PDF",
    "alternativeHeadline": "Cara menandai gambar dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "tag, pdf, ekstrak",
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
    "url": "/net/extract-tagged-content-from-tagged-pdfs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-tagged-content-from-tagged-pdfs/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan cara mengekstrak konten bertag dari dokumen PDF menggunakan Aspose.PDF untuk .NET"
}
</script>

Dalam artikel ini Anda akan belajar bagaimana mengekstrak konten bertag dari dokumen PDF menggunakan C#.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Mendapatkan Konten PDF Bertag

Untuk mendapatkan konten dari Dokumen PDF dengan Teks Bertag, Aspose.PDF menawarkan properti [TaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/taggedcontent) dari kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Potongan kode berikut menunjukkan cara mendapatkan konten dari dokumen PDF dengan Teks Bertag:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Membuat Dokumen Pdf
Document document = new Document();

// Mendapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

//
// Bekerja dengan konten Pdf Bertag
//

// Mengatur Judul dan Bahasa untuk Dokumen
taggedContent.SetTitle("Simple Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// Menyimpan Dokumen Pdf Bertag
document.Save(dataDir + "TaggedPDFContent.pdf");
```
## Mendapatkan Struktur Akar

Untuk mendapatkan struktur akar dari Dokumen PDF Bertag, Aspose.PDF menawarkan properti [StructTreeRootElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/properties/structtreerootelement) dari antarmuka [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) dan [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). Cuplikan kode berikut menunjukkan cara mendapatkan struktur akar dari Dokumen PDF Bertag:

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

// Properti StructTreeRootElement dan RootElement digunakan untuk akses ke
// objek StructTreeRoot dari dokumen pdf dan ke elemen struktur akar (elemen struktur Dokumen).
StructTreeRootElement structTreeRootElement = taggedContent.StructTreeRootElement;
StructureElement rootElement = taggedContent.RootElement;
```
## Mengakses Elemen Anak

Untuk mengakses elemen anak dari Dokumen PDF Bertag, Aspose.PDF menawarkan kelas [ElementList](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/elementlist). Cuplikan kode berikut menunjukkan cara mengakses elemen anak dari Dokumen PDF Bertag:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka Dokumen Pdf
Document document = new Document(dataDir + "StructureElementsTree.pdf");

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Akses ke elemen akar
ElementList elementList = taggedContent.StructTreeRootElement.ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // Dapatkan properti
        string title = structureElement.Title;
        string language = structureElement.Language;
        string actualText = structureElement.ActualText;
        string expansionText = structureElement.ExpansionText;
        string alternativeText = structureElement.AlternativeText;
    }
}

// Akses ke elemen anak dari elemen pertama di elemen akar
elementList = taggedContent.RootElement.ChildElements[1].ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // Atur properti
        structureElement.Title = "title";
        structureElement.Language = "fr-FR";
        structureElement.ActualText = "actual text";
        structureElement.ExpansionText = "exp";
        structureElement.AlternativeText = "alt";
    }
}

// Simpan Dokumen PDF Bertag
document.Save(dataDir + "AccessChildElements.pdf");
```
## Menandai Gambar di PDF yang Ada

Untuk menandai gambar dalam dokumen PDF yang ada, Aspose.PDF menawarkan metode [FindElements](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/findelements/_1) dari kelas [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). Anda dapat menambahkan teks alternatif untuk gambar menggunakan properti [AlternativeText](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/properties/alternativetext) dari kelas [FigureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/figureelement).

Berikut ini adalah cuplikan kode yang menunjukkan cara menandai gambar dalam dokumen PDF yang ada:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inFile = dataDir + "TH.pdf";
string outFile = dataDir + "TH_out.pdf";
string logFile = dataDir + "TH_out.xml";

// Membuka dokumen
Document document = new Document(inFile);

// Mendapatkan konten bertag dan elemen struktur root
ITaggedContent taggedContent = document.TaggedContent;
StructureElement rootElement = taggedContent.RootElement;

// Mengatur judul untuk dokumen pdf bertag
taggedContent.SetTitle("Dokumen dengan gambar");

foreach (FigureElement figureElement in rootElement.FindElements<FigureElement>(true))
{
    // Mengatur Teks Alternatif untuk Gambar
    figureElement.AlternativeText = "Teks alternatif gambar (teknik 2)";


    // Membuat dan Mengatur Atribut BBox
    StructureAttribute bboxAttribute = new StructureAttribute(AttributeKey.BBox);
    bboxAttribute.SetRectangleValue(new Rectangle(0.0, 0.0, 100.0, 100.0));

    StructureAttributes figureLayoutAttributes = figureElement.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
    figureLayoutAttributes.SetAttribute(bboxAttribute);
}

// Memindahkan Elemen Span ke dalam Paragraf (menemukan span dan paragraf yang salah di TD pertama)
TableElement tableElement = rootElement.FindElements<TableElement>(true)[0];
SpanElement spanElement = tableElement.FindElements<SpanElement>(true)[0];
TableTDElement firstTdElement = tableElement.FindElements<TableTDElement>(true)[0];
ParagraphElement paragraph = firstTdElement.FindElements<ParagraphElement>(true)[0];

// Memindahkan Elemen Span ke dalam Paragraf
spanElement.ChangeParentElement(paragraph);


// Menyimpan dokumen
document.Save(outFile);



// Memeriksa Kepatuhan PDF/UA untuk dokumen keluaran
document = new Document(outFile);

bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Kepatuhan PDF/UA: {0}", isPdfUaCompliance));
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

