---
title: Konversi HTML ke PDF dalam Python
linktitle: Konversi file HTML ke PDF
type: docs
weight: 40
url: id/python-java/convert-html-to-pdf/
lastmod: "2023-04-06"
description: Topik ini menunjukkan cara mengonversi HTML ke PDF dan MHTML ke PDF menggunakan Aspose.PDF. untuk Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Ikhtisar 

Aspose.PDF untuk Python via Java adalah solusi profesional yang memungkinkan Anda membuat file PDF dari halaman web dan kode HTML mentah dalam aplikasi Anda.

Artikel ini menjelaskan bagaimana **mengonversi HTML ke PDF menggunakan Python**. Ini mencakup topik-topik berikut.

_Format_: **HTML**
- [Python HTML ke PDF](#python-html-to-pdf)
- [Python Mengonversi HTML ke PDF](#python-html-to-pdf)
- [Python Cara mengonversi HTML ke PDF](#python-html-to-pdf)

## Konversi HTML ke PDF dalam Python

**Aspose.PDF untuk Python** adalah API manipulasi PDF yang memungkinkan Anda mengonversi dokumen HTML yang ada ke PDF dengan mulus. Proses mengonversi HTML ke PDF dapat dikustomisasi dengan fleksibel.

## Mengonversi HTML ke PDF

Contoh kode Python berikut menunjukkan cara mengonversi dokumen HTML ke PDF.

1. Buat instance dari kelas [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
2. Inisialisasi objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. Simpan dokumen PDF keluaran dengan memanggil metode **Document.Save()**.

```python

from asposepdf import Api


# inisialisasi lisensi
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# konversi dari byte array
documentName = "input.html"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array, Api.LoadFormat.HTML)
documentOutName = "result_fromHtml.pdf"
doc.save(documentOutName)

# konversi dari file
documentName = "input.html"
doc = Api.Document(documentName, Api.LoadFormat.HTML)
documentOutName = "result2_fromHtml.pdf"
doc.save(documentOutName)
```

{{% alert color="success" %}}
**Coba konversi HTML ke PDF secara online**


Aspose menghadirkan aplikasi online gratis ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi HTML ke PDF menggunakan Aplikasi Gratis](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}