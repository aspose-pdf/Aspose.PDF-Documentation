```
---
title: Tambah dan Hapus Penanda Buku
type: docs
weight: 10
url: id/cpp/add-and-delete-bookmarks/
---

## <ins>**Tambah Penanda Buku**
Kelas PdfBookmarkEditor memungkinkan Anda untuk menambahkan penanda buku di dalam dokumen PDF. Metode CreateBookmarkOfPage yang ditawarkan oleh kelas ini, memungkinkan Anda untuk membuat penanda buku, yang akan menargetkan ke nomor halaman yang ditentukan. Cuplikan kode berikut menunjukkan fitur ini dari Aspose.PDF untuk API C++:



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-CreateBookmark-1.cpp" >}}
## <ins>**Tambah Penanda Buku Anak dalam dokumen yang ada**
Anda dapat menambahkan penanda buku anak dalam file PDF yang ada menggunakan kelas **PdfBookmarkEditor**.
``` Untuk menambahkan penanda buku anak, Anda perlu membuat objek **Bookmarks** dan *Bookmark*. Anda dapat menambahkan objek **Bookmark** individual ke dalam objek **Bookmarks**. Anda juga perlu membuat objek **Bookmark** dan mengatur properti **ChildItem**-nya ke objek **Bookmarks**. Kemudian, Anda perlu meneruskan objek **Bookmark** ini dengan **ChildItem** ke metode **CreateBookmarks**. Terakhir, Anda perlu menyimpan PDF yang telah diperbarui menggunakan metode **Save** dari kelas **PdfBookmarkEditor**. Cuplikan kode berikut menunjukkan cara menambahkan penanda buku anak dalam file PDF yang ada.

## <ins>**Hapus Semua Penanda Buku dari file PDF**
Anda dapat menghapus semua penanda buku dari file PDF menggunakan metode **DeleteBookmarks** tanpa parameter. First of all, you need to create an object of **PdfBookmarkEditor** class and bind the input PDF file using **BindPdf** method. After that, you need to call the **DeleteBookmarks** method and then save the updated PDF file using **Save** method. The following code snippet shows you how to delete all the bookmarks from the PDF file.

Pertama-tama, Anda perlu membuat objek dari kelas **PdfBookmarkEditor** dan mengikat file PDF input menggunakan metode **BindPdf**. Setelah itu, Anda perlu memanggil metode **DeleteBookmarks** dan kemudian menyimpan file PDF yang diperbarui menggunakan metode **Save**. Cuplikan kode berikut menunjukkan kepada Anda cara menghapus semua penanda buku dari file PDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-DeleteAllBookmarks-1.cpp" >}}
## <ins>**Delete a Particular Bookmark from a PDF File**

## <ins>**Hapus Penanda Buku Tertentu dari File PDF**

In order to delete a particular bookmark, you need to call **DeleteBookmarks** method with string (title) parameter. The **title** here represents the bookmark to be deleted from the PDF. Create an object of **PdfBookmarkEditor** class and bind input PDF file using **BindPdf** method. After that, call **DeleteBookmarks** method and then save the updated PDF file using **Save** method. The following code snippet shows you how to delete a particular bookmark from a PDF file.

Untuk menghapus penanda buku tertentu, Anda perlu memanggil metode **DeleteBookmarks** dengan parameter string (judul). **Judul** di sini mewakili penanda buku yang akan dihapus dari PDF. Buat objek dari kelas **PdfBookmarkEditor** dan ikat file PDF input menggunakan metode **BindPdf**. Setelah itu, panggil metode **DeleteBookmarks** dan kemudian simpan file PDF yang diperbarui menggunakan metode **Save**. Cuplikan kode berikut menunjukkan kepada Anda cara menghapus penanda buku tertentu dari file PDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-DeleteBookmark-1.cpp" >}}