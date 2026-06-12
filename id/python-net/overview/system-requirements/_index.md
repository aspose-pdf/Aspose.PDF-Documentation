---
title: Persyaratan Sistem
linktitle: Persyaratan Sistem
type: docs
weight: 30
url: /id/python-net/system-requirements/
description: Bagian ini mencantumkan sistem operasi yang didukung yang dibutuhkan pengembang untuk berhasil bekerja dengan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Sistem Operasi yang Didukung oleh Aspose.PDF for Python via .NET
Abstract: Aspose.PDF for Python via .NET adalah API pemrosesan PDF yang dirancang untuk pengembang mengelola dokumen PDF tanpa memerlukan Microsoft Office atau Adobe Acrobat Automation. API ini mendukung pengembangan aplikasi Python 32-bit dan 64-bit pada berbagai sistem operasi, termasuk Windows dan Linux, di mana Python 3.5 atau yang lebih baru telah diinstal. API kompatibel dengan beberapa versi Windows, mulai dari Windows XP hingga Windows 11, serta distribusi Linux utama seperti Ubuntu, OpenSUSE, dan CentOS. Untuk sistem Linux, persyaratan khusus meliputi pustaka runtime GCC-6, dependensi .NET Core Runtime (tanpa memerlukan runtime itu sendiri), dan build pymalloc Python untuk versi 3.5-3.7. Selain itu, diperlukan pustaka libpython bersama, yang mungkin memerlukan penyesuaian konfigurasi agar jalur pustaka dikenali dengan benar.
---

## Gambaran Umum

Aspose.PDF for Python via .NET, API Pemrosesan PDF yang memungkinkan pengembang bekerja dengan dokumen PDF tanpa memerlukan Microsoft Office® atau Otomatisasi Adobe Acrobat. Aspose.PDF for Python dapat digunakan untuk mengembangkan aplikasi Python 32-bit dan 64-bit untuk berbagai sistem operasi (seperti Windows dan Linux) di mana Python 3.5 atau lebih baru telah terinstal.

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
- dan lain-lain

## Persyaratan Sistem untuk Linux Target

- Perpustakaan runtime GCC-6 (atau lebih baru).

- Dependensi .NET Core Runtime. Menginstal .NET Core Runtime itu sendiri TIDAK diperlukan.

- Untuk Python 3.5-3.7: Build pymalloc dari Python diperlukan. Opsi build Python --with-pymalloc diaktifkan secara default. Biasanya, build pymalloc dari Python ditandai dengan akhiran m dalam nama file.

- libpython library Python bersama. Opsi build Python --enable-shared dinonaktifkan secara default; beberapa distribusi Python tidak menyertakan library libpython bersama. Untuk beberapa platform Linux, library libpython bersama dapat diinstal menggunakan manajer paket, misalnya: sudo apt-get install libpython3.7. Masalah umum adalah library libpython diinstal di lokasi yang berbeda dari lokasi standar sistem untuk library bersama. Masalah ini dapat diperbaiki dengan menggunakan opsi build Python untuk mengatur jalur library alternatif saat mengompilasi Python, atau dengan membuat tautan simbolik ke file library libpython di lokasi standar sistem untuk library bersama. Biasanya, nama file library libpython bersama adalah libpythonX.Ym.so.1.0 untuk Python 3.5-3.7, atau libpythonX.Y.so.1.0 untuk Python 3.8 atau lebih baru (misalnya: libpython3.7m.so.1.0, libpython3.9.so.1.0).


