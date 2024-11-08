---
title: Membuat PDF dari XML menggunakan XSLT
linktitle: Membuat PDF dari XML menggunakan XSLT
type: docs
weight: 10
url: /id/net/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Perpustakaan C# menyediakan kemampuan untuk mengkonversi file XML menjadi dokumen pdf dengan syarat file XML input harus mengikuti Skema Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Membuat PDF dari XML menggunakan XSLT",
    "alternativeHeadline": "Cara membuat PDF dari XML menggunakan XSLT",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, membuat pdf xml, pdf dengan xslt",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/"
    },
    "dateModified": "2022-02-04",
    "description": "Perpustakaan C# menyediakan kemampuan untuk mengkonversi file XML menjadi dokumen pdf dengan syarat file XML input harus mengikuti Skema Aspose.PDF."
}
</script>
The following code snippet also work with [Aspose.PDF.Drawing](/pdf/id/net/drawing/) library.

Terkadang Anda mungkin memiliki file XML yang ada yang berisi data aplikasi dan Anda ingin menghasilkan laporan PDF menggunakan file-file ini. Anda dapat menggunakan XSLT untuk mengubah dokumen XML yang ada menjadi dokumen XML yang kompatibel dengan Aspose.Pdf dan kemudian menghasilkan file PDF. Ada 3 langkah untuk menghasilkan PDF menggunakan XML dan XSLT.

Silakan ikuti langkah-langkah ini untuk mengonversi file XML menjadi dokumen PDF menggunakan XSLT:

* Buat instance dari kelas PDF yang mewakili dokumen PDF
* Jika Anda telah membeli lisensi, maka Anda juga harus menyematkan kode untuk menggunakan lisensi tersebut dengan bantuan kelas License di namespace Aspose.Pdf
* Ikat file XML dan XSLT input ke instance dari kelas PDF dengan memanggil metode BindXML-nya
* Simpan XML yang terikat dengan instance PDF sebagai dokumen PDF

## File XML Input

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Hello World!</Content>
</Contents>
```

## File XSLT Input

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState
                            Font = "Helvetica" FontSize="8" LineSpacing="4"/>
          <Margin Left="5cm" Right="5cm" Top="3cm" Bottom="15cm" />
        </PageInfo>
        <Page id="mainSection">
          <TextFragment>
            <TextSegment>
              <xsl:value-of select="Content"/>
            </TextSegment>
          </TextFragment>
        </Page>
      </Document>
    </html>
</xsl:template>
</xsl:stylesheet>
```

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Working-Document-HelloWorldPDFUsingXmlAndXslt-HelloWorldPDFUsingXmlAndXslt.cs" >}}

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

---
id: "example"
title: "Contoh Dokumen"
description: "Ini adalah contoh dokumen yang akan diterjemahkan."
author: "John Doe"
changefreq: "monthly"
type: docs
---

# Pendahuluan

Ini adalah bagian pendahuluan dari dokumen. Bagian ini memberikan gambaran umum tentang isi dokumen.

## Tujuan

Tujuan dari dokumen ini adalah untuk memberikan contoh bagaimana menerjemahkan teks ke dalam Bahasa Indonesia sambil mempertahankan format markdown.

## Bagian Utama

Dalam bagian ini, kita akan membahas topik utama dari dokumen. Ini bisa mencakup berbagai subtopik dan penjelasan detail.

### Subtopik 1

Penjelasan tentang subtopik pertama. Ini bisa mencakup beberapa paragraf penjelasan.

### Subtopik 2

Penjelasan tentang subtopik kedua. Ini juga bisa mencakup beberapa paragraf penjelasan.

## Kesimpulan

Bagian kesimpulan merangkum poin-poin utama yang telah dibahas dalam dokumen. Ini memberikan ringkasan singkat tentang isi dokumen.

## Kontak

Untuk informasi lebih lanjut, silakan hubungi penulis di [email@example.com](mailto:email@example.com).
```
