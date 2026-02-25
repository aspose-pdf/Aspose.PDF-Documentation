---
title: متطلبات النظام
linktitle: متطلبات النظام
type: docs
weight: 30
url: /ar/python-net/system-requirements/
description: يسرد هذا القسم أنظمة التشغيل المدعومة التي يحتاجها المطور للعمل بنجاح مع Aspose.PDF للبايثون.
lastmod: "2025-02-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أنظمة التشغيل المدعومة لـ Aspose.PDF للبايثون عبر .NET
Abstract: Aspose.PDF للبايثون عبر .NET هو واجهة برمجة تطبيقات لمعالجة ملفات PDF صُممت للمطورين لإدارة مستندات PDF بدون الحاجة إلى Microsoft Office أو Adobe Acrobat Automation. يدعم تطوير تطبيقات بايثون 32-بت و 64-بت على أنظمة تشغيل مختلفة، بما في ذلك Windows و Linux، حيث يتم تثبيت Python 3.5 أو أحدث. الواجهة متوافقة مع عدة إصدارات من Windows، من Windows XP حتى Windows 11، ومع توزيعات Linux الرئيسية مثل Ubuntu و OpenSUSE و CentOS. بالنسبة لأنظمة Linux، تشمل المتطلبات المحددة مكتبات وقت تشغيل GCC-6، واعتمادات .NET Core Runtime (دون الحاجة إلى تثبيت Runtime نفسه)، وبناء pymalloc من Python للإصدارات 3.5-3.7. بالإضافة إلى ذلك، يلزم وجود مكتبة libpython المشتركة، والتي قد تتطلب ضبط إعدادات لتحديد مسار المكتبة بشكل صحيح.
---

## نظرة عامة

Aspose.PDF للبايثون عبر .NET، واجهة برمجة تطبيقات معالجة PDF تسمح للمطورين بالعمل مع مستندات PDF دون الحاجة إلى Microsoft Office® أو Adobe Acrobat Automation. يمكن استخدام Aspose.PDF للبايثون لتطوير تطبيقات بايثون 32-بت و 64-بت لأنظمة تشغيل مختلفة (مثل Windows و Linux) حيث يتم تثبيت Python 3.5 أو أحدث.

## أنظمة التشغيل المدعومة

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

## متطلبات النظام لـ Linux المستهدفة

- مكتبات وقت تشغيل GCC-6 (أو أحدث).

- تبعيات .NET Core Runtime. تثبيت .NET Core Runtime نفسه غير مطلوب.

- بالنسبة لـ Python 3.5-3.7: يلزم بناء pymalloc من Python. خيار بناء Python --with-pymalloc مفعل افتراضيًا. عادةً ما يُشار إلى بناء pymalloc من Python باللاحقة m في اسم الملف.

- مكتبة libpython المشتركة للبايثون. خيار بناء Python --enable-shared يكون معطلًا افتراضيًا، وبعض توزيعات البايثون لا تحتوي على مكتبة libpython المشتركة. على بعض منصات Linux، يمكن تثبيت مكتبة libpython المشتركة باستخدام مدير الحزم، على سبيل المثال: sudo apt-get install libpython3.7. المشكلة الشائعة هي أن مكتبة libpython تُثبت في موقع مختلف عن الموقع القياسي للنظام للمكتبات المشتركة. يمكن حل المشكلة باستخدام خيارات بناء Python لتعيين مسارات مكتبة بديلة عند تجميع Python، أو بإنشاء رابط رمزي إلى ملف مكتبة libpython في الموقع القياسي للنظام للمكتبات المشتركة. عادةً ما يكون اسم ملف مكتبة libpython المشتركة هو libpythonX.Ym.so.1.0 للبايثون 3.5-3.7، أو libpythonX.Y.so.1.0 للبايثون 3.8 أو أحدث (مثال: libpython3.7m.so.1.0، libpython3.9.so.1.0).



