---
title: متطلبات النظام
linktitle: متطلبات النظام
type: docs
weight: 30
url: /python-net/system-requirements/
description: تسرد هذه القسم أنظمة التشغيل المدعومة التي يحتاجها المطور للعمل بنجاح مع Aspose.PDF لـ Python.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## نظرة عامة

Aspose.PDF لـ Python عبر .NET، واجهة برمجة تطبيقات معالجة PDF التي تتيح للمطورين العمل مع مستندات PDF بدون الحاجة إلى Microsoft Office® أو أتمتة Adobe Acrobat. يمكن استخدام Aspose.PDF لـ Python لتطوير تطبيقات Python بنظامي 32 بت و 64 بت لأنظمة تشغيل مختلفة (مثل Windows و Linux) حيث تم تثبيت Python 3.5 أو أحدث.

## نظام التشغيل المدعوم

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
- وغيرها


## متطلبات النظام لـ Linux المستهدف

- مكتبات وقت تشغيل GCC-6 (أو الأحدث).

- تبعيات .NET Core Runtime. تثبيت .NET Core Runtime نفسه ليس مطلوبًا.

- بالنسبة لـ Python 3.5-3.7: هناك حاجة إلى بناء pymalloc من Python. يتم تمكين خيار بناء Python --with-pymalloc بشكل افتراضي. عادةً ما يتم وضع علامة m في اسم الملف لبناء pymalloc من Python.

- مكتبة Python المشتركة libpython.
 خيار بناء Python --enable-shared معطل بشكل افتراضي، بعض توزيعات بايثون لا تحتوي على مكتبة libpython المشتركة. بالنسبة لبعض منصات لينكس، يمكن تثبيت مكتبة libpython المشتركة باستخدام مدير الحزم، على سبيل المثال: sudo apt-get install libpython3.7. المشكلة الشائعة هي أن مكتبة libpython تُثبت في موقع مختلف عن الموقع القياسي للنظام للمكتبات المشتركة. يمكن حل المشكلة باستخدام خيارات بناء بايثون لتعيين مسارات مكتبة بديلة عند تجميع بايثون، أو حلها عن طريق إنشاء رابط رمزي إلى ملف مكتبة libpython في الموقع القياسي للنظام للمكتبات المشتركة. عادةً، يكون اسم ملف مكتبة libpython المشتركة هو libpythonX.Ym.so.1.0 لبايثون 3.5-3.7، أو libpythonX.Y.so.1.0 لبايثون 3.8 أو أحدث (على سبيل المثال: libpython3.7m.so.1.0، libpython3.9.so.1.0).