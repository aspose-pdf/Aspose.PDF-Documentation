---
title: Persyaratan Sistem
linktitle: Persyaratan Sistem
type: docs
weight: 30
url: /id/python-net/system-requirements/
description: Bagian ini mencantumkan sistem operasi yang didukung yang diperlukan oleh pengembang untuk berhasil bekerja dengan Aspose.PDF untuk Python.
lastmod: "2025-02-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Sistem Operasi yang Didukung oleh Aspose.PDF untuk Python melalui .NET
Abstract: Aspose.PDF untuk Python melalui .NET adalah API pemrosesan PDF yang dirancang untuk pengembang mengelola dokumen PDF tanpa memerlukan Microsoft Office atau Otomatisasi Adobe Acrobat. API ini mendukung pengembangan aplikasi Python 32-bit dan 64-bit pada berbagai sistem operasi, termasuk Windows dan Linux, di mana Python 3.5 atau yang lebih baru telah diinstal. API kompatibel dengan beberapa versi Windows, mulai dari Windows XP hingga Windows 11, serta distribusi Linux utama seperti Ubuntu, OpenSUSE, dan CentOS. Untuk sistem Linux, persyaratan khusus meliputi pustaka runtime GCC-6, dependensi .NET Core Runtime (tanpa perlu menginstal runtime itu sendiri), dan build pymalloc Python untuk versi 3.5‑3.7. Selain itu, diperlukan pustaka libpython berbagi, yang mungkin memerlukan penyesuaian konfigurasi agar jalur pustaka dikenali dengan benar.
---

## Ikhtisar

Aspose.PDF untuk Python melalui .NET, API Pemrosesan PDF yang memungkinkan pengembang bekerja dengan dokumen PDF tanpa memerlukan Microsoft Office® atau Otomatisasi Adobe Acrobat. Aspose.PDF untuk Python dapat digunakan untuk mengembangkan aplikasi Python 32-bit dan 64-bit untuk berbagai sistem operasi (seperti Windows dan Linux) di mana Python 3.5 atau yang lebih baru telah diinstal.

## Sistem Operasi yang Didukung

### Windows

- Windows 2003 Server
- Windows 2008 Server
- Windows 2012 Server
- Windows 2012 R2 Server
- Windows 2016 Server
- Windows 2019 Server
- Windows XP
- Windows Vista
- Windows 7
- Windows 8, 8.1
- Windows 10
- Windows 11

### Linux

- Ubuntu
- OpenSUSE
- CentOS
- dan lainnya

## Persyaratan Sistem untuk Linux Target

- pustaka runtime GCC-6 (atau yang lebih baru).

- Dependensi .NET Core Runtime. Menginstal .NET Core Runtime itu sendiri TIDAK diperlukan.

- Untuk Python 3.5-3.7: Diperlukan build pymalloc dari Python. Opsi build Python --with-pymalloc diaktifkan secara default. Biasanya, build pymalloc Python ditandai dengan akhiran m pada nama file.

- pustaka Python bersama libpython. Opsi build Python --enable-shared dinonaktifkan secara default, beberapa distribusi Python tidak menyertakan pustaka libpython bersama. Untuk beberapa platform Linux, pustaka libpython bersama dapat diinstal menggunakan manajer paket, misalnya: sudo apt-get install libpython3.7. Masalah umum adalah pustaka libpython diinstal di lokasi yang berbeda dari lokasi standar sistem untuk pustaka bersama. Masalah ini dapat diperbaiki dengan menggunakan opsi build Python untuk mengatur jalur pustaka alternatif saat mengompilasi Python, atau dengan membuat tautan simbolik ke file pustaka libpython di lokasi standar sistem untuk pustaka bersama. Biasanya, nama file pustaka libpython bersama adalah libpythonX.Ym.so.1.0 untuk Python 3.5-3.7, atau libpythonX.Y.so.1.0 untuk Python 3.8 atau lebih baru (misalnya: libpython3.7m.so.1.0, libpython3.9.so.1.0).



