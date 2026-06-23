---
title: مزيد من تفاصيل التثبيت
linktitle: مزيد من تفاصيل التثبيت
type: docs
weight: 30
url: /ar/sharepoint/more-installation-details/
lastmod: "2026-06-18"
description: مزيد من المعلومات حول تثبيت PDF SharePoint API يشرح كيفية نشرها وتفعيلها وتعطيلها في مجموعات المواقع.
---

## **النشر**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint يقوم بالإجراءات التالية أثناء النشر:**
- قم بتثبيت Aspose.PDF.SharePoint.dll في ذاكرة التخزين المؤقت للتجميع العامة (Global Assembly Cache) وأضف إدخال SafeControl إلى ملف web.config.
- قم بتثبيت ملف تعريف الميزة وغيرها من الملفات الضرورية في الأدلة المناسبة.
- سجِّل الميزة في قاعدة بيانات SharePoint واجعلها متاحة للتفعيل ضمن نطاق الميزة.

{{% /alert %}}


## **التفعيل**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint مُعبأة كميزة على مستوى الموقع (مجمع المواقع) ويمكن تفعيلها وتعطيلها على مجمعات المواقع.**

{{% /alert %}}

{{% alert color="primary" %}}

أثناء التفعيل، تُجري الميزة بعض التغييرات على الدليل الظاهري لتطبيق الويب الأب لمجمع الموقع: إضافة صفحة إعدادات التحويل إلى ملف خريطة الموقع. نسخ ملفات الموارد الضرورية إلى مجلد App_GlobalResources في الدليل الظاهري.

{{% /alert %}}
