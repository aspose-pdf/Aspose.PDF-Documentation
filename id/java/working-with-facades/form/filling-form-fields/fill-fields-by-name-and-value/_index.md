---
title: "Mengisi Field berdasarkan nama dan nilai"
linktitle: "Mengisi Field berdasarkan nama dan nilai"
type: docs
weight: 60
url: /id/java/fill-fields-by-name-and-value/
description: "Pelajari cara menyesuaikan API pengisian bidang fasad Form di Java untuk pembaruan formulir dinamis berbasis nama-nilai."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengisi beberapa bidang formulir PDF dari pasangan nama-nilai di Java"
Abstract: "Set contoh Java saat ini mengisi bidang secara individual dengan pemanggilan `fillField(...)` berulang. Artikel ini menunjukkan cara menerapkan pola API yang sama pada koleksi nama-nilai Anda sendiri tanpa menciptakan fitur fasad terpisah yang tidak ada dalam contoh repositori."
---
Kelas `FormExamples` dalam Java mengisi bidang individual secara langsung:

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

Jika aplikasi Anda sudah memiliki serangkaian nama bidang dan nilai yang dinamis, terapkan yang sama `fillField(...)` panggil di dalam loop Anda sendiri:

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

Ini adalah pola tingkat aplikasi yang diturunkan dari API Java yang sama digunakan dalam `FormExamples.fillTextFields(...)`; repositori saat ini tidak menyertakan metode pembantu khusus terpisah untuk pengisian berbasis peta.
