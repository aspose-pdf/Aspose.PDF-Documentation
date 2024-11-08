---
title: تعطيل ضغط الملفات عند إضافتها كموارد مدمجة
linktitle: تعطيل ضغط الملفات
type: docs
weight: 40
url: /ar/java/disable-files-compression-when-adding-as-embedded-resources/
description: يشرح هذا المقال كيفية تعطيل ضغط الملفات عند إضافتها كموارد مدمجة
lastmod: "2021-06-05"
---

تسمح فئة [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) للمطورين بإضافة مرفقات إلى مستندات PDF. بشكل افتراضي، يتم ضغط المرفقات. لقد قمنا بتحديث API للسماح للمطورين بتعطيل الضغط عند إضافة الملفات كموارد مدمجة. هذا يمنح المطورين مزيدًا من التحكم في كيفية معالجة الملفات.

للسماح للمطورين بالتحكم في ضغط الملفات تم إضافة طريقة [setEncoding(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#setEncoding-int-) إلى فئة [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification).
 هذه الخاصية تحدد أي ترميز سيتم استخدامه لضغط الملفات. يقبل الأسلوب قيمة من [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding) المجمع. القيم الممكنة هي [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None و [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

إذا تم تعيين الترميز إلى [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None، فلن يتم ضغط المرفق. الترميز الافتراضي هو [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

يظهر مقتطف الكود التالي كيفية إضافة مرفق إلى مستند PDF.

```java
    public static void DisableFilesCompressionWhenAddingAsEmbeddedResources() throws IOException{
  // الحصول على مرجع للملف المصدر/الإدخال
  java.nio.file.Path path = java.nio.file.Paths.get(_dataDir+"input.pdf");
  // قراءة جميع المحتويات من الملف المصدر إلى ByteArray
  byte[] data = java.nio.file.Files.readAllBytes(path);
  // إنشاء مثيل لكائن Stream من محتويات ByteArray
  InputStream is = new ByteArrayInputStream(data);
  // إنشاء مثيل لكائن Document من مثيل stream
  Document pdfDocument = new Document(is);
  // إعداد ملف جديد ليتم إضافته كمرفق
  FileSpecification fileSpecification = new FileSpecification("test.txt", "ملف نصي نموذجي");
  // تحديد خاصية الترميز وضبطها على FileEncoding.None
  fileSpecification.setEncoding(FileEncoding.None);
  // إضافة المرفق إلى مجموعة المرفقات في المستند
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // حفظ المخرجات الجديدة
  pdfDocument.save("output.pdf");
    }
```