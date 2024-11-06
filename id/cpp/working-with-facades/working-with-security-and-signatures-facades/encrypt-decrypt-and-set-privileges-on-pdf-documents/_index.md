```
---
title: Enkripsi, Dekripsi, dan Atur Hak Istimewa pada Dokumen PDF
type: docs
weight: 10
url: id/cpp/encrypt-decrypt-and-set-privileges-on-pdf-documents/
---

## <ins>**Atur Hak Istimewa pada File PDF yang Ada**
Untuk mengatur hak istimewa pada dokumen PDF yang ada, Anda dapat menggunakan metode **Document->Encrypt(...)**, yang mengambil objek **DocumentPrivilege**. Kelas **DocumentPrivilege** digunakan untuk mengatur berbagai hak istimewa untuk mengakses dokumen PDF. Selanjutnya, ada 4 cara berikut menggunakan kelas ini:

1. Menggunakan hak istimewa yang telah ditentukan langsung.
1. Berdasarkan hak istimewa yang telah ditentukan dan mengubah beberapa izin spesifik.
1. Berdasarkan hak istimewa yang telah ditentukan dan mengubah beberapa kombinasi izin Adobe Professional spesifik.
1. Menggabungkan cara 2 dan cara 3.

Cuplikan kode berikut akan menunjukkan 4 cara di atas untuk mengatur hak istimewa dokumen:
```

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-SecurityAndSignatures-SetPrivileges-Priveleges.cpp" >}}