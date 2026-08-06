---
title: Create a Secure PDF in SharePoint
linktitle: Creating a Secure PDF
type: docs
weight: 60
url: /ar/sharepoint/creating-a-secure-pdf/
lastmod: "2020-12-16"
description: باستخدام PDF SharePoint API، يمكنك إنتاج ملفات PDF آمنة ومشفرة وتحديد كلمات المرور الخاصة بها في SharePoint.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint supports creating secure PDFs. Installing Aspose.PDF for SharePoint adds a **PDF Secure Settings** option in Site Setting. Here, You can set the user password, owner password and any value from the algorithm list to encrypt the output PDF. The algorithm list provides different combinations of encryption algorithms and key sizes. Pass the value of your choice.

توضح هذه المقالة كيفية استخدام Aspose.PDF لـ SharePoint لإنشاء ملف PDF مشفر.

{{% /alert %}}

## Creating a Secure PDF

لتوضيح هذه الميزة، نقوم أولاً بتكوين خيار **إعدادات PDF الآمنة** لكلمة مرور المالك والمستخدم وخوارزمية التشفير. يقوم المثال بعد ذلك بدمج مستندين من مكتبة المستندات.

### ضبط خيارات الإعداد الآمن لملف PDF

Open **PDF Secure Settings** option from Site Settings and set algorithm, owner password and user password.

حدد كلمات مرور مختلفة للمستخدم والمالك أثناء تشفير ملف PDF.

- كلمة مرور المستخدم، إذا تم تعيينها، هي ما تحتاج إلى توفيره لفتح ملف PDF. يطالب برنامج Acrobat Reader المستخدم بإدخال كلمة مرور المستخدم. إذا كان الخطأ، لا يتم فتح المستند.
- تتحكم كلمة مرور المالك، إذا تم تعيينها، في الأذونات مثل الطباعة والتحرير والاستخراج والتعليق وما إلى ذلك. ولا يسمح Acrobat Reader بهذه الميزات بناءً على إعدادات الأذونات. يتطلب Acrobat كلمة المرور هذه إذا كنت تريد تعيين/تغيير الأذونات.

![PDF Secure Settings](creating-a-secure-pdf_1.png)

### دمج المستندات

Merge two documents using the **Convert to PDF** option. This feature merges multiple non-PDF files (HTML, text or image) into a PDF file.

1. افتح مكتبة المستندات وحدد المستندات المطلوبة من القائمة.

![Merge Documents](creating-a-secure-pdf_2.png)

1. استخدم خيار **Merge to PDF** من Library Tools لحفظ ملف الإخراج. تتم مطالبتك بحفظ ملف الإخراج على القرص.

![Merge to PDF](creating-a-secure-pdf_3.png)

### الإخراج

ملف الإخراج مشفر.

![Output](creating-a-secure-pdf_4.png)


