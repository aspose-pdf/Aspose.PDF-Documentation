---
title: Bekerja dengan Lampiran di PDF menggunakan Python
linktitle: Bekerja dengan Lampiran
type: docs
weight: 130
url: /id/python-net/attachments/
description: Gunakan Python PDF API untuk mengakses, menambah, dan menghapus lampiran dalam file PDF menggunakan Python dari dalam aplikasi Anda. Panduan lengkap dengan contoh kode Python.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan Lampiran di PDF menggunakan Python",
    "alternativeHeadline": "Lampiran dalam file PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, lampiran di pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/attachments/"
    },
    "dateModified": "2023-02-04",
    "description": "Gunakan Python PDF API untuk mengakses, menambah, dan menghapus lampiran dalam file PDF menggunakan Python dari dalam aplikasi Anda. Panduan lengkap dengan contoh kode Python."
}
</script>


In this section, we will explain how to work with attachments in PDF using Aspose.PDF for Python via .NET.  
Dalam bagian ini, kami akan menjelaskan cara bekerja dengan lampiran dalam PDF menggunakan Aspose.PDF untuk Python via .NET.  

An attachment is an additional file that is attached to a parent document, it can be a variety of file types, such as pdf, word, image, or other files.  
Lampiran adalah file tambahan yang dilampirkan ke dokumen induk, bisa berupa berbagai jenis file, seperti pdf, word, gambar, atau file lainnya.  

You will learn how to add attachments to pdf, get the information of an attachment, and save it to file, delete the attachment from PDF programmatically with Python.  
Anda akan belajar cara menambahkan lampiran ke pdf, mendapatkan informasi lampiran, dan menyimpannya ke file, menghapus lampiran dari PDF secara programatis dengan Python.  

- [Adding attachment to a PDF document](/pdf/id/python-net/add-attachment-to-pdf-document/)  
- [Menambahkan lampiran ke dokumen PDF](/pdf/id/python-net/add-attachment-to-pdf-document/)  

- [Removing attachment from an existing PDF](/pdf/id/python-net/removing-attachment-from-an-existing-pdf/)  
- [Menghapus lampiran dari PDF yang ada](/pdf/id/python-net/removing-attachment-from-an-existing-pdf/)  

- [Portfolio](/pdf/id/python-net/portfolio/)  
- [Portofolio](/pdf/id/python-net/portfolio/)  

<script type="application/ld+json">  
{  
    "@context": "http://schema.org",  
    "@type": "SoftwareApplication",  
    "name": "Aspose.PDF for Python Library",  
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",  
    "url": "https://www.aspose.com/",  
    "publisher": {  
        "@type": "Organization",  
        "name": "Aspose.PDF",  
        "url": "https://products.aspose.com/pdf",  
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",  
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
    "applicationCategory": "PDF Manipulation Library for Python",  
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",  
    "operatingSystem": "Windows, MacOS, Linux",  
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",  
    "softwareVersion": "2022.1",  
    "aggregateRating": {  
        "@type": "AggregateRating",  
        "ratingValue": "5",  
        "ratingCount": "16"  
    }  
}  
</script>