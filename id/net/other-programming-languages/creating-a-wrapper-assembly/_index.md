---
title: Membuat Assembly Pembungkus
type: docs
weight: 80
url: id/net/creating-a-wrapper-assembly/
---

{{% alert color="primary" %}}

Jika Anda perlu menggunakan banyak kelas, metode, dan properti dari Aspose.PDF untuk .NET, pertimbangkan untuk membuat assembly pembungkus (menggunakan C# atau bahasa pemrograman .NET lainnya). Assembly pembungkus membantu menghindari penggunaan langsung Aspose.PDF untuk .NET dari kode yang tidak terkelola.

Pendekatan yang baik adalah mengembangkan assembly .NET yang merujuk pada Aspose.PDF untuk .NET dan melakukan semua pekerjaan dengannya, dan hanya mengekspos sejumlah minimal kelas dan metode ke kode yang tidak terkelola. Aplikasi Anda kemudian harus bekerja hanya dengan pustaka pembungkus Anda.

Mengurangi jumlah kelas dan metode yang perlu Anda panggil melalui COM Interop menyederhanakan proyek. Menggunakan kelas .NET melalui COM Interop sering kali memerlukan keahlian lanjutan.

{{% /alert %}}

## Wrapper Aspose.PDF untuk .NET

```csharp

using System;
using System.Runtime.InteropServices;
namespace PdfText
{
    [Guid("FC969AC9-6591-46FB-A4AB-DB12A776F3BF")]
    [InterfaceType(ComInterfaceType.InterfaceIsIDispatch)]
    public interface IPetriever
    {
        [DispId(1)]
        void SetLicense(string file);

        [DispId(2)]
        string GetText(string file);
    }

    [Guid("3D59100F-3CC5-463D-B509-58FA0520B436")]
    [ClassInterface(ClassInterfaceType.None)]

    [ComSourceInterfaces(typeof(IPetriever))]

    public class Petriever : IPetriever
    {
        public void SetLicense(string file)
        {
            License lic = new License();
            lic.SetLicense(file);
        }

        public string GetText(string file)
        {
            // open document
            Document doc = new Document(file);

            // create TextAbsorber object to extract text
            TextAbsorber absorber = new TextAbsorber();

            // accept the absorber for all document's pages
            doc.Pages.Accept(absorber);

            // get the extracted text

            string text = absorber.Text;
            return text;

        }
    }
}

```

