---
title: تثبيت Aspose.PDF لـ PHP عبر Java
linktitle: التثبيت
type: docs
weight: 20
url: /ar/php-java/installation/
description: يعرض هذا القسم وصف المنتج وتعليمات تثبيت Aspose.PDF لـ PHP عبر Java بنفسك، وكذلك باستخدام NuGet.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يتكون Aspose.PDF لـ PHP عبر Java من مكونين منفصلين: غلاف السكريبت (aspose.pdf.php) و Aspose.PDF لـ Java. تتفاعل هذه المكونات من خلال جسر PHP/Java، مع حاجة كل منهما إلى بيئتها وعملية التنفيذ الخاصة بها.

## التثبيت

1. قم بتثبيت Tomcat في أي موقع مثل \java\apache-tomcat-9.0.24.
1. انسخ JavaBridge.war إلى مجلد webapps في Tomcat مثل \java\apache-tomcat-9.0.24\webapps.
1. انسخ aspose-pdf-xx.x.jar إلى مجلد lib مثل \java\apache-tomcat-9.0.24\lib.
1. قم بتشغيل \bin\startup.bat، سيتم نشر JavaBridge.war إلى \java\apache-tomcat-9.0.24\webapps\JavaBridge.

1. اختبار http://localhost:8080/JavaBridge/test.php للتأكد من أن PHP يعمل بشكل جيد.
1. نسخ aspose.pdf.php وexample.php إلى \java\apache-tomcat-9.0.24\webapps\JavaBridge.
1. فتح http://localhost:8080/JavaBridge/example.php أو إنشاء ملف PHP خاص بك كما يلي.
ستجد مكتبة Jar وPHP في مجلد vendor/aspose/pdf.