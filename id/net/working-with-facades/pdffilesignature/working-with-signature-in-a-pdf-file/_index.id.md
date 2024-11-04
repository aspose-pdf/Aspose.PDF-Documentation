---
title: Bekerja dengan Tanda Tangan dalam File PDF
type: docs
weight: 40
url: /net/working-with-signature-in-a-pdf-file/
description: Bagian ini menjelaskan cara mengekstrak informasi tanda tangan, mengekstrak gambar dari tanda tangan, mengubah bahasa, dan lain-lain menggunakan kelas PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Cara Mengekstrak Informasi Tanda Tangan

Aspose.PDF untuk .NET mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas PdfFileSignature. Saat ini, juga dimungkinkan untuk menentukan validitas sertifikat tetapi kita tidak dapat mengekstrak seluruh sertifikat. Informasi yang dapat diekstraksi adalah kunci publik, sidik jari, dan penerbit, dll.

Untuk mengekstrak informasi tanda tangan, kami telah memperkenalkan metode ExtractCertificate(..) ke kelas PdfFileSignature. Silakan lihat cuplikan kode berikut yang menunjukkan langkah-langkah untuk mengekstrak sertifikat dari objek PdfFileSignature:

```csharp
public static void ExtractSignatureInfo()
        {
            string input = _dataDir + "DigitallySign.pdf";
            string certificateFileName = "extracted_cert.pfx";
            using (PdfFileSignature pdfFileSignature = new PdfFileSignature())
            {
                pdfFileSignature.BindPdf(input);
                var sigNames = pdfFileSignature.GetSignNames();
                if (sigNames.Count > 0)
                {
                    string sigName = sigNames[0];
                    if (!string.IsNullOrEmpty(sigName))
                    {
                        Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
                        if (cerStream != null)
                        {
                            using (cerStream)
                            {
                                using (FileStream fs = new FileStream(_dataDir + certificateFileName, FileMode.CreateNew))
                                {
                                    cerStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## Mengekstraksi Gambar dari Bidang Tanda Tangan (PdfFileSignature)

Aspose.PDF untuk .NET mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas PdfFileSignature dan saat menandatangani dokumen, Anda juga dapat mengatur gambar untuk SignatureAppearance. Sekarang API ini juga menyediakan kemampuan untuk mengekstraksi informasi tanda tangan serta gambar yang terkait dengan bidang tanda tangan.

Untuk mengekstraksi informasi tanda tangan, kami telah memperkenalkan metode ExtractImage(..) ke kelas PdfFileSignature. Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mengekstraksi gambar dari objek PdfFileSignature:

```csharp
public static void ExtractSignatureImage()
        {
            using (PdfFileSignature signature = new PdfFileSignature())
            {
                signature.BindPdf(_dataDir + "DigitallySign.pdf");

                if (signature.ContainsSignature())
                {
                    foreach (string sigName in signature.GetSignNames())
                    {
                        string outFile = _dataDir + "ExtractImages_out.jpg";
                        using (Stream imageStream = signature.ExtractImage(sigName))
                        {
                            if (imageStream != null)
                            {
                                imageStream.Position = 0;
                                using (FileStream fs = new FileStream(outFile, FileMode.OpenOrCreate))
                                {
                                    imageStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## Suppress Location and Reason

Fungsi Aspose.PDF memungkinkan konfigurasi yang fleksibel untuk instance tanda tangan digital. Kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) menyediakan kemampuan untuk menandatangani file PDF. Implementasi metode Sign memungkinkan untuk menandatangani PDF dan mengirimkan objek tanda tangan tertentu ke kelas ini. Metode Sign berisi serangkaian atribut untuk penyesuaian output tanda tangan digital. Jika Anda perlu menghilangkan beberapa atribut teks dari hasil tanda tangan, Anda dapat membiarkannya kosong. Cuplikan kode berikut menunjukkan cara menghilangkan dua baris Lokasi dan Alasan dari blok tanda tangan:

```csharp
public static void SupressLocationReason()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Buat persegi panjang untuk lokasi tanda tangan
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Atur tampilan tanda tangan
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Buat salah satu dari tiga jenis tanda tangan
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
            // Simpan file PDF output
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## Fitur Kustomisasi untuk Tanda Tangan Digital

Aspose.PDF untuk .NET memungkinkan fitur kustomisasi untuk tanda tangan digital. Metode Sign dari kelas [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) diimplementasikan dengan 6 overloads untuk kenyamanan penggunaan Anda. Misalnya, Anda dapat mengonfigurasi tanda tangan hasil hanya dengan instance kelas SignatureCustomAppearance dan nilai propertinya. Cuplikan kode berikut menunjukkan cara menyembunyikan keterangan "Digitally signed by" dari tanda tangan digital keluaran PDF Anda.

```csharp
  public static void CustomizationFeaturesForDigitalSign()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Buat persegi panjang untuk lokasi tanda tangan
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Buat salah satu dari tiga jenis tanda tangan
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Times New Roman",
                DigitalSignedLabel = "Signed by:"
            };
            signature.CustomAppearance = signatureCustomAppearance;

            pdfSign.Sign(1, true, rect, signature);
            // Simpan file PDF keluaran
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## Ubah Bahasa Dalam Teks Tanda Tangan Digital

Menggunakan Aspose.PDF untuk .NET API, Anda dapat menandatangani file PDF menggunakan salah satu dari tiga jenis tanda tangan berikut:

- PKCS#1
- PKCS#7
- PKCS#7

Masing-masing tanda tangan yang disediakan berisi satu set properti konfigurasi yang diterapkan untuk kenyamanan Anda (lokalisasi, format tanggal waktu, keluarga font dll). Kelas [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) menyediakan fungsionalitas yang sesuai. Cuplikan kode berikut menunjukkan cara mengubah bahasa dalam teks tanda tangan digital:

```csharp
     public static void ChangeLanguageInDigitalSignText()
        {
            string inFile = _dataDir + "sample01.pdf";
            string outFile = _dataDir + "DigitallySign.pdf";

            using (Aspose.Pdf.Facades.PdfFileSignature pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
            {
                pdfSign.BindPdf(inFile);
                //buat persegi panjang untuk lokasi tanda tangan
                System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

                //buat salah satu dari tiga jenis tanda tangan
                PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021")
                {
                    Reason = "Pruebas Firma",
                    ContactInfo = "Contacto Pruebas",
                    Location = "Población (Provincia)",
                    Date = DateTime.Now
                };
                SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
                {
                    DateSignedAtLabel = "Fecha",
                    DigitalSignedLabel = "Digitalmente firmado por",
                    ReasonLabel = "Razón",
                    LocationLabel = "Localización",
                    FontFamilyName = "Arial",
                    FontSize = 10d,
                    Culture = System.Globalization.CultureInfo.InvariantCulture,
                    DateTimeFormat = "yyyy.MM.dd HH:mm:ss"
                };
                pkcs.CustomAppearance = signatureCustomAppearance;
                // tandatangani file PDF
                pdfSign.Sign(1, true, rect, pkcs);
                //simpan file PDF output
                pdfSign.Save(outFile);
            }
        }
```