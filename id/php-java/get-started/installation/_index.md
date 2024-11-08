---
title: Install Aspose.PDF untuk PHP melalui Java
linktitle: Instalasi
type: docs
weight: 20
url: /id/php-java/installation/
description: Bagian ini menunjukkan deskripsi produk dan instruksi untuk menginstal Aspose.PDF untuk PHP melalui Java secara mandiri, serta menggunakan NuGet.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF untuk PHP melalui Java terdiri dari dua komponen terpisah: pembungkus skrip (aspose.pdf.php) dan Aspose.PDF untuk Java. Komponen-komponen ini berinteraksi melalui PHP/Java Bridge, dengan masing-masing memerlukan lingkungan dan proses eksekusi sendiri.

## Instalasi

1. Instal Tomcat di lokasi mana saja seperti \java\apache-tomcat-9.0.24.
1. Salin JavaBridge.war ke folder webapps dari Tomcat seperti \java\apache-tomcat-9.0.24\webapps.
1. Salin aspose-pdf-xx.x.jar ke folder lib seperti \java\apache-tomcat-9.0.24\lib.
1. Jalankan \bin\startup.bat, JavaBridge.war akan diterapkan ke \java\apache-tomcat-9.0.24\webapps\JavaBridge.

1. Uji http://localhost:8080/JavaBridge/test.php untuk memastikan bahwa PHP berfungsi dengan baik.
1. Salin aspose.pdf.php dan example.php ke \java\apache-tomcat-9.0.24\webapps\JavaBridge.
1. Buka http://localhost:8080/JavaBridge/example.php atau buat file PHP Anda sendiri seperti berikut.
Anda akan menemukan pustaka Jar dan PHP di folder vendor/aspose/pdf.