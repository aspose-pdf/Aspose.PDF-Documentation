---
title: Bekerja dengan Formulir menggunakan Python
linktitle: Formulir dalam dokumen PDF
type: docs
weight: 60
url: /id/python-java/forms/
lastmod: "2023-05-19"
description: Bagian ini berisi artikel yang berkaitan dengan bekerja dengan formulir dalam dokumen PDF menggunakan API Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Formulir adalah file dengan area untuk pengguna memilih atau mengisi informasi dengan tujuan mengumpulkan dan menyimpan informasi.

AcroForms adalah file PDF yang berisi bidang formulir. Data dapat dimasukkan ke dalam bidang-bidang ini (secara manual atau melalui proses otomatis) oleh pengguna akhir atau penulis formulir. Secara internal, AcroForms adalah anotasi atau bidang yang diterapkan pada dokumen PDF.

Bagian ini menjelaskan pendekatan cepat dan sederhana untuk menyelesaikan dokumen PDF secara programatis melalui penggunaan Aspose.PDF. Bagian ini juga membahas bagaimana seseorang dapat menggunakan Aspose.PDF untuk Java untuk menemukan dan memetakan bidang yang tersedia dalam PDF yang sudah ada dengan AcroForms.

**Aspose.PDF for Python via Java** kami memungkinkan Anda untuk berhasil, cepat, dan mudah bekerja dengan formulir dalam dokumen PDF.

- **AcroForms** - buat formulir, isi bidang formulir, ekstrak data dari formulir, modifikasi bidang dalam PDF Anda dengan pustaka Java.
- **XFA Forms** - isi bidang XFA, konversi XFA, dapatkan properti bidang XFA.

## Fungsi-fungsi berikut tersedia:

- ekspor/impor fdf
- ekspor/impor xfdf
- ekspor/impor xml
- ekspor/atur XfaData
- isi bidang
- ratakan bidang
- menentukan nilai tombol radio yang valid
- dapatkan nama bidang, bendera, tipe, nilai
- ganti nama bidang

```python

from asposepdf import Api, Forms


# inisialisasi lisensi
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

DIR_INPUT = baseDir+"testdata/forms/"
DIR_OUTPUT = baseDir+"testout/"

# contoh isi bidang

input_pdf1 = DIR_INPUT + "Testing.pdf"
output_pdf = DIR_OUTPUT + "test5_1.pdf"

form = Forms.Form(sourceFileName=input_pdf1)
print(form.getFieldType("form1[0].Page1[0].fldBarCode1[0]"))
form.fillField("form1[0].Page1[0].fldBarCode1[0]", "54321")

form.save(output_pdf)
```