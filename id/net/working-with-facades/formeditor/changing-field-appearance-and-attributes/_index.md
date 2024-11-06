---
title: Penampilan dan atribut bidang
type: docs
weight: 20
url: id/net/changing-field-appearance-and-attributes/
description: Bagian ini menjelaskan bagaimana Anda dapat mengubah penampilan dan atribut bidang dengan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) dari [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) memungkinkan Anda tidak hanya mengubah tampilan dan nuansa dari bidang formulir, tetapi juga perilaku dari bidang tersebut. Dalam artikel ini, kita akan melihat bagaimana kita dapat menggunakan kelas FormEditor untuk mengubah penampilan bidang, atribut bidang, dan batas bidang juga.

{{% /alert %}}

## Detail implementasi

Metode [SetFieldAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) digunakan untuk mengubah penampilan suatu bidang formulir. Itu mengambil AnnotationFlag sebagai parameter. AnnotationFlag adalah enumerasi yang memiliki anggota berbeda seperti Hidden atau NoRotate dll.

Metode [SetFieldAttributes](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) digunakan untuk mengubah atribut dari sebuah form field. Parameter yang diteruskan ke metode ini adalah enumerasi PropertyFlag yang berisi anggota seperti ReadOnly atau Required dll.

Kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) juga menyediakan metode untuk mengatur batasan field. Ini memberi tahu field seberapa banyak karakter yang dapat diisi. Cuplikan kode di bawah ini menunjukkan kepada Anda bagaimana semua metode ini dapat digunakan.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ChangingFieldAppearance-ChangingFieldAppearance.cs" >}}