---
title: Salin Bidang Dalam dan Luar
type: docs
weight: 40
url: /net/copy-inner-and-outer-field/
description: Bagian ini menjelaskan cara menyalin Bidang Dalam dan Luar dengan Aspose.PDF Facades menggunakan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---

Metode [CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) memungkinkan Anda menyalin bidang dalam file yang sama, pada koordinat yang sama, pada halaman yang ditentukan. Metode ini memerlukan nama bidang yang ingin Anda salin, nama bidang baru, dan nomor halaman di mana bidang perlu disalin. Kelas [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) menyediakan metode ini. Cuplikan kode berikut menunjukkan kepada Anda bagaimana menyalin bidang pada lokasi yang sama dalam file yang sama.

```csharp
  public static void CopyInnerField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document(_dataDir + "Sample-Form-01.pdf");
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyInnerField("Last Name", "Last Name 2", 2);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Salin Bidang Luar di File PDF yang Ada

Metode [CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) memungkinkan Anda menyalin bidang formulir dari file PDF eksternal dan kemudian menambahkannya ke file PDF masukan pada lokasi yang sama dan nomor halaman tertentu. Metode ini memerlukan file PDF dari mana bidang tersebut perlu disalin, nama bidang, dan nomor halaman di mana bidang tersebut perlu disalin. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Potongan kode berikut menunjukkan cara menyalin bidang dari file PDF eksternal.

```csharp
   public static void CopyOuterField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document();
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
            editor.Save(_dataDir + "Sample-Form-02-mod.pdf");
        }
```