---
title: Menggunakan binding awal di CPP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/using-early-binding-in-cpp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using early binding in CPP",
    "alternativeHeadline": "Effortless PDF Text Extraction with C Early Binding",
    "abstract": "Temukan kekuatan binding awal di C dengan Aspose.PDF for .NET. Fitur ini menyederhanakan ekstraksi teks dari file PDF menggunakan COM Interop, memberikan pendekatan yang efisien yang meminimalkan kesalahan kompilasi dan meningkatkan efisiensi pengkodean. Manfaatkan kemampuan binding awal untuk meningkatkan proyek C Anda dengan penanganan PDF yang andal",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "523",
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
    "url": "/net/using-early-binding-in-cpp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-early-binding-in-cpp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Prasyarat

{{% alert color="primary" %}}

Silakan daftarkan Aspose.PDF for .NET dengan COM Interop, silakan periksa artikel yang berjudul [Gunakan Aspose.pdf untuk .NET melalui COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Contoh

{{% alert color="primary" %}}

Ini adalah contoh kode C++ sederhana untuk mengekstrak teks dari file PDF menggunakan COM Interop dengan binding awal. Sebelum menjalankan contoh, perhatikan bahwa

- **#import** *typelib.tlb* membuat kompiler C++ menghasilkan 2 file: *typelib.tlh* dan *typelib.tli*. Secara default, file-file ini hanya dihasilkan sekali, jadi Anda perlu mengkompilasi ulang proyek sepenuhnya untuk mendapatkan versi baru dari file-file tersebut.
- sering kali mengimpor hanya satu file TLB menyebabkan banyak kesalahan kompilasi. Ada dua jenis kesalahan: ketergantungan yang tidak terpecahkan dan nama yang bertentangan. Jika Anda tidak dapat mengkompilasi proyek, buka file tlh dan lihat pada baris pertama yang dikomentari. Di sini Anda mungkin akan melihat bagian yang dimulai dari baris

```cpp
// Cross-referenced type libraries:
```

dan memiliki satu atau lebih **#import**. Cukup salin mereka ke dalam kode Anda sebelum mengimpor pustaka tipe utama dan lakukan dalam urutan ***yang sama***. Dengan demikian Anda akan mengatasi jenis masalah pertama. Jenis masalah berikutnya berasal dari fakta bahwa lingkungan C++ memiliki banyak makro, fungsi yang telah ditentukan, dll., yang dapat bertentangan dengan metode pustaka tipe. Misalnya, GetType sudah banyak digunakan di C++ tetapi juga ada di Aspose.PDF. Saya menemukan atribut **rename** dan **auto_rename** dari direktif **#import** sangat berguna untuk menghindari kemungkinan peringatan dan kesalahan.

- terkadang kelas dalam namespace **uses** bertentangan dengan nama dalam pustaka tipe, jadi dalam kasus seperti itu, nama kelas lengkap harus digunakan alih-alih **using namespace**. Misalnya, lihat bagaimana StringToBSTR dipanggil dalam cuplikan kode di bawah ini.
{{% /alert %}}

Untuk detail lebih lanjut silakan lihat [ini](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) pos.

Contoh C++

```cpp
#include "stdafx.h"
#import "C:\Windows\Microsoft.NET\Framework\v2.0.50727\System.Drawing.tlb"
#import "C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscorlib.tlb" auto_rename

#import "C:\Temp\Aspose.PDF.tlb" rename("GetType", "GetType_") auto_rename

using namespace System;
String ^earlyBinding(String ^file)
{
    String ^text;
    // Create ComHelper

    Aspose_Pdf::_ComHelperPtr comHelperPtr;
    HRESULT hr = comHelperPtr.CreateInstance(__uuidof(Aspose_Pdf::ComHelper));
    if (FAILED(hr))
    {
        Console::WriteLine(L"Error occured");
    }
    else
    {
        // Set license
        Aspose_Pdf::_LicensePtr licPtr;
        licPtr.CreateInstance(__uuidof(Aspose_Pdf::License));
        licPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        licPtr.Release();

        // Get Document
        Aspose_Pdf::_DocumentPtr docPtr;
        docPtr = comHelperPtr->OpenFile((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());

        comHelperPtr.Release();

        // Create Absorber
        Aspose_Pdf::_TextAbsorberPtr absorberPtr;
        HRESULT hRes = absorberPtr.CreateInstance(__uuidof(Aspose_Pdf::TextAbsorber));

        // Browse text
        docPtr->GetPages()->Accept_4(absorberPtr);

        // Retrieve text
        BSTR extractedText = absorberPtr->GetText();
        text = gcnew String(extractedText);
        docPtr.Release();
        absorberPtr.Release();
    }
    return text;
}

int main(array<System::String ^> ^args)
{
    CoInitialize(NULL);
    if (args->Length != 1)
    {
        Console::WriteLine("Missing parameters\nUsage:testCOM <pdf file>");
        return 0;
    }

    String ^text = earlyBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("Extracted text:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<empty>");
    Console::WriteLine("---");
    return 0;
}
```