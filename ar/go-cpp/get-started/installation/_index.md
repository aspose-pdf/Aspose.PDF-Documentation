---
title: كيفية تثبيت Aspose.PDF لـ Go عبر C++
linktitle: التثبيت
type: docs
weight: 20
url: /ar/go-cpp/installation/
description: يعرض هذا القسم وصفًا للمنتج وتعليمات لتثبيت Aspose.PDF for Go بنفسك.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دليل التثبيت لـ Aspose.PDF for Go
Abstract: يوفر دليل تثبيت Aspose.PDF for Go via C++ إرشادات خطوة بخطوة لتثبيت وتكوين المكتبة للاستخدام في مشاريع Go مع تكامل C++. يغطي الدليل طرق تثبيت مختلفة، بما في ذلك الإعداد اليدوي واستخدام مديري الحزم مثل NuGet. كما يحدد الدليل متطلبات النظام والاعتمادات وخطوات التكوين اللازمة لضمان تكامل سلس في بيئات التطوير. تساعد هذه الوثائق المطورين على البدء في إنشاء وقراءة ومعالجة مستندات PDF في Go عبر C++ بفعالية.
SoftwareApplication: go-cpp
---

## التثبيت

تحتوي هذه الحزمة على ملف كبير يتم تخزينه كأرشيف bzip2.

1. أضف حزمة asposepdf إلى مشروعك:

```sh
go get github.com/aspose-pdf/aspose-pdf-go-cpp@latest
```

2. إنشاء الملف الكبير:

- **macOS و Linux**

1. افتح الطرفية

2. قائمة المجلدات الخاصة بـ github.com/aspose-pdf داخل ذاكرة التخزين المؤقت لوحدات Go:

```sh
ls $(go env GOMODCACHE)/github.com/aspose-pdf/
```

3. غيّر المجلد الحالي إلى مجلد الإصدار المحدد للحزمة المستخرجة في الخطوة السابقة:

```sh
cd $(go env GOMODCACHE)/github.com/aspose-pdf/aspose-pdf-go-cpp@vx.x.x
```

استبدل `@vx.x.x` بالإصدار الفعلي للحزمة.

4. تشغيل go generate بصلاحيات المستخدم المتميز:

```sh
sudo go generate
```

- **ويندوز**

1. افتح موجه الأوامر

2. قائمة المجلدات الخاصة بـ github.com/aspose-pdf داخل ذاكرة التخزين المؤقت لوحدات Go:

```cmd
for /f "delims=" %G in ('go env GOMODCACHE') do for /d %a in ("%G\github.com\aspose-pdf\*") do echo %~fa
```

3. غيّر المجلد الحالي إلى مجلد الإصدار المحدد للحزمة المستخرجة في الخطوة السابقة:

```cmd
cd <specific version folder of the package>
```

4. تشغيل go generate:

```cmd
go generate
```

5. أضف مجلد الإصدار المحدد للحزمة إلى متغير البيئة %PATH%:

```cmd
setx PATH "%PATH%;<specific version folder of the package>\lib\"
```

استبدل `<specific version folder of the package>` مع المسار الفعلي المستخرج من الخطوة 2.

## اختبار

تشغيل الاختبار من مجلد الحزمة الجذر:

```sh
go test -v
```

## البدء السريع

جميع مقتطفات الشيفرة موجودة في [مقتطف](https://github.com/aspose-pdf/aspose-pdf-go-cpp).