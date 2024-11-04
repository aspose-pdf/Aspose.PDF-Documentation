---
title: Add, Delete and Get Annotation - Facades
type: docs
weight: 10
url: /cpp/add-delete-and-get-annotation-facades/
---

## <ins>**Tambahkan Anotasi dalam file PDF yang ada menggunakan PdfContentEditor**
**PdfContentEditor** memungkinkan Anda untuk menambahkan berbagai jenis anotasi dalam file PDF yang ada. Anda dapat menggunakan metode yang sesuai dari kelas **PdfContentEditor** untuk menambahkan jenis anotasi tertentu dalam dokumen PDF yang ada. Misalnya, dalam potongan kode berikut, kami telah menggunakan metode **CreateText(...)** dan **CreateFreeText(...)**, untuk menambahkan komentar dan anotasi teks bebas dalam PDF yang ada masing-masing. Anda perlu melakukan langkah-langkah berikut, untuk menambahkan anotasi menggunakan kelas **PdfContentEditor**:

- Buat objek dari Facades::PdfContentEditor.
- Gunakan metode **BindPdf(...)** untuk memuat PDF yang ada.
- Panggil metode yang sesuai untuk membuat anotasi. misalnya **CreateText(...),CreateFreeText(...), dll.**
- Simpan dokumen PDF dengan menggunakan metode **Save(...)**.
### **Tambahkan Komentar ke Dokumen PDF yang Ada**

Potongan kode berikut menunjukkan kepada Anda bagaimana menambahkan komentar dalam file PDF yang ada.
```

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-AddAnnotation-AddAnnotation.cpp" >}}
## <ins>**Hapus Semua Anotasi dari PDF yang Ada**
Aspose.PDF untuk C++ juga menyediakan kelas **PdfAnnotationEditor**, yang memungkinkan Anda untuk menghapus semua anotasi dari dokumen PDF. Untuk menghapus semua anotasi dari PDF yang ada, Anda perlu membuat objek dari kelas **PdfAnnotationEditor** dan membuka dokumen yang ada. Setelah itu, Anda dapat menggunakan metode **DeleteAnnotations(...)** dari kelas PdfAnnotationEditor untuk menghapus anotasi. Cuplikan kode berikut menunjukkan penggunaan PdfAnnotationEditor untuk melayani tujuan tersebut:



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteAllAnnotations-1.cpp" >}}
## <ins>**Hapus Semua Anotasi berdasarkan Jenis yang Ditentukan**
Anda dapat menggunakan kelas **PdfAnnotationEditor** untuk menghapus semua anotasi, berdasarkan jenis anotasi yang ditentukan, dari file PDF yang ada. Untuk melakukan itu, Anda perlu membuat objek **PdfAnnotationEditor** dan mengaitkan file PDF input menggunakan metode **BindPdf**. Setelah itu, panggil metode **DeleteAnnotations**, dengan parameter string, untuk menghapus semua anotasi dari file; parameter string tersebut mewakili jenis anotasi yang akan dihapus. Akhirnya, gunakan metode **Save** untuk menyimpan file PDF yang telah diperbarui. Cuplikan kode berikut menunjukkan kepada Anda bagaimana menghapus semua anotasi berdasarkan jenis anotasi yang ditentukan.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteParticularAnnotation-1.cpp" >}}
## <ins>**Perbarui/Modifikasi Anotasi dalam File PDF yang Ada**
Untuk memperbarui atau memodifikasi anotasi dalam dokumen PDF, Anda dapat menggunakan metode **ModifyAnnotations(...)** dari kelas **PdfAnnotationEditor** yang mengambil objek Anotasi bersama dengan indeks awal dan akhir dari anotasi. Cuplikan kode berikut akan mendemonstrasikan penggunaan metode **ModifyAnnotations(...)**:

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ModifyAnnotations-1.cpp" >}}## <ins>**Impor Anotasi dari XFDF ke dalam File PDF**
Metode **ImportAnnotationFromXfdf** dari kelas **PdfAnnotationEditor**, memungkinkan Anda untuk mengimpor anotasi ke dalam file PDF. Untuk mengimpor anotasi, Anda perlu membuat objek **PdfAnnotationEditor** dan mengikat file PDF menggunakan metode **BindPdf**. Setelah itu, Anda perlu membuat enumerasi tipe anotasi yang ingin Anda impor ke file PDF. Anda kemudian dapat menggunakan metode **ImportAnnotationFromXfdf** untuk mengimpor anotasi tersebut. Dan akhirnya, simpan file PDF yang telah diperbarui menggunakan metode **Save** dari objek **PdfAnnotationEditor**. Cuplikan kode berikut menunjukkan cara mengimpor anotasi dari file XFDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ImportAnnotations-1.cpp" >}}
## **Ekspor Anotasi dari File PDF ke XFDF**
Metode **ExportAnnotationXfdf** memungkinkan Anda untuk mengekspor anotasi dari file PDF. Untuk mengekspor anotasi, Anda perlu membuat objek **PdfAnnotationEditor** dan mengikat file PDF menggunakan metode **BindPdf**. Setelah itu, Anda perlu membuat enumerasi jenis anotasi yang ingin Anda ekspor dari file PDF. Anda kemudian dapat menggunakan metode **ExportAnnotationXfdf** untuk mengimpor anotasi. Dan akhirnya, simpan file PDF yang telah diperbarui menggunakan metode **Save** dari objek **PdfAnnotationEditor**. Cuplikan kode berikut menunjukkan cara mengekspor anotasi ke file XFDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExportAnnotations-1.cpp" >}}

## <ins>**Ekstrak Anotasi dari File PDF yang Ada**

Metode **ExtractAnnotations** memungkinkan Anda mengekstrak anotasi dari file PDF. Untuk mengekstraksi anotasi, Anda perlu membuat objek **PdfAnnotationEditor** dan mengikat file PDF menggunakan metode **BindPdf**. Setelah itu, Anda perlu membuat enumerasi jenis anotasi yang ingin Anda ekstrak dari file PDF. Anda kemudian dapat menggunakan metode **Extract Annotations** untuk mengekstrak anotasi ke ArrayPtr. Setelah itu, Anda dapat melakukan loop melalui daftar ini dan mendapatkan anotasi individu. Dan akhirnya, simpan file PDF yang telah diperbarui menggunakan metode **Save** dari objek **PdfAnnotationEditor**. Cuplikan kode berikut menunjukkan kepada Anda cara mengekstraksi anotasi dari file PDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExtractAnnotations-1.cpp" >}}