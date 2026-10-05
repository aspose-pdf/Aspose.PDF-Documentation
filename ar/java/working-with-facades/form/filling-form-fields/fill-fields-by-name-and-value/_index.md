---
title: ملء الحقول بالاسم والقيمة
linktitle: ملء الحقول بالاسم والقيمة
type: docs
weight: 60
url: /ar/java/fill-fields-by-name-and-value/
description: تعلم كيفية تعديل واجهة برمجة تطبيقات ملء الحقول في واجهة Form في Java لتحديثات النماذج الديناميكية بالاسم والقيمة.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: ملء حقول نموذج PDF متعددة من أزواج الاسم والقيمة في Java
Abstract: مجموعة عينات Java الحالية تُملئ الحقول فراديًا باستخدام استدعاءات متكررة `fillField(...)`. توضح هذه المقالة كيفية تطبيق نمط API نفسه على مجموعة الاسم‑القيمة الخاصة بك دون اختراع ميزة واجهة منفصلة غير موجودة في أمثلة المستودع.
---
الجافا الفئة `FormExamples` تملأ الحقول الفردية مباشرةً:

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

إذا كان تطبيقك يحتوي بالفعل على مجموعة ديناميكية من أسماء الحقول والقيم، فطبق نفس الشيء `fillField(...)` استدعِ داخل الحلقة الخاصة بك:

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

هذا نمط على مستوى التطبيق مستمد من نفس واجهة برمجة التطبيقات Java المستخدمة في `FormExamples.fillTextFields(...)`; المستودع الحالي لا يتضمن طريقة مساعدة مخصصة منفصلة لملء قائم على الخريطة.
