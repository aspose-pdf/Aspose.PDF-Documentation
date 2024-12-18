---
title: ChatGPT
type: docs
weight: 30
url: /id/net/plugins/chatGPT/
description: Cara menghasilkan respons ChatGPT yang didukung AI dan menyimpannya dalam PDF
lastmod: "2024-02-24"
---

## Menghasilkan Respons Chat yang Didukung AI dengan Plugin ChatGpt

Apakah Anda pernah ingin meningkatkan dokumen PDF Anda dengan respons chat yang dihasilkan AI? Tidak perlu mencari lagi! Dalam panduan ini, kami akan memandu Anda melalui proses integrasi plugin [ChatGpt yang kuat](https://products.aspose.org/pdf/net/chat-gpt/) ke dalam aplikasi C# Anda. Dengan hanya beberapa langkah sederhana, Anda akan menghasilkan respons chat yang menarik dengan mudah.

## Prasyarat

Anda akan memerlukan hal-hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 24.1 atau lebih baru
* Sebuah file PDF sampel

## Langkah-langkah

### 1. Membuat sebuah Objek

Mari kita mulai dengan membuat sebuah objek untuk tugas generasi chat kita. Cuplikan kode C# yang disediakan menunjukkan cara mengatur opsi untuk plugin PdfChatGpt.

```csharp
// Membuat opsi untuk plugin ChatGPT.
var options = new PdfChatGptRequestOptions();
```
### 2. Menambahkan Sumber Data

Selanjutnya, kita perlu menambahkan sumber data, yang dalam hal ini, adalah file PDF masukan yang berisi teks yang ingin Anda tingkatkan dengan respons chat yang dihasilkan AI.

```csharp
// Tambahkan file PDF masukan ke dalam opsi.
options.AddInput(new FileDataSource("c:\\Samples\\sample.pdf"));

// Tambahkan file PDF keluaran ke dalam opsi.
options.AddOutput(new FileDataSource("c:\\Samples\\chat_results.pdf"));
```

Dalam potongan kode di atas, kita menentukan jalur file PDF masukan dan jalur keluaran di mana PDF yang ditingkatkan dengan respons chat akan disimpan.

### 3. Menjalankan Metode Proses

Sekarang, mari kita lakukan semuanya dengan menjalankan metode proses. Ini adalah saatnya terjadi keajaiban – model ChatGPT yang didukung AI menghasilkan respons chat berdasarkan query dan teks yang diberikan.

```csharp
// Atur kunci API untuk autentikasi.
options.ApiKey = "sk-******";

// Atur jumlah token maksimum untuk model ChatGPT.
options.MaxTokens = 1000;

// Atur query untuk model ChatGPT.
options.Query = "Apa kata kunci terbaik untuk teks ini?";

// Buat sebuah instansi dari plugin PdfChatGpt.
var plugin = new PdfChatGpt();

// Proses dokumen PDF menggunakan plugin ChatGPT.
var result = await plugin.ProcessAsync(options);
```
Dengan baris kode ini, kami mengonfigurasi otentikasi, mengatur parameter untuk model ChatGPT, dan memulai proses generasi chat.
