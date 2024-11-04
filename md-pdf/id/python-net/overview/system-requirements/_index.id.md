---
title: Persyaratan Sistem
linktitle: Persyaratan Sistem
type: docs
weight: 30
url: /python-net/system-requirements/
description: Bagian ini mencantumkan sistem operasi yang didukung yang dibutuhkan pengembang untuk bekerja dengan sukses dengan Aspose.PDF untuk Python.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ikhtisar

Aspose.PDF untuk Python melalui .NET, API Pemrosesan PDF yang memungkinkan pengembang untuk bekerja dengan dokumen PDF tanpa memerlukan Microsoft Office® atau Adobe Acrobat Automation. Aspose.PDF untuk Python dapat digunakan untuk mengembangkan aplikasi Python 32-bit dan 64-bit untuk berbagai sistem operasi (seperti Windows dan Linux) di mana Python 3.5 atau lebih baru terpasang.

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

## Persyaratan Sistem untuk Target Linux

- Pustaka runtime GCC-6 (atau yang lebih baru).

- Ketergantungan Runtime .NET Core. Menginstal Runtime .NET Core itu sendiri TIDAK diperlukan.

- Untuk Python 3.5-3.7: Diperlukan build pymalloc dari Python. Pilihan build Python --with-pymalloc diaktifkan secara default. Biasanya, build pymalloc dari Python ditandai dengan akhiran m dalam nama file.

- Pustaka Python bersama libpython.
 Opsi build Python --enable-shared dinonaktifkan secara default, beberapa distribusi Python tidak mengandung pustaka bersama libpython. Untuk beberapa platform linux, pustaka bersama libpython dapat diinstal menggunakan pengelola paket, misalnya: sudo apt-get install libpython3.7. Masalah umum adalah bahwa pustaka libpython diinstal di lokasi yang berbeda dari lokasi sistem standar untuk pustaka bersama. Masalah ini dapat diperbaiki dengan menggunakan opsi build Python untuk mengatur jalur pustaka alternatif saat mengompilasi Python, atau diperbaiki dengan membuat tautan simbolis ke file pustaka libpython di lokasi standar sistem untuk pustaka bersama. Biasanya, nama file pustaka bersama libpython adalah libpythonX.Ym.so.1.0 untuk Python 3.5-3.7, atau libpythonX.Y.so.1.0 untuk Python 3.8 atau lebih baru (misalnya: libpython3.7m.so.1.0, libpython3.9.so.1.0).