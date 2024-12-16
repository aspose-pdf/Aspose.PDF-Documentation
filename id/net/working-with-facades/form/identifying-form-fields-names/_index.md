---
title: Mengidentifikasi nama bidang formulir
type: docs
weight: 10
url: /id/net/identifying-form-fields-names/
description: Aspose.PDF.Facades memungkinkan Anda mengidentifikasi nama bidang formulir menggunakan Kelas Form.
lastmod: "2021-06-05"
draft: false
---

[Aspose.PDF untuk .NET](/pdf/id/net/) menyediakan kemampuan untuk membuat, mengedit, dan mengisi formulir Pdf yang sudah dibuat. Namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) berisi kelas [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), yang berisi fungsi bernama [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) dan mengambil dua argumen yaitu nama bidang dan nilai bidang. Jadi untuk mengisi bidang formulir, Anda harus mengetahui nama bidang formulir yang tepat.

## Detail implementasi

Kita sering menghadapi skenario di mana kita perlu mengisi formulir yang dibuat dalam beberapa alat yaitu. Adobe Designer, dan kami tidak yakin tentang nama-nama bidang formulir. Jadi untuk mengisi bidang formulir, pertama-tama kita perlu membaca nama-nama semua bidang formulir Pdf. Kelas [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) menyediakan properti bernama [FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) yang mengembalikan seluruh nama bidang dan mengembalikan null jika PDF tidak mengandung bidang apapun. Namun, ketika menggunakan properti ini, kita mendapatkan nama seluruh bidang dalam formulir PDF dan kita mungkin tidak yakin nama mana yang sesuai dengan bidang mana di formulir.

Sebagai solusi untuk masalah ini, kita akan menggunakan atribut tampilan dari setiap bidang. Kelas Form memiliki fungsi bernama [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade) yang mengembalikan atribut, termasuk lokasi, warna, gaya batas, font, item daftar, dan sebagainya. Untuk menyimpan nilai-nilai ini, kita perlu menggunakan kelas [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), yang digunakan untuk merekam atribut visual dari bidang-bidang tersebut. Setelah kita memiliki atribut-atribut ini, kita dapat menambahkan bidang teks di bawah setiap bidang yang akan menampilkan nama bidang tersebut.

{{% alert color="primary" %}}
Pada titik ini, muncul pertanyaan "bagaimana kita menentukan lokasi di mana menambahkan bidang teks?"
{{% /alert %}}

{{% alert color="primary" %}}
Solusi untuk masalah ini adalah properti Box dalam kelas [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), yang menyimpan lokasi bidang tersebut. Kita perlu menyimpan nilai-nilai ini ke dalam array tipe persegi panjang dan menggunakan nilai-nilai ini untuk mengidentifikasi posisi di mana akan menambahkan kolom teks baru.
{{% /alert %}}

Dalam namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) kami memiliki kelas bernama [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) yang menyediakan kemampuan untuk memanipulasi formulir PDF. Buka formulir pdf; tambahkan kolom teks di bawah setiap kolom formulir yang ada dan simpan formulir Pdf dengan nama baru.