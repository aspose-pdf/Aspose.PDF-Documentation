---
title: Encrypt and Decrypt PDF
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 30
url: /python-cpp/set-privileges-encrypt-and-decrypt-pdf-file/
description: Enkripsi dan Dekripsi File PDF dengan Python melalui aplikasi C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Enkripsi File PDF menggunakan Jenis dan Algoritma Enkripsi yang Berbeda

Salah satu cara efektif untuk melindungi file PDF adalah melalui enkripsi. Dalam artikel ini, kita akan menjelajahi cara mengenkripsi dokumen PDF menggunakan Python dengan bantuan pustaka Aspose.PDF.

Enkripsi PDF melibatkan pengacakan isi dari dokumen PDF menggunakan algoritma kriptografi untuk mencegah akses tidak sah. File PDF yang dienkripsi memerlukan kata sandi untuk dibuka dan mungkin memiliki batasan pada tindakan seperti mencetak, menyalin, dan mengedit.

- **Kata sandi Pengguna**, jika diatur, adalah yang harus Anda berikan untuk membuka PDF. Acrobat/Reader akan meminta pengguna untuk memasukkan kata sandi pengguna. Jika tidak benar, dokumen tidak akan terbuka.
- **Kata sandi Pemilik**, jika diatur, mengontrol izin, seperti mencetak, mengedit, mengekstraksi, memberi komentar, dll.
 Acrobat/Reader akan menolak hal-hal ini berdasarkan pengaturan izin. Acrobat akan memerlukan kata sandi ini jika Anda ingin mengatur/mengubah izin.

Cuplikan kode berikut menunjukkan cara mengenkripsi file PDF.

1. Membuat jalur file input dan output
1. Memuat dokumen PDF menggunakan AsposePDFPythonWrappers
1. Menentukan izin untuk dokumen terenkripsi
1. Menentukan algoritma enkripsi yang akan digunakan
1. Mengenkripsi dokumen dengan kata sandi pengguna dan pemilik yang ditentukan, izin, dan algoritma enkripsi menggunakan metode 'document.encrypt'
1. Menyimpan dokumen terenkripsi ke file output yang ditentukan dengan metode 'document.save'.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Mengatur jalur direktori untuk file sampel
    dataDir = os.path.join(os.getcwd(), "samples")

    # Mengatur jalur file input
    input_file = os.path.join(dataDir, "sample.pdf")

    # Mengatur jalur file output
    output_file = os.path.join(dataDir, "results", "sample-enc.pdf")

    # Memuat dokumen PDF menggunakan AsposePDFPythonWrappers
    document = apw.Document(inputFile)

    # Menentukan izin untuk dokumen terenkripsi
    permission = apCore.Permissions(apCore.Permissions.ExtractContent | apCore.ModifyContent)

    # Menentukan algoritma enkripsi yang akan digunakan
    cryptoAlgorithm = apCore.CryptoAlgorithm.RC4x128

    # Mengenkripsi dokumen dengan kata sandi pengguna dan pemilik yang ditentukan, izin, dan algoritma enkripsi
    document.encrypt("user", "owner", permission, cryptoAlgorithm)

    # Menyimpan dokumen terenkripsi ke file output yang ditentukan
    document.save(output_file)
```

## Mendekripsi File PDF menggunakan Kata Sandi Pemilik

1. Membuat jalur file input dan output
1. Membuat instance baru dari kelas Document dari modul AsposePDFPythonWrappers
1. Mendekripsi dokumen menggunakan metode [document_decrypt](https://reference.aspose.com/pdf/python-cpp/core/document_decrypt/)
1. Menyimpan dokumen yang telah didekripsi ke jalur file output menggunakan metode save() dengan fungsi [document_save](https://reference.aspose.com/pdf/python-cpp/core/document_save/).

```Python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Mengatur jalur direktori untuk file sampel
    dataDir = os.path.join(os.getcwd(), "samples")

    # Mengatur jalur file input
    input_file = os.path.join(dataDir, "sample_enc.pdf")

    # Mengatur jalur file output
    output_file = os.path.join(dataDir, "results", "sample-dec.pdf")

    # Membuat instance baru dari kelas Document dari modul AsposePDFPythonWrappers
    document = apw.Document(input_file, "owner")

    # Mendekripsi dokumen menggunakan metode decrypt()
    document.decrypt()

    # Menyimpan dokumen yang telah didekripsi ke jalur file output menggunakan metode save()
    document.save(output_file)
```