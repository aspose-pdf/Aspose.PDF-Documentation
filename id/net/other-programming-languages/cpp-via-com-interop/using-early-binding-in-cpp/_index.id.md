---
title: Menggunakan early binding di CPP
type: docs
weight: 10
url: /net/using-early-binding-in-cpp/
---

## Prasyarat

{{% alert color="primary" %}}

Silakan daftar Aspose.PDF untuk .NET dengan COM Interop, silakan periksa artikel yang bernama [Gunakan Aspose.pdf untuk .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Contoh

{{% alert color="primary" %}}

Ini adalah contoh kode C++ sederhana untuk mengekstrak teks dari file PDF menggunakan COM Interop dengan menggunakan early binding. Sebelum menjalankan contoh perhatikan bahwa

- **#import** *typelib.tlb* membuat kompiler C++ menghasilkan 2 file: *typelib.tlh* dan *typelib.tli*. Secara default, file-file ini hanya dihasilkan sekali, sehingga Anda perlu mengkompilasi ulang proyek secara penuh untuk mendapatkan versi baru dari mereka.
- seringkali mengimpor hanya satu file TLB menyebabkan sejumlah besar kesalahan kompiler.
- seringkali mengimpor hanya satu file TLB mengakibatkan banyak kesalahan kompiler.

```cpp
// Perpustakaan tipe yang saling berhubungan:
```

dan memiliki satu atau lebih **#import**. Cukup salin mereka ke dalam kode Anda sebelum mengimpor perpustakaan tipe utama dan lakukan dengan ***urutan yang sama***. Dengan demikian Anda akan mengatasi tipe masalah pertama. Tipe masalah berikutnya berasal dari fakta bahwa lingkungan C++ memiliki banyak makro, fungsi yang telah didefinisikan sebelumnya, dll., yang dapat bertentangan dengan metode perpustakaan tipe. Misalnya, GetType telah banyak digunakan dalam C++ tetapi Aspose.PDF juga memilikinya. Saya menemukan atribut **rename** dan **auto_rename** dari direktif **#import** sangat nyaman untuk menghilangkan kemungkinan peringatan dan kesalahan.

- terkadang kelas dalam namespace **uses** bertentangan dengan nama dalam perpustakaan tipe, sehingga dalam kasus seperti itu, nama kelas lengkap harus digunakan alih-alih **using namespace**. Sebagai contoh, lihat bagaimana StringToBSTR dipanggil dalam potongan kode di bawah ini.
{{% /alert %}}

Untuk detailnya silakan lihat di [postingan ini](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558).
Untuk detailnya, silahkan lihat [postingan ini](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558).

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
    // membuat ComHelper

    Aspose_Pdf::_ComHelperPtr comHelperPtr;
    HRESULT hr = comHelperPtr.CreateInstance(__uuidof(Aspose_Pdf::ComHelper));
    if (FAILED(hr))
    {
        Console::WriteLine(L"Terjadi kesalahan");
    }
    else
    {
        // mengatur lisensi
        Aspose_Pdf::_LicensePtr licPtr;
        licPtr.CreateInstance(__uuidof(Aspose_Pdf::License));
        licPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        licPtr.Release();

        // mendapatkan Dokumen
        Aspose_Pdf::_DocumentPtr docPtr;
        docPtr = comHelperPtr->OpenFile((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());

        comHelperPtr.Release();

        // membuat Absorber
        Aspose_Pdf::_TextAbsorberPtr absorberPtr;
        HRESULT hRes = absorberPtr.CreateInstance(__uuidof(Aspose_Pdf::TextAbsorber));

        // menjelajahi teks
        docPtr->GetPages()->Accept_4(absorberPtr);

        // mengambil teks
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
        Console::WriteLine("Parameter hilang\nPenggunaan:testCOM <file pdf>");
        return 0;
    }

    String ^text = earlyBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("Teks yang diekstrak:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<kosong>");
    Console::WriteLine("---");
    return 0;
}
```

