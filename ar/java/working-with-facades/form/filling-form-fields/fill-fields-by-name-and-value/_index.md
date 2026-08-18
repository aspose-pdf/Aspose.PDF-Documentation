---
title: املأ الحقول بالاسم والقيمة
linktitle: املأ الحقول بالاسم والقيمة
type: docs
weight: 60
url: /java/fill-fields-by-name-and-value/
description: تعرف على كيفية تكييف واجهة برمجة تطبيقات ملء الحقول لواجهة النموذج في Java لتحديثات نماذج قيمة الاسم الديناميكية.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: املأ حقول نموذج PDF متعددة من أزواج الاسم والقيمة في Java
Abstract: تقوم مجموعة نماذج Java الحالية بملء الحقول بشكل فردي باستدعاءات `fillField(...)` المتكررة. توضح هذه المقالة كيفية تطبيق نفس نمط واجهة برمجة التطبيقات (API) على مجموعة قيمة الاسم الخاصة بك دون اختراع ميزة واجهة منفصلة غير موجودة في أمثلة المستودع.
---
تقوم فئة Java `FormExamples` بملء الحقول الفردية مباشرةً:

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

إذا كان تطبيقك يحتوي بالفعل على مجموعة ديناميكية من أسماء الحقول وقيمها، فقم بتطبيق نفس الاستدعاء `fillField(...)` داخل الحلقة الخاصة بك:

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

هذا نمط على مستوى التطبيق مشتق من نفس واجهة برمجة تطبيقات Java المستخدمة في `FormExamples.fillTextFields(...)`؛ لا يتضمن المستودع الحالي طريقة مساعدة مخصصة منفصلة للتعبئة المستندة إلى الخريطة.
